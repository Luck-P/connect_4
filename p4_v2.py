#new attempt to obtain a clean, working tic tac toe game

'''
####################################### log #######################################
- first commit 22/07-18:31 : seems to work ; however rigid input required



###################################################################################
'''

#gameboard : input = grid dimensions // each list a column  
grid_w,grid_h=input('width x height : ').split("x");grid_w,grid_h=int(grid_w),int(grid_h)
global grid ; grid=[[0 for i in range(grid_h)] for i in range(grid_w)]

def coord(last_col):
    x=last_col
    if 0 in grid[last_col]:
        y=grid[last_col].index(0)-1
    else:y=len(grid[last_col])-1
    return x,y

def win_cond(ipos,side):        #ipos : tuple (x,y) #most important step 
    x,y=ipos
    tgl=(1,-1)
    #checking the column
    vt_count=1
    hz_count=1
    tl_br=1
    bl_tr=1
    i=1 
    while 'checking the column':
        if y-i>=0 and grid[x][y-i]==side:
            vt_count+=1
            i+=1
        else:break

    #checking the line : toggle -> check right then left 

    for direction in tgl:
        i=1
        while 'checking the line':
            if 0<=x+(direction*i)<len(grid) and grid[x+(direction*i)][y]==side:
                hz_count+=1;i+=1
            else:break

    #checking the first diag : top-left to bot-right 

    for direction in tgl:
        i=1
        while 'checking the \ diagonal ':
            if 0<=x+(direction*i)<len(grid) and 0<=y-(direction*i)<len(grid[x]) and grid[x+(direction*i)][y-(direction*i)]==side:  #x+i ; y-i then x-i ; y+i -> checking the \ diagonal  
                tl_br+=1;i+=1
            else:break
    
    #checking the second diag : bot-left to top-right 

    for direction in tgl:
        i=1
        while "checking the / diagonal ":
            if 0<=x+(direction*i)<len(grid) and 0<=y+(direction*i)<len(grid[x]) and grid[x+(direction*i)][y+(direction*i)]==side:
                bl_tr+=1;i+=1
            else:break

    for w in (vt_count,hz_count,tl_br,bl_tr):
        if w>=4:
            return True
    return False
    
def adder(side,col):
    if 0<=col<=grid_w-1 and 0 in grid[col] :
        grid[col][grid[col].index(0)]=side
        if win_cond(coord(col),side):
            return True
        else:return False
    else:
        print(f'column {col+1} is full/inexistant, pick another')
        return adder(side,int(input(f'player {side} - column : '))-1)

def quick_disp(grid):
    for i in range(1,len(grid[0])+1):
        ltp=[]
        for j in range(grid_w):
            ltp.append(str(grid[j][-i]))
        print('  '.join(ltp))
    







#################################################### DEBUG ####################################################
quick_disp(grid)
players=(1,2)
end=False
while end==False:
    for side in players:
        end= adder(side,int(input(f'player {side} to play - column : '))-1)
        quick_disp(grid)
        if end==True:
            print(f'player {side} win')
            break
    
    
