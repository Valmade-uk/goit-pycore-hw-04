def get_cats_info(path):
    cats_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  # видаляємо зайві пробіли та символи нового рядка
                if not line:
                    continue  # пропускаємо порожні рядки
                parts = line.split(',')
                if len(parts) != 3:
                    continue  # пропускаємо рядки з неправильним форматом
                cat_id, name, age = parts
                cats_list.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except Exception as e:
        print(f"Сталася помилка при читанні файлу: {e}")
    
    return cats_list