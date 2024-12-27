import re

class Validator:
    def isEmail(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    def isDomain(self, domain):
        domain_regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)(\.[A-Za-z]{2,})+$'
        return re.match(domain_regex, domain) is not None

    def isNumber(self, string):
        return string.isdigit()


validator = Validator()
print(validator.isEmail("example@example.com"))  
print(validator.isEmail("invalid-email.com"))     
print(validator.isDomain("example.com"))           
print(validator.isDomain("-example.com"))          
print(validator.isNumber("12345"))                 
print(validator.isNumber("123a45"))                 



