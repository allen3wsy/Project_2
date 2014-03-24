#!/usr/bin/python

import json
import Setting
#class type_check

class Type_check:

    setting = Setting

    def __init__(self, json_doc_mid):

        self.json_doc_mid = json_doc_mid
        self.valid_type_included = []

    def valid_type_included(self):

        for key in self.json_doc_mid['property'].keys():
            if setting.type_list.has_key(key):
                self.valid_type_include.append()


