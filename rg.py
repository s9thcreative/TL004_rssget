"""
TL004 note記事のRSS取得

:author: Yu
:version: v1.0.2610001
:date: 2026-10-31
:copyright 2026 #9th creative
"""

from lib.lib1 import getrss
from lib.lib2 import loadrss
from lib.lib3 import dataupd
from lib.lib4 import joinlist
from lib.lib5 import saverss

import sys

def main():
	url = "https://note.com/wh_yu/rss"
	dtp = "rss/rss.txt"
	rss = getrss(url)
	dt = loadrss(dtp)
	nl = dataupd(rss, dt)
	joinlist(nl, dt)
	saverss(dtp, nl)

if (__name__ == "__main__"):
	main()