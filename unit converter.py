from tkinter import*
from tkinter import ttk 

#Creating start window
start_window = Tk()
start_window.title('Start Window')
start_window.geometry('500x300')

#label Title
ttk.Label(start_window, text = "Collect Unit", background = '#F0FFF0', foreground = '#FD6A02',
                        font = ("arial", 20)).grid(row = 1, column = 2)
ttk.Label(start_window,text='',width='18').grid(row=0,column=0)
ttk.Label(start_window,text='',width='15').grid(row=2,column=2)
ttk.Label(start_window,text='',width='15').grid(row=5,column=2)
ttk.Label(start_window,text='',width='15').grid(row=8,column=2)
ttk.Label(start_window,text='',width='15').grid(row=11,column=2)

#Create Lenght Window
def lenghtunit_window (event):
    lenghtunit_window = Tk()
    lenghtunit_window.title('ThaiUnit to MatricUnit Lenght Window')
    lenghtunit_window.geometry('750x300')

    #Create Funtion Convert Lenght Unit
    unit_lenght = {'inch' : 0.00052,'keub' : 0.00625,'sok'  :0.0125,'wa' : 0.05,'sen' : 1,'centimaters' : 0.00025,
                   'maters' : 0.025,'kilomaters' : 25,'yot' : 400}
    unit_lenght_dict = {'inch' : 'นิ้ว','keub' : 'คืบ','sok' : 'ศอก','wa' : 'วา','sen' : 'เส้น',
                        'centimaters' : 'เซนติเมตร','maters' : 'เมตร','kilomaters' : 'กิโลเมตร','yot' : 'โยชน์'}
    def convert_lenght (event):
        unit_ch = unit_choosen.get()
        unit_con_ch = unit_converted_choosen.get()
        user_input = int(input_entry.get())
        resalt_label.configure(text=(str((user_input*unit_lenght[unit_ch])/unit_lenght[unit_con_ch])) + ' '
                               + unit_lenght_dict[unit_con_ch])
    
    #Create Clear Funtion
    def clear_unit_lenght (event) :
        unit_choosen.set('')
        unit_converted_choosen.set('')
        resalt_label.configure(text = '0')
        input_entry.delete(0,END)

    #Label for Title
    ttk.Label(lenghtunit_window, text = 'ThaiUnit to MatricUnit Lenght', background = '#F0FFF0',
                                 foreground ="#FD6A02", font = ("arial", 17)).grid(row = 0, column = 1)
    ttk.Label(lenghtunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 2 )    
    ttk.Label(lenghtunit_window, text = "Select Unit : ",font = ("arial", 11)).grid(column = 0,row = 5)
    ttk.Label(lenghtunit_window, text = " to ",font = ("arial", 11),width=10).grid(column = 2,row = 5 )
    ttk.Label(lenghtunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 6 ) 

    #Comboblox ThaiUnit
    n = StringVar()
    unit_choosen = ttk.Combobox(lenghtunit_window, width = 27, textvariable = n)
    unit_choosen ['values'] = ('inch','keub','sok','wa','sen','centimaters','maters','kilomaters','yot')
    unit_choosen.grid(column = 1 , row = 5)
    unit_choosen.current() 

    n = StringVar()
    unit_converted_choosen = ttk.Combobox(lenghtunit_window, width = 27, textvariable = n)
    unit_converted_choosen ['values'] =('inch','keub','sok','wa','sen','centimaters','maters','kilomaters','yot')
    unit_converted_choosen.grid(column = 4 , row = 5)
    unit_converted_choosen.current()

    #Input Lenght   
    input_label = ttk.Label(lenghtunit_window, text = " Input Your Number : ",font = ("arial", 11))
    input_label.grid(column = 0,row = 7 )

    input_entry = ttk.Entry (lenghtunit_window,width='30')
    input_entry.grid(column = 1,row = 7 )

    ttk.Label(lenghtunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 8 )  
    ttk.Label(lenghtunit_window, text = " to ",font = ("arial", 11),width=10).grid(column = 2,row = 7 )

    resalt_label = ttk.Label(lenghtunit_window, text = "0",font = ("arial", 11))
    resalt_label.grid(column = 4,row = 7 )

    enter_button = Button(lenghtunit_window, text = " Enter ",font = ("arial", 11),
                                  background = 'red',foreground ="white")
    enter_button.grid(column = 0,row = 9 )
    enter_button.bind('<Button-1>',convert_lenght)

    clear_button = Button(lenghtunit_window, text = " Clear ",font = ("arial", 11))
    clear_button.grid(column = 1,row = 9 )
    clear_button.bind('<Button-1>',clear_unit_lenght)

    lenghtunit_window.mainloop()
    
