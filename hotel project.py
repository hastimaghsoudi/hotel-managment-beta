   
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox
import hotel_database as hdata
#from tkinter import PhotoImage


main_window= tk.Tk()

#icon=PhotoImage(file="khazar-logo.png")

class book:
    def __init__(self):
        self.bookwindow = tk.Toplevel(main_window)
        self.bookwindow.title('book a hotel room')
        self.bookwindow.geometry('600x650')
        
        self.bookframe = tk.Frame(self.bookwindow)
        self.bookframe.pack(fill='both', expand=True)
        
        current=0 
        self.savedic1={}
        self.savedic2={}
        self.customersub={}
        
        page1 = tk.Frame(self.bookframe)
        page1.pack(fill='both', expand=True)  
        page2 = tk.Frame(self.bookframe)
        page3= tk.Frame(self.bookframe)
        
        
        infotitle = tk.LabelFrame(page1, text='your identity information'#, bg='light blue'
                                  )
        infotitle.place(x=20, y=20, width=560, height=194)
        
        addtitle = tk.LabelFrame(page1, text='your address information')
        addtitle.place(x=20, y=220, width=560, height=190)
#=================================================        
        
        name = tk.Label(infotitle,
                        text='First Name:',
                        font=('Times New Roman Bold',18),
#                        bg='#02319e',
                        fg='#02319e',
                        justify='center'
                        )
        name.place(x=20, y=4)
        
        name_entry = tk.Entry(infotitle,
        font=('Times New Roman',18),
#        bg='light blue',
        fg='#02319e',
        width=12)
        name_entry.place(x=10, y=34)
        
        self.namef=tk.StringVar()
        self.namef.set('Name:')
#---------------------------------------------------
        last = tk.Label(infotitle,
                       text='Last name:',
                       font=('Times New Roman Bold',18),
#                       bg='light blue',
                       fg='#02319e',
                       justify='center'
                       )
        last.place(x=205, y=4)
        
        last_entry = tk.Entry(infotitle,
        font=('Times New Roman',18),
   #    bg='light blue',
        fg='#02319e',
        width=12)
        last_entry.place(x=190, y=34)
        
        self.lastf=tk.StringVar()
        self.lastf.set('Lastname:')
        
#-----------------------------------------------------       
        age = tk.Label(infotitle,
                       text='Age:',
                       font=('Times New Roman Bold',18),
#                      bg='light blue',
                       fg='#02319e',
                       justify='center'
                       )
        age.place(x=415, y=4)
        
        age_entry = tk.Entry(infotitle,
        font=('Times New Roman',18),
#        bg='light blue',
        fg='#02319e',
        width=12)
        age_entry.place(x=370, y=34)
        
        self.agef=tk.StringVar()
        self.agef.set('Age:')
#------------------------------------------------------        
        ID = tk.Label(infotitle,
                       text='Your ID:',
                       font=('Times New Roman Bold',18),
#                      bg='light blue',
                       fg='#02319e',
                       justify='left'
                       )
        ID.place(x=35, y=84)
        
        ID_entry = tk.Entry(infotitle,
        font=('Times New Roman',18),
#       bg='light blue',
        fg='#02319e',
        width=12)
        ID_entry.place(x=10, y=114)
        self.IDf=tk.StringVar()
        self.IDf.set('ID:')
#-------------------------------------------------        
        def clearing():
            name_entry.delete(0,tk.END)
            last_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            ID_entry.delete(0, tk.END)
         
        clear = tk.Button(infotitle,
                         text='clear all',
                         font=('Times New Roman',14),
                         activebackground='black',
                         activeforeground='white',
                         command=clearing
                         )
        clear.place(x=450, y=114)
        
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^  
        number= tk.Label(addtitle, text='Number:',
                          font=('Times New Roman Bold',18),
#                         bg='light blue',
                          fg='#02319e')
        number.place(x=10, y=12)
        
        number_entry = tk.Entry(addtitle,
        font=('Times New Roman',18),
#       bg='light blue',
        fg='#02319e',
        width=35)
        number_entry.place(x=120, y=15)
        self.numberf=tk.StringVar()
        self.numberf.set('Phone number:')
#-----------------------------------------------------        
        email= tk.Label(addtitle, text='Email:',
                       font=('Times New Roman Bold',18),
 #                     bg='light blue',
                       fg='#02319e')
        email.place(x=10, y=75)
        
        email_entry = tk.Entry(addtitle,
                             font=('Times New Roman',18),
#                            bg='light blue',
                             fg='#02319e',
                             width=35)
        email_entry.place(x=120, y=75)
        self.emailf=tk.StringVar()
        self.emailf.set('Email:(none)')
#-------------------------------------------------------        
       
        def clearing2():
            email_entry.delete(0, tk.END)
            number_entry.delete(0, tk.END)
         
        clear2 = tk.Button(addtitle,
                          text='clear all',
                          font=('Times New Roman',14),
                          activebackground='black',
                          activeforeground='white',
                          command=clearing2
                          )
        clear2.place(x=450, y=120)
#==================================================
        def submit():
            ageenter=age_entry.get().strip()
            numberenter= number_entry.get().strip()
            if not name_entry.get().strip():
                messagebox.showwarning(title="Warning", message="First name entry is empty!")
            elif not last_entry.get().strip():
                messagebox.showwarning(title="Warning", message="Last name entry is empty!")
            elif not ageenter:
                messagebox.showwarning(title="Warning", message="Age entry is empty!")
            elif not ageenter.isdigit() or int(ageenter) <= 0:
                 messagebox.showwarning(title="Warning",message="Please enter a valid positive number for age!")
            elif not ID_entry.get().strip():
                messagebox.showwarning(title="Warning",message="ID entry is empty!")
            elif not numberenter:
                messagebox.showwarning(title="Warning", message="Phone number entry is empty!")
            elif not numberenter.isdigit() or int(numberenter) <= 0: 
                messagebox.showwarning(title="Warning", message="Please enter a valid positive number for phone!")
            
            else:
                surance= messagebox.askyesno(title='wait' , message='are you sure you want to submit all your informatins?')
                if surance :
                    self.namef.set(f"Name: {name_entry.get()}")
                    self.lastf.set(f"Last name: {last_entry.get()}")
                    self.agef.set(f"Age: {age_entry.get()}")
                    self.IDf.set(f"ID: {ID_entry.get()}")
                    self.numberf.set(f"Phone number: {number_entry.get()}")
                    self.emailf.set(f"Email: {email_entry.get()}")
                    #place something here to add the valuebles of entry(yadet nare)
                    self.savedic1={ 
                        'first_name': name_entry.get(),
                        'last_name': last_entry.get(),
                        'age': age_entry.get(),
                        'id': ID_entry.get(),
                        'phone': number_entry.get(),
                        'email': email_entry.get()
                        }
                    name_entry.config(state='disabled')
                    last_entry.config(state='disabled')
                    age_entry.config(state='disabled')
                    ID_entry.config(state='disabled')
                    email_entry.config(state='disabled')
                    number_entry.config(state='disabled')
                
            
        record_button = tk.Button(page1, text='Submit all',
                                font=('Times New Roman Bold',18), 
                                bg='light blue', 
                                fg='#02319e',
                                activebackground='#0050D1',
                                activeforeground='light blue',
                                command=submit)
        record_button.place(x=235, y=440)
        def nextbtn():
            nonlocal current
            nonlocal next_button
            current+=1
            if current==1:
                page1.pack_forget()  
                page2.pack(fill='both', expand=True)
            elif current==2:
                page2.pack_forget()
                page3.pack(fill='both', expand=True)
                next_button.config(state=tk.DISABLED)
                
                
        
        def backbtn():
            nonlocal current
            current-=1
            if current==0:
                page2.pack_forget()  # مخفی کردن صفحه اول
                page1.pack(fill='both', expand=True)
            elif current==1:
                next_button.config(state=tk.NORMAL)
                page3.pack_forget()
                page2.pack(fill='both', expand=True)
            elif current==-1:
                backwarn= messagebox.askyesno(title='wait', message='are you sure you want to close the window?')
                if backwarn:
                    self.bookwindow.destroy()
                else:
                    current=0
            
        next_button = tk.Button(self.bookframe, text='next => \n (Hotel rooms)',
                                font=('Times New Roman',14),
                                activebackground='black',
                                activeforeground='white',
                                command=nextbtn)
        next_button.place(x=450, y=570)
        
        back_btn= tk.Button(self.bookframe, text=' <= back  \n (Hotel rooms)',
                                font=('Times New Roman',14),
                                activebackground='black',
                                activeforeground='white',
                                command=backbtn)
        back_btn.place(x=30, y=570)
