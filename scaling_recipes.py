#Kattis: Scaling Recipes
recipes = int(input())



for i in range(recipes):
    main_ingredient = ''
    scaled_main = 0

    ingredients, portions, desired = [int(i) for i in input().split()]
    scaling_factor = desired/portions

    ingredients_list = []
    weights_list = []
    for j in range(ingredients):
        line = input().split()
        name, weight, percentage = line[0], float(line[1]), float(line[2])
        ingredients_list.append(name)
        weights_list.append(percentage)

        if percentage == 100:
            main_ingredient = name
            scaled_main = scaling_factor*weight

    print("Recipe # {}".format(i+1))
    for k in range(ingredients):
        print(ingredients_list[k], round(scaled_main*(weights_list[k]/100), 1))
    print('----------------------------------------')

        

