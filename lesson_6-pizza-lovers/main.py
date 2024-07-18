#модуль для загрузки данных из CSV-файлов
from data_loader import load_csv
#модуль для создания архитектуры БД
from db_initializer import create_tables

# Реляционная База Данных: SQLite
import sqlite3
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Загрузка данных из CSV-фафйлов
    pizzas_csv = load_csv('venv/resources/pizzas.csv')
    pizza_types_csv = load_csv('venv/resources/pizza_types.csv', encoding='cp1251')
    orders_csv = load_csv('venv/resources/orders.csv')
    order_details_csv = load_csv('venv/resources/orders.csv')

    print(pizza_types_csv.info())

    # Подключение к базе данных SQLite
    conn = sqlite3.connect('pizza.db')
    c = conn.cursor()

    # Создание структуры БД
    create_tables()

    # Вставка данных  в таблицу pizzas
    for index, row in pizzas_csv.iterrows():
        c.execute("INSERT INTO pizzas (pizza_id, pizza_type_id, size, price) VALUES (?, ?, ?, ?)",
                      (row['pizza_id'], row['pizza_type_id'], row['size'], row['price']))

    # Вставка данных  в таблицу pizzas
    for index, row in pizza_types_csv.iterrows():
        c.execute("INSERT INTO pizza_types (pizza_type_id, name, category, ingredients) VALUES (?, ?, ?, ?)",
                      (row['pizza_type_id'], row['name'], row['category'], row['ingredients']))

    # Запрос данных из таблицы pizza_types
    c.execute("SELECT * FROM pizza_types")
    print(c.fetchall())

    # Запрос данных по средним пиццам
    c.execute("SELECT * FROM pizzas WHERE size = 'M'")
    print(c.fetchall())

    # По каждому наименованию типа пиццы ищем минимальную, максимальную и среднюю стоимость, а также количество пицц
    c.execute("SELECT pizza_types.name, "
              "MAX(pizzas.price) as MAX_PRICE, "
              "MIN(pizzas.price), "
              "ROUND(AVG(pizzas.price), 2), "
              "COUNT(*)"
              "FROM pizzas "
              "JOIN pizza_types ON pizzas.pizza_type_id = pizza_types.pizza_type_id "  
              "GROUP BY pizza_types.name")
    results = c.fetchall()

    for result in results:
        type_name, max_price, min_price, avg_price, count = result
        print(f"Type: {type_name}, Max Price: {max_price}, Min Price: {min_price}, Avg Price: {avg_price}, Count: {count}")

    # Данные для гистограммы
    labels = ['Max Price', 'Min Price', 'Avg Price']
    values = [max_price, min_price, avg_price]

    # Создание гистограммы
    plt.bar(labels, values, color=['blue', 'green', 'orange'])
    plt.title(f'Pizza Prices Histogram for {type_name}')
    plt.xlabel('Price Type')
    plt.ylabel('Price')
    plt.show()


    # Закрытие соединения
    conn.commit()
    conn.close()





