# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:23:44 2018

@author: salma
""" 
import heapq
import math
import timeit
#A class for nodes in search tree
class Node:
#constructor
    def __init__( self, board, parent, operator, depth):
        self.board= board
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.manhattan_cost = self.depth+self.Manhattan([0,1,2,3,4,5,6,7,8])
        self.euclidean_cost= self.depth+self.Euclidean([0,1,2,3,4,5,6,7,8])
#A function to check if a given node(board) is a duplicate in this node's path 
    def checkPath(self,nodeBoard):
        temp=self
        while True:
            if temp.board==nodeBoard:
                return False
            if temp.parent == None:
                break
            temp = temp.parent
        return True
#A function to calculate Manhattan distance from goal
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
#A function to calculate Euclidean distance from goal
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
#Less than function to compare nodes according to their costs(used by heap in A* search)
#    def __lt__(self, other):
#         return self.manhattan_cost < other.manhattan_cost
    def __lt__(self, other):
         return self.euclidean_cost < other.euclidean_cost
#Takes index of element in board reprsented by 1-D array and returns its X co-ordinate in 2-D board         
def getx(index):
    if index in [0,1,2]:
        return 0
    elif index in [3,4,5]:
        return 1
    else:
        return 2
#Takes index of element in board reprsented by 1-D array and returns its Y co-ordinate in 2-D board 
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
       
#Move functions in four directions
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
    


def createNode( board, parent, operator, depth):
	return Node( board, parent, operator, depth)

def expandNode( node ):
    children = []
    if moveRight(node.board) != None:
            newNode=createNode( moveRight( node.board), node, "r", node.depth + 1)
            if node.checkPath(newNode.board):
                children.append(newNode)
    if moveDown(node.board) != None:
            newNode=createNode( moveDown( node.board ), node, "d", node.depth + 1  )
            if node.checkPath(newNode.board):
                children.append(newNode)
    if moveLeft(node.board) != None:
            newNode=createNode( moveLeft( node.board ), node, "l", node.depth + 1)
            if node.checkPath(newNode.board):
                 children.append(newNode)  
    if moveUp(node.board) != None:
        newNode=createNode( moveUp( node.board ), node, "u", node.depth + 1)
        if node.checkPath(newNode.board):
            children.append(newNode)
    return children
             
nodes_Expanded=0
#BFS search
def BFS(start,goal):
    print("Visited Nodes:")
    global nodes_Expanded
    frontier =[]
    frontier.append( createNode( start, None, None, 0))
    while True:
        if len( frontier ) == 0:
            return None
        node = frontier.pop(0)
        displayBoard(node.board)
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
        nodes_Expanded=nodes_Expanded+len(children)
        frontier.extend(children)
#DFS search
def DFS(start,goal):
    print("Visited Nodes:")
    global nodes_Expanded
    frontier =[]
    frontier.append( createNode( start, None, None, 0) )
    while True:
        if len( frontier ) == 0:
            return None
        node = frontier.pop()
        displayBoard(node.board)
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
        nodes_Expanded=nodes_Expanded+len(children)
        frontier.extend(children) 
#A* search
def A_star(start,goal):
    print("Visited Nodes:")
    global nodes_Expanded
    frontier=[]
    start=createNode(start, None, None, 0)
    heapq.heappush(frontier,start)
    
    while True:
        
        if len( frontier ) == 0:
            return None
        node=heapq.heappop(frontier)
        displayBoard(node.board)
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
        nodes_Expanded=nodes_Expanded+len(children)
        for num in range(0,len(children)):
            heapq.heappush(frontier,children[num])
 
def main(): 
    start=stop=0
#    startState=[]
#    print('Enter start state element by element:')
#    for i in range(9):
#        x = int(input('-->'))
#        startState.append(x)
#    print (startState) 
    startState=[1,2,3,4,0,5,6,7,8]
    goal = [0,1,2,3,4,5,6,7,8]
    method=int(input("Choose method:1-bfs 2-dfs 3-a-star :"))
    if method==1:
        start = timeit.default_timer()
        moves = BFS(startState,goal)
        stop = timeit.default_timer()
    if method==2:  
        start = timeit.default_timer()
        moves = DFS(startState,goal)
        stop = timeit.default_timer()
    if method==3:
        start = timeit.default_timer()
        moves = A_star(startState,goal)
        stop = timeit.default_timer()
    print("Moves are:")
    for num in range(0,len(moves)):
         displayBoard(moves[num].board)
    print("Cost of path is: %d" %moves[len(moves)-1].depth) 
    print("Depth of path is: %d" %moves[len(moves)-1].depth)
    print("Number of nodes expanded is: %d "%(nodes_Expanded+1))
    print ("Running time is: %d s" %(stop - start ))
if __name__ == "__main__":
	main()    