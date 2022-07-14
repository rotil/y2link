#!/usr/bin/python
# useage python3 2link.py https://www.youtube.com/watch?v=DRR9fOXkfRE
from urllib import urlopen
from urlparse import parse_qs, urlparse
import sys
myurl = 'http://youtube.com/get_video_info?&video_id=%s&el=detailpage&ps=default&eurl=&gl=US&hl=en'
url = (sys.argv[1])
key = 'url_encoded_fmt_stream_map'
videoid = parse_qs(urlparse(url).query)['v'][0]
videoinfo = parse_qs(urlopen(myurl % videoid).read())
if key in videoinfo:
        for video in videoinfo[key][0].split(','):
                video = parse_qs(video)
                print(video)

