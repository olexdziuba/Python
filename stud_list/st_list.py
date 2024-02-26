import csv

# Запитуємо у користувача початкові значення
start_container_id = int(input("Введіть номер першого ID контейнера: "))
start_ip_address = int(input("Введіть першу IP адресу: "))

# Запитуємо назву файлу від користувача
file_name = input("Введіть назву файлу (наприклад, student.csv): ")

# Відкриття файлу для читання
with open(file_name, mode='r') as infile:
    reader = csv.reader(infile, delimiter=';')

    # Проходимо по кожному рядку у вхідному файлі
    for row in reader:
        # Формуємо новий рядок без пробілу між ID контейнера і IP адресою
        new_row = f"{start_container_id};{start_ip_address};{row[0]};{row[1]};{row[2]}"

        # Виведення рядка на екран
        print(new_row)

        # Збільшуємо ID контейнера та IP адресу на 1 для наступного рядка
        start_container_id += 1
        start_ip_address += 1

print("Операція завершена успішно.")
