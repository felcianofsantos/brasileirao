import pandas as pd

def get_championship_data():
    data = [
        {"Year": 2006, "Champion": "São Paulo", "Points": 78, "GoalDiff": 34, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2007, "Champion": "São Paulo", "Points": 77, "GoalDiff": 36, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2008, "Champion": "São Paulo", "Points": 75, "GoalDiff": 36, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2009, "Champion": "Flamengo", "Points": 67, "GoalDiff": 14, "State": "RJ", "Lat": -22.9068, "Lon": -43.1729},
        {"Year": 2010, "Champion": "Fluminense", "Points": 71, "GoalDiff": 26, "State": "RJ", "Lat": -22.9068, "Lon": -43.1729},
        {"Year": 2011, "Champion": "Corinthians", "Points": 71, "GoalDiff": 17, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2012, "Champion": "Fluminense", "Points": 77, "GoalDiff": 28, "State": "RJ", "Lat": -22.9068, "Lon": -43.1729},
        {"Year": 2013, "Champion": "Cruzeiro", "Points": 76, "GoalDiff": 40, "State": "MG", "Lat": -19.9167, "Lon": -43.9345},
        {"Year": 2014, "Champion": "Cruzeiro", "Points": 80, "GoalDiff": 29, "State": "MG", "Lat": -19.9167, "Lon": -43.9345},
        {"Year": 2015, "Champion": "Corinthians", "Points": 81, "GoalDiff": 40, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2016, "Champion": "Palmeiras", "Points": 80, "GoalDiff": 30, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2017, "Champion": "Corinthians", "Points": 72, "GoalDiff": 20, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2018, "Champion": "Palmeiras", "Points": 80, "GoalDiff": 38, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2019, "Champion": "Flamengo", "Points": 90, "GoalDiff": 49, "State": "RJ", "Lat": -22.9068, "Lon": -43.1729},
        {"Year": 2020, "Champion": "Flamengo", "Points": 71, "GoalDiff": 48, "State": "RJ", "Lat": -22.9068, "Lon": -43.1729},
        {"Year": 2021, "Champion": "Atlético-MG", "Points": 84, "GoalDiff": 33, "State": "MG", "Lat": -19.9167, "Lon": -43.9345},
        {"Year": 2022, "Champion": "Palmeiras", "Points": 81, "GoalDiff": 39, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2023, "Champion": "Palmeiras", "Points": 70, "GoalDiff": 31, "State": "SP", "Lat": -23.5505, "Lon": -46.6333},
        {"Year": 2024, "Champion": "Botafogo", "Points": 79, "GoalDiff": 30, "State": "RJ", "Lat": -22.9068, "Lon": -43.1729},
        {"Year": 2025, "Champion": "Flamengo", "Points": 79, "GoalDiff": 51, "State": "RJ", "Lat": -22.9068, "Lon": -43.1729},
    ]
    return pd.DataFrame(data)
