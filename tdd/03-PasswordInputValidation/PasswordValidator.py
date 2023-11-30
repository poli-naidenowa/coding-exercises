import re

def passwordValidator(password):

    special_symbols = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    pass_valid = True
    message = []

    if len(password) < 8:
        message.append("Password must be at least 8 characters")
        pass_valid = False
    if sum(map(str.isdigit, password)) < 2:
        message.append("The password must contain at least 2 numbers")
        pass_valid = False
    if sum(map(str.isupper, password)) < 1:
        message.append("password must contain at least one capital letter")
        pass_valid = False
    if special_symbols.search(password) == None:
        message.append("password must contain at least one special character")
        pass_valid = False
        
    return pass_valid, "\n".join(message)
