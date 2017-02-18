#!/usr/bin/python3
# databases.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.row_factory = sqlite3.Row
    db.execute('drop table if exists test')
    db.execute('create table test (name text, id int)')
    db.execute('insert into test (name, id) values (?,?)', ('rob', 401))
    db.execute('insert into test (name, id) values (?,?)', ('steve', 402))
    db.execute('insert into test (name, id) values (?,?)', ('Akash', 403))
    db.execute('insert into test (name, id) values (?,?)', ('Joy', 404))
    db.execute('insert into test (name, id) values (?,?)', ('Bill', 405))
    db.commit()
    cursor = db.execute('select name , id from test order by name')
    for row in cursor:
        print(row['name'], row['id'])
if __name__ == "__main__": main()
