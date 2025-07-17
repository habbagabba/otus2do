import json
import os
import sys

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Загружает контакты из файла."""
    if os.path.exists(CONTACTS_FILE):
        try:
            with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data
        except json.JSONDecodeError as e:
            print(f"Ошибка при загрузке JSON: {e}")
            return {}
    return {}


def save_contacts(contacts):
    """Сохраняет контакты в файл."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)


def show_contacts(contacts):
    """Выводит все контакты на экран."""
    if not contacts:
        print("Нет контактов для отображения.")
        return

    for contact_id, contact in contacts.items():
        print(
            f"Айди: {contact_id}, Имя: {contact['name']}, Телефон: {contact['phone']}, Комментарий: {contact.get('comment', '')}"
        )


def get_next_contact_id(contacts):
    """Получает следующий доступный айди для нового контакта."""
    existing_ids = [int(id_num) for id_num in contacts.keys()]
    if existing_ids:
        return str(max(existing_ids) + 1)
    return "1"  # Если нет существующих контактов, начинаем с 1


def create_contact(contacts, name, phone, comment=""):
    """Создает новый контакт."""
    contact_id = get_next_contact_id(contacts)  # Генерация ID
    contacts[contact_id] = {"name": name, "phone": phone, "comment": comment}
    save_contacts(contacts)
    print(f"Контакт с айди {contact_id} создан.")


def find_contact(contacts, keyword):
    """Находит контакт по ключевому слову."""
    found_contacts = {}
    for contact_id, contact in contacts.items():
        if (
            keyword in contact["name"]
            or keyword in contact["phone"]
            or (contact.get("comment") and keyword in contact["comment"])
        ):
            found_contacts[contact_id] = contact

    if not found_contacts:
        print("Контакты не найдены.")
    else:
        show_contacts(found_contacts)


def update_contact(contacts, contact_id, name=None, phone=None, comment=None):
    """Обновляет существующий контакт."""
    if contact_id not in contacts:
        print(f"Контакт с айди {contact_id} не найден.")
        return

    updated = False  # Флаг для отслеживания изменений

    if name is not None and name != "":  # Если передано имя (не пустое)
        contacts[contact_id]["name"] = name
        updated = True
    if phone is not None and phone != "":  # Если передан телефон (не пустой)
        contacts[contact_id]["phone"] = phone
        updated = True
    if comment is not None and comment != "":  # Если передан комментарий (не пустой)
        contacts[contact_id]["comment"] = comment
        updated = True

    if updated:  # Если были изменения, сохраняем
        save_contacts(contacts)
        print(f"Контакт с айди {contact_id} обновлен.")
    else:
        print("Нет изменений для обновления.")


def delete_contact(contacts, contact_id):
    """Удаляет контакт по айди."""
    if contact_id in contacts:
        del contacts[contact_id]
        save_contacts(contacts)
        print(f"Контакт с айди {contact_id} удален.")
    else:
        print(f"Контакт с айди {contact_id} не найден.")


def show_usage():
    """Выводит инструкцию по использованию программы."""
    print("Использование: python3 phonebook_cli.py <команда> [аргументы]")
    print("\nДоступные команды:")
    print("  show                                            : Показать все контакты.")
    print("  create <имя> <телефон> [комментарий]            : Создать новый контакт.")
    print(
        "  find <ключевое слово>                           : Найти и показать контакты по ключевому слову."
    )
    print('  update <id> [имя|""] [телефон|""] [комментарий] : Обновить контакт.')
    print(
        "  delete <id>                                     : Удалить контакт по айди."
    )

    print("\nПримеры:")
    print('  python3 phonebook_cli.py create "Имя" "Телефон" "Комментарий"')
    print('  python3 phonebook_cli.py update 1 "" "" "Новый комментарий" ')
    print('  python3 phonebook_cli.py find "Комментарий"')
    print("  python3 phonebook_cli.py delete 1")


def main():
    """Основная функция для обработки команд."""
    contacts = load_contacts()

    if len(sys.argv) < 2:
        show_usage()
        return

    command = sys.argv[1].lower()

    if command == "show":
        show_contacts(contacts)
    elif command == "create":
        if len(sys.argv) < 5:
            print(
                "Используйте: python3 phonebook_cli.py create <имя> <телефон> [комментарий]"
            )
        else:
            name = sys.argv[2]
            phone = sys.argv[3]
            comment = sys.argv[4] if len(sys.argv) > 4 else ""
            create_contact(contacts, name, phone, comment)
    elif command == "find":
        if len(sys.argv) < 3:
            print("Используйте: python3 phonebook_cli.py find <ключевое слово>")
        else:
            keyword = sys.argv[2]
            find_contact(contacts, keyword)
    elif command == "update":
        if len(sys.argv) < 3:
            print(
                "Используйте: python3 phonebook_cli.py update <id> [имя] [телефон] [комментарий]"
            )
        else:
            contact_id = sys.argv[2]  # Айди, который мы хотим обновить
            # Передаем только те параметры, которые были указаны пользователем
            name = sys.argv[3] if len(sys.argv) > 3 else None
            phone = sys.argv[4] if len(sys.argv) > 4 else None
            comment = sys.argv[5] if len(sys.argv) > 5 else None
            update_contact(contacts, contact_id, name, phone, comment)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Используйте: python3 phonebook_cli.py delete <id>")
        else:
            contact_id = sys.argv[2]
            delete_contact(contacts, contact_id)
    else:
        print("Неизвестная команда.")
        show_usage()


if __name__ == "__main__":
    main()
