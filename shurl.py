'''
2022 by _Team_X_Official_ & AlAlig Dev
Код написан на основе библиотеки cuttpy
https://github.com/IAmThe2ndHuman/cuttpy
'''
import random
from colorama import Fore, init
from cuttpy import Cuttpy
from random import choice
from time import sleep
init(autoreset=True)

# Ключ API
shortener = Cuttpy('9b8daa5362ec807e634f13e0450d1dd0ab8e1')

# Функция для очистки консоли
def clear():
    import os
    # Очистка консоли Windows
    if os.name in ['ce', 'nt', 'dos']:
        os.system('cls')
    # Очистка консоли Linux, и т.д
    else:
        os.system('clear')

# Вывод приветствия
def hello():
    banner = f'''
 _____                       __  __    ____  _   _ _   _ ____  _
|_   _|__  __ _ _ __ ___     \ \/ /   / ___|| | | | | | |  _ \| |
  | |/ _ \/ _` | '_ ` _ \     \  /    \___ \| |_| | | | | |_) | |
  | |  __/ (_| | | | | | |    /  \     ___) |  _  | |_| |  _ <| |___
  |_|\___|\__,_|_| |_| |_|___/_/\_\___|____/|_| |_|\___/|_| \_\_____|
                        |_____|  |_____|
'''

    colors = random.choice([Fore.RED, Fore.YELLOW, Fore.CYAN, Fore.GREEN, Fore.BLUE, Fore.MAGENTA])
    banner = colors + banner

    fun = f'''{Fore.LIGHTBLUE_EX}
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$____$$$$$____$$$
$$$$$$$$$$$$$$$$______$$$_____$$$
$$$$$$$$$$$$$$$$______$$$_____$$$
$$$$$$$$$$$$$$$$______$$$_____$$$
$$$$$$$$$$$$$$$$______$$_____$$$$
$$$$$$$$$$$$$$$$______$$_____$$$$
$$$$$$$$$$$$$$$$______$$_____$$$$
$$$$$$$$$$_____$______$$_____$$$$
$$$$___$$______$______$_____$$$$$
$$$_____$______$______$_____$$$$$
$$$_____$______$______$_____$$$$$
$$$_____$______$______$_____$$$$$
$$$_____$____$$$$$$$$$$$$$$$$$$$$
$_$_____$___$$________________$$$
$_$_____$__$$__________________$$
$__$$$$$$_$$$_________$$$_______$
$_________$$________$___________$
$____________$$$$$$$____________$
$$_____________$$_______________$
$$_______________$$_____________$
$$$______________$_____________$$
$$$_______________$___________$$$
$$$$$_____________$__________$$$$
$$$$$$_____________________$$$$$$
$$$$$$____________________$$$$$$$
'''
    print(banner, '\n', fun, '\n')
    print(f'{Fore.LIGHTCYAN_EX}by _Team_X_Official & AlAlig\n')

# Проверка на правильность введения url, т.к в случае отсутствия http:// в url, api выдает код 2 (неверно введеннный url)
def check_http_url(url):
    if url[:4] == 'http':
        pass
    else:
        url = 'http://' + url
    return url

# Основная функция, проверяет ошибки и в случаи их обнаружения выводит их причины
def check_errors(url):
    response = shortener.shorten(url)
    code = response.code
    if code == 7:
        print(f'{Fore.GREEN}URL успешно сокращен: ', response.shortened_url)
    elif code == 0:
        print(f'{Fore.RED}[!] Произошла серверная ошибка, повторите попытку позже')
    elif code == 1:
        print(f'{Fore.RED}[!] URL-Адрес уже был сокращен')
    elif code == 2:
        print(f'{Fore.RED}[!] Введенные данные, не являются URL-адресом')
    elif code == 3:
        print(f'{Fore.RED}[!] Предпочтительное имя URL-адреса уже занято')
    elif code == 4:
        print(f'{Fore.RED}[!] Недействительный ключ API, просьба написать разработчику, приложив скриншот ошибки')
    elif code == 5:
        print(f'{Fore.RED}[!] URL-адрес включает в себя недопустимые символы')
    elif code == 6:
        print(f'{Fore.RED}[!] Данный URL-адрес относится к заблокированному домену')
    else:
        print(f'{Fore.RED}[!] Произошла неизвестная ошибка сокращения URL: ', response.description)

