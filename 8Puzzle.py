# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:23:44 2018

@author: salma
""" 
import heapq
import math
class Node:
    def __init__( self, board, parent, operator, depth):
        self.board= board
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.manhattan_cost = self.depth+self.Manhattan([0,1,2,3,4,5,6,7,8])
        self.euclidean_cost= self.depth+self.Euclidean([0,1,2,3,4,5,6,7,8])
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
#    def __lt__(self, other):
#         return self.manhattan_cost < other.manhattan_cost
    def __lt__(self, other):
         return self.euclidean_cost < other.euclidean_cost
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

def createNode( board, parent, operator, depth):
	return Node( board, parent, operator, depth)

def expandNode( node ):
    children = []
    
           
    if moveDown(node.board) != None:
            newNode=createNode( moveDown( node.board ), node, "d", node.depth + 1  )
            if node.checkPath(newNode.board):
                children.append(newNode)
    if moveUp(node.board) != None:
        newNode=createNode( moveUp( node.board ), node, "u", node.depth + 1)
        if node.checkPath(newNode.board):
            children.append(newNode)
         
    if moveLeft(node.board) != None:
            newNode=createNode( moveLeft( node.board ), node, "l", node.depth + 1)
            if node.checkPath(newNode.board):
                 children.append(newNode)
              
    if moveRight(node.board) != None:
            newNode=createNode( moveRight( node.board), node, "r", node.depth + 1)
            if node.checkPath(newNode.board):
                children.append(newNode)
    return children
             

"bfsssssssssss"
def BFS(start,goal):
    frontier =[]
    frontier.append( createNode( start, None, None, 0) )
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
    frontier.append( createNode( start, None, None, 0) )
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
    start=createNode(start, None, None, 0)
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
     
    startState=[]
    print('Enter start state element by element:')
    for i in range(9):
        x = int(input('-->'))
        startState.append(x)
    print (startState)  
    goal = [0,1,2,3,4,5,6,7,8]
#    tiles=[]
#    i=0
#    root=tkinter.Tk()
#    for num in range(0,9):
#       tiles.append(tkinter.Label(root,text=goal[num]))
#    for row in range(3):
#        for col in range(3):
#            tiles[i].grid(row=row,column=col)
#            i=i+1
#    root.mainloop() 
    method=int(input("Choose method:1-bfs 2-dfs 3-a-star :"))
    if method==1:
        moves = BFS(startState,goal)
    if method==2:    
        moves = DFS(startState,goal)
    if method==3:
        moves = A_star(startState,goal)
    print("Moves are")
    for num in range(0,len(moves)):
         displayBoard(moves[num].board)
         
if __name__ == "__main__":
	main()    