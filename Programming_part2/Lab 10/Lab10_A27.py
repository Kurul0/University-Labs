def find_operators (text):
    valid_signs = {'<', '>', '=', '!'}
    return valid_signs.intersection(text)

user_input = input("\nEnter your data with relational operators:\n\n")
result = find_operators (user_input)
print(f"\nThe result is {result}\n")