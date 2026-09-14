from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Triangle"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin1 = Goblin("Griddle")

    print(f"{goblin1.name} enters the arena with {goblin1.health} health.")

    goblin2 = Goblin("Scribble")
    
    print(f"{goblin2.name} enters the arena with {goblin2.health} health.")

    hero1 = Hero("Glimmer")

    print((f"{hero1.name} enters the arena with {hero1.health} health."))

    goblin1.take_damage(hero1.attack())

    if goblin1.is_alive():
        hero1.take_damage(goblin1.attack())


if __name__ == "__main__":
    main()
