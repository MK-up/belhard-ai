#модуль для загрузки данных
from data_loader import load_csv
#модуль визуализалции данных
from visualization_manager import show_histogram, show_line_chart
import pandas as pd

# Метод для подсчета пропущенных значений
def count_missing_values(df):
    missing_values = df.isnull().sum()
    return missing_values

# Метод для вывода отчёта о пропущенных значениях
def report_missing_values(df):
    missing_values = count_missing_values(df)
    missing_columns = missing_values[missing_values > 0]

    if missing_columns.empty:
        print('Пропущенных значений нет в столбцах.')
    else:
        print('Пропущенные значения в следующих столбцах:')
        print(missing_columns)

# Метод для заполнения пропущенных значений средним
def fill_missing_with_mean(df, column):
    mean_value = df[column].mean()
    df[column] = df[column].fillna(mean_value)

# Метод для заполнения пропущенных значений медианой
def fill_missing_with_median(df, column):
    median_value = df[column].median()
    df[column].fillna(median_value, inplace=True)

# Метод для заполнения пропущенных значений наиболее частым значением (mode)
def fill_missing_with_mode(df, column):
    mode_value = df[column].mode()[0]
    df[column].fillna(mode_value, inplace=True)


if __name__ == '__main__':

    # Загрузка данных из CSV
    data_csv = load_csv('venv/resources/bank.csv', delimiter=';')

    # Показать загруженные данные
    print(data_csv)

    # Удаляем дубликаты перед созданием Data Frame
    df = data_csv.copy().drop_duplicates()
    #print(df.info())

    # Строим линейный график
    show_line_chart(df, 'day', 'campaign')

    # Строим гисторамму
    show_histogram(df, 'age')
    show_histogram(df, 'marital')

    report_missing_values(df)

    # Заполнить данные о балансе средним
    fill_missing_with_mean(df, 'balance')

    report_missing_values(df)