from tkinter import*
from PIL import Image,ImageTk
from record import record
from in_out import in_out
from motion  import noise
import tkinter.font as font
from find_motion import find_motion
from identify import maincall
from rect_noise import rect_noise





window=Tk()
window.title("SMART CCTV CAMERA")
window.iconphoto(False,PhotoImage(file=r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\record.png"))
window.geometry('1080x600')




#mainframe
mainFrame = Frame (window,bd=2)
label_title = Label(mainFrame,text = "SMART CCTV CAMERA",font=('Helvitica',40,'bold'))
label_title.grid(pady=(10,10),column=1)




icon_1=Image.open(r"C:\Users\user\OneDrive\Pictures\security camera.png")
icon_1=icon_1.resize((70,70),Image.Resampling.LANCZOS)
icon_1=ImageTk.PhotoImage(icon_1)
label_icon_1=Label(mainFrame,image=icon_1)
label_icon_1.grid(row=0,pady=(5,10),column=0)




icon_spy=Image.open(r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\spy.png")
icon_spy=icon_spy.resize((180,180),Image.Resampling.LANCZOS)
icon_spy=ImageTk.PhotoImage(icon_spy)
label_icon_spy=Label(mainFrame,image=icon_spy)
label_icon_spy.grid(row=1,pady=(5,10),column=1)




btn_image=Image.open(r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\recording.png")
btn_image=btn_image.resize((50,50),Image.Resampling.LANCZOS)
btn_image=ImageTk.PhotoImage(btn_image)





btn=Button(mainFrame,text="VideoRecord",font=('Helvitica',25,'bold'),height=50,width=250,fg='orange',image=btn_image,compound='left',command=record)
btn.grid(row=2,pady=(20,10),column=2)


btn_image1=Image.open(r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\images.png")
btn_image1=btn_image1.resize((50,50),Image.Resampling.LANCZOS)
btn_image1=ImageTk.PhotoImage(btn_image1)


btn_exit=Button(mainFrame,text="EXIT",font=('Helvitica',25,'bold'),height=50,width=140,fg='red',image=btn_image1,compound='left',command=window.quit)
btn_exit.grid(row=3,pady=(20,10),column=1)

btn_inout=Image.open(r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\inout.png")
btn_inout=btn_inout.resize((50,50),Image.Resampling.LANCZOS)
btn_inout=ImageTk.PhotoImage(btn_inout)

btn=Button(mainFrame,text="IN-OUT",font=('Helvitica',25,'bold'),height=50,width=175,fg='green',image=btn_inout,compound='left',command=in_out)
btn.grid(row=4,pady=(20,10),column=2)

btn_noise=Image.open(r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\noise.jpeg")
btn_noise=btn_noise.resize((50,50),Image.Resampling.LANCZOS)
btn_noise=ImageTk.PhotoImage(btn_noise)

btn=Button(mainFrame,text="NOISE",font=('Helvitica',25,'bold'),height=50,width=175,fg='blue',image=btn_noise,compound='left',command=noise)
btn.grid(row=2,pady=(20,10),column=0)

btn_rec = Image.open(r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\rec.jpeg")
btn_rec = btn_rec.resize((50,50), Image.Resampling.LANCZOS)
btn_rec = ImageTk.PhotoImage(btn_rec)

btn=Button(mainFrame,text="RECTANGLE",font=('Helvitica',25,'bold'),height=60,width=250,fg='black',image=btn_rec,compound='left',command=rect_noise)
btn.grid(row=4,pady=(20,10),column=0)


btn_monitor = Image.open(r"C:\Users\user\OneDrive\Desktop\smart cctv camera\mn.png\monitor.jpeg")
btn_monitor = btn_monitor.resize((50,50), Image.Resampling.LANCZOS)
btn_monitor = ImageTk.PhotoImage(btn_monitor)

btn=Button(mainFrame,text="MONITOR",font=('Helvitica',25,'bold'),height=60,width=250,fg='red',image=btn_monitor,compound='left',command=find_motion)
btn.grid(row=5,pady=(20,10),column=1)


mainFrame.pack()


window.mainloop()