#Create Lenght Button
thai_to_matric_lenghtbutton = Button(start_window,text='ThaiUnit to MatricUnit Lenght',font=('arial,7'),
                              background = '#FFF0F5',foreground='#1C2951',width='25')
thai_to_matric_lenghtbutton.grid(row=4,column=2)
thai_to_matric_lenghtbutton.bind('<Button-1>',lenghtunit_window)


#Create Measure Window
def measureunit_window (event):
    measureunit_window = Tk()
    measureunit_window.title('ThaiUnit to MatricUnit Measure Window')
    measureunit_window.geometry('700x300')
    #Label for Title
    ttk.Label(measureunit_window, text = 'ThaiUnit to MatricUnit Measure', background = '#F0FFF0',
                                 foreground ="#FD6A02", font = ("arial", 17)).grid(row = 0, column = 1)
    ttk.Label(measureunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 2 )    
    ttk.Label(measureunit_window, text = "Select Unit : ",font = ("arial", 11)).grid(column = 0,row = 5)
    #ttk.Label(unitlenght_window, text = " to ",font = ("arial", 11)).grid(column = 1,row = 5 )
    ttk.Label(measureunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 6 ) 

    #Input Lenght   
    input_label = ttk.Label(measureunit_window, text = " Input Your Number : ",font = ("arial", 11))
    input_label.grid(column = 0,row = 7 )

    input_entry = ttk.Entry (measureunit_window,width='30')
    input_entry.grid(column = 1,row = 7 )

    ttk.Label(measureunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 8 )    

    enter_button = Button(measureunit_window, text = " Enter ",font = ("arial", 11),
                                  background = 'red',foreground ="white")
    enter_button.grid(column = 0,row = 9 )

    clear_button = Button(measureunit_window, text = " Clear ",font = ("arial", 11))
    clear_button.grid(column = 1,row = 9 )

    measureunit_window.mainloop()

#Create Measure Button
thai_to_matric_measurebutton = Button(start_window,text='ThaiUnit to MatricUnit Measure ',font=('arial,7'),
                              background = '#FFF0F5',foreground='#1C2951',width='25')
thai_to_matric_measurebutton.grid(row=7,column=2)
thai_to_matric_measurebutton.bind('<Button-1>',measureunit_window)


#Create Science Window
def scienceunit_window (event):
    scienceunit_window = Tk()
    scienceunit_window.title('ScienceUnit Window')
    scienceunit_window.geometry('700x300')

    #Label for Title
    ttk.Label(scienceunit_window, text = 'Convented Science Unit', background = '#F0FFF0',
                                 foreground ="#FD6A02", font = ("arial", 17)).grid(column=1,row=0)
    ttk.Label(scienceunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 2 )    
    ttk.Label(scienceunit_window, text = "Select Unit : ",font = ("arial", 11)).grid(column = 0,row = 5)
    #ttk.Label(unitlenght_window, text = " to ",font = ("arial", 11)).grid(column = 1,row = 5 )
    ttk.Label(scienceunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 6 ) 

    #Input Lenght   
    input_label = ttk.Label(scienceunit_window, text = " Input Your Number : ",font = ("arial", 11))
    input_label.grid(column = 0,row = 7 )

    input_entry = ttk.Entry (scienceunit_window,width='30')
    input_entry.grid(column = 1,row = 7 )

    ttk.Label(scienceunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 8 )    

    enter_button = Button(scienceunit_window, text = " Enter ",font = ("arial", 11),
                                  background = 'red',foreground ="white")
    enter_button.grid(column = 0,row = 9 )

    clear_button = Button(scienceunit_window, text = " Clear ",font = ("arial", 11))
    clear_button.grid(column = 1,row = 9 )

    scienceunit_window.mainloop()
    
#Create Science Button
science_button = Button(start_window,text='Convented Science Unit',font=('arial,7'),width='25',
                     background = '#FFF0F5',foreground='#1C2951' )
science_button.grid(row=10,column=2)
science_button.bind('<Button-1>',scienceunit_window)


#Create About Window
def about_window (event):
    about_window = Tk()
    about_window.title('About Window')
    about_window.geometry('400x100')

    #Label for Title
    ttk.Label(about_window, text = 'About Program', background = '#F0FFF0',
                                 foreground ="#FD6A02", font = ('arial',25)).grid(column=1,row=0)
    ttk.Label(about_window,text = ' ',width='13').grid(column=0,row=0)                             
    ttk.Label(about_window,text = ' ').grid(column=0,row=2)          
    ttk.Label(about_window,text = 'develop by : Palathip Singchoo',font=('arial',12)).grid(column=1,row=3)

    about_window.mainloop()

#Create About Button
about_button = Button(start_window,text='About',font=('arial,7'),width='25',
                     background = '#9DC183',foreground='#5E1914')
about_button.grid(row=12,column=2)
about_button.bind('<Button-1>',about_window)


start_window.mainloop()