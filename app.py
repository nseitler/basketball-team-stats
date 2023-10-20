#Import data
import constants

# Clean player data
def clean_data():
	for player in players:
		# Height
		player["height"] = int(player["height"][0])
		# Experience
		if player["experience"] == "YES":
			player["experience"] = True
		else:
			player["experience"] = False
		# Guardian
		player["guardians"] = player["guardians"].split(" and ")

# Create a menu function
def menu_screen():
	print("BASKETBALL TEAM STATS TOOL")  
	print("----MENU--- \n")
	Print("Here are your options:")
	print("1: Display Team Stats ")
	print("2: Quit ")
	while True:
		user_option = input("Please enter an option from the list:  ")
		if user_option == "1"
		team_choice = input("Select from the teams below: \n 1: Panthers \n 2: Bandits \n 3: Warriors")
		team_choice = int(team_choice)-1

# Save player data to new collection


# Create a balance_teams function
# Ensure teams have the same number of total players
def balance_teams():
	Panthers = []
	Bandits = []
	Warriors = []
	
	max_team = len(PLAYERS) / len(TEAMS)

	experienced_players = [player["name"] for player in players if player["experience"] == True]
	max_experienced_players = len(experienced_players) / len(TEAMS)
	inexperienced_players = [player["name"] for player in players if player["experience"] == False]
	max_inexperienced_players = len(inexperienced_players) / len(TEAMS)
	
	for team in teams:
		while num_players_team(team) < max_team:



# Display stats
def display_team_stats():
	team = teams[]
	print("")

	# Team's name as a string
	print("")
	# Total players on that team as an integer
	print("Total players: {}".format(experienced_players))
	# The player names as strings separated by commas
	print("Player names: ")
	# number of inexperienced players on that team
	print("Inexperienced players: {}".format(inexperienced_players)
	# number of experienced players on that team
	print("Experienced players: {}".format(experienced_players)
	# the average height of the team
	print("Average height: ") round(sum([player["height"] for player in team])  / len(players_on_team), 2)
	# the guardians of all the players on that team (as a comma-separated string)
	print("Guardian list: ")


# Dunder main
if __name__ == "__main__":
	main()