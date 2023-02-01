<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<a name="readme-top"></a>

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
    <img src="images/logo.png" alt="Logo" width="80" height="80">

  <h3 align="center">Website Traffic Report From Google Analytics API</h3>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#libraries">Libraries</a></li>
        <li><a href="#packages">Packages</a></li>
        <li><a href="#service-accounts">Service Accounts</a></li>
        <li><a href="#known-exceptions">Known Exceptions</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![cover]

* Project Name: Website Traffic Report From Google Analytics API
* Version: v1.0.0
* Organization Department: Technology

### Description

I am developing a customised admin panel for my website automagicdeveloper.com,
and I needed to develop this project to display and visualize statistics about
my website traffic. 

The reason that I am doing this because I am don't want to manage my website from
multiple sources; such as the generic admin panel of the website and my 
Google Analytics account.

In this project, I achieved the following targets:
* Authenticated with Google Analytics API.
* Designed one API call to retrieve all the data that I need.
* The project takes exactly two seconds only to:
  * Make the API call
  * Analyse the data
  * Prepare the data for visualization that I will do with JavaScript.
* I retrieve the following data for the last 30 days:
  * Total users count.
  * Users count per date.
  * Users count per country.
  * Users count per device.
  * Users count per page title.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This project was developed using the following tech stacks:

* Python

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

In this section, I will give you instructions on setting up this project locally.
To get a local copy up and running follow these simple steps.

### Libraries

* pip
  ```sh
  pip install google-analytics-data==0.16.1
  ```

### Packages
* googleAnalytics
* dateTimeTools
* logger
* file

### Service Accounts
* automagic-developer: A service account that has access to Google Analytics API.

### Known Exceptions
* None

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Screenshots

<img src="images/screenshot.jpg">

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Authenticated with Google Analytics API.
- [x] Designed one API call to retrieve all the data that I need.
- [x] The project takes exactly two seconds only to:
  - [x] Make the API call
  - [x] Analyse the data
  - [x] Prepare the data for visualization that I will do with JavaScript.
- [x] I retrieve the following data for the last 30 days:
  - [x] Total users count.
  - [x] Users count per date.
  - [x] Users count per country.
  - [x] Users count per device.
  - [x] Users count per page title.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Mohamed AbdelGawad Ibrahim - [@m-abdelgawad](https://www.linkedin.com/in/m-abdelgawad/) - <a href="tel:+201069052620">+201069052620</a> - muhammadabdelgawwad@gmail.com

GitHub Profile Link: [https://github.com/m-abdelgawad](https://github.com/m-abdelgawad)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Resources that I found helpful during the development of this project:

* [Google Analytics Data API (GA4) - API Dimensions & Metrics](https://developers.google.com/analytics/devguides/reporting/data/v1/api-schema)
* [Apply Thousand Separator (and Other Formatting) to Pandas Dataframe](https://towardsdatascience.com/apply-thousand-separator-and-other-formatting-to-pandas-dataframe-45f2f4c7ab01)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/m-abdelgawad/
[cover]: images/cover.jpg
