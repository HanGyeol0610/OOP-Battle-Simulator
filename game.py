from goblin import Goblin
from hero import Hero


ARENA_NAME = "The Iron Triangle"

def battle(hero: Hero, enemy: Goblin):
    while hero.is_alive() and enemy.is_alive():
        hero_damage = hero.attack()
        enemy.take_damage(hero_damage)

        if enemy.is_alive():
            enemy_damage = enemy.attack()
            hero.take_damage(enemy_damage)

    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} wins!")

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

    battle(hero1,goblin1)



if __name__ == "__main__":
    main()
