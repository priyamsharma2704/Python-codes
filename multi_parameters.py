def parameters(fname,lname,*color,**relation_age):
    print fname,lname
    print color
    print relation_age
    print relation_age["father"]

parameters("priyam","sharma","red","blue","green","yellow",son=18,father=56,mother=49,daughter=20,dog=4)
