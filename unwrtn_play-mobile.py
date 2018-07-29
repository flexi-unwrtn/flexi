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
        html = html + '<dl><strong><a href="https://d2uzw09ppuvr94.cloudfront.net/title/'+crow['Const']+'" alt="flexi TV-R">'+crow['Title']+'</a></strong><a> </a><a href="http://m.imdb.com/title/'+crow['Const']+'"alt="IMDb">'+crow['Year']+'</a><a> </a><a href="http://m.imdb.com/list/ls064891288/?sort=alpha,asc&st_dt=&mode=grid&page=1&ref_=ttls_vw_grd"alt="Genres"> '+crow['Genres']+'</a><a> </a><a href="http://m.imdb.com/title/'+crow['Const']+'/reviews?ref_=tt_urv'+'"alt="Reviews">read reviews</a></dl>'
        f = open('flexi.html','w')
f.write(html)
f.close()
