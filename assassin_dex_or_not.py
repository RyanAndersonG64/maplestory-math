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

base_damage = [0, 0, 0]
double_shot_damage = [0, 0, 0]
one_crit_damage = [0, 0, 0]
two_crit_damage = [0, 0, 0]
average_double_shot_damage = [0, 0, 0]

for i in range(len(dex)):
    double_shot_damage[i-1] = base_damage[i-1] * 2.6
    one_crit_damage[i-1] = base_damage[i-1] * 3.6
    two_crit_damage[i-1] = base_damage[i-1] * 4.6
    average_double_shot_damage[i-1] = (double_shot_damage[i-1] + 2 * one_crit_damage[i-1] + two_crit_damage[i-1]) / 4

# print results rounded down to nearest integer
print(f"strless base damage: {int(base_damage[0])}, low str base damage: {int(base_damage[1])}, normal str base damage: {int(base_damage[2])}")
print(f"strless double shot damage: {int(double_shot_damage[0])}, low str double shot damage: {int(double_shot_damage[1])}, normal str double shot damage: {int(double_shot_damage[2])}")
print(f"strless one crit damage: {int(one_crit_damage[0])}, low str one crit damage: {int(one_crit_damage[1])}, normal str one crit damage: {int(one_crit_damage[2])}")
print(f"strless two crit damage: {int(two_crit_damage[0])}, low str two crit damage: {int(two_crit_damage[1])}, normal str two crit damage: {int(two_crit_damage[2])}")
print(f"strless average double shot damage: {int(average_double_shot_damage[0])}, low str average double shot damage: {int(average_double_shot_damage[1])}, normal str average double shot damage: {int(average_double_shot_damage[2])}")
print(f"strless DPS: {int(average_double_shot_damage[0] / attack_speed_modifier[attack_speed[0]])}, low str DPS: {int(average_double_shot_damage[1] / attack_speed_modifier[attack_speed[1]])}, normal str DPS: {int(average_double_shot_damage[2] / attack_speed_modifier[attack_speed[2]])}")
