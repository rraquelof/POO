
from customtkinter import *
from tkintermapview import TkinterMapView
from tkinter import Listbox
#import geocoder

class Map:
    set_appearance_mode("Light")
    def __init__(self):
        #self.local = geocoder.ip('me')
        
        self.lista=["Malta","Brasil","New York","China","Japan","Cajazeiras","Bangladesh"]
        self.lista2=[]


        self.window=CTk()
        self.window.geometry("900x520")
        self.window.title("GEOLOCALIZATION")
        self.font_sans=("Calibri",15)
        self.frame()
        self.change_frame_page1()
        #self.map_background()
        self.label()
        self.map_background()
        self.entry()
        self.buttons_frame1()
        self.window.mainloop()


    def get_button(self,btn):
        if btn=="find":
            self.change_frame_page2()
            address_find=entry_address.get()
            map_find=TkinterMapView(self.frame_page2, width=900,height=550)
            map_find.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
            
            marker_1 = map_find.set_address("colosseo, rome, italy", marker=True)  #self.local.city
            marker_2=map_find.set_address("Berlin,Germany", marker=True)        #address_find
            print(marker_1.position, marker_2.position)  # get position 
            
            marker_1.set_text("Colosseo in Rome")   #self.local.city
            marker_2.set_text("Berlin Germany")   #adress_find
            path_1 = map_find.set_path([marker_1.position, marker_2.position])

           
            map_find.pack(fill='both',expand=True)
            self.buttons_frame2()
            btn_back.place(x=720,y=20)

        elif btn=="back":
            self.change_frame_page1()
             
            
        elif btn=="save":
            count=0
            #text_label=getattr(label_saved,'text')
            #text=Text(label_saved,width=80, height=15)
            #label_saved.configure(text=self.lista)
            list_box=Listbox(label_saved,relief=None,bg='#CECECF',selectbackground='#BFBEBF',bd=0,font=self.font_sans,highlightthickness = 0)
            address_save=entry_save.get()
            self.lista2.append(address_save)
            if self.lista2:
                for address in self.lista2:
                    list_box.insert(count,address)
                    count+=1

                list_box.place(x=30,y=40)
            #text.place()
            
            print("executou")


    def frame(self):
        self.frame_page1=CTkFrame(master=self.window,width=900,height=520)   #.place(relx=0.5, rely=0.5, anchor="center")
        self.frame_page2=CTkFrame(master=self.window,width=900,height=520)
       


    #CHANGES BETWEEN PAGES (FRAMES)
    def change_frame_page2(self):
        self.frame_page2.pack(fill='both',expand=True)
        self.frame_page1.pack_forget()

    def change_frame_page1(self):
        self.frame_page1.pack(fill='both',expand=True)
        self.frame_page2.pack_forget()

    def map_background(self):
        map_widget = TkinterMapView(label_map, width=500, height=300,corner_radius=10)
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
        map_widget.place(relx=0.5, rely=0.5, anchor="center")

    def label(self):
        global label_map,label_saved

        #creating labels
       

        #label_bottom=CTkLabel(master=self.frame_page1,text=None,fg_color="#E2E2E2", width=900, height=150,corner_radius=20)
        label_map=CTkLabel(master=self.frame_page1,text=None,fg_color="#CECECF", width=550, height=350,corner_radius=20)
            
            
        #label_bottom.place(y=380)
        label_map.place(x=300,y=40)

        if self.lista:
            label_saved=CTkLabel(master=self.frame_page1,text="Favorite Places",fg_color="#CECECF", width=250, height=450,corner_radius=20,text_font=self.font_sans,anchor="w")
          
            label_saved.place(x=30,y=40)
            
     


     


    def entry(self):
        global entry_save,entry_address
        entry_address=CTkEntry(master=self.frame_page1,placeholder_text="Find Address",fg_color="#FEFFFE", border_color="#FEFFFE",corner_radius=10, width=150, height=30,text_color="#262A33")
        entry_save=CTkEntry(master=self.frame_page1,placeholder_text="Save Address",corner_radius=10,fg_color="#FEFFFE", border_color="#FEFFFE", width=150, height=30, text_color="#262A33")

        entry_address.place(x=400, y=420)
        entry_save.place(x=600, y=420)



    def buttons_frame1(self):
        global btn_find,btn_save

        #creating buttons at frame 1
        btn_find=CTkButton(master=self.frame_page1,text="Find Local",width=150,height=30,corner_radius=10,fg_color="#010001",text_color='#F0F1F0',hover_color="#1A1C1D",command=lambda which="find": self.get_button(which))
        btn_save=CTkButton(master=self.frame_page1,text="Save Local",width=150,height=30,corner_radius=10,fg_color="#010001",text_color='#F0F1F0',hover_color="#1A1C1D",command= lambda which="save": self.get_button(which))

        #placing buttons with place()
        btn_find.place(x=400,y=460)
        btn_save.place(x=600,y=460)

    def buttons_frame2(self):
        global btn_back
        btn_back=CTkButton(master=self.frame_page2,text="Back",width=150,height=30,corner_radius=10,fg_color="#010001",text_color='#F0F1F0',hover_color="#1A1C1D", command=lambda which="back":self.get_button(which))

   

map=Map()

    




