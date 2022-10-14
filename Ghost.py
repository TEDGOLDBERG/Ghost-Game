# Ghost Game
from random import randint, random
from time import sleep
feeling_brave = True
score = 0
count_wrong = 0
print('Дом с привидениями!')
sleep (1)
print ('Не поздновато-ли для пролгулки, Незнакомец? Don\'t You?')
sleep (1)
person = input ('Ваш псевдоним ?')
sleep(3)
print ('Давно-о-о-о-о.. ты,',person)
print (' ...присматриваешься к этому особняку на краю города.')
sleep (1)
print ('Ну там!... Где кладбище!')
sleep (2)
print('В пятницу 13 ...')
sleep (1)
print('В дождь...')
sleep (1)
print('Ты идёшь...')
sleep (1)
print('Ворота поместья подозрительно распахнуты настежь...')
sleep (2)
print('Осторожно ты пробираешься по заросшей чертополохом' 
    '...едва различимой трапинке - она ведет к особняку!')
sleep (3)
print ('Внимание! Дальше вы не поняли как,')
print ('но вдруг ваше имя изменилось на...')
sleep(2)
print(person[::-1])
sleep (1)
print ('Сейчас на вас это никак не повлияет, '
    '...живите спокойно, просто вы вдруг ощутили всей кожей, '
    'что теперь вас могут звать еще и ...')
print(person[::-1])
sleep (5)
print('Долго ли - коротко ли - привела тебя,',person,'тропинка ' 
    'к особняку...')
sleep (1)
print('И ВОТ...')
sleep (1)
while feeling_brave:
    ghost_door = randint(1,3)
    sleep(2)
    print('Три двери впереди...')
    sleep(1)
    print('За одной из них - призрак.')
    sleep(1)
    print('В какую дверь пойдешь?')
    sleep(1)
    print('Выбери цифру и нажми "Enter"')
    door = input('1, 2 или 3 ?') 
    door_num = int(door)
    if door_num == ghost_door:
        print('Призрак!')
        feeling_brave = False
    elif door_num == (42):
        print ('Bingo, ты открыл секретную комнату номер 42'
        'и выиграл кучу очков, крутяк, Ваще,'
        'Играем дальше!')
        score = score + 10000000
    elif door_num > 3:
        print('Тебе же сказали! А ты опять за своё...'
            'Дверей только три штуки - больше - не будет...')
    elif door_num != ghost_door:
        print('Повезло!')
        sleep(1)
        print('Ты осторожно открываешь дверь...')
        sleep(1)
        print('Cо скрипом дверь поддается.')
        print('Ты оказался в комнате...')
        score = score + 1
print('Беги - спасайся!')
sleep(3)
print('МАМА!!!!')
sleep(3)
print('Ужас... !')
sleep(2)
print('Игра закончена! Тебя немного скушали.'
    ' Твой результат:', score, 'очков')
sleep(3)
exit