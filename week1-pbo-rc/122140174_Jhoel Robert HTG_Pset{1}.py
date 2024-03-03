import random
import sys
class Character:
    def __init__(self, name, hp, attack_point, defense_point):
        self.name = name
        self.hp = hp
        self.attack_point = attack_point
        self.defense_points = defense_point
        self.is_blocking = False

    # hp = 0 = mati
    def is_alive(self):
        return self.hp > 0

    def attack(self, other):
        damage = self.attack_point
        if other.is_blocking:
            damage = self.attack_point // 2
            other.is_blocking = False

        # pengurangan dmg berdasarkan defense point yang ada pada char
        damage_reduced = max(0, damage - other.defense_points)
        other.hp -= damage_reduced

    def block(self):
        self.is_blocking = True
        print(f"{self.name} is preparing to block the next attack.")

    # implementation of skills (scrapped)

    def show_stats(self):
        print(f"{self.name} - HP: {self.hp}")


def combat(player1, player2):
    while player1.is_alive() and player2.is_alive():
        player1.show_stats()
        player2.show_stats()

        # auto p1 turn
        action = input("Do you want to (a)ttack or (b)lock? [e to exit]\n").lower()
        if action == "a":
            player1.attack(player2)
            print("="*30)
        elif action == "b":
            player1.block()
            print("="*30)
        elif action == "e":
            print("Kill switch...")
            sys.exit()
        else:
            print("Invalid action. You lose your turn.\n" + "="*30)

        # cek apakah player2 masih hidup
        if not player2.is_alive():
            break

        player2_decision = random.choice(['attack', 'block'])
        if player2_decision == 'attack':
            print(f"{player2.name} decides to attack!")
            player2.attack(player1)
        else:
            print(f"{player2.name} decides to block!")
            player2.block()
        print("-"*30)

    if player1.is_alive():
        print("player1 wins!")
    else:
        print("player2 wins!")

player1 = Character("Hero", 50, 17, 5)
player2 = Character("Renegade", 50, 20, 4)

combat(player1, player2)
