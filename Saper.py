import os
from math import floor
from random import randint
from colorama import Fore, Style

def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printYellow(data):
    print(Fore.YELLOW,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printBlueBright(data):
    print(Fore.BLUE,Style.BRIGHT,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printBlueDim(data):
    print(Fore.BLUE,Style.DIM,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printRedDim(data):
    print(Fore.RED,Style.DIM,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printCyanBright(data):
    print(Fore.CYAN,Style.BRIGHT,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def printWhiteDim(data):
    print(Fore.WHITE,Style.DIM,data,end="",sep="")
    print(Style.RESET_ALL,end="")

def screenMinesweeper(screen):
    os.system('cls')
    
    corners = {
               "upperLeft":     "┌",
               "upperRight":    "┐",
               "mediumLeft":    "├", 
               "mediumRight":   "┤",
               "bottomLeft":    "└",
               "bottomRight":   "┘",
               "upperMid":      "┬",
               "midiumMid":     "┼",
               "bottomMid":     "┴"
              }
    lines =   {
               "vertical": "│",
               "horizontal": "─"
              }
    
    size = len(screen)
    
    verticalLine = [lines["horizontal"] * 3] * size
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
    
    printWhite(corners["upperLeft"] + verticalUp + corners["upperRight"] + "\n")
    
    for i, row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if j == "blank":
                printWhiteDim(" ■ ")
            elif j == "bomb":
                printRed(" ⬤ ")
            elif j == "flag":
                printRed(" ⚑ ")
            elif j == 0:
                printWhite("   ")
            elif j == 1:
                printBlueBright(" 1 ")
            elif j == 2:
                printGreen(" 2 ")
            elif j == 3:
                printRed(" 3 ")
            elif j == 4:
                printBlueDim(" 4 ")
            elif j == 5:
                printRedDim(" 5 ")
            elif j == 6:
                printCyanBright(" 6 ")
            elif j == 7:
                printWhiteDim(" 7 ")
            elif j == 8:
                printWhite(" 8 ")
            else:
                printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size - 1): printWhite(corners["mediumLeft"] + verticalMid + corners["mediumRight"] + "\n")
    
    printWhite(corners["bottomLeft"] + verticalDown + corners["bottomRight"] + "\n")

def waitForInput():
    printRed("Wciśnij dowolny klawisz aby kontynować...")
    input()

def checkXY(x, y):
    if (x < 0 or x > grid_size - 1) and (y < 0 or y > grid_size - 1):
        printRed("Podane współrzędne są poza zakresem\n")
        waitForInput()
        return False
    elif x < 0 or x > grid_size - 1:
        printRed("Podana współrzędna x jest poza zakresem\n")
        waitForInput()
        return False
    elif y < 0 or y > grid_size - 1:
        printRed("Podana współrzędna y jest poza zakresem\n")
        waitForInput()
        return False
    else:
        return True

def openField(x, y, first_time):
    global is_game_over
    
    if checkXY(x, y) == True:
        if grid_opened[y][x] == "blank":
            if grid_data[y][x] == 0:
                grid_opened[y][x] = grid_data[y][x]
                if x != 0: openField(x - 1, y, False)
                if x != grid_size - 1: openField(x + 1, y, False)
                if y != 0: openField(x, y - 1, False)
                if y != grid_size - 1: openField(x, y + 1, False)
            elif grid_data[y][x] in range(1, 8):
                grid_opened[y][x] = grid_data[y][x]
            elif grid_data[y][x] == "bomb":
                is_game_over = True
        elif grid_opened[y][x] == "flag":
            printRed("Nie możesz otworzyć oflagowanego pola\n")
            waitForInput()
        elif first_time == True:
            printRed("Pole jest już otwarte\n")
            waitForInput()

def flagField(x, y):
    global flags_available
    global bombs_left
    global is_game_over
    
    if checkXY(x, y) == True:
        if grid_opened[y][x] == "blank" and flags_available > 0:
            grid_opened[y][x] = "flag"
            flags_available-=1
            if grid_data[y][x] == "bomb":
                bombs_left-=1
                if bombs_left == 0:
                    is_game_over = True
        elif grid_opened[y][x] == "flag":
            grid_opened[y][x] = "blank"
            flags_available+=1
            if grid_data[y][x] == "bomb":
                bombs_left+=1
        elif flags_available == 0:
            printRed("Przekroczyłeś limit flag\n")
            waitForInput()
        else:
            printRed("Nie można oflagować otwartego pola\n")
            waitForInput()

if __name__ == "__main__":
    os.system('cls')
    
    printYellow("                           ,-.----.                         \n")
    printYellow("  .--.--.      ,---,       \    /  \      ,---,.,-.----.    \n")
    printYellow(" /  /    '.   '  .' \      |   :    \   ,'  .' |\    /  \   \n")
    printYellow("|  :  /`. /  /  ;    '.    |   |  .\ :,---.'   |;   :    \  \n")
    printYellow(";  |  |--`  :  :       \   .   :  |: ||   |   .'|   | .\ :  \n")
    printYellow("|  :  ;_    :  |   /\   \  |   |   \ ::   :  |-,.   : |: |  \n")
    printYellow(" \  \    `. |  :  ' ;.   : |   : .   /:   |  ;/||   |  \ :  \n")
    printYellow("  `----.   \|  |  ;/  \   \;   | |`-' |   :   .'|   : .  /  \n")
    printYellow("  __ \  \  |'  :  | \  \ ,'|   | ;    |   |  |-,;   | |  \  \n")
    printYellow(" /  /`--'  /|  |  '  '--'  :   ' |    '   :  ;/||   | ;\  \ \n")
    printYellow("'--'.     / |  :  :        :   : :    |   |    \:   ' | \.' \n")
    printYellow("  `--'---'  |  | ,'        |   | :    |   :   .':   : :-'   \n")
    printYellow("            `--''          `---'.|    |   | ,'  |   |.'     \n")
    printYellow("                             `---`    `----'    `---'       \n")
    printYellow("\n\nPo prostu Saper\n")
    printYellow("Odkrywaj pola aby dowiedzieć się z iloma bombami graniczą\n")
    printYellow("Aby wygrać musisz oznaczyć wszystkie bomby za pomocą flag\n")
    printYellow("Aby odznaczyć polę należy jeszcze raz użyć polecenia oznaczenia pola\n\n")
    printYellow("Gra wykonana przez Szymona Kumorka i Krystiana Filipka\n\n")
    
    waitForInput()
    
    while True:
        try:
            os.system('cls')
            
            printWhiteDim("Podaj rozmiar kwadratowej planszy\n")
            input_grid_size = int(input())
            
            input_bombs_amount_min = max(1, floor(input_grid_size**2 / 10))
            input_bombs_amount_max = input_grid_size**2 - 1
            
            printYellow("Ilość bomb powinna być od " + str(input_bombs_amount_min) + " do " + str(input_bombs_amount_max) + "\n")
            
            printWhiteDim("Podaj ilość bomb\n")
            input_bombs_amount = int(input())
            if input_bombs_amount >= input_bombs_amount_min and input_bombs_amount <= input_bombs_amount_max:
                os.system('cls')
                
                printWhiteDim("Czy następujące dane zgadzają się? (napisz Y aby kontynować)\n")
                printYellow("Rozmiar planszy: " + str(input_grid_size) + "\n")
                printYellow("Ilość bomb: " + str(input_bombs_amount) + "\n")
                
                decision = input()
                
                if decision == "Y":
                    break
            else:
                printRed("Podana ilość bomb jest poza zakresem\n")
                waitForInput()
        except:
            printRed("Podano nieprawidłowe dane\n")
            waitForInput()
    
    grid_size = input_grid_size
    bombs_amount = input_bombs_amount
    grid_data = []
    grid_opened = []
    
    for i in range(grid_size):
        row = [0 for i in range(grid_size)]
        grid_data.append(row)
     
    for i in range(grid_size):
        row = ["blank" for i in range(grid_size)]
        grid_opened.append(row)
    
    i = 0
    while True:
        bomb_x = randint(0, grid_size - 1)
        bomb_y = randint(0, grid_size - 1)
        if grid_data[bomb_y][bomb_x] != "bomb":
            grid_data[bomb_y][bomb_x] = "bomb"
            i+=1
        if i == bombs_amount:
            break
    
    grid_y = 0
    while grid_y<grid_size:
        grid_x = 0
        while grid_x<grid_size:
            bordering_bombs_amount = 0
            if grid_data[grid_y][grid_x] == 0:
                if grid_y != 0 and grid_data[grid_y - 1][grid_x] == "bomb":
                    bordering_bombs_amount+=1
                if grid_y != grid_size - 1 and grid_data[grid_y + 1][grid_x] == "bomb":
                    bordering_bombs_amount+=1
                if grid_x != 0 and grid_data[grid_y][grid_x - 1] == "bomb":
                    bordering_bombs_amount+=1
                if grid_x != grid_size - 1 and grid_data[grid_y][grid_x + 1] == "bomb":
                    bordering_bombs_amount+=1
                if grid_y != 0 and grid_x != 0 and grid_data[grid_y - 1][grid_x - 1] == "bomb":
                    bordering_bombs_amount+=1
                if grid_y != 0 and grid_x != grid_size - 1 and grid_data[grid_y - 1][grid_x + 1] == "bomb":
                    bordering_bombs_amount+=1
                if grid_y != grid_size - 1 and grid_x != 0 and grid_data[grid_y + 1][grid_x - 1] == "bomb":
                    bordering_bombs_amount+=1
                if grid_y != grid_size - 1 and grid_x != grid_size - 1 and grid_data[grid_y + 1][grid_x + 1] == "bomb":
                    bordering_bombs_amount+=1
                grid_data[grid_y][grid_x] = bordering_bombs_amount
            grid_x+=1
        grid_y+=1
    
    is_game_over = False
    flags_available = bombs_amount
    bombs_left = bombs_amount
    
    while True:
        try:
            screenMinesweeper(grid_opened)
            
            printYellow("Zostało " + str(flags_available) + " flag do użycia\n")
            #printYellow("Zostało " + str(bombs_left) + " nieoznaczonych bomb\n")
            
            printYellow("Współrzędne powinny być od 1 do " + str(grid_size) + "\n")
            printYellow("Dostępne akcje: open, flag\n")
            printWhiteDim("Podaj jaką akcję chcesz wykonać i współrzędne(akcja x y)\n")
            input_string = input()
            input_list = input_string.split(" ")
            action = input_list[0]
            x = int(input_list[1]) - 1
            y = int(input_list[2]) - 1
            
            if action == "open":
                openField(x, y, True)
            elif action == "flag":
                flagField(x, y)
            else:
                printRed("Podano akcja nie istnieje\n")
                waitForInput()
            
            if is_game_over == True:
                if(bombs_left == 0):
                    screenMinesweeper(grid_opened)
                    printYellow("Wygrałeś")
                else:
                    screenMinesweeper(grid_data)
                    printYellow("Przegrałeś")
                break
        except:
            printRed("Podano nieprawidłowe dane\n")
            waitForInput()
