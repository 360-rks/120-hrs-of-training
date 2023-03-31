'''The International Cricket Council (ICC) wanted to do some 
analysis of international cricket matches held in last 
10 years.

Given a list containing match details as shown below:
[match_detail1,match_detail2……]

Format of each match_detail in the list is as shown below:
country_name : championship_name : total_number_of_matches_played : number_of_matches_won
Example: AUS:CHAM:5:2 means Australia has participated in 
Champions Trophy 5 times and have won 2 times.

Write a python program which performs the following:

find_matches (country_name): Accepts the country_name and 
returns the list of details of matches played by that country.
max_wins(): Returns a dictionary containing the championship name as the key and the list of country/countries which have won the maximum number of matches in that championship as the value.
find_winner(country1,country2): Accepts name of two countries and returns the country name which has won more number of matches in all championships. If both have won equal number of matches, return "Tie".
Perform case sensitive string comparison wherever necessary.
match_list – ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']

Sample Input	    Expected Output
find_matches ("AUS")	['AUS:CHAM:5:2', 'AUS:WOR:2:1']
max_wins()	{'WOR': ['AUS', 'IND'], 'CHAM': ['AUS'], 'T20': ['IND']}
find_winner("AUS","IND")	IND'''
match_list = ['ENG:WOR:2:0', 'AUS:CHAM:5:2', 'PAK:T20:5:1', 'AUS:WOR:2:1', 'SA:T20:5:0', 'IND:T20:5:3', 'PAK:WOR:2:0', 'SA:WOR:2:0', 'SA:CHAM:5:1', 'IND:WOR:2:1']

def find_matches(country_name):
    result = []
    for match in match_list:
        details = match.split(":")
        if details[0] == country_name:
            result.append(match)
    return result

def max_wins():
    result = {}
    for match in match_list:
        details = match.split(":")
        championship = details[1]
        country = details[0]
        wins = int(details[3])
        if championship not in result:
            result[championship] = [0, [country]]
        else:
            if wins > int(match_list[result[championship][0]].split(":")[3]):
                result[championship] = [match_list.index(match), [country]]
            elif wins == int(match_list[result[championship][0]].split(":")[3]):
                result[championship][1].append(country)
    return {k: v[1] for k, v in result.items()}


def find_winner(country1, country2):
    country1_wins = 0
    country2_wins = 0
    for match in match_list:
        details = match.split(":")
        if details[0] == country1:
            country1_wins += int(details[3])
        elif details[0] == country2:
            country2_wins += int(details[3])
    if country1_wins > country2_wins:
        return country1
    elif country2_wins > country1_wins:
        return country2
    else:
        return "Tie"
print(find_matches("AUS"))
print(max_wins())
print(find_winner("AUS","IND"))
