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

        html = html + '<dl><span class='ghost'>|</span><a target='_blank' href='https://d2uzw09ppuvr94.cloudfront.net/title/'+crow['Const']+'><img src="https://raw.githubusercontent.com/Ede123/userscripts/master/icons/Rotten_Tomatoes.png" style="vertical-align: bottom;" width="16" height="16"></a></dl>'

        f = open('flexi.html','w')

f.write(html)

f.close()
