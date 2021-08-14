import random
answer=int(input("do nafare(1)   tak nafare(2) : "))
def show_game_board():
    for i in range(3):
        for j in range(3):
            print(game[i][j] , end=' ')  
        print()
def check():
    if (game[0][0]=='X' and game[0][1]=='X' and game[0][2]=='X') or (game[1][0]=='X' and game[1][1]=='X' and game[1][2]=='X') or (game[2][0]=='X' and game[2][1]=='X' and game[2][2]=='X'):
        print("nafar aval bord")
        exit()
    elif (game[0][0]=='X' and game[1][0]=='X' and game[2][0]=='X') or (game[0][1]=='X' and game[1][1]=='X' and game[2][1]=='X') or (game[0][2]=='X' and game[1][2]=='X' and game[2][2]=='X'):
        print("nafar dovom board")
        exit()  
    elif (game[0][0]=='X' and game[1][1]=='X' and game[2][2]=='X') or (game[0][2]=='X' and game[1][1]=='X' and game[2][0]=='X') :
        print("nafar aval bord")
        exit()      
    elif (game[0][0]=='O' and game[0][1]=='O' and game[0][2]=='O') or (game[1][0]=='O' and game[1][1]=='O' and game[1][2]=='O') or (game[2][0]=='O' and game[2][1]=='O' and game[2][2]=='O'):
        print("nafar dovom bord")
        exit() 
    elif (game[0][0]=='O' and game[1][0]=='O' and game[2][0]=='O') or (game[0][1]=='O' and game[1][1]=='O' and game[2][1]=='O') or (game[0][2]=='O' and game[1][2]=='O' and game[2][2]=='O'):
        print("nafar dovom bord")
        exit() 
    elif (game[0][0]=='O' and game[1][1]=='O' and game[2][2]=='O') or (game[0][2]=='O' and game[1][1]=='O' and game[2][0]=='O') :
        print("nafar dovom bordplayer2 win")
        exit()           


game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]

show_game_board()    

while True:

    print("vared kon:")
    while True:
        row=int(input("enter the row: ")) 
        col=int(input("enter the clomun "))  
        if 0<=row<=2 and 0<=col<=2:
            if game[row][col]=='_':
                game[row][col] = 'X'
                break
            else:
                print("bazi ro glitch nakon")
                break
        else:
            print("index is out of range , Try again!")
    show_game_board()
    check()   
    print("vared kon nafar dovom")
    while True:
        if answer == "1":
            row=int(input("enter the row")) 
            col=int(input("enter the clomun"))
        if 0<=row<=2 and 0<=col<=2:  
            if game[row][col]=='_': 
                    game[row][col] = 'O'
                    break
            else:
                print("glitch nakon")
                break
  
        else:
            print("index is out of range , Try again!")
        show_game_board()
        check()

   
        print("player 2 PC :")
        while True:
            if answer == "2":
                row=random.randint(0,2)
                col=random.randint(0,2)  
            if game[row][col]=='_': 
                game[row][col] = 'O'
                break
        show_game_board()
        check()