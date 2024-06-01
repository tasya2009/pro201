from tkinter import *
window=Tk()

def calculate_BMI():
    n = username.get()
    w = int(weight.get())
    h = int(height.get())/100
    bmi = w/(h * h)
    bmi = round(bmi, 1)
    m = ""
    if bmi < 18.5 :
        m = "UNDERWEIGHT"
    elif bmi > 18.5 and bmi <= 24.9 :
        m = "NORMAL"
    elif bmi > 25 and bmi <= 29.9 :
        m = "OVERWEIGHT"
    elif bmi > 30 :
        m = "OBESE"
    else :
        m = "SOMETHING WENT WRONG"
    
    result_label.destroy()
    result = n + ", YOUR BMI IS " + str(bmi) + "AND " + m
    output_label = Label(result_frame, text = result, bg = "white", fg = "black", font = ("calibri", 15),bd = 1)
    output_label.place(x = 20,y=40)
    output_label.pack()

window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')


app_label=Label(window, text="BMI CALCULATOR", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

name_label=Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
name_label.place(x=20, y=90)

username=Entry(window, text="", bd=2, width=22)
username.place(x=150, y=92)

height_label = Label(window, text = "Your Height", fg = "black", bg = "lightcyan", font = ("calibri", 12),bd = 1)
height_label.place(x = 20, y = 120)

height = Entry(window, text = "", bd = 2, width = 22)
height.place(x = 150, y = 123)

weight_label = Label(window, text = "Your Weight", fg = "black", bg = "lightcyan", font = ("calibri", 12), bd = 1)
weight_label.place(x = 20, y = 150)

weight = Entry(window, text = "", bd = 2, width = 22)
weight.place(x = 150, y = 153)

calculate = Button(window, text = "CALCULATE", fg = "black", bg = "blue", command = calculate_BMI)
calculate.place(x = 20, y = 180)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=20,y=300)

result_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()