import random

number_of_friends = int(input("Enter the number of friends joining (including you): "))
print()
friends_dictionary = {}

if number_of_friends > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(number_of_friends):
        friend = input()
        friends_dictionary[friend] = 0
        
    print()
    total_bill = int(input("Enter the total bill value: "))
        
    print()
    lucky_or_not = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    
    if lucky_or_not == 'Yes':
        lucky_one = random.choice(list(friends_dictionary.keys()))
        print()
        print(f"{lucky_one} is the lucky one!")
        
        splitted_bill = round(total_bill / (number_of_friends - 1), 2)
    
        for friend in friends_dictionary.keys():
            if friend != lucky_one:
                friends_dictionary[friend] = splitted_bill
            else:
                friends_dictionary[friend] = 0
        print()
        print(friends_dictionary)
        
    else:
        print()
        print("No one is going to be lucky")
        
        splitted_bill = round(total_bill / (number_of_friends), 2)
        for friend in friends_dictionary.keys():
            friends_dictionary[friend] = splitted_bill
            
        print()
        print(friends_dictionary)
    
else:
    print()
    print("No one is joining for the party")
