#!/usr/bin/python

#class setting

class Setting:

    url_query = 'https://www.googleapis.com/freebase/v1/search'
    url_mid   = 'https://www.googleapis.com/freebase/v1/topic'
    key = 'AIzaSyCnwZwSuROuYso7LLV4qcd-xfHvSph8XlY'

    #valid type for project2
    type_list = {   '/people/person': 'PERSON',
                    '/book/author'  : 'AUTHOR',
                    '/film/actor'   : 'ACTOR',
                    '/tv/tv_actor'  : 'ACTOR',
                    '/organization/organization_founder' : 'BUSNIESS',
                    '/business/board_member'    : 'BUSNIESS',
                    '/sports/sports_league'     : 'LEAGUE',
                    '/sports/sports_team'       : 'SPORTSTEAM',
                    '/sports/professional_sports_team'   : 'SPORTSTEAM'
    }
    str_white   = '|                '
    str_name    = '| Name:          '
    str_birth   = '| Birthday:      '
    str_bplace  = '| Place of birth:'
    str_death   = '| Death          '
    str_desp    = '| Descriptions:  '
    str_sib     = '| Siblings:      '
    str_spou    = '| Spouses:       '
    str_book    = '| Books:         '
    str_bookab  = '| Books about:   '
    str_influ   = '| Influenced:    '
    str_infu_by = '| Influenced by: '
    str_film    = '| Films:         |Character                              | Film Name                               |'
    str_f_white = '|               '
    str_f_bar   = '----------------------------------------------------------------------------------'
    str_founded = '| Founded:       '
    str_leadsh  = '| Leadership:    |Organization            | Role            | Title            | From-To           |'
    str_b_mem   = '| Board Member:  |Organization            | Role            | Title            | From/To           |'
    
    ## for groups 
    str_name    = '| Name:          '   ## same
    str_sport   = '| Sport:         '
    str_arena   = '| Arena:         '
    str_champion= '| Championship:  '   ## both used (but different content)
    str_founded = '| Founded:       '   ## same
    str_leagues = '| Leagues:       ' 
    str_location= '| Locations:     '
    str_coaches = '| Coaches:       |Name                    | Position                    | From/To                  |'
    str_playrstr= '| PlayersRoster: |Name             | Position             | Number             | From/To           |'
    str_desp    = '| Descriptions:  '   ## same       |
    str_slogan  = '| Slogan:        '
    str_website = '| Website:       '
    str_teams   = '| Teams:         '

    # #people
    # Person = ['/people/person']
    # Author = ['/book/author']
    # Actor = ['/film/actor','/tv/tv_actor']
    # BusinessPerson = ['/organization/organization_founder','/business/board_member']
    # #group
    # League = ['/sports/sports_league']
    # SportsTeam = ['/sports/sports_team','/sports/professional_sports_team']
    # #all
    # All_types = Person + Author + Actor + BusinessPerson + League + SportsTeam
