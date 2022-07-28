def cakes(recipe, available):
    '''Function returns the maximum number of cakes that pete can bake based on the recipe and ingredients'''
    if len(recipe) > len(available):
        return 0
    else:
        ratio = []
        for ingredient in recipe:
            ratio.append(int(available[ingredient]/recipe[ingredient]))
        return min(ratio)


def cakes_best(recipe, available):
    return min([available[i] // recipe[i] if i in available else 0 for i in recipe])

def cakes_2(recipe, available):
    try:
        return min([available[a]/recipe[a] for a in recipe])
    except:
        return 0