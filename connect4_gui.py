

def display(grid,dim):
    import tkinter as tk
    import p4_v2 as c4

    def token_placer(color,x,y):
        token=tk.Canvas(master=board_f,height=100,width=100,border=0)
        token.create_oval(2,2,99,99,fill=color)
        token.grid(column=x,row=y,sticky='NSEW',pady=10,padx=5)

    def killer():
        instance.destroy()

    instance=tk.Tk()
    instance.attributes('-fullscreen',True)

    title_f=tk.Frame(bg='blue')

    title_f.columnconfigure(0,weight=39);title_f.columnconfigure(1,weight=1)

    title=tk.Label(master=title_f,text='Connect 4',fg='yellow',bg='blue',font=('Comic Sans MS',30))
    title.grid(column=0,row=0,sticky='NSEW',rowspan=2)

    exit_b=tk.Button(master=title_f,text='exit',bg='red',fg='white',font=('Arial',10),command=killer)
    exit_b.grid(column=1,row=0,sticky='NSEW')

    menu_b=tk.Button(master=title_f,text='menu',bg='white',font=('Arial',10))
    menu_b.grid(column=1,row=1,sticky='NSEW')

    title_f.pack(side='top',fill='x',pady=(0,20))

    main_frame=tk.Frame(master=instance)
    main_frame.columnconfigure(0,weight=5);main_frame.columnconfigure(1,weight=1)

    board_f=tk.Frame(master=main_frame)

    for i in range(dim[0]):               #creating a graphic column for each connect_4 grid column 
        board_f.columnconfigure(i,weight=1)
    for row in range(dim[1]):
        for col in range(dim[0]):
            token_placer('white',col,row)

    board_f.grid(column=0,sticky='NW',padx=(30,0))

    display_frame=tk.Frame(master=main_frame)

    player_label=tk.Label(master=display_frame,text='player 1 to play',font=('arial',30))
    player_label.pack(side='top')

    display_frame.grid(column=1,row=0,sticky='NW')

    main_frame.pack(fill='both')

    tk.mainloop()













############################################ __name__==__main__ ############################################
if __name__=='__main__':
    display([],(7,6))


