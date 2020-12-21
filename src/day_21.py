import re
from collections import defaultdict, Counter
from itertools import chain
from utils import load_day

foods = load_day(21, sample=False)


def parse_allergen_mapping(foods):
    contains_mapping = defaultdict(set)
    all_foods = []
    for food in foods:
        food_names, contains_names = food.replace(')', '').split('(contains ')
        food_names = food_names.split()
        all_foods.extend(food_names)
        for n in contains_names.split(', '):
            if len(contains_mapping[n]) == 0:
                contains_mapping[n] = set(food_names)
            else:
                contains_mapping[n] &= set(food_names)
    return contains_mapping, all_foods


# Part 1
contains_mapping, all_foods = parse_allergen_mapping(foods)
may_have_allergen = set(chain(*contains_mapping.values()))
no_allergens = set(all_foods) - may_have_allergen
food_counts = Counter(all_foods)
no_allergen_count = sum([food_counts[f] for f in no_allergens])
print(f'Part 1: {no_allergen_count}')


# Part 2
allergens = set(contains_mapping.keys())
allergy_foods = set()
allergen_mapping = {}
while allergens:
    for c, f in contains_mapping.items():
        remaining_foods = f - allergy_foods
        if len(remaining_foods) == 1:
            allergy_food = list(remaining_foods)[0]
            allergen_mapping[c] = allergy_food
            allergy_foods.add(allergy_food)
            allergens.remove(c)
dangerous_ingredients = ','.join([f for _, f in sorted(allergen_mapping.items())])
print(f'Part 2: {dangerous_ingredients}')