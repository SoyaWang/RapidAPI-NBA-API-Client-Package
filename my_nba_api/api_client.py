import requests
import urllib.parse
from typing import Optional, Dict, Any


class NBAApiError(Exception):
    """Base class for NBA API exceptions"""
    pass


class RateLimitError(NBAApiError):
    """Raised when the API rate limit is exceeded"""
    pass


class InvalidParameterError(NBAApiError):
    """Raised when invalid parameters are provided"""
    pass


class NBAApiClient:
    BASE_URL = "https://api-nba-v1.p.rapidapi.com"

    def __init__(self, api_key: str):
        """
        Initialize the API client with an API key
        :param api_key: Your RapidAPI key
        """
        if not api_key:
            raise ValueError("API key must be provided.")
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "api-nba-v1.p.rapidapi.com",
        }

    def _request(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict:
        """
        Send an HTTP GET request to the NBA API
        :param endpoint: API endpoint
        :param params: Optional query parameters
        :return: Parsed JSON response
        """
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 429:
            raise RateLimitError("API rate limit exceeded. Please try again later.")
        elif response.status_code == 400:
            raise InvalidParameterError(f"Invalid parameters: {response.json().get('message', '')}")
        elif response.status_code != 200:
            raise NBAApiError(f"Error {response.status_code}: {response.text}")

        return response.json()

    # ---- Season Data ----
    def get_seasons(self) -> Dict:
        """
        Fetch all available seasons.
        :return: List of available seasons in JSON format
        """
        # Define the endpoint
        endpoint = "seasons"

        # Perform the API request
        return self._request(endpoint)
    
    # ---- League Data ----
    def get_leagues(self) -> Dict:
        """
        Fetch all available leagues.
        :return: List of available leagues in JSON format
        """
        # Define the endpoint
        endpoint = "leagues"

        # Perform the API request
        return self._request(endpoint)
    
    # ---- Game Data ----
    # Fetch games by date
    def get_games_by_date(self, date: str) -> Dict:
        """
        Fetch games by a specific date.
        :param date: The date to fetch games for (YYYY-MM-DD).
        :return: Game data in JSON format.
        """
        if not date:
            raise ValueError("Date parameter must be provided.")    
        params = {"date": date}
        return self._request("games", params=params)

    # Fetch head-to-head games between two teams
    def get_games_h2h(self, team1_id: int, team2_id: int) -> Dict:
        """
        Fetch head-to-head games between two teams.
        :param team1_id: ID of the first team.
        :param team2_id: ID of the second team.
        :return: Game data in JSON format.
        """
        params = {"h2h": f"{team1_id}-{team2_id}"}
        return self._request("games", params=params)

    # Fetch all live games
    def get_live_games(self) -> Dict:
        """
        Fetch all live games.
        :return: Live game data in JSON format.
        """
        params = {"live": "all"}
        return self._request("games", params=params)

    # Fetch games by season
    def get_games_by_season(self, season: int) -> Dict:
        """
        Fetch games for a specific season.
        :param season: The season to fetch games for (e.g., 2021).
        :return: Game data in JSON format.
        """
        params = {"season": season}
        return self._request("games", params=params)

    # Fetch games by season and team
    def get_games_by_season_and_team(self, season: int, team_id: int) -> Dict:
        """
        Fetch games for a specific season and team.
        :param season: The season to fetch games for (e.g., 2021).
        :param team_id: The ID of the team.
        :return: Game data in JSON format.
        """
        if not team_id:
            raise ValueError("Team ID must be provided.")
        params = {"season": season, "team": team_id}
        return self._request("games", params=params)

    # Fetch a specific game by ID
    def get_game_by_id(self, game_id: int) -> Dict:
        """
        Fetch a specific game by its ID.
        :param game_id: The ID of the game.
        :return: Game data in JSON format.
        """
        if not game_id:
            raise ValueError("Game ID must be provided.")
        params = {"id": game_id}
        return self._request("games", params=params)
    
    # ---- Team Data ----
    # Fetch all teams
    def get_all_teams(self) -> Dict:
        """
        Fetch all teams.
        :return: All teams data in JSON format.
        """
        return self._request("teams")

    # Fetch teams by conference
    def get_teams_by_conference(self, conference: str) -> Dict:
        """
        Fetch teams by conference.
        :param conference: Conference name (e.g., "East", "West").
        :return: Teams data in JSON format.
        """
        params = {"conference": conference}
        return self._request("teams", params=params)

    # Fetch teams by division
    def get_teams_by_division(self, division: str) -> Dict:
        """
        Fetch teams by division.
        :param division: Division name (e.g., "Southeast").
        :return: Teams data in JSON format.
        """
        params = {"division": division}
        return self._request("teams", params=params)

    # Fetch teams by code
    def get_teams_by_code(self, code: str) -> Dict:
        """
        Fetch teams by code.
        :param code: Team code (e.g., "ATL" for Atlanta Hawks).
        :return: Teams data in JSON format.
        """
        params = {"code": code}
        return self._request("teams", params=params)

    # Fetch team by ID
    def get_team_by_id(self, team_id: int) -> Dict:
        """
        Fetch team by ID.
        :param team_id: The ID of the team.
        :return: Team data in JSON format.
        """
        if not team_id:
            raise ValueError("Team ID must be provided.")
        params = {"id": team_id}
        return self._request("teams", params=params)
    
    # ---- Player Data ----
    # Fetch players by team and season
    def get_players_by_team_and_season(self, team_id: int, season: int) -> Dict:
        """
        Fetch players by team and season.
        :param team_id: The ID of the team.
        :param season: The season to fetch players for.
        :return: Player data in JSON format.
        """
        if not team_id:
            raise ValueError("Team ID must be provided.")
        params = {"team": team_id, "season": season}
        return self._request("players", params=params)

    # Fetch player by ID
    def get_player_by_id(self, player_id: int) -> Dict:
        """
        Fetch player data by player ID.
        :param player_id: The ID of the player.
        :return: Player data in JSON format.
        """
        if not player_id:
            raise ValueError("Player ID must be provided.")
        params = {"id": player_id}
        return self._request("players", params=params)

    # Fetch players by country
    def get_players_by_country(self, country: str) -> Dict:
        """
        Fetch players by country.
        :param country: The country to filter players by.
        :return: Player data in JSON format.
        """
        params = {"country": country}
        return self._request("players", params=params)
    
    # ---- Standing Data----
    # Fetch standings by league and season
    def get_standings_by_season(self, league: str, season: int) -> Dict:
        """
        Fetch standings by league and season.
        :param league: The league type (e.g., "standard").
        :param season: The season to fetch standings for.
        :return: Standings data in JSON format.
        """
        params = {"league": league, "season": season}
        return self._request("standings", params=params)

    # Fetch standings by league, season, and conference
    def get_standings_by_conference(self, league: str, season: int, conference: str) -> Dict:
        """
        Fetch standings by league, season, and conference.
        :param league: The league type (e.g., "standard").
        :param season: The season to fetch standings for.
        :param conference: The conference name (e.g., "east").
        :return: Standings data in JSON format.
        """
        params = {"league": league, "season": season, "conference": conference}
        return self._request("standings", params=params)

    # Fetch standings by league, season, and division
    def get_standings_by_division(self, league: str, season: int, division: str) -> Dict:
        """
        Fetch standings by league, season, and division.
        :param league: The league type (e.g., "standard").
        :param season: The season to fetch standings for.
        :param division: The division name (e.g., "southeast").
        :return: Standings data in JSON format.
        """
        params = {"league": league, "season": season, "division": division}
        return self._request("standings", params=params)

    # Fetch standings by league, season, and team
    def get_standings_by_team(self, league: str, season: int, team_id: int) -> Dict:
        """
        Fetch standings by league, season, and team.
        :param league: The league type (e.g., "standard").
        :param season: The season to fetch standings for.
        :param team_id: The team ID.
        :return: Standings data in JSON format.
        """
        if not team_id:
            raise ValueError("Team ID must be provided.")
        params = {"league": league, "season": season, "team": team_id}
        return self._request("standings", params=params)
    
    # ---- Statistics Data ----
    # Fetch game statistics by game ID
    def get_game_statistics(self, game_id: int) -> Dict:
        """
        Fetch game statistics by game ID.
        :param game_id: The ID of the game.
        :return: Game statistics in JSON format.
        """
        if not game_id:
            raise ValueError("Game ID must be provided.")
        params = {"id": game_id}
        return self._request("games/statistics", params=params)

    # Fetch team statistics by team ID and season
    def get_team_statistics(self, team_id: int, season: int) -> Dict:
        """
        Fetch team statistics by team ID and season.
        :param team_id: The ID of the team.
        :param season: The season for which to fetch statistics.
        :return: Team statistics in JSON format.
        """
        params = {"id": team_id, "season": season}
        return self._request("teams/statistics", params=params)

    # Fetch player statistics by player ID and season
    def get_player_statistics(self, player_id: int, season: int) -> Dict:
        """
        Fetch player statistics by player ID and season.
        :param player_id: The ID of the player.
        :param season: The season for which to fetch statistics.
        :return: Player statistics in JSON format.
        """
        if not player_id:
            raise ValueError("Player ID must be provided.")
        params = {"id": player_id, "season": season}
        return self._request("players/statistics", params=params)

    # Fetch statistics for all players in a team for a specific season
    def get_team_players_statistics(self, team_id: int, season: int) -> Dict:
        """
        Fetch statistics for all players in a team for a specific season.
        :param team_id: The ID of the team.
        :param season: The season for which to fetch statistics.
        :return: Team players' statistics in JSON format.
        """
        if not team_id:
            raise ValueError("Team ID must be provided.")
        params = {"team": team_id, "season": season}
        return self._request("players/statistics", params=params)

    # Fetch statistics for all players in a specific game
    def get_game_players_statistics(self, game_id: int) -> Dict:
        """
        Fetch statistics for all players in a specific game.
        :param game_id: The ID of the game.
        :return: Game players' statistics in JSON format.
        """
        if not game_id:
            raise ValueError("Game ID must be provided.")
        params = {"game": game_id}
        return self._request("players/statistics", params=params)
    
    # ----Search Data----
    # Search teams by name or keyword
    def search_teams(self, query: str) -> Dict:
        """
        Search teams by name or keyword.
        :param query: The search keyword for the team name.
        :return: Matching teams in JSON format.
        """
        if not query:
            raise ValueError("Query parameter must be provided for team search.")
        params = {"search": query}
        return self._request("teams", params=params)

    # Search players by name or keyword
    def search_players(self, query: str) -> Dict:
        """
        Search players by name or keyword.
        :param query: The search keyword for the player name.
        :return: Matching players in JSON format.
        """
        if not query:
            raise ValueError("Query parameter must be provided for player search.")
        params = {"search": query}
        return self._request("players", params=params)
    






