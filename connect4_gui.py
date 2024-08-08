import p4_v2 as c4

def starter_out():
    display(c4.grider(6,7))

def display(grid):

    import tkinter as tk 

    dim=(len(grid),len(grid[0]))
    global cur_side;cur_side=1

    def side_toggle():
        global cur_side
        if cur_side==1:
            cur_side=2
        else: cur_side=1


    def blank_disp():
        for i in range(dim[0]):               #creating a graphic column for each connect_4 grid column 
            board_f.columnconfigure(i,weight=1)
        for row in range(dim[1]):               #improvement : packing this in a function -> clearer code 
            for col in range(dim[0]):
                token_placer('white',col,row,setup=True)

    def token_placer(color,x,y,setup=False):
        token=tk.Canvas(master=board_f,height=100,width=100,border=0)
        token.create_oval(2,2,99,99,fill=color)
        token.grid(column=x,row=y,sticky='NSEW',pady=10,padx=5)
        if setup==True:         #first occurence > creating a blank grid + binding every blank places to 'token add"
            token.bind('<Button-1>',lambda event: play(event,x) ) 
    
    def play(event,column):
        side_dic={1:'yellow',2:'red'}
        c4.adder(cur_side,column)
        x,y=c4.coord(column)
        token_placer(side_dic[cur_side],x,len(grid[0])-1-y)
        if c4.win_cond((x,y),cur_side):
            win_msg=tk.Label(master=main_frame,text=f'player {cur_side} wins !',font=('Arial',60),fg='red')
            win_msg.grid(column=1,row=0,sticky='NSEW',padx=(0,20))
            for w in board_f.winfo_children():
                w.unbind('<Button-1>')
        else:
            side_toggle()
            player_label=tk.Label(master=main_frame,text=f'player {cur_side}\'s turn',font=('Modern No. 20',50))
            player_label.grid(column=1,row=0,sticky='N',padx=(0,30))
            
    def killer():
        instance.destroy()

    def restarter(event):
        instance.destroy()
        starter_out()

########################################### Tkinter area ###########################################

    instance=tk.Tk()
    instance.attributes('-fullscreen',True)

    title_f=tk.Frame(bg='blue')

    title_f.columnconfigure(0,weight=39);title_f.columnconfigure(1,weight=1)

    title=tk.Label(master=title_f,text='Connect 4',fg='yellow',bg='blue',font=('Comic Sans MS',30))
    title.grid(column=0,row=0,sticky='NSEW',rowspan=2)

    exit_b=tk.Button(master=title_f,text='exit',bg='red',fg='white',font=('Arial',10),command=killer)
    exit_b.grid(column=1,row=0,sticky='NSEW')

    restart_b=tk.Button(master=title_f,text='restart',bg='white',font=('Arial',10))
    restart_b.bind('<Button-1>',restarter)
    restart_b.grid(column=1,row=1,sticky='NSEW')

    title_f.pack(side='top',fill='x',pady=(0,20))

    main_frame=tk.Frame(master=instance)
    main_frame.columnconfigure(0,weight=5);main_frame.columnconfigure(1,weight=1)

    board_f=tk.Frame(master=main_frame)

    blank_disp()                #creating the blank grid + binding every blank space 

    board_f.grid(column=0,sticky='NW',padx=(30,0))

    player_label=tk.Label(master=main_frame,text=f'player {cur_side}\'s turn',font=('Modern No. 20',50))
    player_label.grid(column=1,row=0,sticky='N',padx=(0,30))

    main_frame.pack(fill='both')

    tk.mainloop()













############################################ __name__==__main__ ############################################
if __name__=='__main__':
    starter_out()


