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
        html = html + '<dl><a href="https://d2uzw09ppuvr94.cloudfront.net/title/'+crow['Const']+'" alt="flexi TV-R">'+crow['Title']+'</a><a> ' +' - '+'</a><a href="http://www.imdb.com/title/'+crow['Const']+'" alt="flexi TV-R">'+'IMDb'+'</a></dl>'
        f = open('flexi.html','w')
f.write(html)
f.close()
