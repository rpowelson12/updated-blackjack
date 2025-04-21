class Player():
    def __init__(self, hand):
        self.balance = 0
        self.hand = hand

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

    