from random import randint

# def funny_little_demonstrations(message_passed: str):

    # for character in message_passed:
    #     if character == 'e':
    #         return "Your message has an e"
        
    # return "No e D:"

    # result_string = ""
    # for character in message_passed:
    #     if character in ['a', 'e', 'i', 'o', 'u'] or not character.isalpha():
    #         result_string += character  
    #     else:
    #         result_string += 'x'
            
    # return result_string

    # return "You gotta comment something out buddy"

def handle_response(message):

    if(message == 'hi'):
        return 'hello'

    if(message == 'roll'):
        return str(randint(1,6))
    
    if(message == 'help'):
        return "`say hi or roll for a response`"
    

    return "huh"
    # return funny_little_demonstrations(message)

def frankResponses(message):
    if(message == 'hi'):
        return 'i dont like talking to you'

    if(message == 'roll'):
        return 'im not doing that for you'
    
    if(message == 'help'):
        return "`im not giving you any help`"
    
    return 'im not listening'





    
