user_data = input("Enter 12 months in Ukrainian, separated by spaces:\n") + " "
months_list = []
while len(user_data) > 0:
    space_ind = user_data.find(' ')
    word = user_data[:space_ind]
    months_list.append(word.lower())
    user_data = user_data[space_ind + 1:]
valid_months = [
    "січень", "лютий", "березень", "квітень", "травень", "червень", 
    "липень", "серпень", "вересень", "жовтень", "листопад", "грудень"
]
for word in months_list:
    if word not in valid_months:
        print(f"'{word}' is not valid. Please restart the program with valid data.\n")
        break
else:
    n = len(months_list)
    for i in range(n - 1):
        for j in range(n - 1):
            if months_list[j] > months_list[j+1]:
                months_list[j], months_list[j+1] = months_list[j+1], months_list[j]
    print() #відступ
    print("The month list in alphabetical order:\n")
    for word in months_list:
        print(word)