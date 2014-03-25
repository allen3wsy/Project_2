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


