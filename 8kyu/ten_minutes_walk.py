
#You live in the city of Cartesia where all roads are laid out in a perfect grid.
# You arrived ten minutes too early to an appointment,
# so you decided to take the opportunity to go for a short walk.
# The city provides its citizens with a Walk Generating App on their phones --
# everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg.
# ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction)
# and you know it takes you one minute to traverse one city block,
# so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will,
# return you to your starting point. Return false otherwise.
def isValidWalk(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
# def is_valid_walk(walk):
#     #determine if walk is valid
#     north = 0
#     south = 0
#     west = 0
#     east = 0
#     for i in walk:
#         if i == 'n':
#             north += 1
#         elif i == 's':
#             south += 1
#         elif i == 'w':
#             west += 1
#         else:
#             east += 1
#     if (north == south and west == east) and len(walk) == 10:
#         return True
#     else:
#         return False
#
# print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))