import random;
X = "X";
O = "O";
EMPTY = " ";
squares = 9 ;
MAX = [];
human1 = "";
human2 = "";
x=0;
def board(MAX):
    
    print "tttt";
    print "\n\t" , MAX[0], " |" ,MAX[1], "|" ,MAX[2];
    print "\t___|___|___";
    print "\t" , MAX[3], " |" ,MAX[4], "|" ,MAX[5];
    print "\t___|___|___";
    print "\t" , MAX[6], " |" ,MAX[7], "|" ,MAX[8];
    print "\t   |   |   ";


def  go_h1():
    flag = 0;
    pos  = int( raw_input( "PLAYER 1 : Enter the position : "));
    while (pos < 0 or pos > 8)or MAX[pos] !=EMPTY and flag == 0 :
        pos  = int( raw_input( " Invalid position..Enter the position again : "));
    for j in range(squares) :
        if pos == j:
            MAX[j] = X;
    flag = 1;
    


def go_h2():
    flag = 0;
    pos  = int( raw_input( "PLAYER 2 : Enter the position : "));
    while (pos < 0 or pos > 8) or MAX[pos] !=EMPTY and flag == 0:
        pos  = int( raw_input( " Position Occupied..Enter the position again : "));
    for j in range(squares) :
        if pos == j:
            MAX[j] = O;                
    flag = 1;


def win(MAX , str):
    str1 = "human1";
    way = ((0,1,2),
           (3,4,5),
           (6,7,8),
           (0,3,6),
           (1,4,7),
           (2,5,8),
           (0,4,8),
           (2,4,6) );
    
    for k in (way):
        if MAX[k[0]] == MAX[k[1]] == MAX[k[2]] != EMPTY and str1 == str:            
            print "human 1 winss..!!!";
            global x
            x = 1;
            return x;
        elif MAX[k[0]] == MAX[k[1]] == MAX[k[2]] != EMPTY and str1 != str:            
            print "human 2 winss..!!!";
            global x
            x = 1;
            return x;
        elif EMPTY not in MAX :
            print "ITS A TIE..!!!";
            global x
            x = 1;
            return x; 
            
        

ans = raw_input("You want to go first? Press (y/n)");
while ans[0].lower() != 'y' and ans[0].lower() != 'n' :
    ans = raw_input("Invalid value..Press (y/n)");
print ans.lower();
for i in range(squares):
    MAX.append(EMPTY);
if ans[0] == 'y' or ans[0] == 'Y':
    human1 = X;
    human2 = O;
    while x !=1 and EMPTY in MAX:
        print "x = " , x;
        go_h1();        
        board(MAX);
        win(MAX , "human1");
        if x !=1:
            go_h2();
            board(MAX);
            win(MAX , "human2");
           
else :
    human1 = O;
    human2 = X;
    while x !=1 and EMPTY in MAX:
        go_h2();        
        board(MAX);
        win(MAX,"human2");
        if x !=1:
            go_h1();
            board(MAX);
            win(MAX,"human1");
    



        


    

