import speedtest
from tkinter import *

def bytes_to_mb(bytes):
  KB = 1024 # One Kilobyte is 1024 bytes
  MB = KB * 1024 # One MB is 1024 KB
  return int(bytes/MB)

st = speedtest.Speedtest()
# print("Download: ", bytes_to_mb(st.download()), "Mb/s")
# print("Upload: ", bytes_to_mb(st.upload()), "Mb/s")

# downs = "Download speed: " + str(bytes_to_mb(st.download())) + " Mbp/s"
# up = "Upload speed: " + str(bytes_to_mb(st.upload())) + " Mbp/s"

downs = "Download"
up = "Upload"

windows = Tk() # Tao cua so gui
windows.title("Title - Speed Test - Kha")
windows.geometry("350x200") # Size gui
####
# Them lable noi dung download/upload
down_lable = Label(windows, text=downs).grid(column=0, row=0, sticky=W)
up_lable = Label(windows, text=up).grid(column=0, row=1, sticky=W)

#Thiết lập vị trí của nút nhấn có màu nền và màu chữ
button_check = Button(windows, text="Check !!!", bg="orange", fg="red").grid(column=0, row=2)


windows.mainloop() # Lap vo tan de hien thi cua so

