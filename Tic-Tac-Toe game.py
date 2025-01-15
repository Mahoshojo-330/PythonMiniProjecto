#Write a program to play Tic-Tac-Toe against the computer.
#思路
#如何玩这个游戏？ - 设置一个3*3的矩阵 - 用户输入矩阵的坐标就print出 o - 具体效果如下
#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
import random
from collections import Counter

lis = [0]*9
board = [lis [j:j+3] for j in range (0,9,3)]
print (board)
filename = "数对形式保存的对局信息.txt"
counting = 1
check_list = []
n_index = counting
iterating_output_list = []

def user_input () :
    y = int(input("please input the x coordinate: ")) - 1
    x = int(input("please input the y coordinate: ")) - 1
    
    if 3 > x > -1 and 3 > y > -1:
        if (y+1,x+1) in check_list:
            print("You know this is cheating, right?")
            pair = (0,0)
            check_list.append(pair)
        else :
            board[x][y] = '/'
            pair = (y+1,x+1)
            check_list.append(pair)
    else:
        print("valid coordinates please")
    #在列表中写入(x,y)的数对

def iterating (strlist, check_list,output_list) :
    '''
    check if the current list is in the file
    '''
    list_data = eval(strlist)
    def bool_return():
        '''
        if the current list is in the file, return True
        else return False
        '''
        #if Ture
        for u in range(len(check_list)):
            if list_data [u] == check_list [u]:
                return True
            else:
                return False
        
    if bool_return() == True:
        output_list.append(list_data[counting])
        return True
    else:
        return False
    
        
def check_file(filename, check_list, output_list) :
    '''
    check if the file is valid
    check if there's anything in the file
    '''

    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            #if there's no line written, return False
            #if there is, return iterating
            if not lines:
                return False
            else:
                for line in lines :
                    linestr = line.strip()
                    return iterating (linestr,check_list, output_list)
    except FileNotFoundError:
        print(f"{filename} created")
        with open(filename, 'w') as file:
            return False
        

        
        
# if a list is not qualified, retun False
def add_pair() :
    iterating_output_list 
    if check_file(filename,check_list,iterating_output_list) != False:
        counts = Counter(iterating_output_list)
        most_common = counts.most_common(1)
        x , y = map(int,most_common[0][0])
        pair = (x, y)
        board[y-1][x-1] = "X"
        check_list.append(pair)
        iterating_output_list = []

    else:
        return False

def random_pair():
    while True:
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        new_pair = (y+1, x+1)
        if new_pair not in check_list:
            break
    check_list.append(new_pair)
    board[x][y] = 'X'

def update_lis() :
    if counting % 2 == 1:  # 判断输入次数的奇偶性
        user_input()
    else:
        if add_pair() == False:
            random_pair()
        else:
            add_pair()

    for row in board:
            print(' '.join(map(str, row)))


                
def check_winner(board, player):
    # 检查行和列
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return False
    # 检查对角线
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return False
    return True

while check_winner(board , "X"):
    update_lis()
    counting += 1
    print(check_list)
    if counting == 9:
        break
    if check_winner(board,"/") == False:
        break

if not(check_winner(board,"X")):
     print("you lost...")
elif not(check_winner(board,"/")):
     print("you won!")
else :
    print("draw")

def record(target_tuples):
    with open ("数对形式保存的对局信息.txt","a+") as file:
        file.write (f"{target_tuples} \n")

#假设用户永远先手，即为奇数
if check_winner(board,"/") == True and (0,0) not in check_list:
    print (check_list)
    record(check_list)

