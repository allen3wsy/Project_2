#!/usr/bin/python

#class setting

class Setting:

    url_query = 'https://www.googleapis.com/freebase/v1/search'
    url_mid   = 'https://www.googleapis.com/freebase/v1/topic'
    key = 'AIzaSyCnwZwSuROuYso7LLV4qcd-xfHvSph8XlY'

    #valid type for project2
    type_list = {   '/people/person': 'Person',
                    '/book/author'  : 'Author',
                    '/film/actor'   : 'Actor',
                    '/tv/tv_actor'  : 'Actor',
                    '/organization/organization_founder' : 'BusinessPerson',
                    '/business/board_member'    : 'BusinessPerson',
                    '/sports/sports_league'     : 'League',
                    '/sports/sports_team'       : 'SportsTeam',
                    '/sports/professional_sports_team'   : 'SportsTeam'
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


