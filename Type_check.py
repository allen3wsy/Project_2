#!/usr/bin/python

import json
from setting import Setting
#class type_check

class Type_check:

    def __init__(self, json_doc_mid):

        setting = Setting

        self.json_doc_mid = json_doc_mid
        self.valid_type_included = []
        self.valid_main_type = []

        for types in self.json_doc_mid['property']['/type/object/type']['values']:
            if setting.type_list.has_key(types['id']):
                self.valid_type_included.append(types['id'])

        self.valid_type_included = set(self.valid_type_included)

        for types in self.valid_type_included:
          if setting.type_list.has_key(types):
            self.valid_main_type.append(setting.type_list[types])

        self.valid_main_type = set(self.valid_main_type)
