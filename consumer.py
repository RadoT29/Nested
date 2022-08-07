class Consumer:

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 2

    def decrement(self):
        self.count -= 2

    def get_count(self):
        return self.count