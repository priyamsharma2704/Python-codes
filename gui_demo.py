from Tkinter import *
##root  = Tk();
##root.title("GUI_DEMO");
##root.geometry("300x300");
##
##frame = Frame(root)
##frame.grid();
##
##lbl = Label(frame,text = "HIIIIIII...!!");
##lbl.grid();
##
##b1 = Button(frame,text = "Done!");
##b1.grid();
##
##root.mainloop();
class app(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid();
        self.btn_click=0;
        self.widget();

    def widget(self):
        self.btn = Button(self);
        self.btn["text"] = "Total Clicks = 0"
        self.btn["command"] = self.update();
        self.btn.grid();

    def update(self):
        self.btn_click += 1;
        #print self.btn_click;
        self.btn["text"] = "Total Clicks = " + str(self.btn_click);

#main
root = Tk();
root.title("Counter");
root.geometry("400x400");
a1 = app(root);
root.mainloop()
