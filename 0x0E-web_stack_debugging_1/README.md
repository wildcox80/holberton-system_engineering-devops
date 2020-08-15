<h1 align="center">0x0F. Load balancer</h1>
<p align="center"> <img src = "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/275/qfdked8.png" /></p>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[![Twitter Wilder](https://img.shields.io/twitter/follow/WildsRincon?label=Wilder_Rincon&style=social)](https://twitter.com/WildsRincon)

## Background Context

You have been given 2 additional servers:

- gc-[STUDENT_ID]-web-02-XXXXXXXXXX
- gc-[STUDENT_ID]-lb-01-XXXXXXXXXX

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.



## Resources :notebook:

Read or watch:

- [Introduction to load-balancing and HAproxy](https://intranet.hbtn.io/rltoken/ngIXarEyu8jZwOL3Y30PLQ)

- [HTTP header](https://intranet.hbtn.io/rltoken/v32JmcDrSiOnFBfqzXvs_Q)

- [Debian/Ubuntu HAProxy packages](https://intranet.hbtn.io/rltoken/BXGrW_6ocecWaOJb7OK_WA)



## Requirements

### General :minidisc:


- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing



## Task :notebook:

### Mandatory :heavy_check_mark:

- Double the number of webservers
- Install your load balancer

### Advanced :heavy_check_mark:
- Add a custom HTTP header with Puppet


## Authors :busts_in_silhouette:
[@Wilder Rincón - Github](https://github.com/wildcox80)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/wildcox80/holberton-system_engineering-devops.svg?style=plastic
[contributors-url]: https://github.com/wildcox80/holberton-system_engineering-devops/graphs/contributors
[license-shield]: https://img.shields.io/github/license/wildcox80/holberton-system_engineering-devops.svg?style=plastic
[license-url]: https://github.com/wildcox80/holberton-system_engineering-devops/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=plastic&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/wildsrincon