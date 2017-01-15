class shop(object):
    name = "";
    price = 0;

    def __init__(self):
        print "A new article has been created";
    def get_name(self):
        name = raw_input("Enter the name of the article = ");
        return name;
    def get_price(self):
        price = raw_input( "Enter the price of the article = ");
        return price;
    def show(self):
        print "NAME = ",self.name;
        print "PRICE = ",self.price;

apple = shop();
apple.name = apple.get_name();
apple.price = apple.get_price();

pen = shop();
pen.name = pen.get_name();
pen.price = pen.get_price();

apple.show();
pen.show();

