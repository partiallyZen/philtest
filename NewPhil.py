#importing my old philosophers program
import csv
import pandas as pd




#reading recommendation list
religlist=["Buddhist", "Catholic", "Christian", "Jewish", "Muslim", "Hindu", "Other"]
religlists = (sorted(religlist))
philosophers = {}
users = {}



philosophers = pd.read_csv('philosophers.csv')

philosophers_tuple = [
    ('Socrates', 'Ancient Greece', 'Wisest Man'), #Name/Location/Notable Books?
    ('David Hume', 'Modern England', 'Question Identity'),
    ('Bertrand Russell', 'Modern England', 'Logical Inquiry')
    ]
                
username = input("What is your name?")  #establish user
print("Hello, " + username + ". How much do you know about philosophy?")
userprep = str(input("None, Average, Above Average, PhD?"))
print(userprep)
userpref=input("Would you conside yourself religious? Y/N:")
print(userpref)



if "N" in userpref:
    print("Not religious, eh?")
    print("Which do you trust more? Thoughts or Feelings?")
    usertype = input()
    print("You picked:" +usertype)
    users[username]= (userprep, userpref, usertype)
    if "Thoughts" in usertype:
        print("This system recommends the following Authors/books for: ")
        print(users)
        print(philosophers_tuple)
    if "Feelings" in usertype:
        print("Waffles") #placeholder

        
if "Y" in userpref:
    print("You considered yourself religious.") 
 nn    print(religlists)
    userrelig = input()
    if userrelig in religlists:
        print("You Picked: " + userrelig)
        users[username]= (userprep, userpref, userrelig)
        print(users)
        if "Buddhist" in userrelig:
            print("What tradition are you?")
            print("Mahayana? or Theravada? Other?:")
            usertrad = input()
            print(" I seek refuge in the Buddha. I seek refuge in the sangha, I seek refuge in the Dharma.") #replace with some Buddhist Philosophy EX: Shambhala: Way of the Warrior
        if "Catholic" in userrelig:
            print("You picked: " + userrelig)
            print("Some suggested reading is: Thomas Aquinus")  #add catholic philosophy >Aquinas? 
        if "Jewish" in userrelig:
            print("Waffles") #placeholder
        if "Muslim" in userrelig:
            print("Waffles") #placeholder
        if "Hindu" in userrelig:
            print("Waffles") #placeholder
        if "Other" in userrelig:
            print("Can't decide? Pick one of these: ")
            print("Theist, Atheist, Agnostic.")
            godtype = input()
    else:
        print("That is not on the list")



#Need to create a function for sorting the books by the key users{}
        