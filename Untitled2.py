import random
import time

def calculate(arm, hl):
    temp = 0
    if arm <= 25:
        temp = hl // 10 + arm // 10
    elif arm <= 50:
        temp = hl // 7 + arm // 7
    elif arm <= 75:
        temp = hl // 4 + arm // 4
    elif arm <= 100:
        temp = hl // 4 + arm // 2
    return hl + arm + temp

def health_bar(hp, name="Health"):
    bar_length = 10
    filled_length = max(0, min(bar_length, hp // 10))
    bar = "#" * filled_length + "-" * (bar_length - filled_length)
    print(f"{name}: [{bar}] ({max(0, hp)})")

# Oyuncu başlangıç değerleri
heal = int(input('Enter your heal (10-100): '))
armor = int(input('Enter your armor (0-100): '))

if heal == 0:
    print("You are already dead. Game Over.")
    exit()

# Total health hesaplama
if armor > 0:
    player_hp = calculate(armor, heal)
else:
    player_hp = heal

print("\nYour total health is being calculated...")
time.sleep(1)
health_bar(player_hp, "Player")

# Düşman oluştur
enemy_hp = random.randint(50, 250)
print(f"\n⚔️ A wild enemy appears with {enemy_hp} HP!\n")
health_bar(enemy_hp, "Enemy")

# Oyun döngüsü
while player_hp > 0 and enemy_hp > 0:
    action = input("\nDo you want to (A)ttack or (R)un? ").lower()

    if action == "r":
        print("You ran away! Game over.")
        break
    elif action == "a":
        print("\nChoose your action:")
        print("1. Heal yourself (no damage to enemy)")
        print("2. Chaotic attack (random damage to both you and enemy)")
        print("3. Safe attack (damage enemy only, no risk)")

        choice = input("Enter 1, 2 or 3: ")

        if choice == "1":
            heal_amount = random.randint(15, 30)
            player_hp += heal_amount
            print(f"You healed yourself for {heal_amount} HP!")

        elif choice == "2":
            dmg_to_enemy = random.randint(5, 40)
            dmg_to_player = random.randint(5, 40)
            enemy_hp -= dmg_to_enemy
            player_hp -= dmg_to_player
            print(f"Chaotic attack! You dealt {dmg_to_enemy} damage to the enemy and took {dmg_to_player} damage yourself.")

        elif choice == "3":
            dmg = random.randint(10, 25)
            enemy_hp -= dmg
            print(f"You safely attacked the enemy for {dmg} damage.")

        else:
            print("Invalid choice! You lost your turn.")

        if enemy_hp <= 0:
            print("🎉 You defeated the enemy!")
            break

        # Düşmanın saldırısı - aynı 3 seçenekten biri rastgele seçilir
        enemy_action = random.choice(["1", "2", "3"])
        print(f"\nEnemy's turn! Enemy chooses option {enemy_action}.")

        if enemy_action == "1":
            enemy_heal = random.randint(15, 30)
            enemy_hp += enemy_heal
            print(f"Enemy healed itself for {enemy_heal} HP!")

        elif enemy_action == "2":
            dmg_to_player = random.randint(5, 40)
            dmg_to_enemy = random.randint(5, 40)
            player_hp -= dmg_to_player
            enemy_hp -= dmg_to_enemy
            print(f"Enemy's chaotic attack! It dealt {dmg_to_player} damage to you and took {dmg_to_enemy} damage itself.")

        elif enemy_action == "3":
            dmg = random.randint(10, 25)
            player_hp -= dmg
            print(f"Enemy safely attacked you for {dmg} damage.")

        # Tur sonunda can durumları gösteriliyor
        print("\n--- Current Status ---")
        health_bar(player_hp, "Player")
        health_bar(enemy_hp, "Enemy")

    else:
        print("Invalid action. Type 'A' to attack or 'R' to run.")

if player_hp <= 0:
    print("💀 You died. Game over.")
elif enemy_hp <= 0:
    print("🎉 You defeated the enemy!")
