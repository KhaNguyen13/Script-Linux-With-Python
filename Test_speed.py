import speedtest
from tkinter import *

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

st = speedtest.Speedtest()
# print("Download: ", bytes_to_mb(st.download()), "Mb/s")
# print("Upload: ", bytes_to_mb(st.upload()), "Mb/s")

windows = Tk() # Tao cua so gui
windows.title("Title - Speed Test - Kha")
windows.geometry("350x200") # Size gui

# #Thêm label có nội dung Hello, font chữ
down_lable = Label(windows, text=down_lable)
# #Xác định vị trí của label
down_lable.grid(column=0, row=0)

# lbl = Label(windows, text="Hello")
# lbl.grid(column=0, row=0)
# #Thêm một nút nhấn Click Me
# btn = Button(windows, text="Click Me", bg="orange", fg="red")
# #Thiết lập vị trí của nút nhấn có màu nền và màu chữ
# btn.grid(column=1, row=0)


windows.mainloop() # Lap vo tan de hien thi cua so

