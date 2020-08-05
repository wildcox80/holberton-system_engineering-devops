<h1 align="center">0x0C. Web server</h1>
<p align="center"> <img src = "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png" /></p>

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

In this project, some of the tasks will be graded on 2 aspects:

Is your web-01 server configured according to requirements

Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:

```
sylvain@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
sylvain@ubuntu
```

As you can tell, I am not using emacs to perform the task in my answer file. This exercise is aiming at training you on automating your work. If you can automate tasks that you do manually, you can then automate yourself out of repetitive tasks and focus your energy on something more interesting. For an SRE, that comes very handy when there are hundreds or thousands of servers to manage, the work cannot be only done manually. Note that the checker will execute your script as the root user, you do not need to use the sudo command.

A good Software Engineer is a lazy Software Engineer.

<p> <img src = "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/82VsYEC.jpg" /></p>

Tips: to test your answer Bash script, feel free to reproduce the checker environment:

- start an ubuntu:16.04 Docker container
- run your script on it
- see how it behaves

Check out the Docker concept page for more info about how to manipulate containers.


## Resources :notebook:

Read or watch:

- [How the web works](https://intranet.hbtn.io/rltoken/4tRRzyyETAySzU-bgNGLSw)
- [Nginx](https://intranet.hbtn.io/rltoken/H9OfhUnBDdxV-QQnIucMlA)
- [How to Configure Nginx](https://intranet.hbtn.io/rltoken/wePwmjbJDgJZO7YPvffWxQ)
- [Child process](https://intranet.hbtn.io/rltoken/V8RZRTiBQBweSGFenuQX5w)
- [Root and sub domain](https://intranet.hbtn.io/rltoken/qkpso3mgcpv3tPUhBrZBOA)
- [HTTP requests](https://intranet.hbtn.io/rltoken/C9s3U62JbiOAvn9WCoxKsA)
- [HTTP redirection](https://intranet.hbtn.io/rltoken/8N-RlUma9lwGfyZp1_C-Wg)
- [Not found HTTP response code](https://intranet.hbtn.io/rltoken/5UvC588x2hZR7dm6eRFPoQ)
- [Logs files on Linux](https://intranet.hbtn.io/rltoken/bkqQ72HZVAV65G8nB503Pw)

For reference:

- [RFC 7231 (HTTP/1.1)](https://intranet.hbtn.io/rltoken/gdZet6dJ30MzaeoucXCfRA)
- [RFC 7540 (HTTP/2)](https://intranet.hbtn.io/rltoken/EWo6KcJSfShUKLPqzeiXqQ)


## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google:**

### General

- What is the main role of a web server
- What is a child process
- Why web servers usually have a parent process and child processes
- What are the main HTTP requests

### DNS

- What DNS stands for
- What is DNS main role

### DNS Record Types

- A
- CNAME
- TXT
- MX


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
- You can’t use systemctl for restarting a process



## Task :notebook:

### Mandatory :heavy_check_mark:

- Transfer a file to your server
- Install nginx web server
- Setup a domain name
- Redirection
- Not found page 404

### Advanced :red_circle:

- Design a beautiful 404 page
- Install Nginx web server (w/ Puppet) 

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