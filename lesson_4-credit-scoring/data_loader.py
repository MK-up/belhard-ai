import pandas as pd
import requests
import json

# Загрузка данных из CSV
def load_csv(file_path, delimiter=','):
    try:
        data = pd.read_csv(file_path, delimiter=delimiter)
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None


def load_json(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None

def load_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error loading data from API: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON response: {e}")
        return None