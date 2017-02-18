#!/usr/bin/python3
# variables.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    d = dict(
        one =1, two=2, three=3
        )
    for i in d:
        print(i, d[i])

if __name__ == "__main__": main()
