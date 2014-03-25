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

query = 'Bill Gates'
query = query.replace(' ', '%20') #url_encode for white space

url_query = setting.url_query + '?' + 'query=' + query + '&' + 'key=' + setting.key
response_query = json.loads(urllib.urlopen(url_query).read()) #get JASON document for most relevant entities by Freebase API
#response_query[result]: list
for result in response_query['result']: #result:dict
    #print result['name'] +  ' ' + result['mid'] + ' (' + str(result['score']) + ')'
    url_mid = setting.url_mid + result['mid'] + '?key=' + setting.key
    response_mid = json.loads(urllib.urlopen(url_mid).read()) #get JASON document by the Topic API with mid
    type_mid = Type_check(response_mid)

    if len(type_mid.valid_type_included) >= 1:
        result_mid = result
        break

if len(type_mid.valid_type_included) >= 1: #guarantee that it includes the types valid
    #case 1: 'Person'
    if 'PERSON' in type_mid.valid_main_type:
        infor_box = Info_box_person(type_mid.json_doc_mid, type_mid.valid_type_included, type_mid.valid_main_type)
    #case 2: 'Group'
    else
        infor_box = Info_box_group(type_mid.json_doc_mid, type_mid.valid_type_included, type_mid.valid_main_type)
else #empty result
