from pprint import pprint

def get_cook_book():
    with open('recipes.txt',  encoding='UTF-8') as file:
        cook_book = {}
        while True:
            key = file.readline().strip()
            if not key:
                break
            cook_book[key] = []
            quantity_ingredient = int(file.readline().strip())
            for line in range(quantity_ingredient):
                ingredient = file.readline().strip().split('|')
                cook_book[key] += [{'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}]
            file.readline()
    return cook_book
# print(get_cook_book())

cook_book = {
    'Омлет': [{'ingredient_name': 'Яйцо ', 'quantity': 2, 'measure': ' шт'},
              {'ingredient_name': 'Молоко ', 'quantity': 100, 'measure': ' мл'},
              {'ingredient_name': 'Помидор ', 'quantity': 2, 'measure': ' шт'}],
    'Утка по-пекински': [{'ingredient_name': 'Утка ', 'quantity': 1, 'measure': ' шт'},
                         {'ingredient_name': 'Вода ', 'quantity': 2, 'measure': ' л'},
                         {'ingredient_name': 'Мед ', 'quantity': 3, 'measure': ' ст.л'},
                         {'ingredient_name': 'Соевый соус ', 'quantity': 60, 'measure': ' мл'}],
    'Запеченный картофель': [{'ingredient_name': 'Картофель ', 'quantity': 1, 'measure': ' кг'},
                             {'ingredient_name': 'Чеснок ', 'quantity': 3, 'measure': ' зубч'},
                             {'ingredient_name': 'Сыр гауда ', 'quantity': 100, 'measure': ' г'}],
    'Фахитос': [{'ingredient_name': 'Говядина ', 'quantity': 500, 'measure': ' г'},
                {'ingredient_name': 'Перец сладкий ', 'quantity': 1, 'measure': ' шт'},
                {'ingredient_name': 'Лаваш ', 'quantity': 2, 'measure': ' шт'},
                {'ingredient_name': 'Винный уксус ', 'quantity': 1, 'measure': ' ст.л'},
                {'ingredient_name': 'Помидор ', 'quantity': 2, 'measure': ' шт'}]}


# print(cook_book.get('Запеченный картофель'))

def get_shop_list_by_dishes(dishes: list, person_count: int):
    count_ingredient = {}
    cook_book = get_cook_book()
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity']
                if ingredient_name in count_ingredient:
                    quantity = count_ingredient[ingredient_name]['quantity'] + quantity
                count_ingredient[ingredient_name] = {'measure': measure, 'quantity': quantity}
    for ingredient_name in count_ingredient:
        if person_count > 0:
            count_ingredient[ingredient_name]['quantity'] *= person_count
        else:
            return 'Ошибка заказа'

    return count_ingredient

order = get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Омлет', 'Утка по-пекински'], 2)
pprint(order)









