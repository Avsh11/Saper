import os
from random import randint
from colorama import Fore, Back

def printWhite(data):
    print(Fore.WHITE,data,end="",sep="")

def printRed(data):
    print(Fore.RED,data,end="",sep="")

def printGreen(data):
    print(Fore.GREEN,data,end="",sep="")

def screenXO(screen):
    os.system('cls')

    
    corners = {
               "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195 
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
              }
    lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
              }
    
    size = len(screen)                  #grid_size ekranu

    verticalLine = [lines["horizontal"]*3]*size         #lista zawierająca poziome linie
    # print(verticalLine)
    
    verticalUp = corners["upperMid"].join(verticalLine)
    verticalMid = corners["midiumMid"].join(verticalLine)
    verticalDown = corners["bottomMid"].join(verticalLine)
    # print(verticalUp)
    # print(verticalMid)
    # print(verticalDown)

   

    printWhite(corners["upperLeft"]+verticalUp+corners["upperRight"]+"\n")
 
    for i,row in enumerate(screen):
        printWhite(lines["vertical"])
        for j in row:
            if j == "" : printRed("   ")
            elif j == -1 : printRed(" ⚑ ")
            elif j == 0: printWhite(" 0 ")
            elif j == 1 : printGreen(" 1 ")
            elif j == 2 : printGreen(" 2 ")
            elif j == 3 : printGreen(" 3 ")
            elif j == 4 : printGreen(" 4 ")
            elif j == 5 : printGreen(" 5 ")
            elif j == 6 : printGreen(" 6 ")
            elif j == 7 : printGreen(" 7 ")
            elif j == 8 : printGreen(" 8 ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")

def openField(x, y):
    if grid_opened[y][x] == "":
        if grid_data[y][x] == 0:
            grid_opened[y][x] = grid_data[y][x]
            if x != 0: openField(x - 1, y)
            if x != grid_size - 1: openField(x + 1, y)
            if y != 0: openField(x, y - 1)
            if y != grid_size - 1: openField(x, y + 1)
        elif grid_data[y][x] > 0:
            grid_opened[y][x] = grid_data[y][x]
        elif grid_data[y][x] == -1:
            grid_opened[y][x] = grid_data[y][x]

if __name__ == "__main__":

    grid_size = 10
    bombs_amount = 10
    grid_data = []
    grid_opened = []
    
    for i in range(grid_size):
        row = [0 for i in range(grid_size)]
        grid_data.append(row)
     
    for i in range(grid_size):
        row = ["" for i in range(grid_size)]
        grid_opened.append(row)
    
    i = 0
    while True:
        bomb_x = randint(0, grid_size - 1)
        bomb_y = randint(0, grid_size - 1)
        if grid_data[bomb_y][bomb_x] != -1:
            grid_data[bomb_y][bomb_x] = -1
            i+=1
        if i == bombs_amount:
            break
    
    grid_y = 0
    while grid_y<grid_size:
        grid_x = 0
        while grid_x<grid_size:
            bordering_bombs_amount = 0
            if grid_data[grid_y][grid_x] == 0:
                if grid_y != 0 and grid_data[grid_y - 1][grid_x] == -1:
                    bordering_bombs_amount+=1
                if grid_y != grid_size - 1 and grid_data[grid_y + 1][grid_x] == -1:
                    bordering_bombs_amount+=1
                if grid_x != 0 and grid_data[grid_y][grid_x - 1] == -1:
                    bordering_bombs_amount+=1
                if grid_x != grid_size - 1 and grid_data[grid_y][grid_x + 1] == -1:
                    bordering_bombs_amount+=1
                if grid_y != 0 and grid_x != 0 and grid_data[grid_y - 1][grid_x - 1] == -1:
                    bordering_bombs_amount+=1
                if grid_y != 0 and grid_x != grid_size - 1 and grid_data[grid_y - 1][grid_x + 1] == -1:
                    bordering_bombs_amount+=1
                if grid_y != grid_size - 1 and grid_x != 0 and grid_data[grid_y + 1][grid_x - 1] == -1:
                    bordering_bombs_amount+=1
                if grid_y != grid_size - 1 and grid_x != grid_size - 1 and grid_data[grid_y + 1][grid_x + 1] == -1:
                    bordering_bombs_amount+=1
                grid_data[grid_y][grid_x] = bordering_bombs_amount
            grid_x+=1
        grid_y+=1

    while True:
        screenXO(grid_opened)
        x = int(input("Podaj wsp x: "))
        y = int(input("Podaj wsp y: "))
        openField(x, y)
