from tkinter import*
from tkinter import ttk 

#Creating start window
start_window = Tk()
start_window.title('Start Window')
start_window.geometry('500x300')

#label Title
ttk.Label(start_window, text = "Select Unit", background = '#F0FFF0', foreground = '#FD6A02',
                        font = ("arial", 20)).grid(column = 2, row = 1)
ttk.Label(start_window,text='',width='18').grid(column=0,row=0)
ttk.Label(start_window,text='',width='15').grid(column=2,row=2)
ttk.Label(start_window,text='',width='15').grid(column=2,row=5)
ttk.Label(start_window,text='',width='15').grid(column=2,row=8)
ttk.Label(start_window,text='',width='15').grid(column=2,row=11)

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
        resalt_label.configure(text=(str('%.2f'%((user_input*unit_lenght[unit_ch])/unit_lenght[unit_con_ch])))
                                               + ' ' + unit_lenght_dict[unit_con_ch])
    
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
thai_to_matric_lenghtbutton.grid(column=2,row=4)
thai_to_matric_lenghtbutton.bind('<Button-1>',lenghtunit_window)


#Create Measure Window
def measureunit_window (event):
    measureunit_window = Tk()
    measureunit_window.title('ThaiUnit to MatricUnit Measure Window')
    measureunit_window.geometry('740x300')

    unit_measure  = {'ban' : 220,'kwian' : 440,'thang'  : 4.4 ,'liters' : 0.22 ,
                     'cubic centimaters' : 0.00022,'gallon(Br.)' : 1,'cubic maters' : 220,
                     'pound' : 0.128205,'kilogram' : 0.28205 ,'gram' : 0.00028205,'ounce': 0.00801}

    unit_measure_dict = {'ban' : 'บั้น' ,'kwian' : 'เกวียน' ,'thang'  : 'ถัง' ,'liters' : 'ลิตร' ,
                        'cubic centimaters' : 'ลูกบาศก์เซนติเมตร' ,'gallon(Br.)' : 'แกลลอน' ,
                        'cubic maters' : 'ลูกบาศก์เมตร' ,'pound' : 'ปอนด์' ,'kilogram' : 'กิโลกรัม' ,
                        'gram' : 'กรัม' ,'ounce' : 'ออนซ์'}

    def convert_measure (event):
        unit_ch = unit_choosen.get()
        unit_con_ch = unit_converted_choosen.get()
        user_input = int(input_entry.get())
        resalt_label.configure(text=(str('%.3f'%((user_input*unit_measure[unit_ch])/unit_measure[unit_con_ch])))
                                         + ' ' + unit_measure_dict[unit_con_ch])
    
    #Create Clear Funtion
    def clear_unit_measure (event) :
        unit_choosen.set('')
        unit_converted_choosen.set('')
        resalt_label.configure(text = '0')
        input_entry.delete(0,END)

    #Label for Title
    ttk.Label(measureunit_window, text = 'ThaiUnit to MatricUnit Measure', background = '#F0FFF0',
                                   foreground ="#FD6A02", font = ("arial", 17)).grid(column = 1, row = 0)
    ttk.Label(measureunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 2 )    
    ttk.Label(measureunit_window, text = "Select Unit : ",font = ("arial", 11)).grid(column = 0,row = 5)
    ttk.Label(measureunit_window, text = " to ",font = ("arial", 11),width=10).grid(column = 2,row = 5 )
    ttk.Label(measureunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 6 ) 

    #Comboblox ThaiUnit
    n = StringVar()
    unit_choosen = ttk.Combobox(measureunit_window, width = 27, textvariable = n)
    unit_choosen ['values'] = ('ban','kwian','thang','liters','cubic centimaters','gallon(Br.)','cubic maters',
                               'pound','kilogram','gram','ounce')
    unit_choosen.grid(column = 1 , row = 5)
    unit_choosen.current() 

    n = StringVar()
    unit_converted_choosen = ttk.Combobox(measureunit_window, width = 27, textvariable = n)
    unit_converted_choosen ['values'] = ('ban','kwian','thang','liters','cubic centimaters','gallon(Br.)',
                                         'cubic maters','pound','kilogram','gram','ounce')
    unit_converted_choosen.grid(column = 4 , row = 5)
    unit_converted_choosen.current()

    #Input Lenght   
    input_label = ttk.Label(measureunit_window, text = " Input Your Number : ",font = ("arial", 11))
    input_label.grid(column = 0,row = 7 )

    input_entry = ttk.Entry (measureunit_window,width='30')
    input_entry.grid(column = 1,row = 7 )

    ttk.Label(measureunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 8 )  
    ttk.Label(measureunit_window, text = " to ",font = ("arial", 11),width=10).grid(column = 2,row = 7 )

    resalt_label = ttk.Label(measureunit_window, text = "0",font = ("arial", 11))
    resalt_label.grid(column = 4,row = 7 )

    enter_button = Button(measureunit_window, text = " Enter ",font = ("arial", 11),
                                  background = 'red',foreground ="white")
    enter_button.grid(column = 0,row = 9 )
    enter_button.bind('<Button-1>',convert_measure)

    clear_button = Button(measureunit_window, text = " Clear ",font = ("arial", 11))
    clear_button.grid(column = 1,row = 9 )
    clear_button.bind('<Button-1>',clear_unit_measure)

    measureunit_window.mainloop()

