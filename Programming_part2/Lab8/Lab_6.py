months=input('Enter 12 months in Ukrainian, separated by spaces:\n')
months_list=months.split()
valid_months = [
    "січень", "лютий", "березень", "квітень", "травень", "червень", 
    "липень", "серпень", "вересень", "жовтень", "листопад", "грудень"
]
for word in months_list:
    if word.lower() not in valid_months:
        print(f"'{word}' is not valid. Please restart the program with valid data.\n")
        break
else:
    months_list.sort(key=str.lower)
    print() #відступ
    print('The month list in alphabetical order:\n')
    for i in range(len(months_list)):
        print(months_list[i])