# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:23:44 2018

@author: salma
""" 
import heapq
import math
import tkinter
import time
class Node:
    def __init__( self, board, parent, operator, depth, manhattan_cost,euclidean_cost):
        self.board= board
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.manhattan_cost = self.depth+self.Manhattan([1,2,3,4,5,6,7,8,0])
        self.euclidean_cost= self.depth+self.Euclidean([1,2,3,4,5,6,7,8,0])
    def checkPath(self,nodeBoard):
        temp=self
        while True:
            if temp.board==nodeBoard:
                return False
            if temp.parent == None:
                break
            temp = temp.parent
        return True
    def Manhattan(self,goal):
        distance=0
        for num in range(0,9):
            index1=self.board.index(num)
            index2=goal.index(num)
            x1=getx(index1)
            y1=gety(index1)
            x2=getx(index2)
            y2=gety(index2)
            distance+=abs(x1-x2)+abs(y1-y2)
        return distance
    def Euclidean(self,goal):
        distance=0
        for num in range(0,9):
            index1=self.board.index(num)
            index2=goal.index(num)
            x1=getx(index1)
            y1=gety(index1)
            x2=getx(index2)
            y2=gety(index2)
            distance+=math.sqrt((x1-x2)**2+(y1-y2)**2)
        return distance
    def __lt__(self, other):
         return self.manhattan_cost < other.manhattan_cost
   
def getx(index):
    if index in [0,1,2]:
        return 0
    elif index in [3,4,5]:
        return 1
    else:
        return 2
def gety(index):
    if index in [0,3,6]:
        return 0
    elif index in [1,4,7]:
        return 1
    else:
        return 2

def displayBoard( state ):
    print ("-------------")
    print ("| %d | %d | %d |" % (state[0], state[1], state[2])) 
    print ("-------------")
    print ("| %d | %d | %d |" % (state[3], state[4], state[5])) 
    print ("-------------")
    print ("| %d | %d | %d |" % (state[6], state[7], state[8])) 
    print ("-------------")       
        
"moveeeeeee"
def moveLeft( board ):
    indexZero = board.index( 0 )
    if indexZero not in [0, 3, 6]:
        newBoard = board[:]
        temp = newBoard[indexZero - 1]
        newBoard[indexZero - 1] = newBoard[indexZero]
        newBoard[indexZero] = temp
        return newBoard
    else:
        return None
    
def moveRight( board ):
    indexZero = board.index( 0 )
    if indexZero not in [2, 5, 8]:
        newBoard = board[:]
        temp = newBoard[indexZero + 1]
        newBoard[indexZero + 1] = newBoard[indexZero]
        newBoard[indexZero] = temp
        return newBoard
    else:
        return None    
     
def moveUp( board ):
    indexZero = board.index( 0 )
    if indexZero not in [0, 1, 2]:
        newBoard = board[:]
        temp = newBoard[indexZero - 3]
        newBoard[indexZero - 3] = newBoard[indexZero]
        newBoard[indexZero] = temp
        return newBoard
    else:
        return None     
    
def moveDown( board ):
    indexZero = board.index( 0 )
    if indexZero not in [6, 7, 8]:
        newBoard = board[:]
        temp = newBoard[indexZero + 3]
        newBoard[indexZero + 3] = newBoard[indexZero]
        newBoard[indexZero] = temp
        return newBoard
    else:
        return None   
    
"buildddddddd"

def createNode( board, parent, operator, depth, manhattan_cost,euclidean_cost):
	return Node( board, parent, operator, depth, manhattan_cost,euclidean_cost )

def expandNode( node ):
    children = []
    
           
    if moveDown(node.board) != None:
            newNode=createNode( moveDown( node.board ), node, "d", node.depth + 1, 0,0 )
            if node.checkPath(newNode.board):
                children.append(newNode)
    if moveUp(node.board) != None:
        newNode=createNode( moveUp( node.board ), node, "u", node.depth + 1, 0 ,0)
        if node.checkPath(newNode.board):
            children.append(newNode)
         
    if moveLeft(node.board) != None:
            newNode=createNode( moveLeft( node.board ), node, "l", node.depth + 1, 0 ,0)
            if node.checkPath(newNode.board):
                 children.append(newNode)
              
    if moveRight(node.board) != None:
            newNode=createNode( moveRight( node.board), node, "r", node.depth + 1, 0 ,0)
            if node.checkPath(newNode.board):
                children.append(newNode)
    return children
             

"bfsssssssssss"
def BFS(start,goal):
    frontier =[]
    frontier.append( createNode( start, None, None, 0, 0 ,0) )
    while True:
        if len( frontier ) == 0:
            return None
        node = frontier.pop(0)
        if node.board == goal:
            moves = []
            moves.insert(0, node)
            temp = node         
            while True:
                 if temp.parent == None: 
                     break
                 moves.insert(0, temp.parent)
                 temp = temp.parent
            return moves
        children= expandNode(node) 
        frontier.extend(children)
"dfssssssssssss"
def DFS(start,goal):
    frontier =[]
    frontier.append( createNode( start, None, None, 0, 0 ,0) )
    while True:
        if len( frontier ) == 0:
            return None
        node = frontier.pop()
        if node.board == goal:          
            moves = []
            moves.insert(0, node)
            temp = node           
            while True:
                 if temp.parent == None: 
                     break
                 moves.insert(0, temp.parent)
                 temp = temp.parent
            return moves
        children= expandNode(node) 
        frontier.extend(children) 

def A_star(start,goal):
    frontier=[]
    start=createNode(start, None, None, 0, 0 ,0)
    heapq.heappush(frontier,start)
    
    while True:
        
        if len( frontier ) == 0:
            return None
        node=heapq.heappop(frontier)
        if node.board == goal:          
            moves = []
            moves.insert(0, node)
            temp = node           
            while True:
                 if temp.parent == None: 
                     break
                 moves.insert(0, temp.parent)
                 temp = temp.parent
            return moves
        children= expandNode(node)
        for num in range(0,len(children)):
            heapq.heappush(frontier,children[num])
          
     
    
       

def main():
    startState=[1,4,2,6,5,8,7,3,0]
    goal = [1,2,3,4,5,6,7,8,0]
    tiles=[]
    i=0
    root=tkinter.Tk()
    root.state('zoomed')
    root.title('8-Puzzle')
    root.geometry("50x200")
    root.maxsize(50,200)
    root.resizable(1,1)
    f=tkinter.Frame(master=root,bg='pink')
    f.pack(fill=tkinter.BOTH,expand=1)
    for num in range(0,9):
       tiles.append(tkinter.Label(master=f,text=goal[num],borderwidth=2,relief="groove",font='times 40'))
    for rows in range(3):
        for col in range(3):
            tiles[i].grid(row=rows,column=col,sticky="nsew")
            i=i+1
    moves = A_star(startState,goal)
    for i in range(0,len(moves)):
        for num in range(0,9):
            tiles[num]['text']=moves[i].board[num]
    
    print("Moves are")
    for num in range(0,len(moves)):
         displayBoard(moves[num].board)
    root.mainloop() 
   
if __name__ == "__main__":
	main()    