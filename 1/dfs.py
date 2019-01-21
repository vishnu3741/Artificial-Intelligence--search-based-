def goalTest(a,b):
    if(a[0:9]==b[0:9]):
        return True
    return False
def swap(i,j,L):
    L[i],L[j]=L[j],L[i]
    b=L[:]
    L[i],L[j]=L[j],L[i]
    return b
def moveGen(a):
    moves=[]
    if(a[0]==0):
        move=swap(0,1,a)
        move[9]=move[9]+" move 0,0 to 0,1\n"
        moves.append(move)
        move=swap(0,3,a)
        move[9]=move[9]+" move 0,0 to 1,0\n"
        moves.append(move)
        return moves
    elif(a[1]==0):
        move=swap(1,0,a)
        move[9]=move[9]+" move 0,1 to 0,0\n"
        moves.append(move)
        move=swap(1,2,a)
        move[9]=move[9]+" move 0,1 to 0,2\n"
        moves.append(move)
        move=swap(1,4,a)
        move[9]=move[9]+" move 0,1 to 1,1\n"
        moves.append(move)
        return moves
    elif(a[2]==0):
        move=swap(2,1,a)
        move[9]=move[9]+" move 0,2 to 0,1\n"
        moves.append(move)
        move=swap(2,5,a)
        move[9]=move[9]+" move 0,2 to 1,2\n"
        moves.append(move)
        return moves
    elif(a[3]==0):
        move=swap(3,0,a)
        move[9]=move[9]+" move 1,0 to 0,0\n"
        moves.append(move)
        move=swap(3,4,a)
        move[9]=move[9]+" move 1,0 to 1,1\n"
        moves.append(move)
        move=swap(3,6,a)
        move[9]=move[9]+" move 1,0 to 2,0\n"
        moves.append(move)
        return moves
    elif(a[4]==0):
        move=swap(4,1,a)
        move[9]=move[9]+" move 1,1 to 0,1\n"
        moves.append(move)
        move=swap(4,3,a)
        move[9]=move[9]+" move 1,1 to 1,0\n"
        moves.append(move)
        move=swap(4,5,a)
        move[9]=move[9]+" move 1,1 to 1,2\n"
        moves.append(move)
        move=swap(4,7,a)
        move[9]=move[9]+" move 1,1 to 2,1\n"
        moves.append(move)
        return moves
    elif(a[5]==0):
        move=swap(5,2,a)
        move[9]=move[9]+" move 1,2 to 0,2\n"
        moves.append(move)
        move=swap(5,4,a)
        move[9]=move[9]+" move 1,2 to 1,1\n"
        moves.append(move)
        move=swap(5,8,a)
        move[9]=move[9]+" move 1,2 to 2,2\n"
        moves.append(move)
        return moves
    elif(a[6]==0):
        move=swap(6,3,a)
        move[9]=move[9]+" move 2,0 to 1,0\n"
        moves.append(move)
        move=swap(6,7,a)
        move[9]=move[9]+" move 2,0 to 2,1\n"
        moves.append(move)
        return moves
    elif(a[7]==0):
        move=swap(7,4,a)
        move[9]=move[9]+" move 2,1 to 1,1\n"
        moves.append(move)
        move=swap(7,6,a)
        move[9]=move[9]+" move 2,1 to 2,0\n"
        moves.append(move)
        move=swap(7,8,a)
        move[9]=move[9]+" move 2,1 to 2,2\n"
        moves.append(move)
        return moves
    elif(a[8]==0):
        move=swap(8,5,a)
        move[9]=move[9]+" move 2,2 to 1,2\n"
        moves.append(move)
        move=swap(8,7,a)
        move[9]=move[9]+" move 2,2 to 2,1\n"
        moves.append(move)
        return moves
print("input the state of the board left to right, top to bottom using 0 for space\nFor example: 1 2 3 4 0 5 6 7 8")
a=map(int,raw_input().split())
if(goalTest(a,[1,2,3,4,5,6,7,8,0])):
    print("initial state is the goal state")
else:
    a.append("The moves are :\n")
    open=moveGen(a)
    closed=[a[0:9]]
    found=0
    c = -1
    d = 0
    while(len(open)>0):
        state1=open[len(open)-1][:]
        open=open[:len(open)-1]
        closed.append(state1[0:9])
        if(goalTest(state1,[1,2,3,4,5,6,7,8,0])):
            found=1        
            print(state1[9])
            break
        moves=moveGen(state1)
	d = d+1
        while(len(moves)>0):
            state2=moves.pop(0)
            bit=0
            if((state2[0:9] not in closed)  and (state2[0:9] not in open))  :
                open.append(state2)
    if(found==0):
        print("Solution not Possible")
for i in range(0,len(state1[9])):
	if state1[9][i]=='\n':
		c=c+1
print("Length of path : " + str(c))
print("Number of states visited during the search :" + str(len(closed)))
