def main():
	print("\n" + "Velkommen til #NavnPåApp#!")
	print("Dette er et program som skal gjøre matlagingen enkel for deg")
	print('Velg fra menyen hva du vil gjøre. Hvis du noen gang vil gå tilbake er det bare å skrive "back"')
	var = True
	while var:
		print()
		print("[1] Finn oppskrift".ljust(30), "[2] Legg til ny oppskrift".ljust(30))
		choice = input(">> ")

		if choice == "1":
			if seacrh_category() == "back":
				continue
			answ = input("Tilbake til hovedmenyen? ")
			if answ == "ja" or answ == "Ja":
				continue
			else:
				break

		if choice == "2":
			if add() == "back":
				continue
			answ = input("Tilbake til hovedmenyen? ")
			if answ == "ja" or answ == "Ja":
				continue
			else:
				break

def random_recipe(recipes):
	import random
	r_key = random.choice(list(recipes.keys()))
	return r_key

def print_recipe(recipes_dict, recipe_key):
	print("\n" + "##", recipe_key + "##" + "\n")
	for ingredient in recipes_dict[recipe_key][0]:
		print(ingredient)
	print()
	for instruction in recipes_dict[recipe_key][1]:
		print(instruction)


def seacrh_category():
	var = True
	while var:
		print("Hvilken kategori vil du se? (trykk enter for å hente en tilfeldif oppskrift fra en tilfeldig kategori)")
		print("[1] Fisk".ljust(20), "[2] Kjøtt".ljust(20), "[3] Pasta".ljust(20))
		print("[4] Kylling".ljust(20), "[5] Supper".ljust(20), "[6] Annet".ljust(20))
		category = input(">> ")
		if category == "back":
			return "back"
		elif category == "":
			while category != "jo":
				if category == "back":
					break
				import random
				category = random.randint(1,6)
				recipes = recipes_dict(category)
				r_key = random_recipe(recipes)
				print_recipe(recipes, r_key)
				category = input('Ikke fornøyd? Trykk enter for å prøve en annen tilfeldig oppskrift (skriv "jo" for å avslutte): ')
			if category == "back":
				continue
			else:
				break
		recipes = recipes_dict(category)
		for key in sorted(recipes.keys()):
			print(key)
		while var:
			recipe = input("Hvilken oppskrift vil du ha? (trykk enter for å velge en tilfeldig oppskrift) ")
			if recipe == "back":
				break
			elif recipe == "":
				while recipe != "jo":
					if recipe == "back":
						break
					r_key = random_recipe(recipes)
					print_recipe(recipes, r_key)
					recipe = input('Ikke fornøyd? Trykk enter for å prøve en annen tilfeldig oppskrift (skriv "jo" for å avslutte): ')
				if recipe == "back":
					continue
				var = False
			else:
				if recipe in recipes:
					print_recipe(recipes, recipe)
				else:
					search_results = []
					for key in recipes:
						if recipe in key:
							search_results.append(key)
					if len(search_results) == 0:
						print("Ingen oppskrifter matcher søket ditt. Husk å skille mellom store og små bokstaver!")
					else:
						print("Oppskrifter med søkeord i:")
						index = 1
						for recipe in search_results:
							print("[" + str(index) + "]", recipe)
							index += 1
						while var:
							choice = input("Hvilken oppskrift vil du ha? (skriv inn nummeret) ")
							if choice == "back":
								break
							else:
								choice = int(choice)
							recipe = search_results[choice - 1]
							print_recipe(recipes, recipe)
							var = False

def add():
	var = True
	while var:
		print("I hvilken kategori vil du legge til oppskriften? ")
		print("[1] Fisk".ljust(20), "[2] Kjøtt".ljust(20), "[3] Pasta".ljust(20))
		print("[4] Kylling".ljust(20), "[5] Supper".ljust(20), "[6] Annet".ljust(20))
		add_category = input(">> ")
		if add_category == "back":
			return "back"
		else:
			add_category = int(add_category)
		f = open(str(add_category)+".txt", "a")
		while var:
			add_recipe = input("Navn på oppskrift: ")
			if add_recipe == "back":
				break
			add_ingredient = " "
			ingredients = []
			print("Skriv inn ingredienser, trykk enter for å avslutte (OBS! ikke bruk komma eller semikolon!)")
			add_ingredient = input(">> ")
			while add_ingredient != "":
				if add_ingredient == "back":
					break
				ingredients.append(add_ingredient)
				add_ingredient = input(">> ")
			while var:
				instructions = input("Skriv inn framgangsmåte for oppskriften: ")
				if instructions == "back":
					break
				f.writelines(add_recipe + ";" + ",".join(ingredients) + ";" + instructions)
				var = False
		f.close()
	

def recipes_dict(category):
	f = open(str(category)+".txt", "r")
	recipes = {}
	for line in f:
		info = line.split(";")
		ingredients = info[1].split(",")
		instructions = info[2].split(". ")
		recipes[info[0]] = [ingredients, instructions]
	f.close
	return recipes

main()
