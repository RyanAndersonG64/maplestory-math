level = int(input("Enter level: "))

dexless_dex = 4
dexless_luk = int(8 + 5 * level)

normal_dex = int(level * 2)
if level >= 40:
    normal_dex = int(level + 40)

normal_luk = int(12 + 5 * level - normal_dex)

luk = [dexless_luk, normal_luk]
dex = [dexless_dex, normal_dex]

weapon_attack = [int(input("Enter dexless weapon attack: ")), int(input("Enter normal weapon attack: "))]
attack_speed = [int(input("Enter dexless attack speed: ")), int(input("Enter normal attack speed: "))]

attack_speed_modifier = [0, 0, .63, .69, .72, .78, .87]

base_damage = [0, 0]
double_stab_damage = [0, 0]
savage_blow_damage = [0, 0]

for i in range(len(dex)):
    base_damage[i-1] = int((luk[i-1] * 3.6 + dex[i-1] + 4) * weapon_attack[i-1] / 100)
    double_stab_damage[i-1] = base_damage[i-1] * 2.6
    savage_blow_damage[i-1] = base_damage[i-1] * 4.8

# print results rounded down to nearest integer
print(f"dexless base damage: {int(base_damage[0])}, normal base damage: {int(base_damage[1])}")
print(f"dexless double stab damage: {int(double_stab_damage[0])}, normal double stab damage: {int(double_stab_damage[1])}")
print(f"dexless savage blow damage: {int(savage_blow_damage[0])}, normal savage blow damage: {int(savage_blow_damage[1])}")
print(f"dexless double stab DPS: {int(double_stab_damage[0] / attack_speed_modifier[attack_speed[0]])}, normal double stab DPS: {int(double_stab_damage[1] / attack_speed_modifier[attack_speed[1]])}")
print(f"dexless savage blow DPS: {int(savage_blow_damage[0] / attack_speed_modifier[attack_speed[0]])}, normal savage blow DPS: {int(savage_blow_damage[1] / attack_speed_modifier[attack_speed[1]])}")