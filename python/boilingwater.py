temp = input("enter a number here: ")
ans = (temp*5)-400
if temp >= 80 and temp <=200:
    print(ans)

if temp <= 80:
    print("-1")
elif temp == 0:
    print("0")
elif temp >=80:
    print("1")