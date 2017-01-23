from Tkinter import *

class app(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid();
        self.btn_click=0;
        self.widget();

    def widget(self):
        self.l1 = Label(self,text = "Select your choices: ");
        self.l1.grid(row = 0, column = 0, columnspan = 2, sticky = W);

        self.likes_comedy = BooleanVar();
        Checkbutton(self,
                    text = "Comedy",
                    variable = self.likes_comedy,
                    command = self.update
                    ).grid(row = 1, column = 0,sticky = W ,)
        
        self.likes_action = BooleanVar();
        Checkbutton(self,
                    text = "Action",
                    variable = self.likes_action,
                    command = self.update
                    ).grid(row = 1, column = 1,sticky = W ,padx = 24)
        
        self.likes_war = BooleanVar();
        Checkbutton(self,
                    text = "War",
                    variable = self.likes_war,
                    command = self.update
                    ).grid(row = 1, column = 2,sticky = W )

        self.fav = StringVar();
        Radiobutton(self,
                    text = "Rock",
                    variable = self.fav,
                    value = "rock.",
                    command = self.update_radio
                    ).grid(row = 2 , column = 0 , sticky = W)

        Radiobutton(self,
                    text = "Metal",
                    variable = self.fav,
                    value = "metal.",
                    command = self.update_radio
                    ).grid(row = 2 , column = 1 , sticky = W,padx=24)

        Radiobutton(self,
                    text = "Hip Hop",
                    variable = self.fav,
                    value = "hip hop.",
                    command = self.update_radio
                    ).grid(row = 2 , column = 2 , sticky = W)
        
        self.l1 = Label(self,text = "Enter the password:");
        self.l1.grid(row = 3, column = 0, columnspan = 2, sticky = W);
        
        self.l_pass = Label(self , text = "Password: ");
        self.l_pass.grid(row = 4, column = 0, sticky = W);

        self.pw_entry = Entry(self);
        self.pw_entry.grid(row = 4,column = 1, sticky = W);
        
        self.btn = Button(self, text = "Submit", command = self.reveal);
        self.btn.grid(row = 5, column = 0,sticky = W,padx = 5,pady = 10);

        self.text  = Text(self, width = 23, height = 8, wrap = WORD)
        self.text.grid(row = 6, column = 0, columnspan = 2 , sticky = W,padx = 5,pady = 5);

    def update(self):
        like =" ";
        if self.likes_comedy.get():
            like += "\nYou like comedy movies";
        if self.likes_action.get():
            like += "\nYou like action movies";
        if self.likes_war.get():
            like += "\nYou like war movies";
        
        self.text.delete(0.0,END);
        self.text.insert(0.0,like);

    def update_radio(self):
        msg = "\nYou selected ";
        msg +=self.fav.get()
        self.text.insert(5.0,msg);

            
    def reveal(self):
        content = self.pw_entry.get();
        if content == "correct":
            msg = "\nCorrect Password";
        else :
            msg = "\nIncorrect Password";

        #self.text.delete(0.0,END);
        self.text.insert(7.0,msg);
#main
root = Tk();
root.title("Counter");
root.geometry("400x400");
a1 = app(root);
root.mainloop()
