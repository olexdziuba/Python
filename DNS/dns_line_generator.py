import csv

# Запитуємо назву файлу від користувача
file_name = input("Введіть назву файлу (наприклад, student.csv): ")

# Відкриття файлу для читання
with open(file_name, mode='r') as infile:
    reader = csv.reader(infile, delimiter=';')
    
    # Проходимо по кожному рядку у вхідному файлі
    for row in reader:
        if len(row) >= 4:
            # Отримуємо необхідні дані
            IP = row[0]
            nom = row[1]
            
            # Побудова рядка для виводу
            dns_line = f"address=/{nom}.lan/10.10.0.{IP}"
            
            # Виведення рядка на екран
            print(dns_line)

print("Операція завершена успішно.")

