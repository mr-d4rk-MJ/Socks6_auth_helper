class AUTHENTICATION_METHOD:
    NO_AUTH = 0x00
    USERPASS = 0x02
    @staticmethod
    def build_method(methods : bytes):
        total_length = 4 + len(methods)
        bt = bytearray()
        bt.append(2)
        bt.append(total_length)
        bt.append(0)
        bt.append(0)
        for x in methods:
            bt.append(x)
        return bt
class AUTHENTICATION_DATA:
    def __init__(self,user,password):
        bt = bytearray()
        bt.append(1)
        bt.append(len(user))
        for x in user.encode():
            bt.append(x)
        bt.append(len(password))
        for y in password.encode():
            bt.append(y)
        self.data = bt
    def build_user_pass(self):
        total_length = 3 + len(self.data)
        bt = bytearray()
        bt.append(3)
        bt.append(total_length)
        bt.append(2)
        for x in self.data:
            bt.append(x)
        return bt