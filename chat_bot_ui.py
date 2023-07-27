from tkinter import *
from Chat_bot import *
 
# GUI
root = Tk()
root.title("Chatbot")
 
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
 
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"
 


def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
 
    user = e.get().lower()
    
    if "exit" in user:
        txt.insert(END, "\nBot -> Goodbye! Closing the chatbot.")
        root.after(1000, root.destroy) 
        return
    context.append({'role':'user', 'content':f"{user}"})
    response = get_completion_from_messages(context)

    if "ServiceError" in response:
        txt.insert(END, "\n" + "Bot -> Let Me Have Some Coffee to regain my Energy")
        time.sleep(30)
        return
    elif "ServiceError" in response:
        txt.insert(END, "\n" + "Bot -> Let Me Have Some Coffee to regain my Energy")
        time.sleep(120)
        return
    else:
        txt.insert(END, "\n" + "Bot -> "+response)
 
    e.delete(0, END)
messages =  [  

{'role':'system', 'content':'You are a Car Expert Chatbot who suggests Cars according to Budget and Requirement.'},    

{'role':'user', 'content':'Input your Budget '}  ]




context = [{'role': 'system', 'content': """

Hello! I'm CarExpert, your friendly Car Guide here to provide general Car information. \

Please keep in mind that i give Advice according to data provided. \

Let's talk about your needs and budget, and I'll do my best to assist you. \

I can provide Car Price According to Ex-Showroom Of your City. \

However, for On-road Price, it's best to Visit the nearst showroom 

Please provide Budget and Your Requirements

To exit this conversation, simply type "exit."

"""}

 ]   
 
lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
    row=0)
 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)
 
scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=send).grid(row=2, column=1)
 
root.mainloop()