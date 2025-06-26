import sys
from pathlib import Path
from colorama import init, Fore, Style

# Ініціалізація colorama
init()

def print_directory_structure(path: Path, indent: str = ""):
    try:
        for item in sorted(path.iterdir()):
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}📂 {item.name}{Style.RESET_ALL}")
                print_directory_structure(item, indent + " ┃ ")
            else:
                print(f"{indent}{Fore.GREEN}📜 {item.name}{Style.RESET_ALL}")
    except PermissionError:
        print(f"{indent}{Fore.RED}⛔ Permission denied: {item}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}❌ Помилка: вкажіть шлях до директорії як аргумент.{Style.RESET_ALL}")
        print(f"Приклад: python hw03.py /шлях/до/директорії")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}❌ Шлях не існує: {path}{Style.RESET_ALL}")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}❌ Вказаний шлях не є директорією: {path}{Style.RESET_ALL}")
        sys.exit(1)

    print(f"{Fore.CYAN}📦 {path.name}{Style.RESET_ALL}")
    print_directory_structure(path)

if __name__ == "__main__":
    main()