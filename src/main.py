#!/usr/bin/env python

# Author: Jasper Hawks

import click

from calculate import logic
from define import *
from times import *
from todo import *

@click.group()
def main():
    pass

@main.command()
def s():
    """Start a stopwatch"""
    stopwatch()

@main.command()
def t():
    """Start a timer"""
    timer()

@main.command()
def su():
    """Run setup for the TODO list"""
    setup()

@main.command()
def w():
    """Write to the TODO list file"""
    write()

@main.command()
def r():
    """Read from the TODO list file"""
    read()

@main.command()
def d():
    """Define a word"""
    define()

@main.command()
def c():
    """Calculate an equation"""
    logic()

@main.command()
def rm():
    """Remove an entry in the TODO list"""
    remove()

m = click.CommandCollection(sources=[main])

if __name__ == "__main__":
    main()
