# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 15:23:44 2018

@author: salma
""" 
class Node:
    def __init__( self, board, parent, operator, depth, cost ):
        self.board= board
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost
    def checkPath(self,nodeBoard):
        temp=self
        while True:
            if temp.board==nodeBoard:
                return False
            if temp.parent == None:
                break
            temp = temp.parent
        return True


             

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

def createNode( board, parent, operator, depth, cost ):
	return Node( board, parent, operator, depth, cost )

def expandNode( node ):
    children = []
    if moveUp(node.board) != None:
        newNode=createNode( moveUp( node.board ), node, "u", node.depth + 1, 0 )
        if node.checkPath(newNode.board):
            children.append(newNode)
           
    if moveDown(node.board) != None:
            newNode=createNode( moveDown( node.board ), node, "d", node.depth + 1, 0 )
            if node.checkPath(newNode.board):
                children.append(newNode)
             
    if moveLeft(node.board) != None:
            newNode=createNode( moveLeft( node.board ), node, "l", node.depth + 1, 0 )
            if node.checkPath(newNode.board):
                 children.append(newNode)
              
    if moveRight(node.board) != None:
            newNode=createNode( moveRight( node.board), node, "r", node.depth + 1, 0 )
            if node.checkPath(newNode.board):
                children.append(newNode)
    return children
             

"bfsssssssssss"
def BFS(start,goal):
    frontier =[]
    frontier.append( createNode( start, None, None, 0, 0 ) )
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
def DFS(start,goal):
    frontier =[]
    frontier.append( createNode( start, None, None, 0, 0 ) )
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

def main():
    startState=[1,2,5,3,4,0,6,7,8]
    goal = [0,1,2,3,4,5,6,7,8]
#    root = createNode( startState , None , None , 0, 0 )
#    children1 = expandNode(root)
#    print ("1")
#    for num in range(0,len(children1)): 
#     print (children1[num].board)
#    children2 = expandNode(children1[0])
#    print ("2")
#    
#    
#    for num in range(0,len(children2)):
#       
#     print (children2[num].board)
#    children3 = expandNode(children1[1])
#    print ("3") 
#    for num in range(0,len(children3)): 
#     print (children3[num].board)
    moves = BFS(startState,goal)
    print("moves are")
    for num in range(0,len(moves)):
         displayBoard(moves[num].board)
if __name__ == "__main__":
	main()    