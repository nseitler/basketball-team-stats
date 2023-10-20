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
	print("----MENU---")
	Print("Here are your choices: \n")
	print("A Display Team stats ")
	print("B Quit ")


# Save player data to new collection


# Create a balance_teams function
# Ensure teams have the same number of total players
def balance_teams():
	Panthers = []
	Bandits = []
	Warriors = []
	
	num_players_team = len(PLAYERS) / len(TEAMS)

	experienced_players = 

	inexperienced_players = 



# Display stats
def display_team_stats():


	# Team's name as a string

	# Total players on that team as an integer

	# The player names as strings separated by commas

	# number of inexperienced players on that team

	# number of experienced players on that team

	# the average height of the team

	# the guardians of all the players on that team (as a comma-separated string)



# Dunder main
if __name__ == "__main__":
	main()