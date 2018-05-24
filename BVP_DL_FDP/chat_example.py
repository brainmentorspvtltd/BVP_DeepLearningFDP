import random
greetings = ['hi',
             'hello',
             'hey',
             'how are you',
             ]

farewell = ['bye',
            'bie',
            'see you',
            'take care']

while True:
    user_message = input("Enter your message : ")
    cpu_greet = random.choice(greetings)
    cpu_farewell = random.choice(farewell)
    if user_message in greetings:
        print(cpu_greet)
    elif user_message in farewell:
        print(cpu_farewell)
    else:
        print("I don't understand")

    






