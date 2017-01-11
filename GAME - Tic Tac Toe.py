import random;
X = "X";
O = "O";
EMPTY = " ";
squares = 9 ;
MAX = [];
human = "";
comp = "";
x=0;
def board(MAX):
    
    print "tttt";
    print "\n\t" , MAX[0], " |" ,MAX[1], "|" ,MAX[2];
    print "\t___|___|___";
    print "\t" , MAX[3], " |" ,MAX[4], "|" ,MAX[5];
    print "\t___|___|___";
    print "\t" , MAX[6], " |" ,MAX[7], "|" ,MAX[8];
    print "\t   |   |   ";


def  go_h():
    flag = 0;
    pos  = int( raw_input( "Enter the position : "));
    while MAX[pos] !=EMPTY and flag == 0:
        pos  = int( raw_input( " Position Occupied..Enter the position again : "));
    for j in range(squares) :
        if pos == j:
            MAX[j] = X;
    flag = 1;
    


def go_c():
    flag = 0;
    pos = random.randrange(squares);
    while MAX[pos] !=EMPTY and flag == 0:
        pos = random.randrange(squares);
    for j in range(squares) :
        if pos == j:
            MAX[j] = O;                
    flag = 1;


def win(MAX):
    way = ((0,1,2),
           (3,4,5),
           (6,7,8),
           (0,3,6),
           (1,4,7),
           (2,5,8),
           (0,4,8),
           (2,4,6) );
    
    for k in (way):
        if MAX[k[0]] == MAX[k[1]] == MAX[k[2]] != EMPTY:            
            print "human winss..!!!";
            global x
            x = 1;
            return x;
        
    

ans = raw_input("You want to go first? Press (y/n)");
print ans.lower();
for i in range(squares):
    MAX.append(EMPTY);
#board(MAX);
if ans[0] == 'y' or ans[0] == 'Y':
    human = X;
    comp = O;
    while x !=1:
        print "x = " , x;
        go_h();
        go_c();
        board(MAX);
        win(MAX);
        #result();
        
        
    
else :
    #print"noo";
    human = O;
    comp = X;
    



        


    

