file = open('story.txt','w')

oldprint = print 
oldinput = input

def print(*argument):
    '''одновременно печатает введенную фразу в коде, и записывает эту фразу в тхт файл'''
    argument = ' '.join(argument)
    file.write(argument+'\n')
    oldprint(argument)

def input(argument):
    output = oldinput(argument)
    file.write(f'{argument}{output}\n')
    return output

def timesleep(seconds):
    for _ in range(23000000*seconds):
        i = 999999999//567

def printspace(time,separator,enters,sep = True):
    for _ in range(enters): print()
    if sep: print(separator*125)
    for _ in range(enters): print()
    timesleep(time)

false_input = True


print()
print('Начало истории')
printspace(0,'-',1)
print('Наш герой - фермер. У него сгорели посевы. Ему срочно нужны деньги чтобы заплатить за обучение в ВШЭ, а взять их негде.')
printspace(1,'-',1)
choice_1 = input('Что делать фермеру? 1 - Посмотреть, что в сейфе или 2 - поискать в комнатах дома? \nВведите цифру: ') 
printspace(0,'-',1)
if choice_1 == '1':
    print(f'Герой открывает сейф, а там - бутылка водки. Фермер пробует. "А зачем вообще мне учиться в Вышке, если я и бесплатно могу потратить время зря?"')
    printspace(1,'',0)
    print(f'Герой спивается.\n')
    printspace(1,'',0)
    false_input = False

