class Character:
    def __init__(self, name, level, health, attack):
        self.name = name
        self.level = level
        self.health = health
        self.attack_power = attack

    def info(self):
        print(f"👤 {self.name} (Рівень {self.level}) | Здоров’я: {self.health} | Атака: {self.attack_power}")

    def attack(self, other):
        if self.health <= 0:
            print(f"❌ {self.name} не може атакувати, бо переможений.")
            return
        if other.health <= 0:
            print(f"⚠️ {other.name} вже переможений.")
            return
        other.health -= self.attack_power
        print(f"⚔️ {self.name} атакує {other.name} на {self.attack_power} одиниць.")
        if other.health <= 0:
            print(f"💀 {other.name} переможений!")
        else:
            print(f"🛡️ У {other.name} залишилося {other.health} одиниць здоров’я.")

    def heal(self):
        print(f"🩹 {self.name} відновлює здоров’я на 20 одиниць.")
        self.health += 20

# Класи Героїв
class Warrior(Character):
    def __init__(self, name, level):
        super().__init__(name, level, health=150, attack=20)
        self.armor = 30

    def info(self):
        super().info()
        print(f"🛡️ Броня: {self.armor}")

    def heal(self):
        print(f"🛡️ {self.name} медитує та відновлює 30 одиниць здоров’я.")
        self.health += 30

class Mage(Character):
    def __init__(self, name, level):
        super().__init__(name, level, health=100, attack=25)
        self.mana = 50

    def info(self):
        super().info()
        print(f"✨ Мана: {self.mana}")

    def heal(self):
        if self.mana >= 20:
            print(f"🔮 {self.name} використовує магію та відновлює 40 одиниць здоров’я.")
            self.health += 40
            self.mana -= 20
        else:
            print(f"⚠️ {self.name} не має достатньо мани.")


class Archer(Character):
    def __init__(self, name, level):
        super().__init__(name, level, health=110, attack=18)
        self.arrows = 10

    def info(self):
        super().info()
        print(f"🏹 Стріли: {self.arrows}")

    def heal(self):
        print(f"🍃 {self.name} приймає лікувальні трави та відновлює 25 одиниць здоров’я.")
        self.health += 25

# Демонстрація бою
if __name__ == "__main__":
    hero1 = Warrior("Тарік", 5)
    hero2 = Mage("Міріель", 4)
    hero3 = Archer("Ліан", 3)

    print("\n--- Інформація про героїв ---")
    hero1.info()
    hero2.info()
    hero3.info()

    print("\n--- Початок бою ---")
    hero1.attack(hero2)
    hero2.attack(hero1)
    hero3.attack(hero1)

    print("\n--- Відновлення здоров’я ---")
    hero1.heal()
    hero2.heal()
    hero3.heal()

    print("\n--- Оновлена інформація ---")
    hero1.info()
    hero2.info()
    hero3.info()
