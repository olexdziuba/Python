import csv


# Функція транслітерації французьких символів
def transliterate_french(string):
    translit_dict = {
        'à': 'a', 'â': 'a', 'æ': 'ae', 'ç': 'c', 'é': 'e', 'è': 'e',
        'ê': 'e', 'ë': 'e', 'î': 'i', 'ï': 'i', 'ô': 'o', 'œ': 'oe',
        'ù': 'u', 'û': 'u', 'ü': 'u', 'ÿ': 'y',
        'À': 'A', 'Â': 'A', 'Æ': 'AE', 'Ç': 'C', 'É': 'E', 'È': 'E',
        'Ê': 'E', 'Ë': 'E', 'Î': 'I', 'Ï': 'I', 'Ô': 'O', 'Œ': 'OE',
        'Ù': 'U', 'Û': 'U', 'Ü': 'U', 'Ÿ': 'Y'
    }
    return ''.join(translit_dict.get(char, char) for char in string)


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
        # Видаляємо небажані символи з кожного елемента рядка і транслітеруємо
        row = [transliterate_french(elem.replace('="', '').replace('";', '').replace('"', '').replace('-', '')) for elem
               in row]

        # Обробка імені (PRENOM) та прізвища (NOM) з видаленням дефісів
        prenom_processed = ''.join(row[2].lower().split())[:3].replace('-', '')
        nom_processed = ''.join(row[1].lower().split()).replace('-', '')

        # Формуємо новий рядок з урахуванням усіх вимог
        new_row = f"{start_container_id};{start_ip_address};{nom_processed}{prenom_processed};{row[0]};{row[1]};{row[2]}"

        # Виведення рядка на екран
        print(new_row)

        # Збільшуємо ID контейнера та IP адресу на 1 для наступного рядка
        start_container_id += 1
        start_ip_address += 1

print("Операція завершена успішно.")
