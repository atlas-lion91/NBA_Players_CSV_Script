import json
import requests
import csv

# Set up headers for the request
headers = {'X-RapidAPI-Key': '',
'X-RapidAPI-Host': 'free-nba.p.rapidapi.com'}

# Step 1: Retrieve JSON data using the requests module with headers
url = "https://free-nba.p.rapidapi.com/players"
response = requests.get(url, headers=headers)

#  Set up Error Handling
if response.status_code != 200:
    print(f"Error: Unable to retrieve API data. Status code: (response.status_code)")
else:
    print(response.text)

data = response.json()

if 'data' not in data:
    print("Error: The key 'data' is not present")
    print(data)
    exit()


# Step 2: Extract required details for each player
players = data['data']
player_details = []
for player in players:
    player_info = {
        'id': player['id'],
        'first_name': player['first_name'],
        'last_name': player['last_name'],
        'position': player['position'],
        'team': player['team']['full_name']
    }
    player_details.append(player_info)

# Step 3: Write the details to a CSV file
with open('nba_players.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'first_name', 'last_name', 'position', 'team']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for player in player_details:
        writer.writerow(player)

print("CSV file created successfully!")
