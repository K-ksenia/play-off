import random


def draw(team_list, match):
    if len(team_list) > 0:
        # Определяем команду рандомно
        random.shuffle(team_list)
        match.append(team_list[0])
        del team_list[0]
        # Определяем количество ею забыитых голов в первом матче
        match.append(random.randint(0,8))
        # Определяем количество ею забыитых голов в ответном матче
        match.append(random.randint(0,8))
        return True
    else:
        return False


def check_goals(match, i):
    # Проверяем, чтобы по сумме голов в двух матчах не было ничьи
    while match[1] + match[2] == match[4] + match[5]:
        match[5] = random.randint(0,8)
    # А это мы проверяем, чтобы в финале не было ничьи
    if i == 3:
        while match[2] == match[5]:
            match[5] = random.randint(0, 8)


def print_match_info(match):
    print(f'Первый матч {match[0]} - {match[3]} счет {match[1]}:{match[4]}')
    print(f'Ответный матч {match[3]} - {match[0]} счет {match[5]}:{match[2]}')
    print(f'Победитель {match[6]}\n')


def print_final(match):
    print(f'{match[0]} - {match[3]} счет {match[2]}:{match[5]}')
    print(f'Победитель {match[6]}')


# Исходный список
original_list = ['Barcelona','PSG','Real Madrid','ManCity','Monaco','Atl. Madrid','Bayer Leverkusen','Juventus','FC Porto','Sevillia','Bayer Munich','Arsenal','Leicester','Borussia Dortmund','Napoli','Benfica']
print('Список команд, вышедших в плей-офф: {}'.format(', '.join(original_list)))

# копирование списка
team_list = original_list[:]
stages = []

for i in range(4):
    match = []
    # список match будет иметь следующую структуру [[0]Команда1, [1]Голы команды1 в 1 матче, [2]Голы команды1 во 2 матче,
    # [3]Команда2, [4]Голы команды2 в 1 матче, [5]Голы команды2 во 2 матче, [6]Победитель]
    stage = []

    # print('Играют команды: {}'.format(', '.join(team_list)))
    while draw(team_list, match):
        draw(team_list, match)
        check_goals(match, i)
        # Определяем победителя:
        if i == 3:
            # В финале за единственный матч будем считать ответный
            match.append(match[0] if match[2] > match[5] else match[3])
        else:
            match.append(match[0] if match[1] + match[2] > match[4] + match[5] else match[3])
        stage.append(match)
        match = []
    team_list = []

    for match in stage:
        team_list.append(match[6])
        # print_match_info(match)
    stages.append(stage)

# Вводим команду
while True:
    team = input('Введите команду, матчи которой хотите посмотреть: ')
    if original_list.count(team) == 1:
        for stage in stages:
            for match in stage:
                    if match[0] == team or match[3] == team:
                        if len(stage) != 1:
                            print(f'1/{len(stage)} финала:')
                            print_match_info(match)
                        else:
                            print(f'Финал:')
                            print_final(match)
    else:
        print('Данная команда не участвовала в турнире :(')

    if input('Хотите посмотреть другую команду? (Y/N)') == 'N':
        break
