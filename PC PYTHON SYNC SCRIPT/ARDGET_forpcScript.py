# ===========================================================

# _______  __   __  __   __  __   __
# |       ||  | |  ||  | |  ||  |_|  |
# |  _____||  |_|  ||  | |  ||       |
# | |_____ |       ||  |_|  ||       |
# |_____  ||       ||       ||       |
# _____| ||   _   ||       || ||_|| |
# |_______||__| |__||_______||_|   |_|
#    all project "ARDUINOGET"
#                            made by SHUM 
# ===========================================================
import time
import webbrowser
from urllib.request import Request, urlopen
from os import system, name

mode_page = Request('https:///arduinofin/modes/', headers={'User-Agent': 'Mozilla/5.0'})
temper_page = Request('https://iLoveShum.com/arduinofin/temperature/', headers={'User-Agent': 'Mozilla/5.0'})
weather_page = Request('https://iLoveShum.com/arduinofin/weathr/', headers={'User-Agent': 'Mozilla/5.0'})
links_page = Request('https://iLoveShum.com/arduinofin/links/', headers={'User-Agent': 'Mozilla/5.0'})
customtext_page = Request('https://iLoveShum.com/arduinofin/arcustomtext/', headers={'User-Agent': 'Mozilla/5.0'})

# ==============================================

# INIT
mode = 0
temperature = '0'
weather = ''
links = ''
custom_text = ''
link_open = 1
mode1_open = 1

# Get pc id
print('\nривет, я смарт :)')
pc_num = input('pc1 or pc2, pc order: ')


# ==============================================


def start(link_open, mode1_open):
    system('cls')
    print('    ___    ____  ____  __________________\n\
       /   |  / __ \/ __ \/ ____/ ____/_  __/\n\
      / /| | / /_/ / / / / / __/ __/   / /   \n\
     / ___ |/ _, _/ /_/ / /_/ / /___  / /    \n\
    /_/  |_/_/ |_/_____/\____/_____/ /_/')
    print('              PROJECT BY SHUM        ')
    print('============================================')

    # GET MODE
    with urlopen(mode_page) as response:
        for line in response:
            line = line.decode('utf-8')
            if '0' in line or '1' in line or '2' in line or '3' in line:
                mode = line
    time.sleep(1)
    # GET TEMPERATURE
    try:
        with urlopen(temper_page) as response:
            for line in response:
                line = line.decode('utf-8')
                temperature = line
    except None:
        print('       (-) Не смог получить температуру')
    time.sleep(1)
    # GET WEATHER
    with urlopen(weather_page) as response:
        for line in response:
            line = line.decode('utf-8')
            weather = line

    print(f' [-] Температурка: {temperature}')
    print(f' [-] Погодка: {weather}')
    print(f' [-] Текущий режим: {mode}')
    print(f'[news] А вы знали, что SHUM это бог?')

    if mode == '0':
        print('\nUpdating 20s...')
        time.sleep(20)
        start(link_open, mode1_open)

    if mode == '1':
        link_open = 1
        if not mode1_open > 1:
            mode1_open = mode1_open + 1
            webbrowser.open('https://iLoveShum.com/arduinofin/')
            print('[!] Режим 1, панель открыта. \n')
            print('\nUPDATING 10s...')
            time.sleep(10)
            start(link_open, mode1_open)
        else:
            print('[!] Режим 1, панель была уже открыта. \n')
            print('\nUPDATING 10s...')
            time.sleep(10)
            start(link_open, mode1_open)
    elif mode == '2':
        mode1_open = 1
        if not link_open > 1:
            # GET LINKS
            with urlopen(links_page) as response:
                for line in response:
                    line = line.decode('utf-8')
                    links = line

            r1 = links.split(',')

            res = []
            url = 'not found.'

            for e in r1:
                r = e.split('#')
                res.append(r)

            for word in res:
                if pc_num in word:
                    url = word[1]
            webbrowser.open(url)
            link_open = link_open + 1
            print(f'[RECV] БЫЛО ПОЛУЧЕНО КОМАНДУ ОТКРЫТЬ URL: {url} - - - ВЫПОЛНЕНО!')
            print('\n Wait 20s...')
            time.sleep(20)
            start(link_open, mode1_open)
        else:
            print('[!] Режим 2, страницы была уже открыта. Пропускаю \n')
            print('\nUPDATING Wait 10s...')
            time.sleep(10)
            start(link_open, mode1_open)
    elif mode == '3':
        print('\n\n\n[!] 3 РЕЖИМ!\n=======================================\n')
        print(" .----------------. \n\
                | .--------------. |\n\
                | |    ______    | |\n\
                | |   / ____ `.  | |\n\
                | |   `'  __) |  | |\n\
                | |   _  |__ '.  | |\n\
                | |  | \____) |  | |\n\
                | |   \______.'  | |\n\
                | |              | |\n\
                | '--------------' |\n\
                 '----------------' ")
        print('\n=======================================')
        # GET CUSTOM TEXT
        with urlopen(customtext_page) as response:
            for line in response:
                line = line.decode('utf-8')
                custom_text = line
        print(f'ПОЛЬЗОВАТЕЛЬСКИЙ ТЕКСТ:\n — {custom_text} — ')
        time.sleep(1)
        print('\n\n\n[U] Обновлю через 14 секунд...')
        time.sleep(14)
        start(link_open, mode1_open)


start(link_open, mode1_open)
enter = input()

# =====================
