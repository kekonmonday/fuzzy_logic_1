from model import input_lvs
from itertools import product

experience = {	"Without experience": 0,
				"Minimum experience": 0.3,
				"Average experience": 0.6,
				"Considerable experience": 0.8,
				"Extensive experience": 1}

diplom_score = {"Satisfactory": 0,
		 		"Good": 0.5,
		 		"Excellent": 1}

professional_test = {"Low score": 0,
		     		 "Medium score": 0.5,
		     		 "High score": 1}

english_level = {"Basic": 0.1,
				 "Pre-Intermediate": 0.4,
				 "Intermediate": 0.6,
				 "Upper-Intermediate": 0.8,
				 "Advanced": 1}

coef = {"experience": 0.25,
		"diplom_score": 0.25,
		"professional_test": 0.25,
		"english_level": 0.25}

Suitability = { "Excellent suitable": 0.9,
				"Probably suitable": 0.7,
				"Partially suitable": 0.5,
				"Maybe suitable": 0.2,
				"Unlikely suitable": 0.05,
				"Not suitable": 0}


# Извлекаем имена терминов принадлежности для каждой переменной
term_names_lists = [list(var['terms'].keys()) for var in input_lvs]

# Создаем список кортежей всех возможных комбинаций
combinations = list(product(*term_names_lists))
rule_base = []
values = set()
keys = []
for comb in combinations:
	experience_coef = experience[comb[0]] * coef["experience"]
	score_coef = diplom_score[comb[1]] * coef["diplom_score"]
	test_coef = professional_test[comb[2]] * coef["professional_test"]
	english_coef = english_level[comb[3]] * coef["english_level"]
	res = experience_coef + score_coef + test_coef + english_coef
	values.add(res)

	for key, value in Suitability.items():
		if res >= value:
			keys.append(key)
			rule_base.append((comb, key))
			break

# set_key = set(keys)

# for key in set_key:
# 	print(key, "-", keys.count(key))

# i = 0
# for value in sorted(values):
# 	i = i + 1
# 	if i == 26:
# 		print(value)
# 		i = 0


for rule in rule_base:
	print(str(rule) + ",")

# print(len(values))


