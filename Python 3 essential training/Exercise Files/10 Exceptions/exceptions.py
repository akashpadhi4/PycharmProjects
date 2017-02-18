#!/usr/bin/python3
# exceptions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC
from fileinput import filename

def main():
    try:
        for line in readfile('xlines.doc'): print(line.strip())
    except IOError as e:
        print('cannot find file', e)
    except ValueError as e:
        print('bad file name!', e)
        
def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('filename must end with .txt')
        

if __name__ == "__main__": main()
