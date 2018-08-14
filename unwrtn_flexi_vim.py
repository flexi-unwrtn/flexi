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
        html = html + ':%s+href="/+href="https://www.imdb.com/+g |:/begin TOP_AD/,/End TOP_AD/d |:/Next/ |:?href?s+https://www.imdb.com++ |:?Previous? |:?href?s+https://www.imdb.com++|:/Episode aired/ |:/    /s+    +<span class="ghost">|</span><a target="_blank" href="https://d2uzw09ppuvr94.cloudfront.net/title/'+crow['Const']+'"><img src="https://raw.githubusercontent.com/Ede123/userscripts/master/icons/Rotten_Tomatoes.png" style="vertical-align: bottom;" width="16" height="16"></a>+ |:wnext\n'
        f = open('flexi.html','w')
f.write(html)
f.close()
