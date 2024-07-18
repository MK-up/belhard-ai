import pandas as pd

# Загрузка данных из CSV
def load_csv(file_path, delimiter=',', encoding='utf-8'):
    try:
        data = pd.read_csv(file_path, delimiter=delimiter, encoding=encoding)
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return None
