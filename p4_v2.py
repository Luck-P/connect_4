#new attempt to obtain a clean, working tic tac toe game

'''
####################################### log #######################################
- 1rst commit 22/07-18:31 : seems to work ; however rigid input required
- 2nd commit missed :/ : flexible input 
- 3rd commit 24/07-~4:00pm : loop optimization (seems like) -> single big 'while' loop instead of 4 smalls
- 4th commit 06/08 7:15pm : added 'if main == main' -> now importable (almost)
- 5th commit 07/08 12:46pm : dimension inputs in 'if m==m' -> now imported in gui
###################################################################################
'''

#gameboard : input = grid dimensions // each list a column  

def grider(grid_h,grid_w):
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
    
    for direction in tgl:
        i=1
        th_vt=th_hz=th_tlbr=th_bltr=True
        while th_vt==True or th_hz==True or th_tlbr==True or th_bltr==True:

            if th_vt==True and 0<=y+(direction*i)<len(grid[x]) and grid[x][y+(direction*i)]==side: #checking column (upward useless but opti 'while' loop )
                vt_count+=1
            else:           #issue : adding 1 pt for nothing ? 
                th_vt=False

            if th_hz==True and 0<=x+(direction*i)<len(grid) and grid[x+(direction*i)][y]==side: #checking sides
                hz_count+=1
            else:
                th_hz=False

            if th_tlbr==True and 0<=x+(direction*i)<len(grid) and 0<=y-(direction*i)<len(grid[x]) and grid[x+(direction*i)][y-(direction*i)]==side:  #x+i ; y-i then x-i ; y+i -> checking the \ diagonal  
                tl_br+=1
            else:
                th_tlbr=False
        
            if th_bltr==True and 0<=x+(direction*i)<len(grid) and 0<=y+(direction*i)<len(grid[x]) and grid[x+(direction*i)][y+(direction*i)]==side:  #x+i ; y+i then x-i ; y-i -> checking the / diagonal  
                bl_tr+=1
            else:
                th_bltr=False
            i+=1

    for w in (vt_count,hz_count,tl_br,bl_tr):
        if w>=4:
            return True
    return False
    
def adder(side,col):
    try :
        col=int(col)-1
    except:
        print(f'input : {col} > column input has to be an integer')
        return adder(side,input(f'player {side} - column : '))
    else:
        if 0<=col<=grid_w-1 and 0 in grid[col] :
            grid[col][grid[col].index(0)]=side
            if win_cond(coord(col),side):
                return True
            else:return False
        else:
            print(f'column {col+1} is full/inexistant, pick another')
            return adder(side,input(f'player {side} - column : '))

def quick_disp(grid):
    for i in range(1,len(grid[0])+1):
        ltp=[]
        for j in range(grid_w):
            ltp.append(str(grid[j][-i]))
        print('  '.join(ltp))
    







#################################################### DEBUG ####################################################
if __name__=='__main__':
    grid_w,grid_h=input('width x height : ').split("x");grid_w,grid_h=int(grid_w),int(grid_h)
    grider(grid_h,grid_w)
    quick_disp(grid)
    players=(1,2)
    end=False
    while end==False:
        for side in players:
            end= adder(side,input(f'player {side} to play - column : '))
            quick_disp(grid)
            if end==True:
                print(f'player {side} win')
                break
    
    
