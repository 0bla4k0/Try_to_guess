from random import randint
from time import sleep
from ascii_graphics import graphics
from colorama import Fore, Back, Style
from colorama import init
init()

class control_the_game():
    def gamers_health(self, health):
        '''Отображения здровья игрока, 
           передается переменная health и
           на её основе печатается нужное
           кол-во ХП.
        '''
        print("Health: ", end="")
        print(Fore.RED + "", "♥ " * health, "" + Style.RESET_ALL)

    def check_gamers_number(self, gamers_number):
        '''Проверка числа и выдача результата
           проверки в print и переменной.
        '''
        global var_to_check
        if gamers_number > asked_number:
            var_to_check = 3
        elif gamers_number < asked_number:
            var_to_check = 2
        elif gamers_number == asked_number:
            var_to_check = 5
    
    def diaposon_array(self, level, var_to_creat_array, gamers_number):
        '''Создания диапозона чисел на основе списка.
        '''
        global diaposon
        diaposon = []
        try:
            if len(var_diaposon_array) == 1:
                diaposon = Fore.GREEN + "" + str(var_diaposon_array[0]) + "-----" + str(var_diaposon_array[0]) + "" + Style.RESET_ALL
            elif var_to_creat_array == 0:
                for z in range(0, level + 1):
                    var_diaposon_array.append(z)
                diaposon = Fore.GREEN + "" + str(var_diaposon_array[0]) + "-----" + str(var_diaposon_array[len(var_diaposon_array)-1]) + "" + Style.RESET_ALL
            elif var_to_creat_array == 3:
                for z in range(len(var_diaposon_array) - 1, var_diaposon_array.index(gamers_number) - 1, -1):
                    var_diaposon_array.remove(var_diaposon_array[z])
                diaposon = Fore.GREEN + "" + str(var_diaposon_array[0]) + "-----" + str(var_diaposon_array[len(var_diaposon_array)-1]) + "" + Style.RESET_ALL
            elif var_to_creat_array == 2:
                for z in range(0, var_diaposon_array.index(gamers_number) + 1):
                    var_diaposon_array.remove(var_diaposon_array[0])
                diaposon = Fore.GREEN + "" + str(var_diaposon_array[0]) + "-----" + str(var_diaposon_array[len(var_diaposon_array)-1]) + "" + Style.RESET_ALL
        except ValueError:
            diaposon = Fore.GREEN + "" + str(var_diaposon_array[0]) + "-----" + str(var_diaposon_array[len(var_diaposon_array)-1]) + "" + Style.RESET_ALL
        except IndexError:
            diaposon = Fore.GREEN + "" + str(var_diaposon_array[0]) + "-----" + str(var_diaposon_array[len(var_diaposon_array)-1]) + "" + Style.RESET_ALL 


try_to_guess = control_the_game()
game_graphics = graphics()
start_the_game = True
global game_record
game_record = 0
with open("records.txt", "r", encoding="utf-8") as record:
    for line in record:
        game_record = int(line)

while start_the_game:
    print("\n"*100)   
    game_graphics.intro()
    sleep(1)
    print("\n"*100)
    game_graphics.game_intro()
    game_graphics.stage()
    print("")
    i = str(input("Введите число(1-0): "))
    if i == "1":
        print("\n"*100)
        game_graphics.main_character("Привет, друг!")
        sleep(0.9)
        print("\n"*100)
        game_graphics.main_character("Мне нужно....")
        sleep(0.5) 
        print("\n"*100)
        game_graphics.main_character("Угадать число,")
        sleep(0.9)  
        print("\n"*100)
        game_graphics.main_character("чтобы получить")
        sleep(0.7)
        print("\n"*100)
        game_graphics.main_character("золото, котором")
        sleep(0.8)
        print("\n"*100)
        game_graphics.main_character("я поделюсь с...")
        sleep(0.5)
        print("\n"*100)
        game_graphics.main_character("..тобой.")
        sleep(0.7)
        print("\n"*100)
        game_graphics.main_character("Числовой диапозон")
        sleep(0.6)
        print("\n"*100)
        game_graphics.main_character("будет на песке")
        sleep(0.9)
        print("\n"*100)
        game_graphics.main_character("Будь осторожен!")
        sleep(0.9)
        print("\n"*100)
        game_graphics.main_character("У тебя есть...")
        sleep(0.8)
        print("\n"*100)
        game_graphics.main_character("..несколько...")
        sleep(0.5)
        print("\n"*100)
        game_graphics.main_character("...попыток.")
        sleep(0.5)
        print("\n"*100)
        game_graphics.main_character("Если исчерпаешь..")
        sleep(0.9)
        print("\n"*100)
        game_graphics.main_character("..их, то умрешь")
        sleep(0.7)
        print("\n"*100)
        game_graphics.main_character("    Удачи!")
        sleep(1)
        print("\n"*100)
        menu = True                       
    elif i == "0":
        menu = True
    while menu:
        print("\n"*100)
        game_graphics.game_intro()
        print("")
        game_graphics.menu_c("Начинай игру!")
        print("\nМаксимальное количество уровней, которое вы смогли пройти: {0}\n".format(game_record))
        game_graphics.menu_buttons()
        i = str(input("Введите число(1-0): ")) 
        if i == "0":
            menu = False
            start_the_game = False
        elif i == "1":
            new_try = True
            while new_try:
                global level_number, health, var_diaposon_array, new_level, asked_number, gamers_number, var_to_creat_array, warning
                health = 7
                diaposon = []
                var_diaposon_array = []
                var_to_creat_array = 0
                asked_number = 0
                new_level = 2
                level_number = 0
                gamers_number = 0
                warning = " Введите число!" 
                game_creat_number = True
                while game_creat_number:
                    var_diaposon_array = []
                    level = 2**new_level + 3
                    asked_number = randint(0, level)
                    game = True
                    while game:
                        print("\n"*100)
                        if health == 0:
                            print("\n"*100)
                            game_graphics.death(level_number)
                            i = str(input("Введите число(1-0): "))
                            if i == "0":
                                new_try = False
                                game_creat_number = False
                                game = False
                                break
                            elif i == "1":
                                game_creat_number = False
                                game = False
                                break
                            else:
                                continue
                        try_to_guess.diaposon_array(level, var_to_creat_array, gamers_number)
                        game_graphics.game(warning, diaposon)
                        try_to_guess.gamers_health(health)
                        try:
                            gamers_number = int(input())
                            try_to_guess.check_gamers_number(gamers_number)
                            if var_to_check  == 3:
                                warning = Fore.RED + " Число меньше!.." + Style.RESET_ALL
                                var_to_creat_array = 3
                                health -= 1
                            elif var_to_check == 2:
                                warning = Fore.MAGENTA +  " Число больше!.." + Style.RESET_ALL
                                var_to_creat_array = 2
                                health -= 1
                            elif var_to_check == 5:
                                
                                print("\n"*100)
                                level_number += 1
                                if game_record < level_number:
                                    level_number = str(level_number)
                                    record = open("records.txt", "w")
                                    record.write(level_number)
                                    record.close
                                    game_record = int(level_number)
                                level_number = int(level_number)
                                game_graphics.chest(level_number)
                                sleep(2)
                                var_to_creat_array = 0
                                health += 1
                                new_level += 1
                                warning = " Введите число!"
                                game = False                                
                        except ValueError:
                            pass
        else:
            continue    
            
            


