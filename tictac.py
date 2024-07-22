print("Welcome to tic tac toe ",end="\n")
t=[" "," "," "," "," "," "," "," "," "]

def print_board():
    print("----------",end="\n")
    print(t[0],"|",t[1],"|",t[2],end="\n")
    print("----------",end="\n")
    print(t[3],"|",t[4],"|",t[5],end="\n")
    print("----------",end="\n")
    print(t[6],"|",t[7],"|",t[8],end="\n")
    print("----------",end="\n")

print_board()

print("Instruction to play",end="\n")
print("For player 1 the move symbol is x and for player 2 is O",end="\n")
print("To enter the symbol you will have to enter the position no",end="\n")
print("The position in row 1 is 1 2 3 and row 2 is 4 5 6 and row 3 is 7 8 and 9",end="\n")
p1=0
p2=0
g=1
while g!=2:
    print("Enter your move Player1",end="\n")
    m=int(input("Enter the position in the board:-"))
    while(t[m-1]!=" "):
        print("Invalid Choice")
        print("Enter your move Player1",end="\n")
        m=int(input("Enter the position in the board:-"))
        
    t[m-1]="X"
    print_board()

    if(t[0] == t[1] == t[2] == 'X' or t[3] == t[4] == t[5] == 'X' or t[6] == t[7] == t[8] == 'X' or
        t[0] == t[3] == t[6] == 'X' or t[1] == t[4] == t[7] == 'X' or t[2] == t[5] == t[8] == 'X' or
        t[0] == t[4] == t[8] == 'X' or t[2] == t[4] == t[6] == 'X'):
        print_board()
        print("Player 1 wins")
        g = 2
        break

    if " " not in t:
        print("The game is a draw")
        break

    print("Enter your move Player2",end="\n")
    k=int(input("Enter the position in the board:-"))
    
    while(t[k-1]!=" "):
        print("Invalid Choice")
        print("Enter your move Player2",end="\n")
        k=int(input("Enter the position in the board:-"))

    t[k-1]="O"
    print_board()

    if (t[0] == t[1] == t[2] == 'O' or t[3] == t[4] == t[5] == 'O' or t[6] == t[7] == t[8] == 'O' or
        t[0] == t[3] == t[6] == 'O' or t[1] == t[4] == t[7] == 'O' or t[2] == t[5] == t[8] == 'O' or
        t[0] == t[4] == t[8] == 'O' or t[2] == t[4] == t[6] == 'O'):
        print_board()
        print("Player 2 wins")
        g = 2
        break

    if " " not in t:
        print("The game is a draw")
        break
    
    
    
