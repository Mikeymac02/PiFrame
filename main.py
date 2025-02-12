import os
import pickle
import cv2
import qrcode
import PIL
from PIL import Image
import json
import time
import pygame
import requests
import RPi.GPIO as GPIO
import google_auth_oauthlib.flow
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying the scope/switching the user, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/photospicker.mediaitems.readonly']


#This sets up physical the reset key 
KEY_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEY_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
stop_loop = False


#This function is the key interrupt to switch the photos
def key_pressed_callback(channel):
    global stop_loop
    stop_loop = True
return None


#This sets up the key_pressed_callback to work as an interrupt function
GPIO.add_event_detect(KEY_PIN, GPIO.FALLING, callback=key_pressed_callback, bouncetime=50)


#This function does its namesake & generates a QR Code for the selection link
def generate_qr_code(data):
    #Creates a qr code of the link to select photos
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
  
    qrr = qr.make_image(fill_color="black", back_color="white")
    type(qrr)
    qrr.save("selectionQR.png")
    return None

#Authenticate and authorize the user to access their Google Photos
def authenticate_google_photos():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('Credentials.json', SCOPES)
            creds = flow.run_local_server(port=8080)  # Open a local server for OAuth
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds

#Creates the session to pick your photos
def create_session(creds):
    #This function creates an api session *Maybe only run it once?
    url = 'https://photospicker.googleapis.com/v1/sessions'
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type':'application/json'
    }

    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Session created successfully")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f'Failed to create session. Status code: {response.status_code}')
        print(response)

    response = response.json()
    return response
    
#Removes the session once finished to ensure we do not have session overflow   
def delete_session(creds, session_id):
    url = f'https://photospicker.googleapis.com/v1/sessions/{session_id}'
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type':'application/json'
    }
    response = requests.delete(url, headers=headers)


