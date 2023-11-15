import re

def passwordValidator(password):

    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if len(password) < 8 and sum(map(str.isdigit, password)) < 2:
        return "Password must be at least 8 characters\nThe password must contain at least 2 numbers"
    elif sum(map(str.isdigit, password)) < 2:
        return "The password must contain at least 2 numbers"
    elif len(password) < 8:
        return "Password must be at least 8 characters"
    elif sum(map(str.isupper, password)) < 1:
        return "password must contain at least one capital letter"
    elif regex.search(password) == None:
        return "password must contain at least one special character"
