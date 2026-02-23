# ordered and unique
str = (1, 2, 8, 9, 10, "hoo", 8, 9, 2)

uniq_str = tuple(dict.fromkeys(str))
print(uniq_str)
