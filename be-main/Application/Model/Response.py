class Response:

    def __init__(self, meta, data):
        self.metadata = meta
        self.data = data

    def serialize(self):
        return {
            "meta": self.metadata.serialize(),
            "data": [data_object.serialize() for data_object in self.data]
        }
