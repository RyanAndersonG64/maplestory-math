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
    base_damage[i-1] = int((dex[i-1] * 3.6 + str[i-1]) * weapon_attack[i-1] / 100)
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
