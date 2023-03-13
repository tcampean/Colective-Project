class Metadata:

    def __init__(self, pages):
        self.page_count = pages

    def serialize(self):
        return {
            "pages": self.page_count
        }