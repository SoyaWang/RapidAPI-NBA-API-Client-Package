from my_nba_api.api_client import NBAApiClient

# Replace "your_api_key" with your actual RapidAPI key
client = NBAApiClient(api_key="Your-API-Key")

# ----Fetch Season----
# Fetch all available seasons
print("\n=== Fetching Available Seasons ===")
seasons = client.get_seasons()
print(seasons)

# ----Fetch League----
# Fetch all available leagues
print("\n=== Fetching Available Leagues ===")
leagues = client.get_leagues()
print(leagues)

# ----Fetch Games----
# Fetch games by date
print("\n=== Fetching Games by Date ===")
games_by_date = client.get_games_by_date(date="2022-02-12")
print(games_by_date)

# Fetch head-to-head games between two teams
print("\n=== Fetching Head-to-Head Games ===")
games_h2h = client.get_games_h2h(team1_id=1, team2_id=2)
print(games_h2h)

# Fetch all live games
print("\n=== Fetching Live Games ===")
live_games = client.get_live_games()
print(live_games)

# Fetch games by season
print("\n=== Fetching Games by Season ===")
games_by_season = client.get_games_by_season(season=2021)
print(games_by_season)

# Fetch games by season and team
print("\n=== Fetching Games by Season and Team ===")
games_by_season_and_team = client.get_games_by_season_and_team(season=2021, team_id=1)
print(games_by_season_and_team)

# Fetch a specific game by ID
print("\n=== Fetching Game by ID ===")
game_by_id = client.get_game_by_id(game_id=8899)
print(game_by_id)

# ---- Fetch Teams----
# Fetch all teams
print("\n=== Fetching All Teams ===")
all_teams = client.get_all_teams()
print(all_teams)

# Fetch teams by conference
print("\n=== Fetching Teams by Conference (East) ===")
teams_by_conference = client.get_teams_by_conference(conference="East")
print(teams_by_conference)

# Fetch teams by division
print("\n=== Fetching Teams by Division (Southeast) ===")
teams_by_division = client.get_teams_by_division(division="Southeast")
print(teams_by_division)

# Fetch teams by code
print("\n=== Fetching Teams by Code (ATL) ===")
teams_by_code = client.get_teams_by_code(code="ATL")
print(teams_by_code)

# Fetch team by ID
print("\n=== Fetching Team by ID (1) ===")
team_by_id = client.get_team_by_id(team_id=1)
print(team_by_id)

# ---- Fetch Players----
# Fetch players by team and season
print("\n=== Fetching Players by Team ID 1 and Season 2021 ===")
players_by_team_and_season = client.get_players_by_team_and_season(team_id=1, season=2021)
print(players_by_team_and_season)

# Fetch player by ID
print("\n=== Fetching Player by ID 1 ===")
player_by_id = client.get_player_by_id(player_id=1)
print(player_by_id)

# Fetch players by country (e.g., Spain)
print("\n=== Fetching Players by Country (Spain) ===")
players_by_country = client.get_players_by_country(country="spain")
print(players_by_country)

# ---- Fetch Standings----
# Fetch standings by season
print("\n=== Fetching Standings by League (standard) & Season (2021) ===")
standings_by_season = client.get_standings_by_season(league="standard", season=2021)
print(standings_by_season)

# Fetch standings by conference
print("\n=== Fetching Standings by League (standard) & Season (2021) & Conference (East) ===")
standings_by_conference = client.get_standings_by_conference(
    league="standard", season=2021, conference="east"
)
print(standings_by_conference)

# Fetch standings by division
print("\n=== Fetching Standings by League (Standard) & Season (2021) & Division (Southeast) ===")
standings_by_division = client.get_standings_by_division(
    league="standard", season=2021, division="southeast"
)
print(standings_by_division)

# Fetch standings by team
print("\n=== Fetching Standings by League (Standard) & Season (2021) & Team ID (1) ===")
standings_by_team = client.get_standings_by_team(
    league="standard", season=2021, team_id=1
)
print(standings_by_team)

# ----Fetch Statistics----
# Fetch game statistics by game ID
print("\n=== Fetching Game Statistics for Game ID 10403 ===")
game_stats = client.get_game_statistics(game_id=10403)
print(game_stats)

# Fetch team statistics by team ID and season
print("\n=== Fetching Team Statistics for Team ID 1 and Season 2020 ===")
team_stats = client.get_team_statistics(team_id=1, season=2020)
print(team_stats)

# Fetch player statistics by player ID and season
print("\n=== Fetching Player Statistics for Player ID 236 and Season 2020 ===")
player_stats = client.get_player_statistics(player_id=236, season=2020)
print(player_stats)

# Fetch statistics for all players in a team for a specific season
print("\n=== Fetching Team Players' Statistics for Team ID 1 and Season 2020 ===")
team_players_stats = client.get_team_players_statistics(team_id=1, season=2020)
print(team_players_stats)

# Fetch statistics for all players in a specific game
print("\n=== Fetching Game Players' Statistics for Game ID 8133 ===")
game_players_stats = client.get_game_players_statistics(game_id=8133)
print(game_players_stats)

# ----Fetch Search Data----
# Search for teams by keyword
print("\n=== Searching for Teams with keyword 'atl' ===")
teams = client.search_teams(query="atl")
print(teams)

# Search for players by keyword
print("\n=== Searching for Players with keyword 'james' ===")
players = client.search_players(query="james")
print(players)
