import random

class Game:
    def __init__(self):
        self.player_score = 0
        self.enemy_score = 0

    def get_user_choice(self):
        print("Choose: 1. Rock, 2. Scissors, 3. Paper")
        choice = input("Enter your choice (1/2/3): ")
        return int(choice)

    def get_enemy_choice(self):
        return random.randint(1, 3)

    def determine_winner(self, user_choice, enemy_choice):
        if user_choice == enemy_choice:
            return "It's a tie!"
        elif (
            (user_choice == 1 and enemy_choice == 2)
            or (user_choice == 2 and enemy_choice == 3)
            or (user_choice == 3 and enemy_choice == 1)
        ):
            self.player_score += 1
            return "You win!"
        else:
            self.enemy_score += 1
            return "You lose!"

    def display_scores(self):
        print(f"Your score: {self.player_score}")
        print(f"Computer's score: {self.enemy_score}")

    def play(self):
        while True:
            user_choice = self.get_user_choice()
            enemy_choice = self.get_enemy_choice()

            print(f"You chose: {user_choice}")
            print(f"Computer chose: {enemy_choice}")

            result = self.determine_winner(user_choice, enemy_choice)
            print(result)

            self.display_scores()

            play_again = input("Do you want to play again? (y/n): ")
            if play_again.lower() != "y":
                break

if __name__ == "__main__":
    game = Game()
    game.play()

