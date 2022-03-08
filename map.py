from tkinter import *
from customtkinter import *
from tkintermapview import TkinterMapView



window = Tk()
window.geometry("900x550")
window.title("LOCALIZATION")
font_sans=('Calibri',15)

frame=CTkFrame(master=window,fg_color="blue",width=900, height=550)
frame.place(relx=0.5, rely=0.5, anchor="center")



map_widget = TkinterMapView(window, width=900, height=550)
#map_widget.pack(fill="both")

#map_widget.set_tile_server("http://a.tile.stamen.com/toner/{z}/{x}/{y}.png") 
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  
map_widget.set_address("Berlin Germany", marker=True)

l1=CTkLabel(master=window,text="teste1",fg_color="#121212", width=225, height=250,corner_radius=10,text_font=font_sans,justify="left",anchor="w")
l2=CTkLabel(master=window, text="teste2",fg_color="#121212", width=225, height=250,corner_radius=10,text_font=font_sans,justify="left",anchor="w")
l3=CTkLabel(master=window, text="teste3",fg_color="#121212", width=225, height=250,corner_radius=10,text_font=font_sans,justify="left",anchor="w")


l1.grid(row = 0, column = 0,pady = 100,padx=50,sticky = "w")
l2.grid(row = 0, column = 1, pady = 100, padx=10,sticky = "w")
l3.grid(row=0, column=3,pady=100,padx=50,sticky = "w")



address_localization=StringVar()
address_saved=StringVar()

entry_address=CTkEntry(master=window,placeholder_text="Find Local",fg_color="#FEFFFE", border_color="#FEFFFE",corner_radius=10)
entry_save=CTkEntry(master=window,placeholder_text="Save Local",corner_radius=10)

entry_address.grid(row = 0, column = 1, pady = 100, padx=10,sticky = "w")

map_widget.place(relx=0.5, rely=0.5, anchor="center")





window.mainloop()

