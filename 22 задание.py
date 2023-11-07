import re

class Validator:

    def isEmail(self, string):
        return re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', string)

    def isDomain(self, string):
        return re.fullmatch(r'[A-Za-z0-9-]+\.[A-Za-z0-9]+', string)

    def isNumber(self, string):
        return re.fullmatch(r'^-?\d+(?:\.\d+)?$', string)

validator = Validator()

print(validator.isEmail('test@mail.com')) # True
print(validator.isDomain('python.org')) # True
print(validator.isNumber('12345')) # True