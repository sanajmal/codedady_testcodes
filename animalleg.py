def main(total, Legs):
    for cats in range(total + 1):
        chickens = total - cats
        if 2 * chickens + 4 * cats == Legs:
            return chickens, cats
    return None, None



# if __name__ == '__main__':
    #try:
Heads = int(input("Input number of heads: "))
Legs = int(input("Input number of legs: "))
result = main(Heads, Legs)

if result:
    if result[0]==None or result[1]==None:
        print("No matching result found")
    else:
        print("Number of chickens are %d and cats are %d." % result)
print("-----------------------------------------------")

    #except TypeError:
        #input("press enter to continue")
