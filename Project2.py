#!/usr/bin/python

import json
import urllib
import sys
import Type_check
import Setting
#main function for project2

#URL_escape step:
#TBF
setting = Setting

query = 'Bill Gates'
query = query.replace(' ', '%20') #url_encode for white space

url_query = setting.url_query + '?' + 'query=' + query + '&' + 'key=' + setting.key
response_query = json.loads(urllib.urlopen(url_query).read()) #get JASON document for most relevant entities by Freebase API

for result in response_query['result']:
    #print result['name'] +  ' ' + result['mid'] + ' (' + str(result['score']) + ')'
    url_mid = setting.url_mid + 'query=' + mid + '?key=' + setting.key
    response_mid = json.loads(urllib.urlopen(url_mid).read()) #get JASON document by the Topic API with mid

