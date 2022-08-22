import random
class Die:
    def __init__(self):
        self.value = None

    def roll(self):
        self.value = random.randint(1,7)

class Player:
    
    def __init__(self, die, is_human, counter=10):
        self.die = die
        self.is_human = is_human
        self.counter = counter

    def increment(self):
        self.counter += 1

    def decrement(self):
        self.counter -= 1

    def roll_the_die(self):
        self.die.roll()

class DiceGame:
    def __init__(self, human_player, computer_player):
        self.human_player = human_player
        self.computer_player = computer_player

    def start_game(self):
        print("Welcome to the game! You will have at least 10 rounds to play.")
        begin_game = True
        while begin_game:
            self.start_round()
            begin_game = self.determine_game_over()

    def start_round(self):
        input("Hit Enter to start a round of the game!")

        self.human_player.roll_the_die()
        human_roll = self.human_player.die.value
        self.computer_player.roll_the_die()
        computer_roll = self.computer_player.die.value
        if human_roll > computer_roll:
            self.human_player.decrement()
            self.computer_player.increment()
        elif human_roll < computer_roll:
            self.computer_player.decrement()
            self.human_player.increment()
        print(f"Human counter: {self.human_player.counter}")
        print(f"Computer counter: {self.computer_player.counter}")

    def determine_game_over(self):
        if self.human_player.counter == 0:
            print("Human player won!")
            return False
        elif self.computer_player.counter == 0:
            print("Computer player won!")
            return False
        else:
            return True