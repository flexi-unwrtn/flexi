#!/usr/bin/python2.7
from itertools import izip
import csv
import os.path

html = ''
csvfile = open('flexi.csv', 'rb')
reader = csv.reader(csvfile)
headers = None

for row in reader:
    if reader.line_num == 1:
        headers = row
    else:
        crow = dict(zip(headers, row))
        html = html + ':%s+href="/+href="https://www.imdb.com/+g\n:/egin TOP_AD/,/nd TOP_AD/d\n:/Next/\n:?href?s+https://www.imdb.com++\n:?Previous?\n:?href?s+https://www.imdb.com++\n:/Episode aired/\n:read ' +crow['Const']+'.c\n:wnext\n'
        f = open('flexi.html','w')
f.write(html)
f.close()
