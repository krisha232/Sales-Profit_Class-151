from tkinter import * 
root= Tk()
root.title("Sales Profit")
root.geometry("800x500")
root.configure(background = "beige")


month = ("January","February","March","April","May","June","July","August","September","October", "November", " December")

profit = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)


months_label = Label(root)
months_label["text"] = "Month : " + str(month)
profit_label = Label(root)
profit_label["text"] = "Profit : " + str(profit)
max_profit_label = Label(root)
min_profit_label = Label(root)

def max1() : 
    max_profit = max(profit)
    max_profit_index = profit.index(max_profit)
    print(max_profit_index)

    max_month =    month[max_profit_index] 
    max_profit_label["text"] = "The maximum profit was " + str(max_profit) + " and was recorded in the month of " + str(max_month)


def min1() :
    
    min_profit = min(profit)
    min_profit_index = profit.index(min_profit)
    print(min_profit_index)

    min_month =    month[min_profit_index] 
    min_profit_label["text"] = "The minimum profit was " + str(min_profit) + " and was recorded in the month of " + str(min_month)


btn1 = Button(root, text = "Show Max Profitable Month", command = max1 )
btn1.place(relx =0.5 , rely =0.4 , anchor = CENTER)
btn = Button(root, text = "Show Min Profitable Month", command = min1 )
btn.place(relx =0.5 , rely =0.6 , anchor = CENTER)



months_label.place(relx =0.5 , rely =0.2 , anchor = CENTER)
profit_label.place(relx =0.5 , rely =0.3 , anchor = CENTER)
max_profit_label.place(relx =0.5 , rely =0.5 , anchor = CENTER)
min_profit_label.place(relx =0.5 , rely =0.7 , anchor = CENTER)

root.mainloop()