#!/usr/bin/env python3

matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(f"matches = {matches}")
print(f"Matches len = {len(matches)}")

new_list = list(filter(lambda item: item['home_team_result'] == 'Win',
                       matches))
print(f"new_list = {new_list}")
print(f"new_list len = {len(new_list)}")
