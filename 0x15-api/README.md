<h1 align="center">0x15. API</h1>
<p align="center"> <img src = "https://holbertonintranet.s3.amazonaws.com/uploads/medias/2019/6/897638f42eb1bad6605d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20200914%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20200914T150534Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=745fdfe3f8efdf98096c3c16565bb07dc439c0e7c3a056119ed30a5693aa20d9" /></p>

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

Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them – access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.

This is a perfect example of a task that is not suited for Bash scripting, so let’s build Python scripts.


## Resources :notebook:

Read or watch:

- [Friends don’t let friends program in shell script](https://intranet.hbtn.io/rltoken/6isWaTEpGTrwhzCCG5s_Tw)

- [What is an API](https://intranet.hbtn.io/rltoken/13UaAZ1pQKQYY7VVwzJwCQ)

- [What is an API? In English, please](https://intranet.hbtn.io/rltoken/I1nC8rhySGahG3gXYBfDPA)

- [What is a REST API](https://intranet.hbtn.io/rltoken/0KygelrSeZsIujDu-I2a0w)

- [What are microservices](https://intranet.hbtn.io/rltoken/lewYS0z2RuFuiIkIgaCHSA)

- [PEP8 Python style - having a clean code respecting style guide is really appreciated in the industry](https://intranet.hbtn.io/rltoken/lEisphllQEYAs5yg26Ng0w)


## Learning Objetives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

### General :minidisc:

- What Bash scripting should not be used for
- What is an API
- What is a REST API
- What are microservices
- What is the CSV format
- What is the JSON format
- Pythonic Package and module name style
- Pythonic Class name style
- Pythonic Variable name style
- Pythonic Function name style
- Pythonic Constant name style
- Significance of CapWords or CamelCase in Python


## Requirements

### General :minidisc:


- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- Libraries imported in your Python files must be organized in alphabetical order
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use get to access to dictionary value by key (it won’t throw an exception if the key doesn’t exist in the dictionary)
- Your code should not be executed when imported (by using if __name__ == "__main__":)


## Task :notebook:

### Mandatory :heavy_check_mark:

- Gather data from an API
- Export to CSV
- Export to JSON
- Dictionary of list of dictionaries
- 

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
