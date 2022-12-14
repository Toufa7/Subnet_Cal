from time import sleep
import tkinter as tk
import tkinter.messagebox as msg
import masks
import subnet_cal

#TODO: 8 Enteries


np = tk.Tk()

np.title ("NetPractice")
np.minsize(800,500)
np.resizable(0,0)
np.iconbitmap("./ressources/la.png")

# root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='C:\\Users\\Pc\\Desktop\\icon.png'))


def     check_errors():
    if (len(ip_add.get()) == 0):
        msg.showerror(title="No Input ⚠️", message="Please Provide The IP Address",icon='warning')
    elif (len(clicked.get()) == 0):
        msg.showinfo(title="No Subnet Mask", message="Select Your Subnet Mask", icon='warning')

def     generate_subnet():
        check_errors()
        ip = str(ip_add.get()) 
        bits  = int(masks.subnet_masks[(clicked.get())])
        output = subnet_cal.subnet_calc(ip, bits)
        hosts_subnet.config(text=output['No. of Hosts/Subnet'])
        nbr_of_subnets.config(text=output['Number of Subnets'])
        host_range_min.config(text=output['min host'])
        host_range_max.config(text=output['max host'])
        broadcast.config(text=output['broadcast'])
        wildcard_mask.config(text=output['Wildcard Mask'])
        cidr_notation.config(text=output['CIDR Notation'])


        # text_entry('1.0', tk.END)
        # text_entry(tk.END, output['host range'])
    


clicked = tk.StringVar(np)


background_image= tk.PhotoImage(file = "./ressources/site42-bg.png")
label = tk.Label(np,image=background_image)
label.place(x=0, y=0)

ip_add_position = tk.Label(np, text="Network Address Block", bg='gray38', fg="#fff")
ip_add_position.place(x=100, y=50)

ip_add = tk.Entry(np, border=2, justify = tk.LEFT)
ip_add.place(x = 300, y = 50)

sub_net_text = tk.Label(np, text="Subnet Mask", bg="gray38", fg="#fff")
sub_net_text.place(x=100, y=100)

# Default input
clicked.set("---- Please Select Subnet Mask ----")
# Drop-down Menu with all subnet masks 
sub_net = tk.OptionMenu(np, clicked, *masks.subnet_masks)
sub_net.place(x = 300, y = 100)


sub_net_position = tk.Label(np, text="Subnet Mask", bg='gray38', fg="#fff")
sub_net_position.place(x=100, y=100)


start = tk.Button(np, border=4 ,text="Subnet Details", bg='LightBlue1', padx=10, pady=5, command=generate_subnet)
start.place(x=300, y=150)


hosts_subnet = tk.Label(np, width=20, height=3, border=4, relief=tk.GROOVE)
hosts_subnet.place(x=40, y=200)

nbr_of_subnets = tk.Label(np, width=20, height=3, border=4,relief=tk.GROOVE)
nbr_of_subnets.place(x= 300 , y = 200)

host_range_min = tk.Label(np, width=20, height=2, border=4,relief=tk.GROOVE)
host_range_min.place(x= 550 , y = 200)


host_range_max = tk.Label(np, width=20, height=2, border=4,relief=tk.GROOVE)
host_range_max.place(x= 550 , y = 245)



broadcast = tk.Label(np, width=20, height=3, border=4,relief=tk.GROOVE)
broadcast.place(x= 40 , y = 350)


wildcard_mask = tk.Label(np, width=20, height=3, border=4,relief=tk.GROOVE)
wildcard_mask.place(x= 300 , y = 350)

cidr_notation = tk.Label(np, width=20, height=5, border=4,relief=tk.GROOVE)
cidr_notation.place(x= 550 , y = 350)

np.mainloop()