#==================================================================================
        filterframe= tk.LabelFrame(page2,text='hotel room filter:')
        filterframe.place(x=20, y=10, width=250, height=80)
        roomcombo= ttk.Combobox(filterframe, width = 27, state="readonly")
        roomcombo['values'] = ('All rooms',
                          '1bed', 
                          '2beds',
                          'Suite',
                          'VIP')
                
        roomcombo.place(x=20, y=15, width=200, height=30)
        roomcombo.current(0)
        
        dayframe= tk.LabelFrame(page2, text='staying days')
        dayframe.place(x=275, y=10, width=305, height=80)
        
        daylabel=tk.Label(dayframe, text= 'how many days you want io stay?',
                            font=('Times New Roman',13))
        daylabel.place(x=35, y=0)
        
        dayentry=tk.Entry(dayframe,
                          font=('Times New Roman',18),
 #                        bg='#ccecff',
                          fg='#02319e',
                          justify='center',
                          width=12 )
        dayentry.place(x=70, y=25)
        
        
        treeframe= tk.LabelFrame(page2,text='hotel room type:')
        treeframe.place(x=20, y=100, width=560, height=280)
        
        hottree= ttk.Treeview(treeframe, selectmode= 'browse')
        hottree.place(x=12, y=15)
        hottree['columns']=('room_number', 'room_type','price', 'capacity', 'status', 'description')
         
        hottree.column('#0', width=0, stretch=tk.NO)
        hottree.column('room_number', width=90, anchor=tk.CENTER)
        hottree.column('room_type', width=60, anchor=tk.CENTER)
        hottree.column('price', width=90, anchor=tk.E)
        hottree.column('capacity', width=80, anchor=tk.CENTER)
        hottree.column('status', width=80, anchor=tk.CENTER)
        hottree.column('description', width=130, anchor=tk.W)
        
        hottree.heading('#0', text='')
        hottree.heading('room_number', text='room number')
        hottree.heading('room_type', text='type')
        hottree.heading('price', text='price per night')
        hottree.heading('capacity', text='capacity')
        hottree.heading('status', text='status')
        hottree.heading('description', text='description')
        
        hot_scrollbar_y = ttk.Scrollbar(treeframe,
                                        orient='vertical',
                                        command=hottree.yview)
        
        hot_scrollbar_x = ttk.Scrollbar(treeframe,
                                        orient='horizontal',
                                        command=hottree.xview)
        
        hottree.configure(yscrollcommand=hot_scrollbar_y.set,
                          xscrollcommand=hot_scrollbar_x.set)
        
        hottree.place( x=12,y=15,width=520,height=215)

        hot_scrollbar_y.place(x=532, y=15, width=15, height=215)

        hot_scrollbar_x.place(x=12,y=230,width=520, height=20)

        
        hotrooms= hdata.hoteldata()
        
        def roombox(room_list):
            #delete
            for item in hottree.get_children():
                hottree.delete(item)
            
            for room in room_list:
                hottree.insert('', tk.END, values=(
                    room[1],           # room_number
                    room[2],           # room_type
                    room[3],    # price
                    room[4],           # capacity
                    room[5],           # status
                    room[6]            # description
                ))
        
        for i in hotrooms:
            hottree.insert('', tk.END, values=(
                i[1],  # room_number
                i[2],  # room_type
                f"{i[3]:,}",  # price_per_night با فرمت هزارگان
               i[4],  # capacity
               i[5],  # status
               i[6]   # description
               ))
        def filterrooms(event= None): 
            slct= roomcombo.get()
           
            if slct == 'All rooms':
                filtered= hotrooms
            else:
                filtered=[]
                for room in hotrooms:
                    if room[2]== slct:
                        filtered.append(room)
            
            roombox(filtered)
        
        roomcombo.bind("<<ComboboxSelected>>", filterrooms)
        
        roombox(hotrooms)
         
           
        textframe= tk.LabelFrame(page2, text='description')
        textframe.place(x=20, y=380,width=560, height=180 )
        
        def showchoice(a):
            select= hottree.selection()
            if select:
                val= hottree.item(select,'values')

                
                if val:
                    try: 
                        typelabel.config(text= f'Type:  {val[1]}')
                        capalabel.config(text= f'Capacity: {val[3]}')
                        pricelabel.config(text= f'Price per night: {val[2]} Dollars')
                        descriplabel.config(text= f'Description: {val[5]}')
                        total = int(dayentry.get().strip()) * int(float(val[2]))
                        totalprice.config(text=f'Total price: {total} Dollars')
                    except: 
                        totalprice.config(text='Total price: enter a number in entry')
    
                    
                    
                    
                    
        hottree.bind('<<TreeviewSelect>>', showchoice)
        typelabel= tk.Label(textframe,text='Type:', 
                            font=('Times New Roman',14),
                            justify='left')
        typelabel.place(x=4,y=4)
        capalabel=tk.Label(textframe,text='Capacity:', 
                            font=('Times New Roman',14),
                            justify='center')
        capalabel.place(x=250,y=4)
        pricelabel=tk.Label(textframe, text='Price per night:',
                            font=('Times New Roman',14),
                            justify='right')
        pricelabel.place(x=4, y=40)
        
        totalprice= tk.Label(textframe, text='Total price:',
                            font=('Times New Roman',14),
                            justify='right')
        totalprice.place(x=250,y=40)
        
        descriplabel=tk.Label(textframe, text='Description:',
                            font=('Times New Roman',14),
                            justify='right')
        descriplabel.place(x=4, y=75)
        
        
        def hotelsub():
            select= hottree.selection()
            
            if not select:
                messagebox.showwarning(title="Warning",message="Select a room first")
                return
            
            val= hottree.item(select, 'values')
            
            if not val[4]=='Available': 
                tk.messagebox.showwarning(title='error',message='the room is booked by someone else\n you can not choose it')
                return


            days= dayentry.get().strip()

                
            if not days or not days.isnumeric() or int(days) <=0:
                messagebox.showerror(title='Warning', message='Please enter a valid, positive number for Days')
                return
                        
            totalcal= int(days)* int(float(val[2]))
            confirm=messagebox.askyesno( title="Confirm Selection", message='Are you sure you want to submit your choice?')
            
            if confirm: 
                ftype.config(text= f'Type: {val[1]}')
                fcap.config(text= f'Capacity: {val[3]}')
                fprice.config(text= f'Price per night: {val[2]} Dollars')
                fdesc.config(text=f'Description: {val[5]}')
                fdays.config(text=f'Staying days: {days}')
                ftotal.config(text=f'Total price:{totalcal} Dollars')
                        
                self.savedic2 ={
                    'room_number': val[0],
                    'room_type': val[1],
                    'days': days
                            }
                        
                hotsubbtn.config(state=tk.DISABLED)
                dayentry.config(state=tk.DISABLED)
                        
                messagebox.showinfo(title="Success",message="Room selected successfully!")
                        

                
        
        hotsubbtn= tk.Button(textframe, text='Submit the room',
                             font=('Times New Roman Bold',14),
                                bg='light blue', 
                                fg='#02319e',
                                activebackground='#0050D1',
                                activeforeground='light blue',
                             command=hotelsub)
        hotsubbtn.place(x=200, y=110)
        
        finallabel=tk.LabelFrame(page3, text='personal info' )
        finallabel.place(x=20 , y=20 ,width=560, height=175 )
        
        fname= tk.Label(finallabel, textvariable=self.namef,
                        font=('Times New Roman Bold',14),
                        justify='left')
        fname.place(x=20,y=5)
        
        flast= tk.Label(finallabel, textvariable=self.lastf,
                        font=('Times New Roman Bold',14),
                        justify='right')
        flast.place(x=200,y=5)
        
        fage= tk.Label(finallabel, textvariable= self.agef,
                       font=('Times New Roman Bold',14),
                       justify='right'
                       )
        fage.place(x=400,y=5)
        
        fID= tk.Label(finallabel, textvariable= self.IDf,
                      font=('Times New Roman Bold',14),
                      justify='right'
                      )
        fID.place(x=20, y=65)
        
        fnumber= tk.Label(finallabel, textvariable= self.numberf,
                          font=('Times New Roman Bold',14),
                          justify='right')
        fnumber.place(x=230, y=65)
        
        femail= tk.Label(finallabel, textvariable= self.emailf,
                         font=('Times New Roman Bold',14),
                         justify='right')
        femail.place(x=20 , y=115)
        
        
        finallabel2=tk.LabelFrame(page3, text='hotel order')
        finallabel2.place(x=20 , y=210 ,width=560, height=165 )
        
        ftype= tk.Label(finallabel2, text='Room type:',
                        font=('Times New Roman Bold',14),
                        justify='left')
        ftype.place(x=20,y=5)
        
        fcap= tk.Label(finallabel2, text='Capacity:',
                       font=('Times New Roman Bold',14),
                       justify='right')
        fcap.place(x=200, y=5)
        
        fdays=tk.Label(finallabel2, text='Staying days:',
                       font=('Times New Roman Bold',14),
                       justify='right')
        fdays.place(x=350, y=5)
        
        fprice= tk.Label(finallabel2, text='Price per night:',
                         font=('Times New Roman Bold',14),
                         justify='left')
        fprice.place(x=20, y=105)
        
        fdesc=tk.Label(finallabel2,text='Description:',
                       font=('Times New Roman Bold',14),
                       justify='right')
        fdesc.place(x=20, y=55)
        
        ftotal=tk.Label(finallabel2, text=' Total price:',
                        font=('Times New Roman Bold',14),
                        justify='right')
        ftotal.place(x=250, y=105)
        
        checkvar = tk.IntVar(value=0) 
        fcheck= tk.Checkbutton(page3,
                               text='I agree with privacy policy and terms of service',
                               font=('Times New Roman Bold',14),
                               fg='#062B63',
                               variable= checkvar,
                               onvalue = 1, 
                               offvalue = 0)
        fcheck.place(x=20, y=380)
        
        
        def finalsub():
            nonlocal checkvar
            
            if not self.savedic1:
                messagebox.showwarning(title='Warning', message='Please compelete or submit your personal information first')
                return
            elif not self.savedic2:
                messagebox.showwarning(title='Warning', message='Please compelete or submit your room choice first')
                return
            elif checkvar.get() == 0 :
                messagebox.showwarning(title='Warning', message='You must agree with privacy policy and terms of service first to continue. ') 
                return
            else: 
                if self.savedic1 and self.savedic2 : 
                    self.customersub = {}
                    self.customersub.update(self.savedic1)
                    self.customersub.update(self.savedic2)
                    
                    result = hdata.savedata(self.customersub)

                    if result:
                        roomnum=  self.savedic2['room_number']
                        roomresult= hdata.book_room(roomnum)
                        
                        if roomresult: 
                            messagebox.showinfo(title='Successful', message='Your booking process compeleted. thank you for choosing us.')
                            self.bookwindow.destroy()
                        else:
                            messagebox.showerror(title='Error', message= 'Error, customer is saved, but something happend while submitting')
                    else:
                        messagebox.showerror(title='Error', message='Error,something wrong happened while saving. try again')
                        
                         
                    
                    
            
            
        fsubbtn=tk.Button(page3, text='Final submition',
                          font=('Times New Roman Bold',16),
                          bg='light blue', 
                          fg='#02319e',
                          activebackground='#0050D1',
                          activeforeground='light blue',
                          command= finalsub)
        fsubbtn.place(x=220, y=420)
        
         

                
                


