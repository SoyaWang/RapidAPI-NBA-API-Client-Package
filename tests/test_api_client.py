import pytest
from unittest.mock import patch
from my_nba_api.api_client import NBAApiClient, RateLimitError, InvalidParameterError

# Mock API responses
MOCK_SEASONS_RESPONSE = {"seasons": ["2019", "2020", "2021"]}
MOCK_TEAM_SEARCH_RESPONSE = {"teams": [{"id": 1, "name": "Atlanta Hawks"}]}
MOCK_PLAYER_SEARCH_RESPONSE = {"players": [{"id": 1, "firstName": "LeBron", "lastName": "James"}]}

@pytest.fixture
def client():
    """Fixture for NBAApiClient instance."""
    return NBAApiClient(api_key="test_api_key")

@patch("requests.get")
def test_get_seasons(mock_get, client):
    """Test fetching seasons."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = MOCK_SEASONS_RESPONSE

    response = client.get_seasons()
    assert response == MOCK_SEASONS_RESPONSE
    mock_get.assert_called_once_with(
        "https://api-nba-v1.p.rapidapi.com/seasons",
        headers=client.headers,
        params=None,
    )

@patch("requests.get")
def test_search_teams(mock_get, client):
    """Test searching teams."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = MOCK_TEAM_SEARCH_RESPONSE

    response = client.search_teams(query="atl")
    assert response == MOCK_TEAM_SEARCH_RESPONSE
    mock_get.assert_called_once_with(
        "https://api-nba-v1.p.rapidapi.com/teams",
        headers=client.headers,
        params={"search": "atl"},
    )

@patch("requests.get")
def test_search_players(mock_get, client):
    """Test searching players."""
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = MOCK_PLAYER_SEARCH_RESPONSE

    response = client.search_players(query="james")
    assert response == MOCK_PLAYER_SEARCH_RESPONSE
    mock_get.assert_called_once_with(
        "https://api-nba-v1.p.rapidapi.com/players",
        headers=client.headers,
        params={"search": "james"},
    )

@patch("requests.get")
def test_rate_limit_error(mock_get, client):
    """Test rate limit error handling."""
    mock_get.return_value.status_code = 429
    with pytest.raises(RateLimitError, match="API rate limit exceeded"):
        client.get_seasons()

@patch("requests.get")
def test_invalid_parameter_error(mock_get, client):
    """Test invalid parameter error handling."""
    mock_get.return_value.status_code = 400
    mock_get.return_value.json.return_value = {"message": "Invalid parameter"}

    with pytest.raises(InvalidParameterError, match="Invalid parameters: Invalid parameter"):
        client.get_games_by_date(date="invalid_date")

