#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv


def read_csv_data(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))


def format_description(row):
    sex_map = {'female': 'женского пола', 'male': 'мужского пола'}
    sex = sex_map.get(row.get('sex', ''), 'неопределенного пола')

    age = row.get('age', 'неизвестного возраста')
    device = row.get('device_type', '')
    browser = row.get('browser', '')
    bill = row.get('bill', '')
    region = row.get('region', '')

    return (f"Пользователь {row.get('name', '')} {sex}, {age} лет выполнил(а) покупку на {bill} у.е. "
            f"с {device} браузера {browser}. Регион, из которого выполнилась покупка: {region}.")


def write_descriptions_to_file(descriptions, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(f"{description}\n" for description in descriptions)


def main():
    input_file_path = 'web_clients_correct.csv'
    output_file_path = 'client_descriptions.txt'

    data = read_csv_data(input_file_path)
    descriptions = [format_description(row) for row in data]
    write_descriptions_to_file(descriptions, output_file_path)


if __name__ == '__main__':
    main()


# In[ ]:




