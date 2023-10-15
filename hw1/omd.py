# Guido van Rossum <guido@python.org>
import random


def step2_no_umbrella(rain_state):
    home_returning = False
    walk_options = ('по переулкам 🏢', 'на автобусе 🚌')
    print(
        'Утка-маляр 🦆 не взяла зонтик ☂️, доверившись солнечным '
        'прогнозам погоды🌞\n Время нелетное! 🌓 '
        'Как же добраться до бара: '
        f'{walk_options[0]} или {walk_options[1]}?'
    )

    option = str(input()).lower().strip()
    while option not in [x[:-1].strip() for x in walk_options]:
        print('Не понимаю, о чем ты! Быть может, ты прислал мне '
              'лишнюю картинку? Или забыл предлог?')
        option = str(input()).lower().strip()

    if rain_state == 0:
        if option == walk_options[0][:-1].strip():
            print('Хороша погодка! ☀️ Вместо билета на автобус утка-маляр 🦆 '
                  'купит еще один мартини!')
        else:
            print('Нет времени объяснять! ⏰ Быстрее в бар, водитель! '
                  'Без зонта в салоне меньше нагрузки! 🚀🚀🚀')
    else:
        if option == walk_options[0][:-1].strip():
            rain_answer_dict = {'А': 'лететь в бар и греться '
                                     'ремарковским кальвадосом',
                                'Б': 'остановиться у хлебного ресторана, '
                                     'пока не начался дождь',
                                'В': 'устроить званый ужин дома '
                                     'на сэкономленные деньги'}

            print('Сгущаются тучки над уткой-маляр 🦆 '
                  'Стоит ли в дождь лететь в бар?')

            for key, value in rain_answer_dict.items():
                print(key + ') ' + value)

            option = str(input()).upper().strip()
            while option not in rain_answer_dict.keys():
                print('Не стоит шутить с уткой-маляр🦆! '
                      'Скорее скажи, лететь ли ей в бар ⌛ '
                      'Или она скажет своему другу Дуолинго '
                      'о твоих проступках...')
                option = str(input()).upper().strip()

            if option == 'В':
                home_returning = True
        else:
            print('Не подвело чутье утку-маляр 🦆! Водитель автобуса спас '
                  'пятницу, отвезя ее в бар! 🍺')

    if home_returning:
        print('Прекрасный домашний вечер у утки-маляр 🦆: '
              'с тульскими пряниками под горячий самовар 🫖')
    else:
        home_returning_rain_state = ('Как хорошо, что сегодня '
                                     'не случился дождь!',
                                     'И дождь не помеха: ведь он закончился!')
        print('Прекрасный вечер у утки-маляр 🦆: пора '
              f'возвращаться домой! {home_returning_rain_state[rain_state]}')


def step2_umbrella(rain_state):
    print(
        'Мудрая утка-маляр 🦆 Взяла с собой зонт ☂️\n'
        'Сейчас не сказать: пойдет дождь 🌧️ или не пойдет 🌞'
    )
    if rain_state == 0:
        print('Немного по улицам города пройдясь 🏢 утка-маляр 🦆 '
              'таки явилась в пятничный бар!')
    else:
        print('Сгущались тучи 🌩️ над уткой-маляр 🦆, '
              'собравшись испортить ей пятничный вечер...'
              'Не зря была мудрой утка-маляр 🦆, открывшая зонт! '
              'С сухим оперением утка-маляр 🦆 притопала в бар!')

    bar_objects = set(['сидр', 'кофе', 'вода', 'виски', 'текила',
                       'мартини', 'чай'])    # сет из того, что есть в баре

    print('У стойки чикен-бармен 🐥 спросил у утки-маляр 🦆, '
          'что ей хотелось бы выпить 🍸\n'
          'Перечисли через запятую предпочтения утки-маляр 🦆')
    answer = str(input()).lower().replace(' ', '')

    # сет из того, что любит утка-маляр
    duck_preferences = set(answer.split(','))

    # нет пересечения сетов из того,
    # что есть в баре и того, что нравится утке
    if duck_preferences.intersection(bar_objects) == set():
        print('Чикен-бармен 🐥 не смог найти ничего, что назвала утка-маляр🦆\n'
              'Но зато смог предложить ей специальный напиток 🍾 для тех, '
              'у кого есть зонт☂️! Утка-маляр 🦆 осталась рада!')
    else:
        duck_preferences_string = ', '.join(
            duck_preferences.intersection(bar_objects)
        )
        print('Чикен-бармен 🐥 налил утке-маляр 🦆 все, что смог найти '
              f' для нее: {duck_preferences_string} - все выпила '
              'утка-маляр 🦆 и оставила чикен-бармену 🐥 много чаевых!')

    print('Понравилась пятница утке-маляр 🦆! Как сказано в песнях, '
          'пора возвращаться домой!')


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    rain_state = random.randint(0, 1)   # состояние того, пойдет ли дождь
    if options[option]:
        return step2_umbrella(rain_state)
    return step2_no_umbrella(rain_state)


if __name__ == '__main__':
    step1()