# Вывод "Пока!"
def goodbye():
    sleep(0.05)
    print(f'{Fore.CYAN}Спасибо, за использование скрипта!')
    sleep(0.5)
    print(f'{Fore.RED}Завершение работы через 15 секунд...')
    sleep(5)
    print(f'{Fore.RED}Завершение работы через 10 секунд...')
    sleep(5)
    print(f'{Fore.RED}Завершение работы через 5 секунд...')
    sleep(5)
    print(f'{Fore.RED}Завершение работы через 0 секунд...')  
    exit()

# Ошибка ввода
def er():
    print(f'{Fore.RED}[!]Некорректный ввод, повторите попытку')
    clear()
    hello()
    sleep(1)
    menu()

# Возврат назад
def back():
    import os
    print(f"{Fore.MAGENTA}Вернутся в главное меню?")
    print(f"{Fore.MAGENTA}[1]-да")
    print(f"{Fore.MAGENTA}[2]-нет")
    if os.name in ['ce', 'nt', 'dos']:
        inp = f'{Fore.CYAN}↓↓↓'
        ch = input()
        if ch == '1':
            clear()
            hello()
            sleep(1)
            menu()
        if ch == '2':
            goodbye()
        else:
            er()
    else:
        input(f'{Fore.CYAN}>>>')
        if ch == '1':
            clear()
            hello()
            sleep(1)
            menu()
        if ch == '2':
            goodbye()
        else:
            er()

# Разработчики
def devs():
    devs = f'''{Fore.LIGHTCYAN_EX}
TG #1 разработчика : @Team_X_Official
TG #2 разработчика : @AlAlig
TG канал #1 разработчика : @TeamXofficial0
'''
    print(devs)
# Краткая документация об ошибках
def doc():
    doc = f'''{Fore.RED}
[!]Документация по ошибкам Cuttpy
[0]- Неизвестная ошибка на стороне сервера
[1]- URL-адрес уже был сокращен
[2]- Введенный URL-адрес не является URL-адресом
[3]— Предпочтительное имя URL-адреса уже занято.
[4]- Недействительный ключ API.
[5]— URL-адрес не прошел проверку.  Включает недопустимые символы
[6]— предоставленный URL-адрес относится к заблокированному домену.
[7]- URL-адрес был успешно сокращен
'''
    print(doc)

# Главное меню
def menu():
    import os
    print(f'{Fore.CYAN}Главное меню')
    print(f'{Fore.GREEN}[1] Сократить URL')
    print(f'{Fore.BLUE}[2] FAQ')
    print(f'{Fore.LIGHTCYAN_EX}[3] Dev`s')
    print(f'{Fore.YELLOW}[4] Выйти')
    if os.name in ['ce', 'nt', 'dos']:
        menu_ch = input()
        if menu_ch == '1':
            l = f'{Fore.CYAN}Введите URL ↓↓↓'
            print(l)
            url = input()
            check_errors(check_http_url(url))
        elif menu_ch == '2':
            doc()
            sleep(5)
            back()
        elif menu_ch == '3':
            devs()
            sleep(3)
            back()
        elif menu_ch == '4':
            goodbye()
        else:
            er()
    else:
        menu_ch = input(f'>>>')
        if menu_ch == '1':
            url = input(f'{Fore.CYAN}Введите URL: ')
            check_errors(check_http_url(url))
        elif menu_ch == '2':
            doc()
            sleep(5)
            back()
        elif menu_ch == '3':
            devs()
            sleep(3)
            back()
        elif menu_ch == '4':
            goodbye()
        else:
            er()
        

# Если этот файл будет использоваттся как модуль, то банер выводится не будет, а также не будет делаться запрос URL для сокращения
if __name__ in '__main__':
    clear()
    hello()
    sleep(1)
    menu()