#================================================
class login:
    def __init__(self):
        self.loginwindow= tk.Toplevel(main_window)
        self.loginwindow.title('log in')
        self.loginwindow.geometry('700x400')
        
        self.username=tk.StringVar()
        self.password=tk.StringVar()
        
    #def log_in(self):
        hello=tk.Label(self.loginwindow,
                       text='Hello dear employee/manager.\n  enter your username and password to continue',
                       font=('Times New Roman Bold',16),
                       )
        hello.pack(side='top', pady=20)
        
        tk.Label(self.loginwindow,
                 text="Username:",
                 font=('Times New Roman', 20),
                 
                 ).pack(pady=5)
        username_entry = tk.Entry(self.loginwindow, textvariable=self.username)
        username_entry.pack(pady=5)
        
        tk.Label(self.loginwindow,
                 text="password:",
                 font=('Times New Roman', 20) 
                 ).pack(pady=6)
        pass_entry = tk.Entry(self.loginwindow, textvariable=self.password)
        pass_entry.pack(pady=6)
        
        def loginwndw():
            username= self.username.get().lower()
            password=self.password.get()
            if username== 'mamad' and password=='1234' :
                self.employeewndw= tk.Toplevel(self.loginwindow)
                self.employeewndw.title('Employee panel')
                self.employeewndw.geometry('800x600')
                
                self.employeeframe= tk.Frame(self.employeewndw)
                self.employeeframe.pack(fill='both', expand=True)
                
                epanel= tk.LabelFrame(self.employeeframe,text= 'guest manager panel')
                epanel.place(x=25, y=10, width=750, height=550)
                
                search = tk.Label(epanel,
                                  text='Search:',
                                  font=('Times New Roman Bold', 14),
                                  fg='#02319e')
                search.place(x=35, y=10)

                search_entry = tk.Entry(epanel,
                                        font=('Times New Roman', 14),
                                        bg='white',
                                        fg='#02319e',
                                        width=25)
                search_entry.place(x=110, y=10)
                
                                
              
                columns=('customer_id', 'first_name', 'last_name', 'age', 'id', 'phone', 'email','room_number', 'room_type','days', 'booking_date')
                
                guesttree = ttk.Treeview(epanel,columns=columns, show='headings', selectmode='browse')  
                guesttree.place(x=35, y=40, width=680, height=380)
                
                
                guesttree.column('#0', width=0, stretch=tk.NO)  
                guesttree.column('customer_id', width=100, anchor=tk.CENTER)
                guesttree.column('first_name', width=100, anchor=tk.W)
                guesttree.column('last_name', width=100, anchor=tk.W)
                guesttree.column('age', width=50, anchor=tk.CENTER)
                guesttree.column('id', width=100, anchor=tk.CENTER)
                guesttree.column('phone', width=120, anchor=tk.W)
                guesttree.column('email', width=150, anchor=tk.W)
                guesttree.column('room_number', width=90, anchor=tk.CENTER)
                guesttree.column('room_type', width=80, anchor=tk.CENTER)
                guesttree.column('days', width=120, anchor=tk.CENTER)
                guesttree.column('booking_date', width=150, anchor=tk.CENTER)


                guesttree.heading('#0', text='')
                guesttree.heading('customer_id',text='Customer ID')
                guesttree.heading('first_name', text='Name')
                guesttree.heading('last_name', text='Last')
                guesttree.heading('age', text='Age')
                guesttree.heading('id', text='ID')
                guesttree.heading('phone', text='Phone number')
                guesttree.heading('email', text='Email')
                guesttree.heading('room_number', text='Room number')
                guesttree.heading('room_type', text='Room type')
                guesttree.heading('days', text='reservation days')
                guesttree.heading('booking_date', text='booking date')
                
                customers = hdata.get_customers()
                
                
                for i in customers: 
                    guesttree.insert('', tk.END, values=i)
                def searchcustom(event=None):
                    searchtxt= search_entry.get().strip().lower()
                    
                    for item in guesttree.get_children(): 
                        guesttree.delete(item)
                        
                    for customer in customers: 
                        
                        if not searchtxt:
                            guesttree.insert('', tk.END, values=customer) 
                        elif any(searchtxt in str(value).lower() for value in customer): 
                            guesttree.insert('', tk.END, values=customer)


                search_entry.bind('<KeyRelease>', searchcustom)
    
                scrollbar_y = ttk.Scrollbar(epanel, orient='vertical',command=guesttree.yview) 
                scrollbar_y.place(x=715, y=40, height=380) 
                guesttree.configure(yscrollcommand=scrollbar_y.set) 
               
                scrollbar_x = ttk.Scrollbar(epanel, orient='horizontal', command=guesttree.xview) 
                scrollbar_x.place(x=35,y=420,width=680) 
                guesttree.configure(xscrollcommand=scrollbar_x.set)
                #--------------------------------------------------------
                
                def customer_edit():
                    select = guesttree.selection()
                    
                    if not select: 
                        messagebox.showwarning(title="Warning",message="Select a customer first.")
                        return
                    values = guesttree.item(select[0], 'values')
                    customerid= values[0]
                    
                    editwndw=tk.Toplevel(self.employeewndw)
                    editwndw.title("Edit Customer panel")
                    editwndw.geometry("640x570")
                    
                    editframe= tk.Frame(editwndw)
                    editframe.pack(fill='both', expand=True)
                    
                    editlabelframe= tk.LabelFrame(editframe,text= 'Edit customer info')
                    editlabelframe.place(x=20, y=20, width=600, height=530)
                    
                    
                    name = tk.Label(editlabelframe,
                                    text='First name:',
                                    font=('Times New Roman Bold',18),
                                    fg='#02319e',
                                    justify='center'
                                    )
                    name.place(x=20, y=4)
                    
                    name_entry= tk.Entry(editlabelframe, 
                                     font=('Times New Roman',18),
                                     fg='#02319e',
                                     width=12)
                    name_entry.place(x=7, y=35)
                    name_entry.insert(0, values[1])

                    last= tk.Label(editlabelframe,
                                   text='Last name:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e',
                                   justify='center'
                                   )
                    last.place(x=200, y=4)
                    
                    last_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=12)
                    last_entry.place(x=190, y=35)
                    last_entry.insert(0, values[2])
                          
                    age = tk.Label(editlabelframe,
                                   text='Age:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e',
                                   justify='center'
                                   )
                    age.place(x=420, y=5)
                    
                    age_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=12)
                    age_entry.place(x=370, y=35)
                    age_entry.insert(0, values[3])
                    
                            
                    ID = tk.Label(editlabelframe,
                                   text='your ID:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e',
                                   justify='left'
                                   )
                    ID.place(x=36, y=90)
                    
                    ID_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=12)
                    ID_entry.place(x=10, y=125)
                    ID_entry.insert(0,values[4])

                    number= tk.Label(editlabelframe, text='Number:',
                                      font=('Times New Roman Bold',18),
                                      fg='#02319e')
                    number.place(x=10, y=200)
                    
                    number_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=33)
                    number_entry.place(x=140, y=200)
                    number_entry.insert(0, values[5])
                    
                    email= tk.Label(editlabelframe, text='Email:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e')
                    email.place(x=10, y=275)
                    
                    email_entry = tk.Entry(editlabelframe,
                                         font=('Times New Roman',18),
                                         fg='#02319e',
                                         width=33)
                    email_entry.place(x=140, y=275)
                    email_entry.insert(0,values[6])
                    
                    def saving():
                        naameenter=name_entry.get().strip()
                        lastenter=last_entry.get().strip()
                        ageenter=age_entry.get().strip()
                        IDenter=ID_entry.get().strip()
                        numberenter= number_entry.get().strip()
                        emailenter= email_entry.get().strip()
                        if not naameenter:
                            messagebox.showwarning(title="Warning", message="First name entry is empty!")
                            return
                        elif not lastenter:
                            messagebox.showwarning(title="Warning",message="Last name entry is empty!")
                            return
                        elif not ageenter:
                            messagebox.showwarning(title="Warning",message="Age entry is empty!")
                            return
                        elif not ageenter.isdigit() or int(ageenter) <= 0:
                             messagebox.showwarning(title="Warning",message="Please enter a valid positive number for age!")
                             return
                        elif not IDenter:
                            messagebox.showwarning(title="Warning",message="ID entry is empty!")
                            return
                        elif not numberenter:
                            messagebox.showwarning(title="Warning",message="Phone number entry is empty!")
                            return
                        elif not numberenter.isdigit() or int(numberenter) <= 0: 
                            messagebox.showwarning(title="Warning",message="Please enter a valid positive number for phone!")
                            return
                            
                        result= hdata.update_customer(customerid, naameenter, lastenter, ageenter, IDenter, numberenter, emailenter) 
                        
                        if result: 
                            newval = list(values) 
                            newval[1] = naameenter
                            newval[2] = lastenter
                            newval[3] = ageenter
                            newval[4] = IDenter
                            newval[5] = numberenter
                            newval[6] = emailenter

                            guesttree.item( select[0], values=newval)

                            editwndw.destroy()

                            messagebox.showinfo(title="Success",messagebox="Customer information updated successfully.")

                        else: 
                           messagebox.showerror(title="Error",message="Could not update customer information.")
                            
                        
                    savebtn = tk.Button(editwndw,text="Save Changes",
                                            font=('Times New Roman Bold', 18),
                                            bg='light blue', 
                                            fg='#02319e', 
                                            command=saving) 
                    savebtn.place(x=250,y=400)
                
                #---------------------------------------------
                    
                def delete(): 
                     select= guesttree.selection()

                     if not select: 
                         messagebox.showwarning(title="Warning",message="Please select a customer first.") 
                         return 
                     values = guesttree.item(select[0], 'values')
                     customer_id = values[0]

                     confirm = messagebox.askyesno(title="Confirm Delete", message=f"Are you sure you want to delete customer {customer_id}?")

                     if not confirm: 
                         return 
                     result = hdata.delete_customer(customer_id) 
                     if result:
                         guesttree.delete(select[0])

                         messagebox.showinfo(title="Success",message= f"Customer {customer_id} deleted successfully.")
                     else: 
                         messagebox.showerror(title="Error",message="Could not delete the customer.")
               #-------------------------------------------------------
               
                
                deletebtn= tk.Button(epanel, text='Delete customer',
                                     font=('Times New Roman Bold', 18), 
                                     bg='light blue', 
                                     fg='#02319e', 
                                     width=15, 
                                     command=delete)
                deletebtn.place(x=450, y=450)
                
                editbtn= tk.Button(epanel, text='Edit customer', 
                                   font=('Times New Roman Bold', 18), 
                                   bg='light blue', 
                                   fg='#02319e', 
                                   width=15,
                                   command= customer_edit)
                editbtn.place(x=100, y=450)
                   
               
                
      
            elif username=='hasti' and password=='1234':
                self.managerwndw= tk.Toplevel(self.loginwindow)
                self.managerwndw.title('Manager panel')
                self.managerwndw.geometry('800x600')
                
                # welcomem= tk.Label(self.managerwndw,
                #                    text=f'welcome, Miss/ Mrs {username}',
                #                    font=('Time New Roman', 20)
                #                    )
                # welcomem.place(x=50,y=20)
                tabcontrol=ttk.Notebook(self.managerwndw)
                tab1= ttk.Frame(tabcontrol)
                tab2=ttk.Frame(tabcontrol)
                
                tabcontrol.add(tab1, text='Customer managment')
                tabcontrol.add(tab2, text='hotel management')
                tabcontrol.pack(expand = 1, fill ="both")