elif choice_1 == '2':
    print(f'В доме четыре комнаты; наверное в одной из них лежит немного денег. А возможно удастся захватить еще что нибудь полезное.')
    printspace(1,'',0)
    rooms = ('комната 1, комната 2, комната 3, комната 4')
    rooms = rooms.split(', ')
    things = []
    things_in_rooms = [['фонарик', 'картина', 'лопата', 'веревка', 'ведро'],
                        ['термос', 'ложка', 'чайник', 'чашка'],
                        ['деньги', 'носки', 'подушка', 'свеча'],
                        ['зубная щетка', 'шапмунь', 'мочалка', 'мыло']]

    for i in range(len(rooms)):
        room = rooms[i]
        room_things = things_in_rooms[i]
        print()
        print(f'Герой заходит в комнату {room[-1]}:')
        printspace(1,'',0)
        print(f'В комнате есть: {", ".join(room_things)}')
        things += input(f'Что положить в сумку?: ').split(', ')
        print()
        

    if 'деньги' in things:

        printspace(1,'-',1)
        print('Ура! Мы нашли деньги и заодно взяли немного вещей. Интересно, хватит ли нам денег на обучение?!')
        printspace(1,'-',1)
        print('Фермер заводит трактор, кидает туда сумку с деньгами, и едет в вуз. По дороге его останавливает полицейский за превышение скорости и просит взятку.')
        printspace(1,'',0)

        choice_2 = input('Что делать? 1 - позвонить кому-нибудь, или 2 - посмотреть в сумку, вдруг там что-то есть?: ')
        if choice_2 == '2':
            printspace(1,'-',1)
            print('Фермер видит в сумке', ', '.join(things))
            printspace(1,'',0)
            print('Ничего полезного. Может, предложить полицейскому деньги? ')
            printspace(2,'-',1)

            choice_3 = input('Что делать? 1 - Предложить денег или 2 - закрыть сумку и ничего не предлагать? ')
            if choice_3 == '1':
                printspace(1,'',0)
                print('"Хм, а сколько у тебя есть?" - спросил полицейский')
                printspace(1,'',0)
                bribe = input('Сколько дать? 1 - 30к, 2 - 300к или 3 - все, что есть? ')
                crimes = {}

                if bribe == '1':
                    crimes["УК РФ Статья 291 Пункт 2"] = 'Дача взятки должностному лицу в значительном размере'
                elif bribe == '2':
                    crimes["УК РФ Статья 291 Пункт 4"] = 'Дача взятки должностному лицу в крупном размере'  
                elif bribe == '3':
                    crimes["УК РФ Статья 291 Пункт 5"] = 'Дача взятки должностному лицу в особо крупном размере'

                crime_number = list(crimes.keys())[0]
                printspace(1,'-',1)
                print(f'Слушай, кажется ты арестован по статье "{crimes[crime_number]}"')
                printspace(1,'',0)
                print('Поехали в участок, оформим тебя по', crime_number)
                printspace(3,'',1,sep = False)
                print('Конец. Кажется, фермера посадили в тюрьму')
                printspace(1,'',0)   
                false_input = False

            elif choice_3 == '2':
                printspace(1,'',0)
                print('"Ладно, езжай, я сегодня добрый" - сказал полицейский')
                printspace(1,'-',1)
                print('Фермер едет дальше. И вдруг понимает, что на тракторе пикает бомба - за три попытки надо срочно подобрать от нее пароль')
                               
                flag = False
                count = 3
                while count != 0:
                    printspace(1,'',0)
                    password = input('Введите код (год основания ВШЭ): ')
                    if password != '1992':
                        count -= 1
                        printspace(1,'',0)
                        print(f'Блин, неправильный пароль! Осталось попыток: {count}')
                    else:
                        printspace(1,'',0)
                        print('Ура! Бомбу удалось разминировать. Можно спокойно ехать')
                        flag = True
                        break

                if flag:
                    printspace(1,'-',1)
                    print('Фермер доезжает до вуза и оплачивает обучение, потом возвращается домой, учится и живет долго и счастливо')
                    printspace(2,'',1,sep = False)
                    print('Конец.')
                    printspace(2,'',0)
                    false_input = False
                elif not flag:
                    printspace(1,'-',1)
                    print('"Ну, хотя бы не надо платить за вышку" - думает фермер, сидя во взрывающемся тракторе')
                    printspace(2,'',1,sep = False)
                    print('Фермер умирает')
                    printspace(2,'',0)
                    false_input = False

        elif choice_2 == '1':
            phones = {'Сын студент': "89646221457", "Бабушка": "84951589818", "Друг": "84991147031", "Прокуратура": "89031257437"}
            printspace(1,'-',1)
            print(f'Фермер открывает телефонную книгу и видит записанные контакты: {", ".join(list(phones.keys()))}') 
            printspace(1,'',0)

            choice_4 = input('Кому позвонить? 1 - сынуле, 2 - бабушке, 3 - корешу, 4 - сразу важным людям ')
            while choice_4 in '12':
                printspace(1,'',0)
                print('Очень мило поговорили! Но ситуации это не помогло :(')
                printspace(1,'-',1)
                choice_4 = input('Кому позвонить? ')
            if choice_4 in '34':
                printspace(1,'-',1)
                print('Надо же, как связи работают. Поговорили по существу. Полицейский смутился и отпустил')
                printspace(1,'-',1)
                print('Фермер едет дальше. И вдруг понимает, что на тракторе пикает бомба - за три попытки надо срочно подобрать от нее пароль')
                                
                flag = False
                count = 3
                while count != 0:
                    printspace(1,'',0)
                    password = input('Введите код (год основания ВШЭ): ')
                    if password != '1992':
                        count -= 1
                        printspace(1,'',0)
                        print(f'Блин, неправильный пароль! Осталось попыток: {count}')
                    else:
                        printspace(1,'',0)
                        print('Ура! Бомбу удалось разминировать. Можно спокойно ехать')
                        flag = True
                        break

                if flag:
                    printspace(1,'-',1)
                    print('Фермер доезжает до вуза и оплачивает обучение, потом возвращается домой, учится и живет долго и счастливо')
                    printspace(2,'',1,sep = False)
                    print('Конец.')
                    printspace(2,'',0)
                    false_input = False

                elif not flag:
                    printspace(1,'-',1)
                    print('"Ну, хотя бы не надо платить за вышку" - думает фермер, сидя во взрывающемся тракторе')
                    printspace(2,'',1,sep = False)
                    print('Фермер умирает')
                    printspace(2,'',0)
                    false_input = False


    else:
        printspace(1,'-',1)
        print('Фермер нашел деньги, но отказался их брать. Кажется, ему уже ничего не поможет.')
        printspace(1,'',0)
        print('Ваш герой туповат, попробуйте снова.')
        printspace(2,'',0)
        false_input = False


if false_input:
    printspace(1,'',0,sep = False)
    print('Кажется, вы не разобрались, что надо вводить, и программа сломалась:( Попробуйте запустить ее снова!)')
    printspace(1,'',0)


