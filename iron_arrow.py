nums = [1, 2, 3, 4, 5, 6]

iron_arrow_modifier = 180
arrow_bomb_modifier = 130

iron_arrow_damage = [1, 1, 1, 1, 1, 1]
arrow_bomb_damage = [1, 1, 1, 1, 1, 1]
for num in nums:
    iron_arrow_damage[num - 1] = (0.9 ** (num - 1)) * iron_arrow_modifier
    arrow_bomb_damage[num - 1] = arrow_bomb_modifier

print(f"iron arrow damage per hit: {iron_arrow_damage}")
print(f"arrow bomb damage per hit: {arrow_bomb_damage}")
print("\n")
print(f"iron arrow total damage: {sum(iron_arrow_damage)}")
print(f"arrow bomb total damage: {sum(arrow_bomb_damage)}")
print("\n")
print(f"iron arrow average damage: {sum(iron_arrow_damage) / len(iron_arrow_damage)}")
print(f"arrow bomb average damage: {sum(arrow_bomb_damage) / len(arrow_bomb_damage)}")
