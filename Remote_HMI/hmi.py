import tkinter as tk
import ttkbootstrap as ttk
from tkinter import OptionMenu
import time
from pylogix import PLC
import data as dt


def click_tag(command):
    command_ind = dt.commands[command]
    selected_MCP_ip_address = dt.ip_address[clicked.get()][0]
    tag_name = dt.ip_address[clicked.get()][command_ind]
    print(clicked.get())
    print("Ip_address: " ,selected_MCP_ip_address)
    print("Tagname: ", tag_name)

    with PLC() as comm:
        comm.IPAddress = selected_MCP_ip_address
        comm.Write(tag=tag_name,value=1)
        time.sleep(1)
        comm.Write(tag=tag_name,value=0)
        current_tag_val = comm.Read(tag_name).Value
        print("current_tag_val: ",current_tag_val)


def remote_start():
    click_tag('start')
    print('start_executed\n')


def remote_stop():
    click_tag('stop')
    print('stop_executed\n')


def motor_fault_reset():
    click_tag('fautl_reset')
    print('fault reset executed\n')


def jam_reset(self):
    click_tag('jam_reset')
    print("Jam_reset\n")




#window
window = ttk.Window()
window.title('Control Panel remote access')
window.geometry('600x500')


# Frame
ip_frame = ttk.Frame(master=window)
ip_frame_buttons = ttk.Frame(master=window)

title_label = ttk.Label(master=ip_frame, text='MCP Panel', font = 'Calibri 24 bold')



# select_mcp in dropdown
# dropdown_button
options = dt.drop_down_options
clicked = tk.StringVar()
clicked.set("Select MCP")
drop = OptionMenu(ip_frame, clicked, *options)


# Buttons
style = ttk.Style()
style.configure('start_Button', foreground ='white', backgroun='green')


start_pb = ttk.Button(master=ip_frame_buttons, text="Start", command=remote_start)
stop_pb = ttk.Button(master=ip_frame_buttons, text="Stop", command=remote_stop)
fault_reset = ttk.Button(master=ip_frame_buttons, text="Fault_reset", command=motor_fault_reset)
jam_reset_pb = ttk.Button(master=ip_frame_buttons, text="Jam_reset", command=jam_reset)

ip_frame.pack()
ip_frame_buttons.pack()
title_label.pack()
drop.pack()

start_pb.pack(side='left')
stop_pb.pack(side='left',padx=5,pady=5)
fault_reset.pack(side='left',padx=5, pady=5)
jam_reset_pb.pack(side='left')

window.mainloop()