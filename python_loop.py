from Tkinter import *
 
def clicked():
 
    tempReading = "24.6 C"
    humiReading = "42.6 %"

    #lbl.configure(text= res)
    temperatureTxt.delete(0,'end')
    humidityTxt.delete(0,'end')
    temperatureTxt.insert(0,tempReading)
    humidityTxt.insert(0,humiReading)
    #read_temp(temperatureTxt)
    temperatureTxt.after(1000, clicked)     #sets a timer callback to reload the data into entry boxes
    #label.after(1000, count)

#def read_temp(Entry tempEntry)
#    global DynTempReading = 1
#    humiReading = "5555 %"
    
   # tempEntry.delete(0,'end')
#    tempEntry.insert(0,DynTempReading)
#    DynTempReading +=1

    


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