#Get the list of the selected images & their info
def get_selected_items(creds, id_val):
    url = "https://photospicker.googleapis.com/v1/mediaItems"
    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/json'
    }
    params = {
        'sessionId': id_val
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print('Selected items retrieved successfully:')
        print(json.dumps(response.json(), indent=2))
    else:
        print(f'Failed to retrieve items. Status code: {response.status_code}')
    response = response.json()
    return response

def wait_for_file(file_path):
    while not os.path.exists(file_path):
        time.sleep(1)


#Downloads the images selected from google photos
def download_images(item, url, token):
    #This function downloads the images to the images folder in this directory
    fileName = item.get('mediaFile', {}).get('filename')
    file_path = os.path.join('images', fileName)
    backup_path = os.path.join('backup', fileName)

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type':'application/json'
    }
    response = requests.get(url, headers=headers, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
            wait_for_file(file_path)
        with open(backup_path, 'wb') as file:
            file.write(response.content)
    return None


#Waits for user to select photos on the mobile device before going forward
def wait_for_selection(creds, id):
    #This function delays the rest of the code until the user selects their photos (Max of 2000 seconds)
    url = f"https://photospicker.googleapis.com/v1/sessions/"+id

    headers = {
        'Authorization': f'Bearer {creds.token}',
        'Content-Type': 'application/json'
    }
    elapsed_time = 0
    while elapsed_time < 2000:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            session_data = response.json()
            media_items_set = session_data.get('mediaItemsSet', False)
            if media_items_set:
                print("User has selected media items.")
                return session_data
            else:
                print(f"Waiting for 5 seconds before polling again.")
                time.sleep(5)
                elapsed_time += 5
        else:
            print(f"Failed to poll session. Status code: {response.status_code}")
            break
    return None

#Changes the mage size to the dimensions of the screen
def resize_image(image, screen_width, screen_height):
    img_width, img_height = image.get_size()
    
    screen_aspect_ratio = screen_width/screen_height
    img_aspect_ratio = img_width/img_height
    
    new_height = screen_height
    new_width = screen_width
        
    return pygame.transform.scale(image, (new_width, new_height))
    

#Crossfades current image & next image
def crossfade(current_image, next_image, screen):
    alpha = 0
    while alpha < 255:
        current_image.set_alpha(255-alpha)
        next_image.set_alpha(alpha)
        screen.fill((0,0,0))
        screen.blit(current_image, (0,0))
        screen.blit(next_image, (0,0))
        pygame.display.flip()
        
        alpha+=5
        pygame.time.delay(10)


#Displays the images on a loop until the key interrupt happens
def display_images(images, screen, screen_width, screen_height):
    clock = pygame.time.Clock()
    index = 0
    
    blockade = True
    
    current_image_path = os.path.join('images', images[index])
    current_image = pygame.image.load(current_image_path)
    current_image = resize_image(current_image, screen_width, screen_height)
    
    while True:
        next_index = (index + 1) % len(images)
        next_image_path = os.path.join('images', images[next_index])
        next_image = pygame.image.load(next_image_path)
        next_image = resize_image(next_image, screen_width, screen_height)
        crossfade(current_image, next_image, screen)
        
        current_image = next_image
        index = next_index
        """
        if GPIO.input(18) == GPIO.LOW:
            blockade = False
        """
        #Controls how long image is on screen
        pygame.time.delay(50000)
        clock.tick(60)   
    return None


#Initializes the Pygame display (Must be called again if the quit function is called)
def screen_init():
    pygame.init()
    displayInfo = pygame.display.Info()
    displayWidth = displayInfo.current_w
    displayHeight = displayInfo.current_h
    screen = pygame.display.set_mode((displayWidth, displayHeight),pygame.FULLSCREEN)
    return screen, displayWidth, displayHeight
    

#Creates the photo picking link and calls on generate_qr_code to do its namesake, then display the code and query until the photos are picked
def new_selection(credentials, screen, screenWidth, screenHeight):
    session = create_session(credentials)
    id_value = session.get('id')
    picker_uri = session.get('pickerUri')
    
    generate_qr_code(picker_uri)
    
    newUrl = "https://photospicker.googleapis.com/v1/sessions/"+id_value+"/mediaItems"
    
    #screen, screenWidth, screenHeight = screen_init()
    codeDisplay = pygame.image.load("selectionQR.png")
    codeWidth, codeHeight = codeDisplay.get_size()
    codeDisplay = pygame.transform.scale(codeDisplay, (screenWidth, codeHeight-10))

   # codeDisplay = resize_image(codeDisplay, screenWidth, screenHeight)
    screen.blit(codeDisplay, (0, 120))
    pygame.display.flip()
    wait_for_selection(creds, id_value)
    pygame.display.quit()
    
    items = get_selected_items(creds, id_value)
    media_items = items.get('mediaItems', [])
    for item in media_items:
        base_url = item.get('mediaFile', {}).get('baseUrl')+"=d"
        download_images(item, base_url, creds.token)
    
    return None


#Deletes the contents of the images folder
def delete_images():
    for filename in os.listdir("images"):
        file_path = os.path.join("images", filename)
        try:
            if os.path.isdir(file_path):
                os.rmdir(file_path)
            else:
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")


#Main function, will display currently saved photos [if any] or will let you select new photos if none are found
def photoView(credentials):
    screen, screenWidth, screenHeight = screen_init()
    images = [f for f in os.listdir('images') if f.endswith(('.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG', '.heic', '.HEIC'))]
    listLength = len(images)
    if listLength == 0:
       new_selection(credentials, screen, screenWidth, screenHeight)
       screen, screenWidth, screenHeight = screen_init()
       images = [f for f in os.listdir('images') if f.endswith(('.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG', '.heic', '.HEIC'))]
    display_images(images, screen, screenWidth, screenHeight)
    delete_images()
    pygame.display.quit()



if __name__ == '__main__':
    creds = authenticate_google_photos()
    while True:
        photoView(creds)
	
    
