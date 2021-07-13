from pprint import pprint

# Задача 1


def read_cookbook():
    cook_book = {}
    with open("recipes.txt", "r", encoding = "UTF-8") as file:
        for line in file:
            dish_name = line.strip()
            count_ingredient = int(file.readline().strip())
            ingredient_list = []
            for items in range(count_ingredient):
                ingredients = {}
                ingredient = file.readline().strip()
                ingredients['ingredient_name'], ingredients['quantity'], ingredients['measure'] = ingredient.split(' | ')
                ingredient_list.append(ingredients)
            file.readline()
            cook_book[dish_name] = ingredient_list
    return cook_book


# Задача 2


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_cookbook()
    for dish_name in dishes:
        for ingredient in cook_book[dish_name]:
            new_list = dict()
            if ingredient['ingredient_name'] not in shop_list:
                new_list['measure'] = ingredient['measure']
                new_list['quantity'] = int(ingredient['quantity']) * person_count
                shop_list[ingredient['ingredient_name']] = new_list
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] = (shop_list[ingredient['ingredient_name']]['quantity']
                                                                        + int(ingredient['quantity']) * person_count)
    return shop_list


pprint(get_shop_list_by_dishes(["Омлет", "Фахитос"], 2))




