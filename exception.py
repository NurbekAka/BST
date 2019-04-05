def decorator(func):
    def wrapper(self, *args, **kwargs):#here we construct a wrapper for decorator
        if self.username is None:
            raise Exception("No username is defined!")#if in statement username is not defined, will work here 
        elif self.password is None:
           raise Exception("No password is defined!")# otherwise if password will be missed, will work this part.
        func(self, *args, **kwargs)
    return wrapper

class User:
    def __init__(self):#we create class "User" with function __init__, which initialize parameters
        self.username = None
        self.password = None

    @decorator# here we use decorator for this function
    def get_account_balance(self):
        balance = 5
        self.username.append(balance)

    @decorator# so we can use decorator for many times
    def change_password(self):
        new = "passw"
        if self.password == new:
            pass
u = User()
u.username = "Nurbek"#in this part we call functions in class
u.get_account_balance()
u.change_password()
