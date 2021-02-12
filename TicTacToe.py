# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 22:59:30 2021

@author: Prthamesh
"""

from time import sleep
from tkinter import *
from tkinter import messagebox
import copy

root = Tk()

root.title('Tic-Tac-Toe')
#root.iconbitmap('logo.ico')
root.resizable(width=False,height=False)
root.configure(background='#4287f5')

player_modes = [
    ('Human','H',1),
    ('Computer','C',2)
    ]

def player_1_rb_clicked():
    if player_1.get() == 'C' and player_2.get() == 'C':
        player_2.set('H')

def player_2_rb_clicked():
    if player_2.get() == 'C' and player_1.get() == 'C':
        player_1.set('H')

# Label and radio buttons for player 1 selection
label_1 = Label(root,text='Player 1:',bg='#f7b019',fg='black')
label_1.grid(row=0,column=0,padx=10,pady=10)
player_1 = StringVar()
player_1.set('H')
player_1_radio_button_list = []
for t,v,c in player_modes:
    rb = Radiobutton(root,text=t,variable=player_1,value=v,command=player_1_rb_clicked,bg='#f7b019',activebackground='#f7b019')
    rb.grid(row=0,column=c)
    player_1_radio_button_list.append(rb)
    
# Label and radio buttons for player 2 selection
label_2 = Label(root,text='Player 2:',bg='#f7b019',fg='black')
label_2.grid(row=1,column=0)
player_2 = StringVar()
player_2.set('H')
player_2_radio_button_list = []
for t,v,c in player_modes:
    rb = Radiobutton(root,text=t,variable=player_2,value=v,command=player_2_rb_clicked,bg='#f7b019',activebackground='#f7b019')
    rb.grid(row=1,column=c)
    player_2_radio_button_list.append(rb)
    
def enable_digit_buttons():
    for btn in button_list:
        btn.config(state=ACTIVE)
        btn['text'] = ''
        btn['bg'] = 'SystemButtonFace'
        btn['fg'] = 'white'

def disable_digit_buttons():
    for btn in button_list:
        btn.config(state=DISABLED)
    
def enable_radio_buttons():
    for rb in player_1_radio_button_list: rb.config(state=ACTIVE)
    for rb in player_2_radio_button_list: rb.config(state=ACTIVE)

def disable_radio_buttons():
    for rb in player_1_radio_button_list: rb.config(state=DISABLED)
    for rb in player_2_radio_button_list: rb.config(state=DISABLED)

def start_the_game():
    global player_1_value,player_2_value,current_player,count,availableActions
    count = 0
    availableActions = ['1','2','3','4','5','6','7','8','9']
    player_1_value = player_1.get()
    player_2_value = player_2.get()
    current_player = 1
    enable_digit_buttons()
    disable_radio_buttons()
    play_button.config(state=DISABLED)
    reset_button.config(state=ACTIVE)
    if player_1_value == 'C':
        move = '1'
        play_computer_move(move,'X')
        current_player = 2
        count += 1
        availableActions.remove(move)
    
def reset_the_game():
    for btn in button_list:
        btn['text'] = ''
        btn.config(bg='SystemButtonFace')
        btn.config(activebackground='SystemButtonFace')
    enable_radio_buttons()
    disable_digit_buttons()
    reset_button.config(state=DISABLED)
    play_button.config(state=ACTIVE)
    play_button.config(bg='#f7b019')
    
def get_board_state():
    board_state = [['1','2','3'],['4','5','6'],['7','8','9']]
    for i,btn in enumerate(button_list):
        if btn['text'] == 'X':
            board_state[i//3][i%3] = 'X'
        elif btn['text'] == 'O':
            board_state[i//3][i%3] = 'O'
    print(*board_state,sep='\n')
    return board_state
    
def get_computer_move(board_state):
    move = minimaxDecision(copy.deepcopy(board_state))
    print(move)
    return move

def play_computer_move(move,symbol):
    btn = button_list[int(move)-1]
    btn['text'] = symbol
    btn['bg'] = 'black'
    btn['fg'] = 'white'
    btn['activebackground'] = 'black'
    btn['activeforeground'] = 'white'

def check_if_won():
    global winner,winner_location
    winner = False
    winner_symbol = None
    winner_location = None
    if b1['text']==b2['text'] and b2['text']==b3['text'] and b3['text']!='':
        winner_location = [1,2,3]
    elif b4['text']==b5['text'] and b5['text']==b6['text'] and b6['text']!='':
        winner_location = [4,5,6]
    elif b7['text']==b8['text'] and b8['text']==b9['text'] and b9['text']!='':
        winner_location = [7,8,9]
    elif b1['text']==b4['text'] and b4['text']==b7['text'] and b7['text']!='':
        winner_location = [1,4,7]
    elif b2['text']==b5['text'] and b5['text']==b8['text'] and b8['text']!='':
        winner_location = [2,5,8]
    elif b3['text']==b6['text'] and b6['text']==b9['text'] and b9['text']!='':
        winner_location = [3,6,9]
    elif b1['text']==b5['text'] and b5['text']==b9['text'] and b9['text']!='':
        winner_location = [1,5,9]
    elif b3['text']==b5['text'] and b5['text']==b7['text'] and b7['text']!='':
        winner_location = [3,5,7]
    if winner_location:
        winner = True
        if button_list[winner_location[0]-1]['text'] == 'X':
            winner_symbol = 'X'
        else:
            winner_symbol = 'O'
        for loc in winner_location:
            button_list[loc-1]['fg']='#f7b019'
            button_list[loc-1]['activeforeground']='#f7b019'
        root.update()
        messagebox.showinfo('Tic Tac Toe',winner_symbol+' is the Winner!!!')
        disable_digit_buttons()
        winner = False
        winner_symbol = None
        winner_location = None
        return True
        
def game_over():
    messagebox.showinfo('Tic Tac Toe','Game over! Nobody wins the game.')
    disable_digit_buttons()
    
def terminalTest(m,player):
    if player == 1:
        if player_1_value == 'C':
            l = ['X','X','X']
        elif player_2_value == 'C':
            l = ['O','O','O']
    else:
        if player_1_value == 'H':
            l = ['X','X','X']
        elif player_2_value == 'H':
            l = ['O','O','O']
    if (
        m[0] == l or 
        m[1] == l or
        m[2] == l or
        [row[0] for row in m] == l or
        [row[1] for row in m] == l or
        [row[2] for row in m] == l or   
        [row[i] for (row,i) in zip(m,range(0,3,1))] == l or
        [row[i] for (row,i) in zip(m,range(2,-1,-1))] == l
        ): 
        #print('GAME HAS ENDED')
        return True
    return False
    
def result(s,action,player):
    px,py = (int(action)-1)//3,(int(action)-1)%3
    if player == 1:
        if player_1_value == 'C':
            s[px][py] = 'X'
        elif player_2_value == 'C':
            s[px][py] = 'O'
    else:
        if player_1_value == 'H':
            s[px][py] = 'X'
        elif player_2_value == 'H':
            s[px][py] = 'O'
    return s
    
def minimaxDecision(state):
    print('Computer thinking ...')
    aa = availableActions[:]
    print('available actions:',aa)
    maxv,maxa = (-10,None)
    for action in aa:
        #print(action)
        s = copy.deepcopy(state)
        tempaa = copy.deepcopy(aa)
        tempaa.remove(action)
        v = minValue(result(s,action,1),tempaa)
        if v>maxv:
            maxv = v
            maxa = action
    #print(maxv,maxa)
    return maxa

def minValue(state,aa):
    #print('minValue called')
    if terminalTest(copy.deepcopy(state),1): return 1
    if not aa: return 0
    minv = 10
    # mina = None
    for action in aa:
        s = copy.deepcopy(state)
        tempaa = copy.deepcopy(aa)
        tempaa.remove(action)
        v = maxValue(result(s,action,0),tempaa)
        if v<minv:
            minv = v
            # mina = action
    return minv
        
def maxValue(state,aa):
    #print('maxValue called')
    if terminalTest(copy.deepcopy(state),0): 
        return -1
    if not aa: return 0
    maxv = -10
    # maxa = None
    for action in aa:
        s = copy.deepcopy(state)
        tempaa = copy.deepcopy(aa)
        tempaa.remove(action)
        v = minValue(result(s,action,1),tempaa)
        if v>maxv:
            maxv = v
            # maxa = action
    return maxv
    
def digit_clicked(num):
    btn = button_list[num-1]
    global current_player,count
    if btn['text']=='':
        availableActions.remove(str(num))
        btn['bg'] = 'black'
        btn['fg'] = 'white'
        btn['activebackground'] = 'black'
        btn['activeforeground'] = 'white'
        count += 1
        if current_player == 1:
            btn['text'] = 'X'
            root.update()
            if check_if_won():
                return
            elif count == 9:
                game_over()
                return
            current_player = 2
            if player_2_value == 'C':
                board_state = get_board_state()
                move = get_computer_move(board_state)
                play_computer_move(move,'O')
                availableActions.remove(move)
                count += 1
                if check_if_won():
                    return
                elif count == 9:
                    game_over()
                    return
                current_player = 1
        else:
            btn['text'] = 'O'
            root.update()
            if check_if_won():
                return
            elif count == 9:
                game_over()
                return
            current_player = 1
            if player_1_value == 'C':
                board_state = get_board_state()
                move = get_computer_move(board_state)
                play_computer_move(move,'X')
                availableActions.remove(move)
                count += 1
                if check_if_won():
                    return
                elif count == 9:
                    game_over()
                    return
                current_player = 2
    else:
        messagebox.showerror('Tic Tac Toe','Ooooops! The box you clicked has already been selected.')

# Play button    
play_button = Button(root,text='PLAY',command=start_the_game,bg='#f7b019',activebackground='#f7b019')
play_button.grid(row=2,column=0,columnspan=3,padx=10,pady=10)

# Reset button
reset_button = Button(root,text='RESET',command=reset_the_game,bg='#f7b019',activebackground='#f7b019')
reset_button.grid(row=6,column=0,columnspan=3,padx=10,pady=10)
    
# Digit buttons
b1 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(1))
b2 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(2))
b3 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(3))

b4 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(4))
b5 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(5))
b6 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(6))

b7 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(7))
b8 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(8))
b9 = Button(root,text="",font=('Helvetica',20),height=3,width=6,bg='SystemButtonFace',command=lambda:digit_clicked(9))

button_list = [b1,b2,b3,b4,b5,b6,b7,b8,b9]

b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=4,column=0)
b5.grid(row=4,column=1)
b6.grid(row=4,column=2)

b7.grid(row=5,column=0)
b8.grid(row=5,column=1)
b9.grid(row=5,column=2)

disable_digit_buttons()

root.mainloop()

