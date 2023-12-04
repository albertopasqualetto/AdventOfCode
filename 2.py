from pprint import pprint

registry=[0]
with open("2_input.txt") as f:
	for line in f.readlines():
		line=line.split()
		game_n=int(line[1].strip(":"))
		registry.insert(game_n, {
			"red":0,
			"green":0,
			"blue":0
			})

		all_picks = line[2:]
		couples = [all_picks[i:i+2] for i in range(0,len(all_picks),2)]

		# print(couples)

		for couple in couples:
			if "red" in couple[1] and int(couple[0]) > registry[game_n]["red"]:
				registry[game_n]["red"] = int(couple[0])
			elif "green" in couple[1] and int(couple[0]) > registry[game_n]["green"]:
				registry[game_n]["green"] = int(couple[0])
			elif "blue" in couple[1] and int(couple[0]) > registry[game_n]["blue"]:
				registry[game_n]["blue"] = int(couple[0])

max_red = 12
max_green = 13
max_blue = 14

count_ids=0

for game_n, game in enumerate(registry):
	if game_n == 0:
		continue

	if game["red"] <= max_red and game["green"] <= max_green and game["blue"] <= max_blue:
		count_ids+=game_n
	# 	print("This is ok:", game_n)
	# else:
	# 	print("This is not ok:", game_n)
	# 	pprint(registry[game_n])

print("Sum of playable games ids", count_ids)

sum_of_powers = 0
for game_n, game in enumerate(registry):
	if game_n == 0:
		continue

	power_of_game = game["red"] * game["green"] * game["blue"]
	sum_of_powers += power_of_game

print("Sum of powers", sum_of_powers)