#Create Measure Button
thai_to_matric_measurebutton = Button(start_window,text='ThaiUnit to MatricUnit Measure ',font=('arial,7'),
                              background = '#FFF0F5',foreground='#1C2951',width='25')
thai_to_matric_measurebutton.grid(column = 2 , row = 7)
thai_to_matric_measurebutton.bind('<Button-1>',measureunit_window)


#Create Science Window
def scienceunit_window (event):
    scienceunit_window = Tk()
    scienceunit_window.title('ScienceUnit Window')
    scienceunit_window.geometry('500x300')

    '''unit_science  = {}

    unit_science_dict = {}

    def convert_science (event):
        unit_ch = unit_choosen.get()
        unit_con_ch = unit_converted_choosen.get()
        user_input = int(input_entry.get())
        resalt_label.configure(text=(str('%.3f'%((user_input*unit_science[unit_ch])/unit_science[unit_con_ch])))
                                         + ' ' + unit_science_dict[unit_con_ch])'''
    
    #Create Clear Funtion
    def clear_unit_science (event) :
        unit_choosen.set('')
        unit_converted_choosen.set('')
        resalt_label.configure(text = '0')
        input_entry.delete(0,END)

    #Label for Title
    ttk.Label(scienceunit_window, text = 'ScienceUnit', background = '#F0FFF0',
                                   foreground ="#FD6A02", font = ("arial", 17)).grid(column = 1, row = 0)
    ttk.Label(scienceunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 2 )    
    ttk.Label(scienceunit_window, text = "Select Unit : ",font = ("arial", 11)).grid(column = 0,row = 5)
    ttk.Label(scienceunit_window, text = " to ",font = ("arial", 11),width=10).grid(column = 2,row = 5 )
    ttk.Label(scienceunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 6 ) 

    #Comboblox ThaiUnit
    n = StringVar()
    unit_choosen = ttk.Combobox(scienceunit_window, width = 27, textvariable = n)
    unit_choosen ['values'] = ('ban','kwian','thang','liters','cubic centimaters','gallon(Br.)','cubic maters',
                               'pound','kilogram','gram','ounce')
    unit_choosen.grid(column = 1 , row = 5)
    unit_choosen.current() 

    n = StringVar()
    unit_converted_choosen = ttk.Combobox(scienceunit_window, width = 27, textvariable = n)
    unit_converted_choosen ['values'] = ('ban','kwian','thang','liters','cubic centimaters','gallon(Br.)',
                                         'cubic maters','pound','kilogram','gram','ounce')
    unit_converted_choosen.grid(column = 4 , row = 5)
    unit_converted_choosen.current()

    #Input Lenght   
    input_label = ttk.Label(scienceunit_window, text = " Input Your Number : ",font = ("arial", 11))
    input_label.grid(column = 0,row = 7 )

    input_entry = ttk.Entry (scienceunit_window,width='30')
    input_entry.grid(column = 1,row = 7 )

    ttk.Label(scienceunit_window, text = "  ",font = ("arial", 11)).grid(column = 0,row = 8 )  
    ttk.Label(scienceunit_window, text = " to ",font = ("arial", 11),width=10).grid(column = 2,row = 7 )

    resalt_label = ttk.Label(scienceunit_window, text = "0",font = ("arial", 11))
    resalt_label.grid(column = 4,row = 7 )

    enter_button = Button(scienceunit_window, text = " Enter ",font = ("arial", 11),
                                  background = 'red',foreground ="white")
    enter_button.grid(column = 0,row = 9 )
    #enter_button.bind('<Button-1>',convert_science)

    clear_button = Button(scienceunit_window, text = " Clear ",font = ("arial", 11))
    clear_button.grid(column = 1,row = 9 )
    #clear_button.bind('<Button-1>',clear_unit_science)

    #Create Temperature Button
    sciencebutton = Button(scienceunit_window,text='Temperature Convert',font=('arial,7'),
                                                  background = '#FFF0F5',foreground='#1C2951',width='25')
    sciencebutton.grid(column=2,row=4)
    sciencebutton.bind('<Button-1>',science_window)

    scienceunit_window.mainloop()
    
#Create Science Button
science_button = Button(start_window,text='Convert Science Unit',font=('arial,7'),width='25',
                     background = '#FFF0F5',foreground='#1C2951' )
science_button.grid(row=10,column=2)

science_button.bind('<Button-1>',start_window)


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