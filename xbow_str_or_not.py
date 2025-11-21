level = int(input("Enter level: "))

str_less_str = 4
str_less_dex = 8 + 5 * level

low_str = 22
low_str_dex = int(8 + level * 5 - 18)

if level >= 38:
    low_str = 38
    low_str_dex = int(8 + level * 5 - 26)

normal_str = int(level)
normal_str_dex = int(12 + 4 * level)

str = [str_less_str, low_str, normal_str]
dex = [str_less_dex, low_str_dex, normal_str_dex]

weapon_attack = [int(input("Enter strless weapon attack: ")), int(input("Enter low str weapon attack: ")), int(input("Enter normal str weapon attack: "))]
attack_speed = [int(input("Enter strless attack speed: ")), int(input("Enter low str attack speed: ")), int(input("Enter normal str attack speed: "))]

attack_speed_modifier = [0, 0, .63, .69, .72, .78, .87]

base_damage = [0, 0, 0]
double_shot_damage = [0, 0, 0]
one_crit_damage = [0, 0, 0]
two_crit_damage = [0, 0, 0]
average_double_shot_damage = [0, 0, 0]

for i in range(len(dex)):
    base_damage[i] = int((dex[i] * 3.6 + str[i]) * weapon_attack[i] / 100)
    double_shot_damage[i] = base_damage[i] * 2.6
    one_crit_damage[i] = base_damage[i] * 3.6
    two_crit_damage[i] = base_damage[i] * 4.6
    average_double_shot_damage[i] = (double_shot_damage[i] + 2 * one_crit_damage[i] + two_crit_damage[i]) / 4

# print results rounded down to nearest integer
print(f"strless base damage: {int(base_damage[0])}, low str base damage: {int(base_damage[1])}, normal str base damage: {int(base_damage[2])}")
print(f"strless double shot damage: {int(double_shot_damage[0])}, low str double shot damage: {int(double_shot_damage[1])}, normal str double shot damage: {int(double_shot_damage[2])}")
print(f"strless one crit damage: {int(one_crit_damage[0])}, low str one crit damage: {int(one_crit_damage[1])}, normal str one crit damage: {int(one_crit_damage[2])}")
print(f"strless two crit damage: {int(two_crit_damage[0])}, low str two crit damage: {int(two_crit_damage[1])}, normal str two crit damage: {int(two_crit_damage[2])}")
print(f"strless average double shot damage: {int(average_double_shot_damage[0])}, low str average double shot damage: {int(average_double_shot_damage[1])}, normal str average double shot damage: {int(average_double_shot_damage[2])}")
print(f"strless DPS: {int(average_double_shot_damage[0] / attack_speed_modifier[attack_speed[0]])}, low str DPS: {int(average_double_shot_damage[1] / attack_speed_modifier[attack_speed[1]])}, normal str DPS: {int(average_double_shot_damage[2] / attack_speed_modifier[attack_speed[2]])}")


# Test Results:
# low str is clearly not worth it due to the Fantasia server not having any strless/low str bowman weapons

# Note: tests were done assuming 8 attack gloves, the highest level xbow equippable at that level scrolled to + 10
#   attack above average(balanche and heckler for low str), and no other gear or buffs; booster was factored into attack speed from level 50+