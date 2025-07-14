print('Welcome to Introduction')
print("")
Name = input ("Enter you Name:")
Age = int(input ("Enter you Age:"))
Height = float(input ("Enter you Height:"))
Favourite = int(input ("Enter you Favourite Number:"))
print("")
print("Thank you! Here is the information we collected")
print("")
print("Name:",Name,"type:",type(Name),"Memory Address:",id(Name))
print("Age:",Age,"type:",type(Age),"Memory Address:",id(Age))
print("Height:",Height,"type:",type(Height),"Memory Address:",id(Height))
print("Favourite:",Favourite,"type:",type(Favourite),"Memory Address:",id(Favourite))
print("")

import datetime

age=int(input("how old are you?"))
current_year=datetime.datetime.now().year
birth_year=current_year - age
print("you were born in",birth_year)


"""
Welcome to Introduction

Enter you Name: akshat's
Enter you Age: 18
Enter you Height: 6
Enter you Favourite Number: 18

Thank you! Here is the information we collected

Name:  akshat's type: <class 'str'> Memory Address: 2498951522928
Age: 18 type: <class 'int'> Memory Address: 140706316109256
Height: 6.0 type: <class 'float'> Memory Address: 2498951484656
Favourite: 18 type: <class 'int'> Memory Address: 140706316109256

how old are you? 18
you were born in 2007

"""
