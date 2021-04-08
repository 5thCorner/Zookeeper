ingredient = str(input())
pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"
lst = (('pasta', pasta), ('apple pie', apple_pie), ('ratatouille', ratatouille), ('chocolate cake', chocolate_cake), ('omelette', omelette))

for i in range(len(lst)):
    if ingredient in lst[i][1]:
        print(lst[i][0] + ' time!')
