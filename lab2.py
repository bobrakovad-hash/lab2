# lab2
catalog = ""
count = 0
while True:
    command = input('> ').strip()
    if command == 'exit':
        break
    elif command == 'list':
        print(catalog)
    elif command == 'count':
        print(count)
    elif 'add' in command:
        book = command[4:]
        if '-' not in book:
            print('Ошибка, введите книгу по формату <<автор - название>>')
        else:
            catalog = catalog + command[4:] + "\n"
            count += 1
    else:
        print("add - добавить книгу")
        print("exit - выйти из программы")
        print("count - количество книг")
        print("list - каталог книг")
