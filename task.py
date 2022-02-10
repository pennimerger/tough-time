#task0
#converting celsius to farenheit
celsius=20
farenheit=(celsius*1.8)+32
#print(f'The weather is {celsius}\N{DEGREE SIGN}C in UK but {farenheit}\N{DEGREE SIGN}F in the US and they tell the same temperature.')

#appending (...) to every number a user inputs.
#user_0=float(input())
#print(f'{user_0}...')

#fix this list and print
names=["Priscilla","Mummy G.O","Benedict","Dima",
"Kingsley","Mic"]
#print(f'\n{names}')

#What is the index of c++ ?
programming_languages=['python','javascript','C','pascal',
'c++','php','visual basic']
#print(f'\n{programming_languages}')
#print(f"c++ is indexed 4 as shown by this call - {programming_languages[4]}")

#print python and php
#print(f'\n{programming_languages[0]}')
#print(programming_languages[5])

#fix this list, append your name to this list and print
name=["Priscilla","Mummy G.O","Benedict","Dima",
"Kingsley","Mic"]
name.append("pennimerger")
#print(f'\n{name}')

#delete pascal from this list and print
_programming_languages=['python','javascript','C','pascal',
'c++','php','visual basic']
del _programming_languages[3]
#print(f'\n{_programming_languages}')

#task1
car = {
    'brand': 'Ford',
    'model': 'mustang',
    'year': 1964
}
#using the 'get' method to print the value of the 'model' key of the car dictionary.
_car = car.get('model')
print(_car)

'B. a given object may appear in a  list more than once'
'while that is true, other options are false.'

twitter_user1 = {
    'Username': 'Pennifuse',
    'Year joined': 2017,
    'Interests': 'Politics, Tech, Sports and Music',
}

#task2
#adds 1000 to any input > 1000
#score = int(input('Enter your score: '))
#if score < 1000:
 #   score += 1000
#print(f'New score be {score}\n')

#checks if an alcoholic is of legal age to consume alcohol
#age = int(input('Enter your real age abeg: '))
#if age >= 18:
 #   print('\tCheers\n')
#else:
 #   print("\tYou can't drink alcohol\n")

#checks the length of a list
sample_list = ['Wednesday', 2, 'good', 'to', 'be', True]
_long = len(sample_list)
#print(sample_list)
#if _long < 6:
 #   print('is less than 6')
#elif _long == 6:
 #   print('is equal to 6')
#else:
    #print('Now we are talking.')