#=========================================================
                #customer
                
                custompanel= tk.LabelFrame(tab1,text= 'guest manager panel')
                custompanel.place(x=25, y=10, width=750, height=550)
                
                search = tk.Label(custompanel,
                                  text='Search:',
                                  font=('Times New Roman Bold', 14),
                                  fg='#02319e')
                search.place(x=35, y=10)

                search_entry = tk.Entry(custompanel,
                                        font=('Times New Roman', 14),
                                        bg='white',
                                        fg='black',
                                        width=25)
                search_entry.place(x=110, y=10)
                
                                
              
                columns=('customer_id', 'first_name', 'last_name', 'age', 'id', 'phone', 'email','room_number', 'room_type','days', 'booking_date')
                
                guesttree = ttk.Treeview(custompanel,columns=columns, show='headings', selectmode='browse')  
                guesttree.place(x=35, y=40, width=680, height=380)
                
                
                guesttree.column('#0', width=0, stretch=tk.NO)  
                guesttree.column('customer_id', width=100, anchor=tk.CENTER)
                guesttree.column('first_name', width=100, anchor=tk.W)
                guesttree.column('last_name', width=100, anchor=tk.W)
                guesttree.column('age', width=50, anchor=tk.CENTER)
                guesttree.column('id', width=100, anchor=tk.CENTER)
                guesttree.column('phone', width=120, anchor=tk.W)
                guesttree.column('email', width=150, anchor=tk.W)
                guesttree.column('room_number', width=90, anchor=tk.CENTER)
                guesttree.column('room_type', width=80, anchor=tk.CENTER)
                guesttree.column('days', width=120, anchor=tk.CENTER)
                guesttree.column('booking_date', width=150, anchor=tk.CENTER)


                guesttree.heading('#0', text='')
                guesttree.heading('customer_id',text='Customer ID')
                guesttree.heading('first_name', text='Name')
                guesttree.heading('last_name', text='Last')
                guesttree.heading('age', text='Age')
                guesttree.heading('id', text='ID')
                guesttree.heading('phone', text='Phone number')
                guesttree.heading('email', text='Email')
                guesttree.heading('room_number', text='Room number')
                guesttree.heading('room_type', text='Room type')
                guesttree.heading('days', text='reservation days')
                guesttree.heading('booking_date', text='booking date')
                
                customers = hdata.get_customers()
                
                
                for i in customers: 
                    guesttree.insert('', tk.END, values=i)
                def searchcustom(event=None):
                    searchtxt= search_entry.get().strip().lower()
                    
                    for item in guesttree.get_children(): 
                        guesttree.delete(item)
                        
                    for customer in customers: 
                        
                        if not searchtxt:
                            guesttree.insert('', tk.END, values=customer) 
                        elif any(searchtxt in str(value).lower() for value in customer): 
                            guesttree.insert('', tk.END, values=customer)


                search_entry.bind('<KeyRelease>', searchcustom)
    
                scrollbar_y = ttk.Scrollbar(custompanel, orient='vertical',command=guesttree.yview) 
                scrollbar_y.place(x=715, y=40, height=380) 
                guesttree.configure(yscrollcommand=scrollbar_y.set) 
               
                scrollbar_x = ttk.Scrollbar(custompanel, orient='horizontal', command=guesttree.xview) 
                scrollbar_x.place(x=35,y=420,width=680) 
                guesttree.configure(xscrollcommand=scrollbar_x.set)
                #--------------------------------------------------------
                
                def customer_edit():
                    select = guesttree.selection()
                    
                    if not select: 
                        messagebox.showwarning(title="Warning",message="Select a customer first.")
                        return
                    values = guesttree.item(select[0], 'values')
                    customerid= values[0]
                    
                    editwndw=tk.Toplevel(custompanel)
                    editwndw.title("Edit Customer panel")
                    editwndw.geometry("640x570")
                    
                    editframe= tk.Frame(editwndw)
                    editframe.pack(fill='both', expand=True)
                    
                    editlabelframe= tk.LabelFrame(editframe,text= 'Edit customer info')
                    editlabelframe.place(x=20, y=20, width=600, height=530)
                    
                    
                    name = tk.Label(editlabelframe,
                                    text='first name:',
                                    font=('Times New Roman Bold',18),
                                    fg='#02319e',
                                    justify='center'
                                    )
                    name.place(x=20, y=4)
                    
                    name_entry= tk.Entry(editlabelframe, 
                                     font=('Times New Roman',18),
                                     fg='#02319e',
                                     width=12)
                    name_entry.place(x=5, y=34)
                    name_entry.insert(0, values[1])

                    last= tk.Label(editlabelframe,
                                   text='Last name:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e',
                                   justify='center'
                                   )
                    last.place(x=204, y=4)
                    
                    last_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=12)
                    last_entry.place(x=190, y=35)
                    last_entry.insert(0, values[2])
                          
                    age = tk.Label(editlabelframe,
                                   text='Age:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e',
                                   justify='center'
                                   )
                    age.place(x=420, y=5)
                    
                    age_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=12)
                    age_entry.place(x=370, y=35)
                    age_entry.insert(0, values[3])
                    
                            
                    ID = tk.Label(editlabelframe,
                                   text='your ID:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e',
                                   justify='left'
                                   )
                    ID.place(x=35, y=90)
                    
                    ID_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=12)
                    ID_entry.place(x=10, y=125)
                    ID_entry.insert(0,values[4])

                    number= tk.Label(editlabelframe, text='Number:',
                                      font=('Times New Roman Bold',18),
                                      fg='#02319e')
                    number.place(x=10, y=200)
                    
                    number_entry = tk.Entry(editlabelframe,
                    font=('Times New Roman',18),
                    fg='#02319e',
                    width=33)
                    number_entry.place(x=140, y=200)
                    number_entry.insert(0, values[5])
                    
                    email= tk.Label(editlabelframe, text='Email:',
                                   font=('Times New Roman Bold',18),
                                   fg='#02319e')
                    email.place(x=10, y=275)
                    
                    email_entry = tk.Entry(editlabelframe,
                                         font=('Times New Roman',18),
                                         fg='#02319e',
                                         width=33)
                    email_entry.place(x=140, y=275)
                    email_entry.insert(0,values[6])
                    
                    def saving():
                        naameenter=name_entry.get().strip()
                        lastenter=last_entry.get().strip()
                        ageenter=age_entry.get().strip()
                        IDenter=ID_entry.get().strip()
                        numberenter= number_entry.get().strip()
                        emailenter= email_entry.get().strip()
                        if not naameenter:
                            messagebox.showwarning(title="Warning", message="First name entry is empty!")
                            return
                        elif not lastenter:
                            messagebox.showwarning(title="Warning",message="Last name entry is empty!")
                            return
                        elif not ageenter:
                            messagebox.showwarning(title="Warning",message="Age entry is empty!")
                            return
                        elif not ageenter.isdigit() or int(ageenter) <= 0:
                             messagebox.showwarning(title="Warning",message="Please enter a valid positive number for age!")
                             return
                        elif not IDenter:
                            messagebox.showwarning(title="Warning",message="ID entry is empty!")
                            return
                        elif not numberenter:
                            messagebox.showwarning(title="Warning",message="Phone number entry is empty!")
                            return
                        elif not numberenter.isdigit() or int(numberenter) <= 0: 
                            messagebox.showwarning(title="Warning",message="Please enter a valid positive number for phone!")
                            return
                            
                        result= hdata.update_customer(customerid, naameenter, lastenter, ageenter, IDenter, numberenter, emailenter) 
                        
                        if result: 
                            newval = list(values) 
                            newval[1] = naameenter
                            newval[2] = lastenter
                            newval[3] = ageenter
                            newval[4] = IDenter
                            newval[5] = numberenter
                            newval[6] = emailenter

                            guesttree.item( select[0], values=newval)

                            editwndw.destroy()

                            messagebox.showinfo(title="Success",messagebox="Customer information updated successfully.")

                        else: 
                           messagebox.showerror(title="Error",message="Could not update customer information.")
                            
                        
                    savebtn = tk.Button(editwndw,text="Save Changes",
                                            font=('Times New Roman Bold', 18),
                                            bg='light blue', 
                                            fg='#02319e', 
                                            activebackground='#0050D1',
                                            activeforeground='light blue',
                                            command=saving) 
                    savebtn.place(x=250,y=400)
                
                #---------------------------------------------
                    
                def delete(): 
                     select= guesttree.selection()

                     if not select: 
                         messagebox.showwarning(title="Warning",message="Please select a customer first.") 
                         return 
                     values = guesttree.item(select[0], 'values')
                     customer_id = values[0]

                     confirm = messagebox.askyesno(title="Confirm Delete", message=f"Are you sure you want to delete customer {customer_id}?")

                     if not confirm: 
                         return 
                     result = hdata.delete_customer(customer_id) 
                     if result:
                         guesttree.delete(select[0])

                         messagebox.showinfo(title="Success",message= f"Customer {customer_id} deleted successfully.")
                     else: 
                         messagebox.showerror(title="Error",message="Could not delete the customer.")
               #-------------------------------------------------------
               
                
                deletebtn= tk.Button(custompanel, text='Delete customer',
                                     font=('Times New Roman Bold', 18), 
                                     bg='light blue', 
                                     fg='#02319e', 
                                     activebackground='#0050D1',
                                     activeforeground='light blue',
                                     width=15, 
                                     command=delete)
                deletebtn.place(x=450, y=450)
                
                editbtn= tk.Button(custompanel, text='Edit customer', 
                                   font=('Times New Roman Bold', 18), 
                                   bg='light blue', 
                                   fg='#02319e', 
                                   activebackground='#0050D1',
                                   activeforeground='light blue',
                                   width=15,
                                   command= customer_edit)
                editbtn.place(x=100, y=450)          
