scores = [];
print "\nMENU";
print "\n1. Show scores";
print "2. Add scores";
print "3. Delete scores";
print "4. Sort scores";
print "\nEXIT - press 0";
choice =-1;
while choice != 0:
    choice = int(raw_input( "\nEnter your choice : "));

    if choice == 1:
        if len(scores) != 0:
            for i in scores:
                print i ;
        else :
            print "\nEmpty List"
    elif choice == 2:
        score = int(raw_input("\nEnter the score to be added = "));
        scores.append(score);
    elif choice == 3:
        score = int(raw_input("\nEnter the score to be deleted = "));
        if score in scores:
            scores.remove(score);
        else:
            print"\nNo such score is present in the list";
    elif choice == 4:
        if len(scores) != 0:
            scores.sort();
            print"\nSorted list is = ";
            for i in scores:
                print i ;
        else :
            print "\nEmpty List"
    elif choice == 0:
        print "\nThank You!"
            
    
