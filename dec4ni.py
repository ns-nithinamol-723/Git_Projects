from tkinter import*
import calendar
from pytube import YouTube

root = Tk()
root.config(background="white")
root.geometry("600x600")
root.title("YouTube Downloader and Calendar")

#
# def showCal():
#  newroot = Tk()
#  newroot.config(background="gray")
#  newroot.title("Calendar for the year")
#  newroot.geometry("550x600")
#  year_field = Label(newroot(text=""))
#  fetch_year = year_field.get()
#  year = int(fetch_year)
#
#  newroot_content = calendar.calendar(year)
#  cal_year = Label(new_root, text=newroot_content, font="Consolas 10 bold")
#  cal_year.grid(place(x=500, y=120))
#
#  new_root.mainloop()
#
#
# if __name__ == "__main__" :
#  tube = Label(root, text="YouTube Video Downloader", font='Arial 20 bold').place(x=10,y=20)
# link_enter = Entry(root, width = 60,textvariable = 'link').place(x=10, y=60)
#
# cal = Label(root, text="CALENDAR", font='Arial 20 bold').place(x=500,y=20)
# year = Label(root, text="Enter Year", bg="light green").place(x=550,y=60)
# year = Entry(root, width=30, textvariable='Integer').place(x=550, y=80)
# Show = Button(root, text="show Calendar", fg="white", bg="Green", command=showCal).place(x=550, y=100)
#
# root.mainloop()