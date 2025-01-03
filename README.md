<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/PiFrameLogo.png" alt="Logo" width="270" height="350">
  </a>

<h3 align="center">PI Frame</h3>

  <p align="center">
    A digital picture frame powered by google photos api
    <br />
    <a href="https://github.com/Mikeymac02/PiFrame"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Mikeymac02/PiFrame">View Demo</a>
    ·
    <a href="https://github.com/Mikeymac02/PiFrame/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Mikeymac02/PiFrame/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#required-components">Required Components</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#Setting-up-Google-API-Access">Setting up Google API Access</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

This project was made as a Christmas gift for someone but I decided to post the code for all to use, thus is the Christmas Spirit. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Required Components

- Rapsberry Pi 3B/4B/5
- A display(I am using the official Raspberry Pi 7" Touchscreen)
- A google account
- A mobile device
- Internet connection

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow this tutorial.

### Setting up Google API Access

The project requires a Google API account to access your google photos account. The next steps are how to correctly set up your api account and project.

<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame1.png" alt="Frame1" width="600" height="400">
  </a>

  
Go to Google Cloud Api. If you are signed in, you will see the blue 'Try Google Cloud Free' button, press it and you will be prompted to create your account.


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame3.png" alt="Frame3" width="600" height="400">
  </a>

You will then see a blue 'New Project button on your screen, click it.


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame4.png" alt="Frame4" width="600" height="400">
  </a>

Once you create your project, you will be presented with this dashboard. Click 'APIs & Services'


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame5.png" alt="Frame5" width="600" height="400">
  </a>

You will now see this dashboard. We need to enable the Google Photos Picker API, so we need to click '+ ENABLE APIS AND SERVICES'


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame7.png" alt="Frame7" width="600" height="400">
  </a>

Once you search 'Google Photos API', click on the result and enable it via the enable button


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame8.png" alt="Frame8" width="600" height="400">
  </a>

After that, we need to set up the authentication consent screen. Click 'OAuth Consent Screen' on the left bar & set the user type to be external (it will never be internal), then hit create


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame9.png" alt="Frame9" width="600" height="400">
  </a>

Now we need to set up the credentials so your api can get authenticated and work properly. Click the 'Credentials' tab on the left, then '+ CREATE CREDENTIALS' and click 'OAuth client ID'


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame10.png" alt="Frame10" width="400" height="600">
  </a>

You will be prompted with the above creation screen. Set the Application type to be 'Web application', name your client, and set the Authorized redirect URIs to have 'https://localhost:8080/'. After that, press create.


<br />
<div align="left">
  <a href="https://github.com/Mikeymac02/PiFrame">
    <img src="images/walkthrough/Frame11.png" alt="Frame11" width="500" height="400">
  </a>

After that, you'll be prompted with a confirmation screen. Make sure you hit the 'DOWNLOAD JSON' button and label the file Credentials.json, you will need to put this into your project directory.


## Installation

1. You can either clone this repository or copy the main.py file and build the folders yourself
  - If you clone the repository, make sure to delete all items in the "images" & "backup" folders
  - If you only copy the main.py, you will have to create the "images" & "backup" folders in the same location of your main.py file

2. You now need to install each of the dependencies
   - The first 3 imports are default with python and do not need to be installed
<p align="right">(<a href="#readme-top">back to top</a>)</p>

3. Now you need to put the Credentials JSON file that you generated earlier into the project folder


<!-- ROADMAP -->
## Startup

- Upon running the code, a QR Code will appear. I reccomend using the google app on your phone to scan it as it lets the photos selection be much more streamlined.

See the [open issues](https://github.com/Mikeymac02/PiFrame/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/Mikeymac02/PiFrame/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Mikeymac02/PiFrame" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/Mikeymac02/PiFrame](https://github.com/Mikeymac02/PiFrame)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Mikeymac02/PiFrame.svg?style=for-the-badge
[contributors-url]: https://github.com/Mikeymac02/PiFrame/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Mikeymac02/PiFrame.svg?style=for-the-badge
[forks-url]: https://github.com/Mikeymac02/PiFrame/network/members
[stars-shield]: https://img.shields.io/github/stars/Mikeymac02/PiFrame.svg?style=for-the-badge
[stars-url]: https://github.com/Mikeymac02/PiFrame/stargazers
[issues-shield]: https://img.shields.io/github/issues/Mikeymac02/PiFrame.svg?style=for-the-badge
[issues-url]: https://github.com/Mikeymac02/PiFrame/issues
[license-shield]: https://img.shields.io/github/license/Mikeymac02/PiFrame.svg?style=for-the-badge
[license-url]: https://github.com/Mikeymac02/PiFrame/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/michael-mcnamara-5095b01a0
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
