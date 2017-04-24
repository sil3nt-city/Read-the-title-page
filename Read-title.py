# -*- coding: utf-8 -*-
# code by sil3nt-city
# Email : sil3nt.city@gmail.com
############

import urllib2
from BeautifulSoup import BeautifulSoup
list=open ('list.txt', 'r')
for line in list.readlines():
  source = line.strip('\n')
  try:
    soup = BeautifulSoup(urllib2.urlopen(source))
    print soup.title.string
    ff=open('output.txt', 'ab')
    ff.write(str (source)+'\t'+'= Title =>>'+'\t'+(soup.title.string.encode('utf8'))+'\n'+'+'*30+'\n')
  except:
      print ((source) +"Site is down !!")
