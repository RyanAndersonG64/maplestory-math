level = int(input("Enter level: "))

dexless_dex = 25
dexless_luk = 8 + 5 * level - 21

low_dex = 25
low_dex_luk = int(8 + level * 5 - 21)

if level >= 25:
    low_dex = 50
    low_str_dex = int(8 + level * 5 - 46)

normal_dex = int(level * 2)
if level >= 40:
    normal_dex = int(level + 40)

normal_luk = int(12 + 5 * level - normal_dex)

dex = [dexless_dex, low_dex, normal_dex]
luk = [dexless_luk, low_dex_luk, normal_luk]

weapon_attack = [int(input("Enter dexless weapon attack: ")), int(input("Enter low dex weapon attack: ")), int(input("Enter normal dex weapon attack: "))]
attack_speed = [int(input("Enter dexless attack speed: ")), int(input("Enter low dex attack speed: ")), int(input("Enter normal dex attack speed: "))]

attack_speed_modifier = [0, 0, .63, .69, .72, .78, .87]

lucky_seven_base_damage = [0, 0, 0]
lucky_seven_damage = [0, 0, 0]
one_crit_damage = [0, 0, 0]
two_crit_damage = [0, 0, 0]
average_lucky_seven_damage = [0, 0, 0]

for i in range(len(dex)):
    lucky_seven_base_damage[i-1] = int((luk[i-1] * 5 * weapon_attack[i-1] / 100) * 1.5)
    lucky_seven_damage[i-1] = lucky_seven_base_damage[i-1] * 2

    if level >= 80:
        lucky_seven_damage[i-1] = lucky_seven_damage[i-1] * 1.5

    one_crit_damage[i-1] = lucky_seven_damage[i-1] * 3
    two_crit_damage[i-1] = lucky_seven_damage[i-1] * 4
    average_lucky_seven_damage[i-1] = (lucky_seven_damage[i-1] + 2 * one_crit_damage[i-1] + two_crit_damage[i-1]) / 4

# print results rounded down to nearest integer
print(f"dexless lucky seven base damage: {int(lucky_seven_base_damage[0])}, low dex lucky seven base damage: {int(lucky_seven_base_damage[1])}, normal dex lucky seven base damage: {int(lucky_seven_base_damage[2])}")
print(f"dexless lucky seven damage: {int(lucky_seven_damage[0])}, low dex lucky seven damage: {int(lucky_seven_damage[1])}, normal dex lucky seven damage: {int(lucky_seven_damage[2])}")
print(f"dexless one crit damage: {int(one_crit_damage[0])}, low dex one crit damage: {int(one_crit_damage[1])}, normal dex one crit damage: {int(one_crit_damage[2])}")
print(f"dexless two crit damage: {int(two_crit_damage[0])}, low dex two crit damage: {int(two_crit_damage[1])}, normal dex two crit damage: {int(two_crit_damage[2])}")
print(f"dexless average lucky seven damage: {int(average_lucky_seven_damage[0])}, low dex average lucky seven damage: {int(average_lucky_seven_damage[1])}, normal dex average lucky seven damage: {int(average_lucky_seven_damage[2])}")
print(f"dexless DPS: {int(average_lucky_seven_damage[0] / attack_speed_modifier[attack_speed[0]])}, low dex DPS: {int(average_lucky_seven_damage[1] / attack_speed_modifier[attack_speed[1]])}, normal dex DPS: {int(average_lucky_seven_damage[2] / attack_speed_modifier[attack_speed[2]])}")


# Test Results:
# low dex is better until at least level 70 due to the Meba's crazy attack speed
#   If possible, get 25 dex from gear so you can stay at 25 base dex since the Neva and Shinobi Bracer don't require dex
# Low dex with Meba loses to normal starting at level 70 with <20 attack stars, or level 80 with >= 20 attack stars; 
#   transition to normal dex if you can't get a Neva or Shinobi Bracer
# Low dex with Shinobi Bracer (or Neva) remains vastly superior to normal dex until level 100;
#   start looking for dex gear in time to equip a Red Craven (or Purple Dragon Sleve if you are giga rich)
# With ilbis, low dex remains superior forever, unless there's something about the math that i'm missing

# Note: tests were done assuming 8 attack gloves, the highest level claw equippable at that level scrolled to + 10
#   attack above average, and no other gear or buffs; booster was factored into attack speed from level 50+