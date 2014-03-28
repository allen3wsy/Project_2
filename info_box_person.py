from setting import Setting

class Info_box_person:

  def __init__(self, json_doc, type_list, types):

    self.json_doc = json_doc
    self.type_list = type_list #set
    self.types = types #set

  def generate_info_box(self):
    setting = Setting
    property_dict = self.json_doc['property']
    #width of infobox = 98 * '-' (the same in the group info box)
    width = 100
    #front_len = 17 #not used
    #behind_len = 81
    bar = ' --------------------------------------------------------------------------------------------------'
    print bar
    #information for PERSON------------------------------------------------------------------------------------
    #text for name
    str_name = property_dict['/type/object/name']['values'][0]['text']
    #text for types
    str_type = ''
    for string in self.types:
      if string != 'PERSON':
        if str_type == '':
          str_type += string
        else:
          str_type += ', ' + string

    str_type = '(' + str_type + ')'
    title = str_name + str_type
    half_len_of_title = int(round( len(title)/2 ))

    title_len_front = 49 + half_len_of_title
    title_len_behind = width - title_len_front

    #print title
    front = ''
    behind = ''
    for i in range(title_len_front - len(title) - 1):
      front += ' '
    for i in range(title_len_behind - 1):
      behind += ' '
    print '|' + front + title + behind + '|'
    print bar

    #print name
    print setting.str_name,
    print '{0:<81s}|' .format(str_name)
    print bar

    #print birth day
    #text for birth day
    str_birth = property_dict['/people/person/date_of_birth']['values'][0]['text']
    print setting.str_birth,
    print '{0:<81s}|' .format(str_birth)
    print bar

    #info for death (separately) ex: Death:          1973-07-20 at Kowloon Tong, cause: (Cerebral edema)
    #text for place of death
    if property_dict.has_key('/people/deceased_person/date_of_death'):
      if property_dict.has_key('/people/deceased_person/place_of_death'):
        place_of_death = ' at ' + property_dict['/people/deceased_person/place_of_death']['values'][0]['text']
      else:
        place_of_death = ''

      #text for date of death
      if property_dict.has_key('/people/deceased_person/date_of_death'):
        date_of_death = property_dict['/people/deceased_person/date_of_death']['values'][0]['text']
      else:
        date_of_death = ''

      #text for date of death
      if property_dict.has_key('/people/deceased_person/cause_of_death'):
        cause_of_death = ', cause (' + property_dict['/people/deceased_person/cause_of_death']['values'][0]['text'] + ')'
      else:
        cause_of_death = ''
      print '{0:<81s}|' .format(place_of_death + date_of_death + cause_of_death)
      print bar

    #print place of birth
    #text for place of birth
    str_placeofb = property_dict['/people/person/place_of_birth']['values'][0]['text']
    print setting.str_bplace,
    print '{0:<81s}|' .format(str_placeofb)
    print bar

    #print description
    #text for description
    str_description = property_dict['/common/topic/description']['values'][0]['value'].encode('utf-8').replace('\n',' ')
    print setting.str_desp,
    lines = int(len(str_description)//81)
    end_line = len(str_description)%81
    if lines < 1: #one line
      print '{0:<81s}|' .format(str_description)
    else: #multiple lines
      print '{0:<81s}|' .format(str_description[0:81])
      if lines > 1:
        for n in range(lines-1):
          print setting.str_white,
          print '{0:<81s}|' .format(str_description[(n+1)*81+0:(n+1)*81+81])
      if end_line == 0:
        pass #do nothing
      else:
        print setting.str_white,
        print '{0:<81s}|' .format(str_description[lines*81:])

    print bar

    #print sibling
    #list for siblings (could be none)
    if property_dict.has_key('/people/person/sibling_s'):
      list_siblings = []
      for sib in property_dict['/people/person/sibling_s']['values']:
        list_siblings.append(sib['property']['/people/sibling_relationship/sibling']['values'][0]['text'])
      for i in range(len(list_siblings)):
        if i == 0 :
          print setting.str_sib,
          print '{0:<81s}|' .format(list_siblings[i])
        else:
          print setting.str_white,
          print '{0:<81s}|' .format(list_siblings[i])
      print bar

    #print spouses
    #list for spouses (could be none)
    if property_dict.has_key('/people/person/spouse_s'):
      list_spouses = []
      for spo in property_dict['/people/person/spouse_s']['values']:
        spouse_name = spo['property']['/people/marriage/spouse']['values'][0]['text']
        marriage_from = spo['property']['/people/marriage/from']['values'][0]['text']
        if len(spo['property']['/people/marriage/to']['values'] ) == 0: #empty list: to now
          marriage_to = 'now'
        else:
          marriage_to = spo['property']['/people/marriage/to']['values'][0]['text']

        if len( spo['property']['/people/marriage/location_of_ceremony']['values']) == 0: #marriage_place empty: not recorded
          list_spouses.append( spouse_name + ' (' + marriage_from + '-' + marriage_to + ')' )
        else:
          marriage_place = spo['property']['/people/marriage/location_of_ceremony']['values'][0]['text']
          list_spouses.append( spouse_name + ' (' + marriage_from + '-' + marriage_to + ') ' +  '@ ' +  marriage_place )

      for i in range(len(list_spouses)):
        if i == 0 :
          print setting.str_spou,
          print '{0:<81s}|' .format(list_spouses[i])
        else:
          print setting.str_white,
          print '{0:<81s}|' .format(list_spouses[i])
      print bar

    #information for AUTHOR------------------------------------------------------------------------------------
    if 'AUTHOR' in self.types:
      #print books
      #list for books
      list_books = []
      for book in property_dict['/book/author/works_written']['values']:
        list_books.append(book['text'])
      for i in range(len(list_books)):
        if i == 0:
          print setting.str_book,
          print '{0:<81s}|' .format(summarize(list_books[i]))
        else:
          print setting.str_white,
          print '{0:<81s}|' .format(summarize(list_books[i]))
      print bar
      #print books about
      #list for books about
      list_books_about = []
      for book_ab in property_dict['/book/book_subject/works']['values']:
         list_books_about.append(book_ab['text'])
      for i in range(len(list_books_about)):
        if i == 0:
          print setting.str_bookab,
          print '{0:<81s}|' .format(summarize(list_books_about[i]))
        else:
          print setting.str_white,
          print '{0:<81s}|' .format(summarize(list_books_about[i]))
      print bar
      #print influenced people
      #list for influenced people
      if property_dict.has_key('/influence/influence_node/influenced'):
        list_influenced_ppl = []
        for ppl in property_dict['/influence/influence_node/influenced']['values']:
          list_influenced_ppl.append(ppl['text'])
        for i in range(len(list_influenced_ppl)):
          if i == 0:
            print setting.str_influ,
            print '{0:<81s}|' .format(summarize(list_influenced_ppl[i]))
          else:
            print setting.str_white,
            print '{0:<81s}|' .format(summarize(list_influenced_ppl[i]))
        print bar
      #print influenced_by people
      #list for influenced_by people
      if property_dict.has_key('/influence/influence_node/influenced_by'):
        list_influenced_by_ppl = []
        for ppl in property_dict['/influence/influence_node/influenced_by']['values']:
          list_influenced_by_ppl.append(ppl['text'])
        for i in range(len(list_influenced_by_ppl)):
          if i == 0:
            print setting.str_infu_by,
            print '{0:<81s}|' .format(summarize(llist_influenced_by_ppl[i]))
          else:
            print setting.str_white,
            print '{0:<81s}|' .format(summarize(list_influenced_by_ppl[i]))
        print bar
    #information for ACTOR-------------------------------------------------------------------------------------
    if 'ACTOR' in self.types:
      #list for characters
      list_characters = [] #(could be none)
      #list for film
      list_films = []
      #print character and film participated
      #list_characters[n] partiicipates in list_film[n]
      for film in property_dict['/film/actor/film']['values']:
        if film['property'].has_key('/film/performance/character'):
          list_characters.append(film['property']['/film/performance/character']['values'][0]['text']) #character name
        else:
          list_characters.append('')
        list_films.append(film['property']['/film/performance/film']['values'][0]['text']) #film name
      print setting.str_film
      print setting.str_f_white,
      print setting.str_f_bar
      for i in range(len(list_films)):
        print setting.str_f_white,
        print '|{0:<39s}|' .format(list_characters[i]),
        print '{0:<40s}|' .format(list_films[i])
      print bar

    #information for BUSNIESSPERSON----------------------------------------------------------------------------
    if 'BUSNIESS' in self.types:
      #print founded organization
      #list for founded organization
      if property_dict.has_key('/organization/organization_founder/organizations_founded'):
        list_found_comp = []
        for comp in property_dict['/organization/organization_founder/organizations_founded']['values']:
          list_found_comp.append(comp['text'])
        for i in range(len(list_found_comp)):
          if i == 0 :
            print setting.str_founded,
            print '{0:<81s}|' .format(list_found_comp[i])
          else:
            print setting.str_white,
            print '{0:<81s}|' .format(list_found_comp[i])
        print bar

      #print leadship
      #list for leadship, each element in it is a dictionary
      if property_dict.has_key('/business/board_member/leader_of'):
        list_leadship = []
        temp_list = property_dict['/business/board_member/leader_of']['values']
        for index in range(len(temp_list)):
          list_leadship.append({'organiztion': '', 'role': '', 'title': '', 'from' : '', 'to': ''})
          if temp_list[index]['property'].has_key('/organization/leadership/organization'):
            list_leadship[index]['organization'] = temp_list[index]['property']['/organization/leadership/organization']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/leadership/role'):
            list_leadship[index]['role'] = temp_list[index]['property']['/organization/leadership/role']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/leadership/title'):
            list_leadship[index]['title'] = temp_list[index]['property']['/organization/leadership/title']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/leadership/from'):
            list_leadship[index]['from'] = temp_list[index]['property']['/organization/leadership/from']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/leadership/to'):
            list_leadship[index]['to'] = temp_list[index]['property']['/organization/leadership/to']['values'][0]['text']
          else:
            if temp_list[index]['property'].has_key('/organization/leadership/from'):
              list_leadship[index]['to'] = 'now'

        print setting.str_leadsh
        print setting.str_f_white,
        print setting.str_f_bar

        for i in range(len(list_leadship)):
          print setting.str_f_white,
          print '|{0:<24s}|' .format(busniess_org(list_leadship[i]['organization'])),
          print '{0:<16s}|' .format(busniess_role(list_leadship[i]['role'])),
          print '{0:<17s}|' .format(busniess_title(list_leadship[i]['title'])),
          if list_leadship[i]['from'] != '':
            str_time = '(' +  list_leadship[i]['from'] + ' / ' + list_leadship[i]['to'] + ')'
          else:
            str_time = ''
          print '{0:<18s}|' .format(business_time(str_time))
        print bar
      #print board_member
      #list for board_member, each element in it is a dictionary
      if property_dict.has_key('/business/board_member/organization_board_memberships'):
        list_board_member = []
        temp_list = property_dict['/business/board_member/organization_board_memberships']['values']
        for index in range(len(temp_list)):
          list_board_member.append({'organiztion': '', 'role': '', 'title': '', 'from' : '', 'to': ''})
          if temp_list[index]['property'].has_key('/organization/organization_board_membership/organization'):
            list_board_member[index]['organization'] = temp_list[index]['property']['/organization/organization_board_membership/organization']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/organization_board_membership/role'):
            list_board_member[index]['role'] = temp_list[index]['property']['/organization/organization_board_membership/role']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/organization_board_membership/title'):
            list_board_member[index]['title'] = temp_list[index]['property']['/organization/organization_board_membership/title']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/organization_board_membership/from'):
            list_board_member[index]['from'] = temp_list[index]['property']['/organization/organization_board_membership/from']['values'][0]['text']
          if temp_list[index]['property'].has_key('/organization/organization_board_membership/to'):
            list_board_member[index]['to'] = temp_list[index]['property']['/organization/organization_board_membership/to']['values'][0]['text']
          else:
            if temp_list[index]['property'].has_key('/organization/organization_board_membership/from'):
              list_board_member[index]['to'] = 'now'

        print setting.str_b_mem
        print setting.str_f_white,
        print setting.str_f_bar

        for i in range(len(list_board_member)):
          print setting.str_f_white,
          print '|{0:<24s}|' .format(busniess_org(list_board_member[i]['organization'])),
          print '{0:<16s}|' .format(busniess_role(list_board_member[i]['role'])),
          print '{0:<17s}|' .format(busniess_title(list_board_member[i]['title'])),
          if list_board_member[i]['from'] != '':
            str_time = '(' +  list_board_member[i]['from'] + ' / ' + list_board_member[i]['to'] + ')'
          else:
            str_time = ''
          print '{0:<18s}|' .format(business_time(str_time))

        print bar
#function to extract front part of context for books & book about
def summarize(context):
  if len(context) > 72:
   return context[0:69] + '...'
  else:
    return context

#function to extract front part of context for organization
def busniess_org(context):
  if len(context) > 22:
   return context[0:19] + '...'
  else:
    return context

#function to extract front part of context for role
def busniess_role(context):
  if len(context) > 15:
   return context[0:12] + '...'
  else:
    return context

#function to extract front part of context for title
def busniess_title(context):
  if len(context) > 16:
   return context[0:13] + '...'
  else:
    return context

#function to extract front part of context for time
def business_time(context):
  if len(context) > 17:
    return context[0:14] + '...'
  else:
    return context
