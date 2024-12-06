import random
user_grid=[]
computer_grid=[]

def get_position(i, j):
    if i==1:
        num=j+0
        return num
    elif i==2:
        num=j+3
        return num
    elif i==3:
        num=j+6
        return num

def print_grid(list1,list2):
    text=""
    for i in range(1,4):
        for j in range(1,4):
            position=get_position(i,j)
            check1= position in list1 
            check2= position in list2
            if check1:
                text += "X "
            elif check2:
                text += "O "
            else :
                text += "_ "
        print(text)
        text=""
    print("\n")


def ran_generator():
    l1=[1,2,3,4,5,6,7,8,9]
    num=random.choice(l1)
    while(num in computer_grid or num in user_grid):
        num=random.choice(l1)
    computer_grid.append(num)
    return num

def take_input():
    number=int(input("Enter the number of your grid:")) 
    while((number in user_grid) or (number in computer_grid) or number not in range(1,10)):
        print("wrong number, enter again")
        number=int(input("Enter the number of your grid:"))
    user_grid.append(number)
    return number

def get_cr(n):
    if n in range(1,4):
        return [1, n]
    elif n in range(4,7):
        return [2,n-3]
    elif n in range(7,10):
        return [3,n-6]

def is_win(list):
    wp=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9]]
    for i in wp:
        count=0
        for j in i:
            if j in list:
                count+=1
        if count>=3:
            
            return True
            
    return False
                
def play_game():
    while(1):
        take_input()
        print_grid(user_grid,computer_grid)
        if is_win(user_grid):
            print("Congratulations, you won!")
            return
        if (len(user_grid)+len(computer_grid))==9:
            print("It's a draw")
            break
        ran_generator()
        print_grid(user_grid,computer_grid)
        if is_win(computer_grid):
            print("Oops! You lost")
            return

play_game()