#======================================================                
                #hotel
                hotelpanel= tk.LabelFrame(tab2, text='Hotel managment panel')
                hotelpanel.place(x=5, y=5, width=950, height=650)
                
                search = tk.Label(hotelpanel,text='Search:',
                                  font=('Times New Roman Bold', 14),
                                  fg='#02319e')
                search.place(x=35, y=10)

                search_entry = tk.Entry(hotelpanel,
                                        font=('Times New Roman', 14),
                                        bg='white',
                                        fg='black',
                                        width=25)
                search_entry.place(x=110, y=10)
                
                hottree= ttk.Treeview(hotelpanel, selectmode= 'browse')
                hottree['columns']=('room_number', 'room_type','price', 'capacity', 'status', 'description')
                 
                hottree.column('#0', width=0, stretch=tk.NO)
                hottree.column('room_number', width=90, anchor=tk.CENTER)
                hottree.column('room_type', width=60, anchor=tk.CENTER)
                hottree.column('price', width=90, anchor=tk.E)
                hottree.column('capacity', width=80, anchor=tk.CENTER)
                hottree.column('status', width=80, anchor=tk.CENTER)
                hottree.column('description', width=130, anchor=tk.W)
                
                hottree.heading('#0', text='')
                hottree.heading('room_number', text='room number')
                hottree.heading('room_type', text='type')
                hottree.heading('price', text='price per night')
                hottree.heading('capacity', text='capacity')
                hottree.heading('status', text='status')
                hottree.heading('description', text='description')

                hot_scrollbar_y = ttk.Scrollbar(hotelpanel,
                                                orient='vertical',
                                                command=hottree.yview)

                hottree.place(x=35, y=40, width=680, height=380)
                hot_scrollbar_y.place(x=715, y=40, height=380)

                hottree.configure(yscrollcommand=hot_scrollbar_y.set)
                
                hotrooms= hdata.hoteldata()
                
                def load_rooms(): 
                    for item in hottree.get_children(): 
                        hottree.delete(item) 
                        
                    rooms = hdata.hoteldata()

                    for room in rooms: 
                        hottree.insert('', tk.END, values=(
                                       room[1],
                                       room[2],
                                       f"{room[3]:,}",
                                       room[4],
                                       room[5],
                                       room[6]))


                load_rooms()
                
                def searchroom(event=None):
                    searchtxt= search_entry.get().strip().lower()
                    
                    for item in hottree.get_children(): 
                        hottree.delete(item)
                    rooms = hdata.hoteldata()
                        
                    for room in rooms:             
                        if not searchtxt:
                            hottree.insert('', tk.END, values=(room[1],
                                                               room[2],
                                                               f"{room[3]:,}",
                                                               room[4],
                                                               room[5],
                                                               room[6])) 
                        elif any(searchtxt in str(value).lower() for value in room): 
                            hottree.insert('', tk.END, values=(room[1],
                                                               room[2],
                                                               f"{room[3]:,}",
                                                               room[4],
                                                               room[5],
                                                               room[6]))
                search_entry.bind('<KeyRelease>', searchroom)
                
                
                def addroom():
                    
                    addwndw= tk.Toplevel(self.managerwndw)
                    addwndw.title("Add New Room")
                    addwndw.geometry("500x500")
                    
                    add = tk.LabelFrame(addwndw, text="New room information")
                    add.place( x=20,y=20,width=460,height=450)
                    
                    roomnum=tk.Label(add,text="Room number:",
                                     font=('Times New Roman', 16))
                    roomnum.place(x=20, y=25) 
                    roomnum_entry = tk.Entry(add, 
                                             font=('Times New Roman', 16), 
                                             width=20)
                    roomnum_entry.place(x=180, y=25)
                    
                    rtype= tk.Label(add, text="Room type:", 
                             font=('Times New Roman', 16))
                    rtype.place(x=20, y=80) 
                    typecombo = ttk.Combobox(add,
                                             values=('1bed','2beds','Suite','VIP'), 
                                             state='readonly',
                                             font=('Times New Roman', 14),
                                             width=18) 
                    typecombo.place(x=180, y=80) 
                    typecombo.current(0)
                    
                    price= tk.Label( add, text="Price/night:",
                                     font=('Times New Roman', 16))
                    price.place(x=20, y=135) 
                    price_entry = tk.Entry(add,
                                           font=('Times New Roman', 16),
                                           width=20)

                    price_entry.place(x=180, y=135)
                    
                    capacity= tk.Label(add,text="Capacity:", 
                                       font=('Times New Roman', 16)) 
                    capacity.place(x=20, y=190)

                    capacity_entry = tk.Entry(add, 
                                              font=('Times New Roman', 16), 
                                              width=20)

                    capacity_entry.place(x=180, y=190)
                    
                    desc= tk.Label(add,text="Description:",
                                   font=('Times New Roman', 16))
                    desc.place(x=20, y=245)

                    desc_entry = tk.Entry(add,
                                                 font=('Times New Roman', 16), 
                                                 width=20)

                    desc_entry.place(x=180, y=245)
                    def saveroom():
                        sroomnum= roomnum_entry.get().strip()
                        stypecombo= typecombo.get().strip()
                        sprice= price_entry.get().strip()
                        scapacity= capacity_entry.get().strip()
                        sdesc=desc_entry.get().strip()
                    
                        if not sroomnum: 
                            messagebox.showwarning(title="Warning",message="Please enter the room number.")
                            return
                     
                        if not stypecombo: 
                            messagebox.showwarning(title="Warning",message="Please select a room type first.")
                            return
                        if not sprice: 
                            messagebox.showwarning(title="Warning",message="Please enter the price.")
                            return
                        if not scapacity: 
                            messagebox.showwarning(title="Warning",message="Please select the room's capacity.")
                            return
                        if not sdesc: 
                            messagebox.showwarning(title="Warning",message="Please swrite a description for the room.")
                            return
                        try:
                            capacity_value = int(scapacity)
                            if capacity_value <=0:
                                raise ValueError
                        except ValueError: 
                            messagebox.showwarning(title="Warning", message="Please enter a valid positive capacity.")
                            return
                        result = hdata.add_room(sroomnum, stypecombo, sprice, scapacity, sdesc)
                    
                        if result:
                            load_rooms()
                            messagebox.showinfo(title="Success",message="Room added successfully.")
                            addwndw.destroy()
                        else:
                            messagebox.showerror(title="Error",message="Could not add room or Room already exist.")
                    addroom= tk.Button(addwndw,text='add room',
                                       font=('Times New Roman Bold', 16), 
                                       bg='light blue', 
                                       fg='#02319e',
                                       activebackground='#0050D1',
                                       activeforeground='light blue',
                                       width=15, 
                                       command=saveroom)
                    addroom.place(x=150, y=340)
