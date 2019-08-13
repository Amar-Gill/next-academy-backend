def deaf_aunty(message, name):
    
    if message == 'I love you aunty, I have to go now':
        print('ok. Goodbye.')
        print(f'{name} are you there?')
        input1 = input('Say something: ')
        if input1 == '':
            input2 = input('Say something: ')
        else:
            return False
        if input2 == '':
            return True
        else:
            return False

    words = message.split()
    
    
    if all(
        word.islower() for word in words
    ):
        print('WHAT? SPEAK UP!')
        #print([word.islower() for word in words])
        return False

    if all(
        word.isupper() for word in words
    ):
        print('YOU ARE VERY RUDE!')
        #print([word.isupper() for word in words])
        return False

    print('SHOW SOME RESPECT!')
    
    # if all(
    #     word[0].isupper() and word[1:].islower() for word in words
    # ):
    #     print('SHOW SOME RESPECT!')
    #     print([word[0].isupper() and word[1:].islower() for word in words])
    #     return False

name = input('What is your name? ')


while True:

    message = input('Say something to aunty: ')

    if(deaf_aunty(message, name) == True):
        break