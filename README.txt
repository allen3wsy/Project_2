##########################################################################################
##########################################  README ########################################


1. We classify all the types in “PERSON” and “not PERSON”. There is no overlap,
“PERSON” includes BusinessPerson, Actor and Author.
“not PERSON” includes League and SportsTeam.

Firstly we check whether this JSON file contains the ‘Person’, if it is, then we only output the attributes of PERSON. Otherwise it belongs to Group, then it should only output the attributes belonging to group.

For example, NFL is both LEAGUE and AUTHOR. But AUTHOR, BUSINESS_PERSON, ACTOR all belong to the person kind, so they should not be printed because NFL is already a group type. Then it should be National Football League(LEAGUE).
