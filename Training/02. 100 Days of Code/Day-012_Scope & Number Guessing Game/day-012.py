# Day 12: Scope and Number Guessing Game

# Scope

enemies = 1


def increase_enemies():
    enemies_2 = 2
    print(f"enemies inside function : {enemies_2}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope

def drink_potion():
    # Local Scope
    potion_strength = 2
    print(potion_strength)


drink_potion()

# Global Scope
player_health = 10


def game():
    def drink_potion2():
        # Local Scope
        potion_strength = 2
        print(potion_strength)
        print(player_health)

    drink_potion2()


print(player_health)

# There is no Block Scope in Python

game_level = 3


def create_enemy():
    enemy = ["Skeleton", "Zombie", "Alien"]
    new_enemy = ""

    if game_level < 5:
        new_enemy = enemy[0]

    print(new_enemy)


create_enemy()

# Modifying Global Scope,
# We should avoid modifying global scope
enemies = "Skeleton"


def increase_enemies_2():
    enemies_3 = "Zombie"
    print(f"enemies inside function : {enemies_3}.")


increase_enemies_2()
print(f"enemies outside function: {enemies}.")

# Python Global Constants and Global Scope
pi = 3.14159
url = "www.google.com"
twitter_handle = "ansito"
