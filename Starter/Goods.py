class Goods:
    price: int
    amount: int

    def __init__(self, price=0, amount=0):
        self.price = price
        self.amount = amount
        # self.temp_price = self.price
        # self.temp_amount = self.amount

    def get_price(self):
        return self.price

    def get_amount(self):
        return self.amount

    def set_amount(self, amount):
        self.amount = amount

    def reduce_amount(self, amount):
        self.amount -= amount
        return self.amount

    def multiply_temp_price(self, amount):
        return self.price * amount

    def compare_amount(self, amount):
        if self.amount >= amount:
            return True;
        else:
            return False;
