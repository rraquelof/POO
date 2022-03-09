from tkinter import *
from customtkinter import *
from tkintermapview import TkinterMapView

#import geocoder

#g = geocoder.ip('me')
#print(g.latlng)
#print(g.city)





window = Tk()
window.geometry("900x550")
window.title("LOCALIZATION")
font_sans=('Calibri',15)




def get_button(btn):
    if btn=="find":
        address_find=entry_address.get()
        map_find=TkinterMapView(window, width=900,height=550)
    elif btn=="save":
        address_save=entry_save.get()
        map_save=TkinterMapView(window,width=190,height=150)
#usar for para a lista de mapas
        map_save.set_address("Malta", marker=True)
#place-> x+=algum numero ai
        map_save.grid(row = 0, column = 0,pady = 130,padx=70,sticky = "w")


frame=CTkFrame(master=window,fg_color="blue",width=900, height=550)
frame.place(relx=0.5, rely=0.5, anchor="center")

map_widget = TkinterMapView(window, width=900, height=550)

#map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png") 
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  
map_widget.set_address("Berlin Germany", marker=True)


l1=CTkLabel(master=window,text="teste1",fg_color="#010001", width=225, height=250,corner_radius=10,text_font=font_sans,justify="left",anchor="w")
l2=CTkLabel(master=window, text="teste2",fg_color="#010001", width=225, height=250,corner_radius=10,text_font=font_sans,justify="left",anchor="w")
l3=CTkLabel(master=window, text="teste3",fg_color="#010001", width=225, height=250,corner_radius=10,text_font=font_sans,justify="left",anchor="w")


l1.grid(row = 0, column = 0,pady = 110,padx=50,sticky = "w")
l2.grid(row = 0, column = 1, pady = 110, padx=10,sticky = "w")
l3.grid(row=0, column=3,pady=110,padx=50,sticky = "w")





#INPUT
entry_address=CTkEntry(master=window,placeholder_text="Find Address",fg_color="#FEFFFE", border_color="#FEFFFE",corner_radius=10, width=150, height=30,text_color="#262A33")
entry_save=CTkEntry(master=window,placeholder_text="Save Address",corner_radius=10,fg_color="#FEFFFE", border_color="#FEFFFE", width=150, height=30, text_color="#262A33")


#BUTTONS
btn_find=CTkButton(master=window,text="Find Local",width=150,height=30,corner_radius=10,border_color="#010001",fg_color="#010001",hover_color="#1A1C1D",command=lambda which="find": get_button(which))
btn_save=CTkButton(master=window,text="Save Local",width=150,height=30,corner_radius=10,border_color="#010001",fg_color="#010001",hover_color="#1A1C1D",command= lambda which="save": get_button(which))

entry_address.place(x=275, y=400)
entry_save.place(x=475, y=400)

btn_find.place(x=275,y=440)
btn_save.place(x=475,y=440)


print(entry_address.get())

map_widget.place(relx=0.5, rely=0.5, anchor="center")



window.mainloop()

