from my_nba_api.api_client import NBAApiClient

# Replace "your_api_key" with your actual RapidAPI key
client = NBAApiClient(api_key="Your-API-Key")

# Fetch all available seasons
print("\n=== Fetching Available Seasons ===")
seasons = client.get_seasons()
print(seasons)

# Fetch all available leagues
print("\n=== Fetching Available Leagues ===")
leagues = client.get_leagues()
print(leagues)

# Fetch games by season and team
print("\n=== Fetching Games by Season and Team ===")
games_by_season_and_team = client.get_games_by_season_and_team(season=2021, team_id=1)
print(games_by_season_and_team)

# Fetch a specific game by ID
print("\n=== Fetching Game by ID ===")
game_by_id = client.get_game_by_id(game_id=8899)
print(game_by_id)

# Fetch standings by division
print("\n=== Fetching Standings by League (Standard) & Season (2021) & Division (Southeast) ===")
standings_by_division = client.get_standings_by_division(
    league="standard", season=2021, division="southeast")

# Fetch teams by code
print("\n=== Fetching Teams by Code (ATL) ===")
teams_by_code = client.get_teams_by_code(code="ATL")
print(teams_by_code)

# Fetch player by ID
print("\n=== Fetching Player by ID 1 ===")
player_by_id = client.get_player_by_id(player_id=1)
print(player_by_id)

# Fetch players by country (e.g., Spain)
print("\n=== Fetching Players by Country (Spain) ===")
players_by_country = client.get_players_by_country(country="spain")
print(players_by_country)

# Fetch player statistics by player ID and season
print("\n=== Fetching Player Statistics for Player ID 236 and Season 2020 ===")
player_stats = client.get_player_statistics(player_id=236, season=2020)
print(player_stats)

# Search for players by keyword
print("\n=== Searching for Players with keyword 'james' ===")
players = client.search_players(query="james")
print(players)