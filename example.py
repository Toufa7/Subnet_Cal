import tkinter
import customtkinter
import masks
import subnet_cal

customtkinter.set_appearance_mode("light")




np = customtkinter.CTk()
np.geometry("720x480")
np.resizable(0,0)
np.title("NetPractice")

mode = customtkinter.StringVar(value="light")

def button_callback():
    print("IP", entry_1.get())
    print("Mask", subnet_mask.get())

frame_1 = customtkinter.CTkFrame(master=np)
frame_1.grid(row=5, column=1, columnspan=1, ipady=60, ipadx=10, padx= 10, pady=10, sticky="")
# frame_1.pack(pady=50, padx=50, fill="both", expand=True)








# frame_right = customtkinter.CTkFrame(master=np)
# frame_right.grid(row=0, column=1, sticky="nswe", ipadx=60, padx=50)


# frame_info = customtkinter.CTkFrame(master=np)
# frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, ipadx = 50, ipady= 20, sticky="nswe")


entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="      Network Address Block", width=200, height=30)
entry_1.pack(pady=60, padx=30)

button_1 = customtkinter.CTkButton(master=frame_1,text="Subnet Details",command=button_callback)
button_1.pack(pady=80, padx=30)

lst = list(masks.subnet_masks)
subnet_mask = customtkinter.CTkOptionMenu(frame_1, values=lst)
subnet_mask.set("---- Select Subnet Mask ----")
subnet_mask.pack(pady=12, padx=150)
subnet_mask.place(x=30, y=150)

def theme():
    customtkinter.set_appearance_mode(mode.get())

dark_mode = customtkinter.CTkSwitch(master=frame_1,text="Dark Mode",variable = mode, command=theme, onvalue="dark", offvalue="light")
dark_mode.pack(pady=90, padx=300)
dark_mode.place(x=90, y=300)


np.bind("<Escape>", lambda exit : np.destroy())

np.mainloop()