#-------------------------------------------  
                def editroom():
                    
                    select= hottree.selection()
                    if not select:
                        messagebox.showwarning(title="Warning",message="Please select a room first.")
                        return
                    
                    values = hottree.item(select[0],'values')
                    oldroomnum= values[0]
                    
                    editwndw= tk.Toplevel(self.managerwndw)
                    editwndw.title("Add New Room")
                    editwndw.geometry("500x500")
                    
                    edit = tk.LabelFrame(editwndw, text="New room information")
                    edit.place( x=20,y=20,width=460,height=450)
                    
                    roomnum=tk.Label(edit,text="Room number:",
                                     font=('Times New Roman', 16))
                    roomnum.place(x=20, y=25) 
                    roomnum_entry = tk.Entry(edit, 
                                             font=('Times New Roman', 16), 
                                             width=20)
                    roomnum_entry.place(x=180, y=25)
                    roomnum_entry.insert(0, values[0])
                    
                    rtype= tk.Label(edit, text="Room type:", 
                             font=('Times New Roman', 16))
                    rtype.place(x=20, y=80) 
                    typecombo = ttk.Combobox(edit,
                                             values=('1bed','2beds','Suite','VIP'), 
                                             state='readonly',
                                             font=('Times New Roman', 14),
                                             width=18) 
                    typecombo.place(x=180, y=80) 
                    typecombo.set(values[1])
                    
                    price= tk.Label( edit, text="Price/night:",
                                     font=('Times New Roman', 16))
                    price.place(x=20, y=135) 
                    price_entry = tk.Entry(edit,
                                           font=('Times New Roman', 16),
                                           width=20)
                    price_entry.place(x=180, y=135)
                    price_entry.insert(0,values[2])
                    
                    capacity= tk.Label(edit,text="Capacity:", 
                                       font=('Times New Roman', 16)) 
                    capacity.place(x=20, y=190)

                    capacity_entry = tk.Entry(edit, 
                                              font=('Times New Roman', 16), 
                                              width=20)

                    capacity_entry.place(x=180, y=190)
                    capacity_entry.insert(0,values[3])
                    
                    desc= tk.Label(edit,text="Description:",
                                   font=('Times New Roman', 16))
                    desc.place(x=20, y=245)

                    desc_entry = tk.Entry(edit,
                                          font=('Times New Roman', 16), 
                                          width=20)

                    desc_entry.place(x=180, y=245)
                    desc_entry.insert(0,values[5])
                    
                    def saving():
                        sroomnum= roomnum_entry.get().strip()
                        stypecombo= typecombo.get().strip()
                        sprice= price_entry.get().strip()
                        scapacity= capacity_entry.get().strip()
                        sdesc=desc_entry.get().strip()
                    
                        if not sroomnum: 
                            messagebox.showwarning(title="Warning",message= "the room number cannot be empty.")
                            return
                     
                        if not stypecombo: 
                            messagebox.showwarning(title="Warning",message="Please select a room type first.")
                            return
                        if not sprice: 
                            messagebox.showwarning(title="Warning",message="Please enter the price.")
                            return
                        if not scapacity: 
                            messagebox.showwarning(title="Warning",message="Please select the room's capacity.")
                            return
                        if not sdesc: 
                            messagebox.showwarning(title="Warning",message="Please swrite a description for the room.")
                            return
                        try:
                            capacity_value = int(scapacity)
                            if capacity_value <=0:
                                raise ValueError
                        except ValueError: 
                            messagebox.showwarning(title="Warning", message="Please enter a valid positive capacity.")
                            return
                        result = hdata.update_room(sroomnum, stypecombo, sprice, scapacity, sdesc)
                        if result:
                            load_rooms()
                            messagebox.showinfo(title="Success",message="Room added successfully.")
                            editwndw.destroy()
                        else:
                            messagebox.showerror(title="Error",message="Could not add room or Room already exist.")
                            
                    editroom= tk.Button(editwndw,text='finalize the edit',
                                       font=('Times New Roman Bold', 16), 
                                       bg='light blue', 
                                       fg='#02319e',
                                       activebackground='#0050D1',
                                       activeforeground='light blue',
                                       width=15, 
                                       command=saving)
                    editroom.place(x=150, y=340)
