

cats = 0
while True:
    heads = int(input("enter the total number of heads"))
    legs = int(input("enter the total number of legs:"))
    chicken = int(heads - cats)

    if legs % 2 != 0 or heads == 0 or heads > legs:

        print('No solution')
    else:
        cats = int((legs + (-2 * heads)) / 2)
        chicken = int(heads - cats)

        print('{} {}'.format(chicken, cats))
    break
