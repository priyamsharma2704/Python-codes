import cPickle;

##brand = ["bmw","audi","lambo"];
##cars = ["Sedan", "Hatchback", "Sports", "SUV"];
##file1 = open("Pickeling_demo.dat","w");
##cPickle.dump(brand,file1);
##cPickle.dump(cars,file1);
##file1.close();


file1 = open("Pickeling_demo.dat","r");
brand = cPickle.load(file1);
cars = cPickle.load(file1);
print "brands = ",brand;
print "cards = ",cars;
file1.close();

