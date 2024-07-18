import sqlite3

def create_tables():
    conn = sqlite3.connect('pizza.db')
    cursor = conn.cursor()

    # Создание таблицы pizzas
    cursor.execute('''CREATE TABLE IF NOT EXISTS pizzas (
                    pizza_id TEXT,
                    pizza_type_id TEXT,
                    size TEXT,
                    price REAL
                )''')
    # Удаление данных, чтобы не размножались при каждом запуске
    cursor.execute('''DELETE FROM pizzas''')

    # Создание таблицы  pizza_types
    cursor.execute('''CREATE TABLE IF NOT EXISTS pizza_types (
                    pizza_type_id TEXT,
                    name TEXT,
                    category TEXT,
                    ingredients TEXT
                )''')

    # Удаление данных из таблицы pizza_types, чтобы не размножались при каждом запуске
    cursor.execute('''DELETE FROM pizza_types''')

    conn.commit()
    conn.close()