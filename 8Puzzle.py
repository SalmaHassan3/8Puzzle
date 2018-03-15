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
		
		
		
		

def displayBoard( state ):
    
    print ("-------------")
    print ("| %i | %i | %i |") % (state[0], state[1], state[2])
    print ("-------------")
    print ("| %i | %i | %i |") % (state[3], state[4], state[5])
    print ("-------------")
    print ("| %i | %i | %i |") % (state[6], state[7], state[8])
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
            children.append( createNode( moveUp( node.board ), node, "u", node.depth + 1, 0 ) )
    if moveDown(node.board) != None:
            children.append( createNode( moveDown( node.board ), node, "d", node.depth + 1, 0 ) )
    if moveLeft(node.board) != None:
            children.append( createNode( moveLeft( node.board ), node, "l", node.depth + 1, 0 ) )
    if moveRight(node.board) != None:
            children.append( createNode( moveRight( node.board), node, "r", node.depth + 1, 0 ) )
    return children

"bfsssssssssss"
def BFS(start,goal):
    frontier =[]
    
    frontier.append( createNode( start, None, None, 0, 0 ) )
    while True:
#        print "salma"
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
        print ("new nela")
        children= expandNode(node) 
        print ("parent")
        displayBoard(node.board)
        print ("children")
        for num in range(0,len(children)):
           
           displayBoard(children[num].board)
         
        frontier.extend(children)
    

def main():
    startState=[1,2,3,6,0,7,8,5,4]
    goal = [0,1,2,3,4,5,6,7,8]
    root = createNode( startState , None , None , 0, 0 )
    children1 = expandNode(root)
    print ("1")
    for num in range(0,len(children1)): 
     print (children1[num].board)
    children2 = expandNode(children1[0])
    print ("2")
    
    
    for num in range(0,len(children2)):
       
     print (children2[num].board)
    children3 = expandNode(children1[1])
    print ("3") 
    for num in range(0,len(children3)): 
     print (children3[num].board)
  #  moves = BFS(startState,goal)
#    
#    for num in range(0,len(moves)):
#         
#         displayBoard(moves[num].board)
         
     
    
       
if __name__ == "__main__":
	main()    