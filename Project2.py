#!/usr/bin/python

import json
import urllib
import sys
from type_check import Type_check
from setting import Setting
from info_box_person import Info_box_person
from info_box_group import Info_box_group
#main function for project2

#URL_escape step:
#TBF
setting = Setting

query = 'NY knicks' #Robert Downey Jr.
query = query.replace(' ', '%20') #url_encode for white space

url_query = setting.url_query + '?' + 'query=' + query + '&' + 'key=' + setting.key
#response_query[result]: list
response_query = json.loads(urllib.urlopen(url_query).read()) #get JASON document for most relevant entities by Freebase API

#start prcessing
result_count = 0
print 'Let me see...'

for result in response_query['result']: #result:dict
    #print result['name'] +  ' ' + result['mid'] + ' (' + str(result['score']) + ')'
    result_count += 1
    url_mid = setting.url_mid + result['mid'] + '?key=' + setting.key
    response_mid = json.loads(urllib.urlopen(url_mid).read()) #get JASON document by the Topic API with mid
    type_mid = Type_check(response_mid)

    if len(type_mid.valid_type_included) >= 1:
        #result_mid = result 			# is an mid
        break

    if result_count % 5 == 0:
        print str(result_count) + ' Search API result entries were considered. None of them of a supported type.'

## already breaked, right now the response_mid is the correct JSOn
## print out the JSON for response_
print "##################"
for key in response_mid['property']:
	print key
#print response_mid
print "##################"

# send an mid and get infobox
if len(type_mid.valid_type_included) >= 1: #guarantee that it includes the types valid
    #case 1: 'PERSON'
    if 'PERSON' in type_mid.valid_main_type:
        info_box = Info_box_person(type_mid.json_doc_mid, type_mid.valid_type_included, type_mid.valid_main_type)
        info_box.generate_info_box()
    #case 2: 'Group'
    else: #'LEAGUE' or 'SPORTSTEAM'
        info_box = Info_box_group(type_mid.json_doc_mid, type_mid.valid_type_included, type_mid.valid_main_type)
        info_box.generate_info_box()
else: #empty result
    query = query.replace( '%20', ' ')
    print 'No related information about query [' +  query + '] was found!'
