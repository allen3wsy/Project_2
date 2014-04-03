from setting import Setting

class Info_box_group:

    def __init__(self, json_doc, type_list, types):

    	self.json_doc = json_doc
    	self.type_list = type_list
    	self.types = types #set
  

    def generate_info_box(self):
        setting = Setting
        property_dict = self.json_doc['property']
        #width of infobox = 98 * '-' (the same in the group info box)
        width = 100
        
        bar = ' --------------------------------------------------------------------------------------------------'
        print bar


      	# for leagues:       	
      	    #text for name
        str_name = property_dict['/type/object/name']['values'][0]['text']
        
        #text for types
        str_type = ''
        for string in self.types:
            if ((string != 'AUTHOR') and (string != 'BUSINESS') and (string != 'ACTOR')):
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
        
        # sport (optional)
        if property_dict.has_key("/sports/sports_league/sport"):

            str_sport = property_dict["/sports/sports_league/sport"]["values"][0]["text"]
            # text for name of sport
            print setting.str_sport,
            print '{0:<81s}|' .format(str_sport)
            print bar


      	# slogan (optional)
        if property_dict.has_key("/organization/organization/slogan"):
            str_slogan = property_dict["/organization/organization/slogan"]["values"][0]["text"]

            # text for slogan
            print setting.str_slogan,
            print '{0:<81s}|' .format(str_slogan)
            print bar

        # website 
        if "LEAGUE" in self.types:
            if property_dict.has_key("/common/topic/official_website"):
                
                list_website = []

                for i in range(len(property_dict["/common/topic/official_website"]["values"])):
                    list_website.append(property_dict["/common/topic/official_website"]["values"][i]["text"])
                
                str_website = ""
                for i in range(len(list_website)):
                    str_website += list_website[i]

                    if i != (len(list_website) - 1):
                        str_website += ", "

                # text for slogan
                print setting.str_website,
                print '{0:<81s}|' .format(str_website)
                print bar

       
      	# chapionship (optional)
        if property_dict.has_key("/sports/sports_league/championship"):
            str_champion = property_dict["/sports/sports_league/championship"]["values"][0]["text"].encode("utf-8")

            # text for slogan
            print setting.str_champion,
            print '{0:<81s}|' .format(str_champion)
            print bar

      	# teams
        if property_dict.has_key("/sports/sports_league/teams"):
            list_teams = []
            for team in property_dict["/sports/sports_league/teams"]["values"]:
                list_teams.append(team["property"]["/sports/sports_league_participation/team"]["values"][0]["text"])
            
            for i in range(len(list_teams)):
                if i == 0:
                    print setting.str_teams, "{0:<81s}|".format(list_teams[i].encode('utf-8'))
            # text for slogan
                else:
                    print setting.str_white, 
                    print "{0:<81s}|".format(list_teams[i].encode('utf-8'))
            print bar

        
        ###########################################################################################################################
        ## for Sports Team

        # text for Sport
        if property_dict.has_key("/sports/sports_team/sport"):
            str_sport = property_dict["/sports/sports_team/sport"]['values'][0]['text']
            print setting.str_sport,
            print '{0:<81s}|' .format(str_sport)
            print bar
            
        # text for Arena
        if property_dict.has_key("/sports/sports_team/arena_stadium"):
            str_arena = property_dict["/sports/sports_team/arena_stadium"]['values'][0]['text']
            print setting.str_arena,
            print '{0:<81s}|' .format(str_arena)
            print bar


        # text for Championships
        if property_dict.has_key("/sports/sports_team/championships"):
            
            list_champion = []
            for champion in property_dict["/sports/sports_team/championships"]['values']:
                list_champion.append(champion['text'].encode("utf-8"))
            
            for i in range(len(list_champion)):
                if i == 0 :
                    print setting.str_champion,
                    print '{0:<81s}|' .format(list_champion[i])
                else:
                    print setting.str_white,
                    print '{0:<81s}|' .format(list_champion[i])
            print bar

        # text for sports team founded
        if property_dict.has_key("/sports/sports_team/founded"):
            str_founded = property_dict["/sports/sports_team/founded"]['values'][0]['text'].encode("utf-8")
            print setting.str_founded,
            print '{0:<81s}|' .format(str_founded)
            print bar


        # text for sports league ( can be in more than one leagues)
        if property_dict.has_key("/sports/sports_team/league"):
            list_teams = []
            for team in property_dict["/sports/sports_team/league"]["values"]:
                list_teams.append(team["property"]["/sports/sports_league_participation/league"]["values"][0]["text"])
            
            for i in range(len(list_teams)):
                if i == 0:
                    print setting.str_leagues, "{0:<81s}|".format(list_teams[i].encode('utf-8'))
            
                else:
                    print setting.str_white, 
                    print "{0:<81s}|".format(list_teams[i].encode('utf-8'))
            print bar

        # for sports team locations
        if property_dict.has_key("/sports/sports_team/location"):
            str_location = property_dict["/sports/sports_team/location"]['values'][0]['text'].encode("utf-8")
            print setting.str_location,
            print '{0:<81s}|' .format(str_location)
            print bar

        # text for sports team Coaches
        if property_dict.has_key("/sports/sports_team/coaches"):
            print setting.str_coaches

            # list for names
            list_names = [] #(could be none)
            # list for positions
            list_positions = []

            # list for from_To 
            list_from = []
            list_to = []

            for coach in property_dict["/sports/sports_team/coaches"]['values']:
                # name
                if coach['property'].has_key("/sports/sports_team_coach_tenure/coach"):
                    list_names.append(coach['property']["/sports/sports_team_coach_tenure/coach"]['values'][0]['text']) #character name
                else:
                    list_names.append('')

                # Position
                if coach['property'].has_key("/sports/sports_team_coach_tenure/position"):
                    list_positions.append(coach['property']["/sports/sports_team_coach_tenure/position"]['values'][0]['text']) #character name
                else:
                    list_positions.append('')

                # From / To
                if coach['property'].has_key("/sports/sports_team_coach_tenure/from"):
                    list_from.append(coach['property']["/sports/sports_team_coach_tenure/from"]['values'][0]['text']) #character name
                else:
                    list_from.append('N/A')     

                if coach['property'].has_key("/sports/sports_team_coach_tenure/to") and len(coach['property']["/sports/sports_team_coach_tenure/to"]['values']) != 0:
                    list_to.append(coach['property']["/sports/sports_team_coach_tenure/to"]['values'][0]['text']) 
                else:
                    list_to.append('now')  

            print setting.str_f_white,
            print setting.str_f_bar
            for i in range(len(property_dict["/sports/sports_team/coaches"]['values'])):
                print setting.str_f_white,
                print '|{0:<24s}|' .format(list_names[i].encode('utf-8')),
                print '{0:<28s}|' .format(list_positions[i]),
                ft = list_from[i] + ' / ' + list_to[i]
                print '{0:<25s}|' .format(ft)

            print bar


        # Player Roster
        # name position number From/To

        if property_dict.has_key("/sports/sports_team/roster"):
            print setting.str_playrstr
            print setting.str_f_white,
            print setting.str_f_bar
            
            list_player_roster = []

            # store data into the temp_list

            temp_list = property_dict["/sports/sports_team/roster"]['values']
             
            for index in range(len(temp_list)):

                ## every time we append an empty dictionary
                list_player_roster.append({'name': '', 'position': '', 'number': '', 'from' : '', 'to': ''})
              
                # name
                if temp_list[index]['property'].has_key("/sports/sports_team_roster/player"):
                    list_player_roster[index]['name'] = temp_list[index]['property']["/sports/sports_team_roster/player"]['values'][0]['text']
                
                ## position
                ## but there may be many positions ...
                if temp_list[index]['property'].has_key("/sports/sports_team_roster/position"):
                    
                    position_length = len(temp_list[index]['property']["/sports/sports_team_roster/position"]['values'])

                    for i in range(position_length):
                        list_player_roster[index]['position'] += temp_list[index]['property']["/sports/sports_team_roster/position"]['values'][i]['text']
                        if i != (position_length - 1):
                            list_player_roster[index]['position'] += ', '

                    # list_player_roster[index]['position'] = temp_list[index]['property']["/sports/sports_team_roster/position"]['values'][0]['text']
                
                # number
                if temp_list[index]['property'].has_key("/sports/sports_team_roster/number") and len(temp_list[index]['property']["/sports/sports_team_roster/number"]['values']) != 0:
                    list_player_roster[index]['number'] = temp_list[index]['property']["/sports/sports_team_roster/number"]['values'][0]['text']
                
                # from
                if temp_list[index]['property'].has_key("/sports/sports_team_roster/from"):
                    list_player_roster[index]['from'] = temp_list[index]['property']["/sports/sports_team_roster/from"]['values'][0]['text']
                
                # to
                if temp_list[index]['property'].has_key("/sports/sports_team_roster/to") and len(temp_list[index]['property']["/sports/sports_team_roster/to"]['values']) != 0:
                    list_player_roster[index]['to'] = temp_list[index]['property']["/sports/sports_team_roster/to"]['values'][0]['text']
                else:
                    if temp_list[index]['property'].has_key("/sports/sports_team_roster/from"):
                        list_player_roster[index]['to'] = 'now'

            # print out the data

            for i in range(len(list_player_roster)):
                print setting.str_f_white,
                print '|{0:<17s}|' .format(extract_name(list_player_roster[i]['name'].encode('utf-8'))),
                print '{0:<21s}|' .format(extract_position(list_player_roster[i]['position'].encode('utf-8'))),
                print '{0:<19s}|' .format(list_player_roster[i]['number'].encode('utf-8')),
              

                str_from_to = list_player_roster[i]['from'] + ' / ' + list_player_roster[i]['to']

                print '{0:<18s}|' .format(extract_from_to(str_from_to))
            
            print bar

      	# description (last) (for both LEAGUES and Sports Team !!!)
        str_description = property_dict['/common/topic/description']['values'][0]['value'].encode('utf-8').replace('\n',' ')
        print setting.str_desp,
        lines = int(len(str_description)//81)
        end_line = len(str_description)%81
        
        if lines < 1: #one line
            print '{0:<81s}|' .format(str_description)
        else: #multiple lines
            print '{0:<81s}|' .format(str_description[0:81])
            if lines > 1:
                for n in range(lines - 1):
                    print setting.str_white,
                    print '{0:<81s}|' .format(str_description[(n+1)*81+0:(n+1)*81+81])
            if end_line == 0:
                pass #do nothing
            else:
                print setting.str_white,
                print '{0:<81s}|' .format(str_description[lines*81:])

        print bar



#function to extract front part of content for name
def extract_name(content):
    if len(content) > 17:
        return content[0:14] + '...'
    else:
        return content

#function to extract front part of content for position
def extract_position(content):
    if len(content) > 21:
        return content[0:18] + '...'
    else:
        return content

#function to extract front part of content for from_to
def extract_from_to(content):
    if len(content) > 18:
        return content[0:15] + '...'
    else:
        return content