#-------------------------------------------------
                def deleteroom():
                    select= hottree.selection()
                    if not select:
                        messagebox.showwarning(title="Warning",message="Please select a room first.")
                        return
                    
                    values = hottree.item(select[0],'values')
                    room_number = values[0]
                    status = values[4]
                    
                    if status != 'Available':
                        messagebox.showwarning(title="Warning",message="This room is currently booked and cannot be deleted.")
                        return
                    confirm=messagebox.askyesno(title='delete confirm',message=f"Wait! Are you sure you want to delete room {room_number}?")
                    if not confirm:
                        return
                    result = hdata.delete_room(room_number) 
                    if result:
                        load_rooms() 
                        messagebox.showinfo(title="Success",message=f"The Room deleted successfully.")
                        
                    else: 
                        messagebox.showerror(title="Error",message="Error!Could not delete the room.")


                    
                            
                    
                
#=============================================
                addbtn = tk.Button(hotelpanel,text='Add Room',
                                   font=('Times New Roman Bold', 16), 
                                   bg='light blue',
                                   fg='#02319e',
                                   activebackground='#0050D1',
                                   activeforeground='light blue',
                                   width=15,
                                   command=addroom)

                addbtn.place(x=60,y=450)
                
                editbtn = tk.Button(hotelpanel,text='Edit Room',
                                   font=('Times New Roman Bold', 16), 
                                   bg='light blue',
                                   fg='#02319e',
                                   activebackground='#0050D1',
                                   activeforeground='light blue',
                                   width=15,
                                   command=editroom)
                editbtn.place(x=270,y=450)
                
                deletebtn = tk.Button(hotelpanel,text='Delete Room',
                                      font=('Times New Roman Bold', 16),
                                      bg='light blue',
                                      fg='#02319e',
                                      activebackground='#0050D1',
                                      activeforeground='light blue',
                                      width=15,
                                      command=deleteroom)

                deletebtn.place(x=480,y=450)
                
            else:
                messagebox.showwarning(title='warning',message='The password is incorrect.')

    
                    
                
                    


                
                
        
        loginbtn= tk.Button(self.loginwindow, text='login',
                            font=('Times New Roman Bold', 16), 
                            bg='light blue',
                            fg='#02319e',
                            width= 10 ,
                            command= loginwndw
                            )
        loginbtn.place(x=280, y=300)
        
        

