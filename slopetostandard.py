formula = input("Enter slope formula: ")

lst = formula.split("=")
for x in lst:
    if "+" in x:
        y = lst[0]
        temp=lst[1].split("+")
        mx = temp[0]
        answer = temp[1]

    elif "-" in x:
        y = lst[0]
        temp=lst[1].split("-")
        mx = temp[0]
        answer = temp[1]

if "+" in formula:
    print("Youre ansswer do be: {} - {} = {} :flushed:".format(mx, y, answer))
else:
    print("Youre ansssswer do be: {} + {} = {} :flushed:".format(mx, y, answer))
## print(lst)
