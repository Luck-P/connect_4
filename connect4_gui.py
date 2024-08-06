

def display(grid,dim):
    import tkinter as tk

    def token_placer(color,x,y):
        token=tk.Canvas(master=board_f,height=100,width=100)
        token.create_oval(2,2,99,99,fill=color)
        token.grid(column=x,row=y,sticky='NSEW',pady=10)


    instance=tk.Tk()
    instance.geometry('1000x1000')

    title_f=tk.Frame()

    title=tk.Label(master=title_f,text='Connect 4',fg='yellow',bg='blue',font=(400))
    title.pack(fill='both')

    title_f.pack(side='top',fill='x',pady=(0,20))

    board_f=tk.Frame(master=instance)

    for i in range(dim[0]):               #creating a graphic column for each connect_4 grid column 
        board_f.columnconfigure(i,weight=1)
    for row in range(dim[1]):
        for col in range(dim[0]):
            token_placer('white',col,row)

    board_f.pack(fill='both')

    tk.mainloop()













############################################ __name__==__main__ ############################################
if __name__=='__main__':
    display([],(7,6))


