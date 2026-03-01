# Write a Python function filter_even_numbers(data)
# that takes a list of numbers and returns a list of
# only the even numbers. Use exception handling to
# skip any non-integer values in the list.

output = []
data = ["4", "5", "6", "7.5", "9"]

def filter_even_numbers(input):

    for d in input:
        try:
            numb = int(d)
            if numb % 2 == 0:
                output.append(numb)
            else:
                raise ValueError(f"Invalid number {d}")
        except ValueError as e:
            print(e)
            
    print(output)

filter_even_numbers(data)

