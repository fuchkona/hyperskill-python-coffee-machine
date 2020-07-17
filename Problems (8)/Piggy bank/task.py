class PiggyBank:
    def __init__(self, initial_dollars, initial_cents):
        self.dollars = initial_dollars
        self.cents = initial_cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.add_cents(deposit_cents)

    def add_cents(self, deposit_cents):
        deposit_cents += self.cents
        while deposit_cents >= 100:
            self.dollars += 1
            deposit_cents -= 100
        self.cents = deposit_cents