main_window.geometry('1000x600')
main_window.title('Khazar hotel application')
main_window.configure(bg='light blue')
#main_window.iconphoto(True, icon)

#------------------------------------------

blank= tk.Frame(main_window,
                 bg='#0050D1',
                 width=1000, height=42
                )
blank.place(x=0)


wave= tk.Label(main_window, text='🌊',
               font=('Times New Roman Bold',60),
               bg='light blue',
               fg='#0050D1')
wave.place(x=450,y=42)

stars=tk.Label(main_window, text='★  ★  ★  ★  ★',
               font=('Times New Roman Bold',30),
               bg='light blue',
               fg='orange')
stars.place(x=360,y=135)

greet= tk.Label(main_window,
                text= 'Hello! Welcome to The Khazar Hotel \n ! Thank you for choosing us.',
                font=('Times New Roman Bold',24),
                bg='light blue',
                fg='#0050D1',
                )
greet.place(x=240,y=200)

detail= tk.Label(main_window,
                 text='A 5-star hotel designed for safety and comfort \nPress "book-in" to book a hotel room',
                 font=('Times New Roman',22),
                 bg='light blue',
                 fg='#02319e',
                 justify='left'
                 )
detail.place(x=5,y=300)
 
#---------------------------------

bookbutton= tk.Button(main_window,
                      text='book-in =>',
                      font=('Times New Roman Bold',24),
                      bg='#0050D1',
                      fg='light blue',
                      activebackground='light blue',
                      activeforeground='#0050D1',
                      height=2,
                      bd=6 ,
                      relief='groove',
                      command=book)
bookbutton.place(x=40,y=390)

logbutton= tk.Button(main_window,
                      text='log in as employee / manager',
                      font=('Times New Roman Bold',12),
                      bg='#0050D1',
                      fg='light blue',
                      activebackground='light blue',
                      activeforeground='#0050D1',
                      height=1,
                      bd=6 ,
                      relief='groove',
                      command=login)
logbutton.place(x=760,y=0)
main_window.mainloop()

