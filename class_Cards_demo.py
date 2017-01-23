class Card(object):
    RANKS = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"];
    SUITS = ["C","S","H","D"];

    def __init__(self,rank,suit):
        self.rank = rank;
        self.suit = suit;
       
    def __str__(self):
        rep = self.rank + self.suit;
        return rep;

class Hand(object):
    
    def __init__(self):
        self.cards = [];
        
    def __str__(self):
        if self.cards:
            rep = "";
            for card in self.cards:
                rep += str(card) + " ";
        else:
            rep = "<EMPTY>";
        return rep;
    
    def clear(self):
        self.cards = [];
        
    def add(self,card):
        self.cards.append(card);
        
    def remove(self,card):
        self.cards.remove(card);

        
    def give(self,card,other_hand):
        self.cards.remove(card);
        other_hand.add(card);

class Deck(Hand):
    
    def populate(self):
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.add(Card(rank,suit));
                
    def shuffle(self):
        import random;
        random.shuffle(self.cards);

    def deal(self,hands,per_round):
        for r in range(per_round):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0];
                    self.give(top_card,hand);                    
                else :
                    print "no cards to deal";

    def card_value(self,h):
        
        if h.cards[0].rank == 'J' or h.cards[0].rank == 'Q' or h.cards[0].rank == 'K':
            v = 10;
        elif h.cards[0].rank == 'A':
            v = 1;
        else:
            v = int (h.cards[0].rank);

        if h.cards[1].rank == 'J' or h.cards[1].rank == 'Q' or h.cards[1].rank == 'K':
            v += 10;
        elif h.cards[0].rank == 'A':
            v += 1;
        else:
            v += int (h.cards[1].rank);
        print "v2 ",v;

        #print self.cards[0]
        ans = raw_input( "Do you want to hit? (Y/N)");
        
        while ans == 'Y' or ans == 'y':
            #ans = raw_input( "Do you want to hit? (Y/N)");
            if ans == 'y' or ans == 'Y':
                top = self.cards[0];
                #print top;
                self.give(top,h);
                
                    
##class Value(Hand):
##    def card_value(self,h):
##        
##        if h.cards[0].rank == 'J' or h.cards[0].rank == 'Q' or h.cards[0].rank == 'K':
##            v = 10;
##        elif h.cards[0].rank == 'A':
##            v = 1;
##        else:
##            v = int (h.cards[0].rank);
##
##        if h.cards[1].rank == 'J' or h.cards[1].rank == 'Q' or h.cards[1].rank == 'K':
##            v += 10;
##        elif h.cards[0].rank == 'A':
##            v += 1;
##        else:
##            v += int (h.cards[1].rank);
##        print "v2 ",v;
##
##        print self.cards;
##        ans = raw_input( "Do you want to hit? (Y/N)");
##        
##        #while ans == 'Y' or ans == 'y':
##            #ans = raw_input( "Do you want to hit? (Y/N)");
##            #if ans == 'y' or ans == 'Y':
                
                
        
     
        
#---------
##card1 = Card("A","S");
##card2 = Card("1","D");
##card3 = Card("6","H");
##card4 = Card("K","C");
##card5 = Card("10","H");
###print card1;
##
##h1 = Hand();
##h2 = Hand();
##print "HAND 1 =",h1;
##print "HAND 2 =",h2;
##
##h1.add(card1);
##h1.add(card2);
##h1.add(card3);
##h1.add(card4);
##h1.add(card5);
##print "HAND 1 =",h1;
##h1.give(card5,h2);
##print "After giving :"
##print "HAND 1 =",h1;
##print "HAND 2 =",h2
#-------------
d1 = Deck();
h1 = Hand();
h2 = Hand();
#hh1 = Value();
hands = [h1,h2];
print d1;
d1.populate();
print "Populate = ",d1;
d1.shuffle();
print "\nShuffle = ",d1;

d1.deal(hands,2);

print "\nPlayer 1 = ",h1;
print "Player 2 = ",h2;
#d1.print_deck();
print "\nDECK = ",d1;
d1.card_value(h1);
#hh1.card_value(h1);

