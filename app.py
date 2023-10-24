#Import data
from constants import PLAYERS, TEAMS

team1 = []
team2 = []
team3 = []

experienced_players = []
inexperienced_players = []

# Clean player data
def clean_data(players):
	for player in players:
		# Height - integer
		height_int = player["height"].split()
		if height_int and height_int[0].isnumeric():
			player["height"] = int(height_int[0])
		# Experience
		if player["experience"] == "YES":
			player["experience"] = True
		else:
			player["experience"] = False
		# Guardian
		player["guardians"] = player["guardians"].split(" and ")

# Divide players into experienced and inexperienced groups
for player in PLAYERS:
	if player['experience'] == True:
		experienced_players.append(player)
	else:
		inexperienced_players.append(player)

# Create a menu function
def menu_screen():
	print("BASKETBALL TEAM STATS TOOL\n\n-----MENU-----\n")  
	print("Here are your options:")
	print(" A: Display Team Stats ")
	print(" B: Quit \n")

	while True:
		user_option = input("Please enter an option from the list:   ").strip().upper()
			
		if user_option == "A":
			team_choice = input("\nSelect from the teams below: \n 1: Panthers \n 2: Bandits \n 3: Warriors \n \nEnter an option:   ")
			team_choice = int(team_choice)-1

			# Check if the selected team is within the valid range
			if 0 <= team_choice < len(teams):
				team_name = TEAMS[team_choice]
				team_players = teams[team_choice]  
				team_stats = display_team_stats(team_players, [team_name])
				print(team_stats)

			else:
				print("Invalid team choice.")

		elif user_option == "B":
			print("Goodbye!")
			break

		else:
			print("Invalid option. Please enter 'A' or 'B'.")


# Save player data to new collection


# Create a balance_teams function
# Ensure teams have the same number of total players
def balance_teams():
	max_team_size = len(PLAYERS) // len(TEAMS)

	# Initialize empty teams
	teams = [[] for _ in range(len(TEAMS))]

	for player in experienced_players:
		for team in teams:
			if len(team) < max_team_size:
				team.append(player)


	for player in inexperienced_players:
		for team in teams:
			if len(team) < max_team_size:
				team.append(player)
				break

	return teams

teams = balance_teams()


# Display stats
def display_team_stats(team_players, team_names):
	team_stats = ""
	for i, team in enumerate(TEAMS):
		# Team's name as a string 
		team_name = team_names

		players = team_players
		# Total players on that team as an integer 
		num_players = len(players)

		# The player names as strings separated by commas 
		player_names = ', '.join([player["name"] for player in players])

		# number of inexperienced players on that team 
		num_inexperienced = sum(1 for player in players if player["experience"] is False)

		# number of experienced players on that team 
		num_experienced = num_players - num_inexperienced

		# the average height of the team 
		heights = [player["height"] for player in players if player["height"] is not None]
		average_height = sum(heights) / len(heights) if len(heights) > 0 else 0

		# the guardians of all the players on that team (as a comma-separated string)
		guardians = ', '.join([', '.join(player["guardians"]) for player in players])


		team_stats += f"Team: {team_name}\n"
		team_stats += f"Total Players: {num_players}\n"
		team_stats += f"Player Names: {player_names}\n"
		team_stats += f"Inexperienced Players: {num_inexperienced}\n"
		team_stats += f"Experienced Players: {num_experienced}\n"
		team_stats += f"Average Height: {average_height:.1f} inches\n"
		team_stats += f"Guardians: {guardians}\n\n"

	return team_stats


# Dunder main
if __name__ == "__main__":
	clean_data(PLAYERS)
	balance_teams()
	menu_screen()