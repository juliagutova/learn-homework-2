"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    user_list = [
        {'name': 'Mary', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Vally', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Edward', 'age': 48, 'job': 'Big boss'},
        {'name': 'George', 'age': 22, 'job': 'Assistant'},
        {'name': 'Lidia', 'age': 32, 'job': 'Manager'},
        {'name': 'Alla', 'age': 51, 'job': 'General manager'},
    ]
    
    import csv

    with open('users.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)

if __name__ == "__main__":
    main()
