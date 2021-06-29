# Pysistant

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8274b7d317e04163ba89a9523515e92c)](https://app.codacy.com/gh/Jasper-Hawks/Pysistant?utm_source=github.com&utm_medium=referral&utm_content=Jasper-Hawks/Pysistant&utm_campaign=Badge_Grade_Settings)

A CLI Python Assistant who can complete mundane tasks for you.

## Features
* [x] Calculator (Read about the development [here](https://jasperhawks.netlify.app/blogposts/pysistant/completion%20of%20the%20calculator))
* [x] Todo list (File I/O)
* [x] Dictonary (Working with libraries)
* [x] Stopwatch (Fundamentals)
* [x] Timers (Fundamentals)

## Installation
Clone the repository and export the src directory to PATH like so:

```export PATH=/path/to/repository/:$PATH```
You'll want to always have this in the repository's directory since the other py files are dependencies.

## Dependencies
bs4, click and requests. Just install those with pip.

## Usage
Below is the help message for Pysistant:
```
Usage: pys [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  c   Calculate an equation
  d   Define a word
  r   Read from the TODO list file
  rm  Remove an entry in the TODO list
  s   Start a stopwatch
  su  Run setup for the TODO list
  t   Start a timer
  w   Write to the TODO list file
```
Using Pysistant is as simple as typing in pys and the command, for example:
```pys d```
to define a word

## Development
Feel free to help out in the project if you would like to challenge your Python skills or if you see something that could be more efficent. Make sure when you submit a PR that it is well documented. You should explain every step in your code.

Follow the development of Pysistant on my [Blog](https://jasperhawks.netlify.app/blogposts/pysistant/pysistant)
