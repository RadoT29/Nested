class Consumer:

    def __init__(self):
        self.count = 0

    def increment(self, amount):
        self.count += amount

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count