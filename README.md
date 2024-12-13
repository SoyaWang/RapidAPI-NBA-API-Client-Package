<<<<<<< HEAD
# RapidAPI-NBA-API-Client-Package
A Python client for the RapAPI API-NBA in RapidAPI 
=======
# My NBA API

**My NBA API** is a Python client library for interacting with the **[RapidAPI NBA API](https://rapidapi.com/api-sports/api/api-nba)**. It provides an easy-to-use interface for fetching NBA-related data such as player statistics, team information, game results, and schedules. The library abstracts the complexity of HTTP requests and focuses on delivering simple and intuitive methods for developers.

---

# NBA API Client

A Python client for interacting with the [NBA API](https://rapidapi.com/api-sports/api/api-nba/). This library provides a simple interface to access NBA data, including teams, players, games, standings, and statistics.

## Features

- Fetch data for **seasons**, **leagues**, **teams**, **players**, **games**, **standings**, and **statistics**.
- Support for searching teams and players by name or keyword.
- Error handling for API rate limits and invalid parameters.
- Well-documented and easy-to-use interface.

## Installation

1. Clone this repository or download the source code:
   ```bash
   git clone https://github.com/your_username/nba-api-client.git
   cd nba-api-client
   ```
2. Install the required dependencies:  
     ```bash
     pip install -r requirements.txt
     ```

3. Set up your API key:
Obtain your API key from RapidAPI.

## Usage
Here is an example of how to use the NBAApiClient to fetch NBA data:
```python

from my_nba_api.api_client import NBAApiClient

# Initialize the client with your API key
client = NBAApiClient(api_key="your_api_key")

# Fetch all available seasons
seasons = client.get_seasons()
print("Seasons:", seasons)

# Fetch teams by keyword
teams = client.search_teams(query="atl")
print("Teams:", teams)

# Fetch player statistics by ID and season
player_stats = client.get_player_statistics(player_id=236, season=2020)
print("Player Stats:", player_stats)
```

## Examples
### Fetching Teams by Conference
```python
teams_by_conference = client.get_teams_by_conference(conference="East")
print(teams_by_conference)
```


### Fetching Player Statistics by Game
```python
game_stats = client.get_game_statistics(game_id=10403)
print(game_stats)
```

### Searching for Players
```python
players = client.search_players(query="james")
print(players)
```

For more examples, see the example1.py and example.py(included whole fetch content) file.

## Error Handling
This client handles the following errors:

**RateLimitError**: Raised when the API rate limit is exceeded.
**InvalidParameterError**: Raised for invalid query parameters.
**NBAApiError**: Raised for other general API errors.

```python
try:
    client.get_game_by_id(game_id=99999)
except NBAApiError as e:
    print(f"Error: {e}")
```

## Testing
The project includes a comprehensive test suite using pytest and unittest.mock. To run the tests:
1. Install pytest:
    ```bash
    pip install pytest
    ```

2. Run the tests:
    ```bash
    pytest test_api_client.py
    ```

## Project Structure

```plaintext
my-nba-api/
├── my_nba_api/
│   ├── __init__.py       # Package initializer
│   ├── api_client.py     # Main API client
├── example.py            # Example usage(all)
├── example1.py           # Example usage
├── tests/                # test
│   ├── __init__.py       # test initializer
│   ├── test_api_client.py # Unit tests
├── README.md             # Documentation
└── requirements.txt      # Dependencies
```

## License
This project is licensed under the MIT License.

## Contact
For questions or support, please contact:
**Name**: Xiaoyi Wang
**Email**: xw3028@columbia.edu















>>>>>>> 0d0b2da (Initial commit)
