money = int(input("Сколько у вас всего денег? "))
drink_price = int(input("Сколько стоит сок? "))
bun_price = int(input("Сколько стоит булочка? "))
people = int(input("Количество людей:"))
if people < 1:
    people = 1
combo = money // (drink_price + bun_price)
print(f"{combo} человека могут купить комбо")
def  lunch_balance(money, drink_price, bun_price, people=1):
    return money - (drink_price + bun_price)*people
m = lunch_balance(money, drink_price, bun_price, people)
if m > 0:
    print(f"Останется {m} тенге")
elif m < 0:
    print(f"Не хватаeт {m} тенге")
else:
    print("Хватает ровно!")