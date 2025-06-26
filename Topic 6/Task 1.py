def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            total = 0
            count = 0
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропустити порожні рядки
                try:
                    name, salary = line.split(',')
                    total += int(salary)
                    count += 1
                except ValueError:
                    print(f"Попередження: некоректний формат рядка: '{line}'")
                    continue
            if count == 0:
                return 0, 0
            average = total // count
            return total, average
    except FileNotFoundError:
        print(f"Помилка: файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Виникла помилка при обробці файлу: {e}")
        return 0, 0
