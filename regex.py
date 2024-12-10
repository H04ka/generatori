#\d+[\~р\b|€|$]
#^[a-zA-Z0-9\-0\-?_!]{8,16}$
#\d|\.|\,
#^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{1,9}$
#([a-z.-_])+(\@mail.ru|gmail.com)
#(\d*(\.|\,\d(1,2)?)\s*(₽|RUB|Rub|руб|рублей|р\.))
#(/d*((\.|\,)\d*)?)\s*\$
import re
print("Задание", 6)

expression = r'(\d+((\.|\,)\d+)?)\s*\$'
expression_three_hundreed_buks = r'(\d+(\.|\,\d{1,2})?)\s*(₽|RUB|р|руб\.)'
con_string = '''
Дмитрий Новгородов в своих мечтах видит Macbook Pro за 2000$
Дмитрий Новгородов будучи прорабом получает в месяц 803 RUB (тугриков) степухи
Дмитрий Новгородов хочет себе ладу гранту за 800000 RUB, потому что он шайтан прорабович
'''
curs_bachei = 96.64
def konvertator():
    global con_string
    poisk_baksov = re.findall(expression, con_string)
    poisk_rublei = re.findall(expression_three_hundreed_buks, con_string)
    if poisk_baksov or poisk_rublei:
        for match in poisk_baksov:
            dollar = float(match[0])
            rubas = dollar * curs_bachei
            con_string = con_string.replace(f"{match[0]}$", f"{rubas} RUB")
        for match1 in poisk_rublei:
            rubas = float(match1[0])
            dollar = rubas / curs_bachei
            con_string = con_string.replace(f"{match1[0]} RUB", f"{round(dollar, 2)}$")
        return con_string
    else:
        print('No matches found')
print(konvertator())


print("Задание", 7)
expression = r'\d|\.|\,'
strings = '''
чем больше лес тем шкибиди 10 доп доп ес ес Чем выше горы тем 1123.12 ниже приоры Чем меньше знаешь тем крепче 1111,11 чай заваришь Чем богаче дача 18128 джими джими ача ача Чем больше вес тем Бургер kfc доп доп ec 999ec  Чем больше тумба прораб не тумба юмба Чем больше кнут гуп гуп не румбумтуп
'''
def numbers():
    


    