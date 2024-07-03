def min_max(num_list):
    minimum = num_list[0]
    maximum = num_list[0]
    for n in num_list:
        if n < minimum:
            minimum = n
        if n > maximum:
            maximum = n
    return [minimum, maximum]

print(min_max([6,9,0,-4,-2,10,7]))