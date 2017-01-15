class student(object):
    name="";
    marks = "";
    
    def __init__(self):
        print "\nA new student has been created ";

    def get_name(self,name):
        return name;
    def get_marks(self,marks):
        for i in marks:
            print i,;
    def get_percent(self,marks):
        percent = sum(marks)*100/500;
        print "\nPercentage = ",percent,"%";
        
            
bob = student();
print bob.get_name("BOB");
bob.marks = [100,98,95,86,83];
bob.get_marks(bob.marks);
bob.get_percent(bob.marks);

fred = student();
print fred.get_name("FRED");
fred.marks = [98,99,95,93,94];
fred.get_marks(fred.marks);
fred.get_percent(fred.marks);
    
