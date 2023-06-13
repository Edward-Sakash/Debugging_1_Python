numbers = [1,2,3,5]
def get_total(lst, bla='hello'):
    index = 0
    total = 0
    while index < len(lst):
        total += lst[index]
        index += 1
        
    print(total)

    return total

print(get_total(numbers))