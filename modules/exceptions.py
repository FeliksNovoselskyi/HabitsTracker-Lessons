
class UserNotFound(Exception):
    def __init__(self, code, detail):
        self.CODE = code
        self.DETAIL = detail

class InvalidVerification(Exception):
    def __init__(self, code, detail):
        self.CODE = code
        self.DETAIL = detail
