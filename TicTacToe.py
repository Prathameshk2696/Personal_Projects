# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:26:15 2020

@author: Prthamesh
"""
import copy

availableActions = ['1','2','3','4','5','6','7','8','9']

d = {
            '1':(0,0),'2':(0,1),'3':(0,2),
            '4':(1,0),'5':(1,1),'6':(1,2),
            '7':(2,0),'8':(2,1),'9':(2,2)
    }

def displayState(state):
    s = copy.deepcopy(state)
    '''print()
    for row in state:
        print('\t',row[0],row[1],row[2])'''
    for i in range(3):
        for j in range(3):
            if state[i][j]!='X' and state[i][j]!='O':
                s[i][j]=' '
        
    for i in range(7):
        if i%2==0:
            print('\t','-'*19,sep='')
        else:
            row = s[i//2]
            print('\t|  {}  |  {}  |  {}  |'.format(row[0],row[1],row[2]))

def terminalTest(m,player):
    if player == 1:
        l = ['X','X','X']
    else:
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
    
def startTicTacToe():
    nom = 0
    m = [['1','2','3'],
         ['4','5','6'],
         ['7','8','9']]
    print('Who is going to play first?')
    print('Press 1 for Computer')
    print('Press 0 for Human')
    player = int(input('Your input : '))
    gameEnd = False
    print('Initial Setup : ')
    displayState(m)
    while (not gameEnd) and nom<9:
        print('-'*40)
        #print('available actions',availableActions)
        px,py = None,None
        if player == 1:
            position = minimaxDecision(copy.deepcopy(m))
            print('Computer played',position)
            px,py = d[position]
            del(d[position])
        else:
            while True:
                print('                               1 2 3')
                print('Number schema for reference :  4 5 6')
                print('                               7 8 9')
                position = input('Enter position number : ')
                if position in d:
                    print('You played',position)
                else:
                    print(position,'is not available')
                px,py = d.get(position,(None,None))
                if px!=None and py!=None:
                    del(d[position])
                    break
        if player == 1:
            m[px][py] = 'X'
        else:
            m[px][py] = 'O'
        availableActions.remove(position)
        gameEnd = terminalTest(m,player)
        #print(gameEnd)
        #for row in m:
         #   print(row)
        displayState(m)
        if not gameEnd:
            player = 1 - player
        else:
            print('GAME HAS ENDED')
        nom += 1
        
    if nom == 9:
        print("It's a draw")
    else:
        if player == 1:
            print('COMPUTER WON !!!')
        else:
            print('HUMAN WON !!!')

def result(s,action,player):
    #s = copy.deepcopy(state)
    px,py = d[action]
    if player == 1:
        s[px][py] = 'X'
    else:
        s[px][py] = 'O'
    return s

def minimaxDecision(state):
    print('Computer thinking ...')
    aa = availableActions[:]
    #print('available actions:',aa)
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

startTicTacToe()