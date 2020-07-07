<h1 align="center">0x06-regular_expressions</h1>
<p align="center"> <img src = "https://www.rubyguides.com/wp-content/uploads/2015/06/ruby-regex.png" /></p>
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][https://github.com/wildcox80/holberton-system_engineering-devops/graphs/contributors]
[![Forks][forks-shield]][https://github.com/wildcox80/holberton-system_engineering-devops/network/members]
[![Stargazers][stars-shield]][https://github.com/wildcox80/holberton-system_engineering-devops/stargazers]
[![MIT License][license-shield]][https://github.com/wildcox80/holberton-system_engineering-devops/blob/master/LICENSE]
[![LinkedIn][linkedin-shield]][https://www.linkedin.com/in/wildsrincon/]

## Backgorund Context

For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.

Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the //:

```
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a
```


## Resources :notebook:

Read or watch:

- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular is your best friend](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)


## Requirements

## General :minidisc:

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- The first line of all your Bash scripts should be exactly #!/usr/bin/env ruby
- All your regex must be built for the Oniguruma library 


## Task :notebook:

### Mandatory :heavy_check_mark:
- 0. Simply matching Holberton 
- 1. Repetition Token #0
- 2. Repetition Token #1
- 3. Repetition Token #2
- 4. Repetition Token #3
- Not quite HBTN yet
- Call me maybe
- OMG WHY ARE YOU SHOUTING?

### Advanced :red_circle:
- Textme
- Pass LinkedIn technical interview level0

## Authors :busts_in_silhouette: 
[@Wilder Rincón - Github](https://github.com/wildcox80)
