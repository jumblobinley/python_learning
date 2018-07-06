from Tkinter import *
 
def clicked():
 
    tempReading = "24.6 C"
    humiReading = "42.6 %"

    #lbl.configure(text= res)
    temperatureTxt.delete(0,'end')
    humidityTxt.delete(0,'end')
    temperatureTxt.insert(0,tempReading)
    humidityTxt.insert(0,humiReading)

window = Tk()
window.title("Temperature Sensor 3000")
window.geometry('350x200')
 
temperatureLbl = Label(window, text="Temperature")
temperatureLbl.grid(column=0, row=0)
 
temperatureTxt = Entry(window,width=10)
temperatureTxt.grid(column=1, row=0)

humidityLbl = Label(window, text="Humidity")
humidityLbl.grid(column=0, row=1)
 
humidityTxt = Entry(window,width=10)
humidityTxt.grid(column=1, row=1)
 


tempButton = Button(window, text="Take Temp", width=15, command=clicked)
tempButton.grid(column=0, row=2)
stopButton = Button(window, text='Stop', width=15, command=window.destroy)
stopButton.grid(column=1, row=2)
 
window.mainloop()