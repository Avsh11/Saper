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
    
    size = len(screen)                  #rozmiar ekranu

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
            if j==-1 : printRed("-1 ")
            elif j==1 : printGreen(" 1 ")
            elif j==2 : printGreen(" 2 ")
            elif j==3 : printGreen(" 3 ")
            elif j==4 : printGreen(" 4 ")
            elif j==5 : printGreen(" 5 ")
            elif j==6 : printGreen(" 6 ")
            elif j==7 : printGreen(" 7 ")
            elif j==8 : printGreen(" 8 ")
            elif j==0: printWhite(" 0 ")
            else: printWhite("   ")
            printWhite(lines["vertical"])            
        print()
        if(i < size-1): printWhite(corners["mediumLeft"]+verticalMid+corners["mediumRight"]+"\n")

    printWhite(corners["bottomLeft"]+verticalDown+corners["bottomRight"]+"\n")



if __name__ == "__main__":

    rozmiar = 10
    ilosc_bomb = 50
    dane = []
    
    for i in range(rozmiar):
        kolumna = [0 for i in range(rozmiar)]
        dane.append(kolumna)
    
    i = 0
    while True:
        bomba_x = randint(0, rozmiar-1)
        bomba_y = randint(0, rozmiar-1)
        if dane[bomba_y][bomba_x] == 0:
            dane[bomba_y][bomba_x] = -1
            i+=1
        if i==ilosc_bomb:
            break
    
    dane_y = 0
    while dane_y<rozmiar:
        dane_x = 0
        while dane_x<rozmiar:
            ilosc_obszar_bomb = 0
            if dane[dane_y][dane_x] == 0:
                if dane_y != 0 and dane[dane_y - 1][dane_x] == -1:
                    ilosc_obszar_bomb+=1
                if dane_y != rozmiar - 1 and dane[dane_y + 1][dane_x] == -1:
                    ilosc_obszar_bomb+=1
                if dane_x != 0 and dane[dane_y][dane_x - 1] == -1:
                    ilosc_obszar_bomb+=1
                if dane_x != rozmiar - 1 and dane[dane_y][dane_x + 1] == -1:
                    ilosc_obszar_bomb+=1
                if dane_y != 0 and dane_x != 0 and dane[dane_y - 1][dane_x - 1] == -1:
                    ilosc_obszar_bomb+=1
                if dane_y != 0 and dane_x != rozmiar - 1 and dane[dane_y - 1][dane_x + 1] == -1:
                    ilosc_obszar_bomb+=1
                if dane_y != rozmiar - 1 and dane_x != 0 and dane[dane_y + 1][dane_x - 1] == -1:
                    ilosc_obszar_bomb+=1
                if dane_y != rozmiar - 1 and dane_x != rozmiar - 1 and dane[dane_y + 1][dane_x + 1] == -1:
                    ilosc_obszar_bomb+=1
                dane[dane_y][dane_x] = ilosc_obszar_bomb
            dane_x+=1
        dane_y+=1
    
    # print(dane)
   

    #gracz = 1
    #while True:
    screenXO(dane)
    #    if gracz == 1: printGreen("Gracz 1\n")
    #    else: printRed("Gracz 2\n")
    #    x = int(input("Podaj wsp x: "))
    #    y = int(input("Podaj wsp y: "))
    #    dane[y][x] = gracz
    #    gracz *= -1
