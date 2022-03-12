
from customtkinter import *
from tkintermapview import TkinterMapView
#import geocoder

class Map:
    set_appearance_mode("Light")
    def __init__(self):
        #self.local = geocoder.ip('me')
        
        self.lista=[("Malta"),("Brasil"),("New York"),("China"),("Japan"),("Cajazeiras"),("Bangladesh")]
        self.lista2=[]


        self.window=CTk()
        self.window.geometry("900x520")
        self.window.title("GEOLOCALIZATION")
        self.font_sans=("Calibri",15)
        self.frame()
        self.change_frame_page1()
        self.map_background()
        self.label()
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
            print(marker_1.position, marker_2.position)  # get position and text
            
            marker_1.set_text("Colosseo in Rome")   #self.local.city
            marker_2.set_text("Berlin Germany")   #adress_find
            path_1 = map_find.set_path([marker_1.position, marker_2.position])

           
            map_find.pack(fill='both',expand=True)
            self.buttons_frame2()
            btn_back.place(x=720,y=20)

        elif btn=="back":
            self.change_frame_page1()
             
            
        elif btn=="save":
            address_save=entry_save.get()
            map_save=TkinterMapView(l1,width=190,height=150)
#usar for para a lista de mapas
            map_save.set_address("Malta", marker=True)
#place-> x+=algum numero ai
            map_save.place(x=19,y=20)

    def listagem(self,result):
        for i in range(0, len(result), 3):
            yield result[i:i + 3]


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
        map_widget = TkinterMapView(self.frame_page1, width=900, height=520)
        map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga")
        map_widget.place(relx=0.5, rely=0.5, anchor="center")

    def label(self):
        global l1,l2,l3

        #creating labels
        if self.lista:
            #if self.lista<3:
                #for map in self.lista:
                    #...
            l1=CTkLabel(master=self.frame_page1,text="teste1",fg_color="#010001", width=225, height=250,corner_radius=10,text_font=self.font_sans,justify="left",anchor="w")
            l2=CTkLabel(master=self.frame_page1, text="teste2",fg_color="#010001", width=225, height=250,corner_radius=10,text_font=self.font_sans,justify="left",anchor="w")
            l3=CTkLabel(master=self.frame_page1, text="teste3",fg_color="#010001", width=225, height=250,corner_radius=10,text_font=self.font_sans,justify="left",anchor="w")

            #placing labels with grid()
            l1.grid(row = 0, column = 0,pady = 110,padx=50,sticky = "w")
            l2.grid(row = 0, column = 1, pady = 110, padx=10,sticky = "w")
            l3.grid(row=0, column=3,pady=110,padx=50,sticky = "w")
            
            
            #l1.place(x=50,y=110)
            #l2.place(x=325,y=110)
            #l3.place(x=600,y=110)


        else:
            pass


    def entry(self):
        global entry_save,entry_address
        entry_address=CTkEntry(master=self.frame_page1,placeholder_text="Find Address",fg_color="#FEFFFE", border_color="#FEFFFE",corner_radius=10, width=150, height=30,text_color="#262A33")
        entry_save=CTkEntry(master=self.frame_page1,placeholder_text="Save Address",corner_radius=10,fg_color="#FEFFFE", border_color="#FEFFFE", width=150, height=30, text_color="#262A33")

        entry_address.place(x=275, y=400)
        entry_save.place(x=475, y=400)



    def buttons_frame1(self):
        global btn_find,btn_save

        #creating buttons at frame 1
        btn_find=CTkButton(master=self.frame_page1,text="Find Local",width=150,height=30,corner_radius=10,fg_color="#010001",hover_color="#1A1C1D",command=lambda which="find": self.get_button(which))
        btn_save=CTkButton(master=self.frame_page1,text="Save Local",width=150,height=30,corner_radius=10,fg_color="#010001",hover_color="#1A1C1D",command= lambda which="save": self.get_button(which))

        #placing buttons with place()
        btn_find.place(x=275,y=440)
        btn_save.place(x=475,y=440)

    def buttons_frame2(self):
        global btn_back
        btn_back=CTkButton(master=self.frame_page2,text="Back",width=150,height=30,corner_radius=10,fg_color="#010001",hover_color="#1A1C1D", command=lambda which="back":self.get_button(which))

   

map=Map()

    




