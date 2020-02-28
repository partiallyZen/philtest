#importing my old philosophers program
import csv
import pandas as pd
from pandas import DataFrame


#reading recommendation list
religlist=['B', "Buddhist", 'CA', "Catholic", 'CH', "Christian", 'J', "Jewish", 'M', "Muslim", 'H', "Hindu", 'O', "Other"]
religlists = religlist
philosophers = {}
users = {}

users_tuple = [
    ('TestUser', 'None', 'Thoughts'), #Name/Location/Notable Books?
    ]


data = pd.read_csv('philosophers.csv', index_col='School')

philosophers_tuple = [
    ('Socrates', 'Ancient Greece', 'Wisest Man'), #Name/Location/Notable Books?
    ('David Hume', 'Modern England', 'Question Identity'),
    ('Bertrand Russell', 'Modern England', 'Logical Inquiry')
    ]
                
username = input("What is your name?")  #establish user
print("Hello, " + username + ".")
#userprep = str(input("None, Average, Above Average, PhD?"))
#print(userprep)
userpref=input("Would you consider yourself religious? Y/N:")
userpref = userpref.upper()
print(userpref)



if "N" in userpref:
    print("Not religious, eh?")
    print("Which do you trust more?")
    print('(a)Thoughts') 
    print("(b)Feelings")
    usertype = input()
    usertype = usertype.lower()
    print("You picked:" +usertype)
    users[username]= (userpref, userpref, usertype)
    if "thoughts" or 'a' in usertype:
        print('Good choices there, '+ username + '!')
        print("This system recommends the following Authors/books: ")
        thoughts = (data.loc['Empiricist'])
        print(thoughts)
    if "feelings" or 'b' in usertype:
        feelings = (data.loc["Mystic"])
        print('Good choices there, '+ username + '!')
        print('You should read the following Mystics:')
        print(feelings)

        
if "Y" in userpref:
    print("You considered yourself religious.") 
    print(religlist)
    print('<Please pick the religion\'s shorthand from above>')
    userrelig = input()
    userrelig = userrelig.upper()
    if userrelig in religlist:
        print("You Picked: " + userrelig)
        users[username]= (userpref, userrelig)
        print(users)
        while userrelig == 'B':
            print("What tradition are you?")
            print("Mahayana? or Theravada? Other?:")
            usertrad = input()
            print("I seek refuge in the Buddha. I seek refuge in the sangha, I seek refuge in the Dharma.") #replace with some Buddhist Philosophy EX: Shambhala: Way of the Warrior
            break
        else:    
            while userrelig == 'CA':
                print("You picked: " + userrelig)
                print("This system recommends the following Authors/books: ")
                catholic = data.loc['Catholic'] 
                print(catholic) #add catholic philosophy >Aquinas?
                break
            else:
                while userrelig == 'CH':
                    print("You picked: " + userrelig)
                    print("This system recommends the following Authors/books: ")
                    christian = data.loc['Christian'] 
                    print(christian) #add catholic philosophy >Aquinas?
                    break
                else:
                    while userrelig == 'J':
                        print("Jewish Waffles") #placeholder
                        break
                    else:
                        while userrelig == 'M':
                            print("Muslim Waffles") #placeholder
                            break
                        else:
                            while userrelig == 'H':
                                print("Hindu Waffles") #placeholder
                                break
                            else:
                                while userrelig == 'O':
                                    print("Can't decide? Pick one of these: ")
                                    print("Theist, Atheist, Agnostic.")
                                    godtype = input()
                                    break
    else:
        print("That is not on the list")


#Need to create a function for sorting the books by the key users{}