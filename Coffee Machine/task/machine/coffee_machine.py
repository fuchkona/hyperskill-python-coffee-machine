class CoffeeMachine:
    def __init__(self,
                 has_water,
                 has_milk,
                 has_beans,
                 has_cups,
                 has_money):
        self.has_water = has_water
        self.has_milk = has_milk
        self.has_beans = has_beans
        self.has_cups = has_cups
        self.has_money = has_money

    def print_status(self):
        print("The coffee machine has:")
        print(f"{self.has_water} of water")
        print(f"{self.has_milk} of milk")
        print(f"{self.has_beans} of coffee beans")
        print(f"{self.has_cups} of disposable cups")
        print(f"${self.has_money} of money")

    def do_coffee(self,
                  need_water,
                  need_milk,
                  need_beans,
                  need_cups,
                  cost):
        if self.has_water < need_water:
            print("Sorry, not enough water!")
            return False

        if self.has_milk < need_milk:
            print("Sorry, not enough milk!")
            return False

        if self.has_beans < need_beans:
            print("Sorry, not enough coffee beans!")
            return False

        if self.has_cups < need_cups:
            print("Sorry, not enough disposable cups!")
            return False

        print("I have enough resources, making you a coffee!")

        self.has_water -= need_water
        self.has_milk -= need_milk
        self.has_beans -= need_beans
        self.has_cups -= need_cups
        self.has_money += cost

        return True

    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        user_input = input()
        if user_input == 'back':
            return False

        sort_of_coffee = int(user_input)
        if sort_of_coffee == 1:
            self.do_coffee(250, 0, 16, 1, 4)
        elif sort_of_coffee == 2:
            self.do_coffee(350, 75, 20, 1, 7)
        elif sort_of_coffee == 3:
            self.do_coffee(200, 100, 12, 1, 6)

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.has_water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.has_milk += int(input())
        print("Write how many ml of coffee beans do you want to add:")
        self.has_beans += int(input())
        print("Write how many ml of disposable cups do you want to add:")
        self.has_cups += int(input())

    def take(self):
        print(f"I gave you ${self.has_money}")
        self.has_money = 0

    def main_menu(self):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "remaining":
            self.print_status()
        elif action == "take":
            self.take()
        else:
            return False
        return True


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    if not coffee_machine.main_menu():
        break
