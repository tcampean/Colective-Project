class LoginMeta:

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type
        }
