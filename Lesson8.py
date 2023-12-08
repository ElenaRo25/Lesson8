def print_contacts(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end ='\n\n')
        else:
            print('Список контактов пуст')

def connect_with_user():
    print('Введите имя, фамилию и телефон (через пробел, например: Иван Петров 89187845122): ')
    cont_info = input()
    return cont_info

def add_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)

def find_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    
    print("""
          
Выберите критерий для поиска:
1 - Имя 
2 - Фамилия 
3 - Телефон
    """)
    comm = int(input())
    print('Введите строку для поиска:')
    data = input()
    print('Найденные контакты:')
    for cont in all_cont:
        cont_as_list = cont.strip().split()
        if cont_as_list[comm - 1] == data:
            print(*cont_as_list)
            all_cont.remove(cont)

def edit_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        print('Введите имя или фамилию контакта, который надо изменить:')
        data = input()
        for i, cont in enumerate(all_cont):
           cont_as_list = cont.strip().split()
           if cont_as_list[0] == data or cont_as_list[1] == data:
               new_cont = connect_with_user()
               all_cont[i] = new_cont + ''
               with open(file_name, 'w', encoding='utf8') as file:
                   file.writelines(all_cont)
               print('Контакт успешно изменен')
               return
           print('Контакт не найден')

def delete_contact(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        print('Введите имя или фамилию контакта, который надо удалить:')
        data = input()
        for i, cont in enumerate(all_cont):
            cont_as_list = cont.strip().split()
            if cont_as_list[0] == data or cont_as_list[1] == data:
                del all_cont[i]
                with open(file_name, 'w', encoding='utf8') as file:
                    file.writelines(all_cont)
                print('Контакт успешно удален')
                return
        print('Контакт не найден')