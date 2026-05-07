
class UserNotFound(Exception):
    def __init__(self, code, detail):
        self.CODE = code
        self.DETAIL = detail

class InvalidVerification(Exception):
    def __init__(self, code, detail):
        self.CODE = code
        self.DETAIL = detail

class HabitNotFound(Exception):
    def __init__(self, code, detail):
        self.CODE = code
        self.DETAIL = detail

class EmptyRequestBody(Exception):
    def __init__(self, code, detail):
        self.CODE = code
        self.DETAIL = detail

class InvalidFields(Exception):
    def __init__(self, code, detail):
        self.CODE = code
        self.DETAIL = detail