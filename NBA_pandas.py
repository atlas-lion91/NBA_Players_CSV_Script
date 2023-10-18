import pandas as pd

# Load api_data.csv into dataframe bball_players
bball_players = pd.read_csv("nba_players.csv")

# Show the basic statistics of the 'id' column
print(bball_players['id'].describe())

# Find the number of unique positions in the 'position' column
unique_positions = bball_players['position'].nunique()
print(f"Number of unique positions: {unique_positions}")

# Rename the column names (assuming you want to rename all columns to lowercase)
bball_players.columns = [col.lower() for col in bball_players.columns]

# Display the first 5 rows
print(bball_players.head())

# Filter rows where the 'position' is 'C'
center_players = bball_players[bball_players['position'] == 'C']
print(center_players)

# Sort the DataFrame by 'last_name' in ascending order
sorted_df = bball_players.sort_values(by='last_name')
print(sorted_df)

# Group the DataFrame by 'team.full_name' and count players in each team
team_counts = bball_players.groupby('team').size()
print(team_counts)

# Select specific columns 'first_name' and 'last_name'
selected_columns = bball_players[['first_name', 'last_name']]
print(selected_columns)

# Create a new column 'full_name' by combining 'first_name' and 'last_name' with a space in between
bball_players['full_name'] = bball_players['first_name'] + ' ' + bball_players['last_name']

# Show the rows where 'team.full_name' contains the word 'Grizzlies'
grizzlies_players = bball_players[bball_players['team'].str.contains('Grizzlies')]
print(grizzlies_players)
