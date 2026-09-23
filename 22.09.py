city = "Алматы" #глобальная
def show_trip():
    city = "Шымкент" #локальная
    print("Поездка ЕКЕВ: ", city)
show_trip()
print("Исходный город: ", city)

#===================================================================

total = 10000
def lunch_total (price, quantity):
    total = price * quantity
    return total
result = lunch_total(1200, 3)
print(result)
print(lunch_total(1200, 0))
print(lunch_total(0, 2))
print(total)

#===================================================================

bugs_found = 0
def register_bugs (amount):
    global bugs_found #добавил
    bugs_found += amount
    return bugs_found
print(register_bugs(2))
print(register_bugs(3))
print(register_bugs(0))

#===================================================================

def make_counter ():
    count = 0
    def next_check ():
        nonlocal count
        count += 1
        return count
    return next_check
counter_a = make_counter()
counter_b = make_counter()
print(counter_a())
print(counter_a())
print(counter_b())
print(counter_a())
print(counter_b())

#===================================================================

def make_wallet(start_balance):
    balance = start_balance
    def buy(price):
        nonlocal balance
        if price <= balance:
            balance -= price
            return balance
        else:
            return -1
    return buy
ekeb_wallet = make_wallet(2000)
trip_wallet = make_wallet(500)
print(ekeb_wallet(700))
print(ekeb_wallet(1500))
print(ekeb_wallet(300))
print(ekeb_wallet(1000))
print(ekeb_wallet(1))
print(ekeb_wallet(0))
print(trip_wallet(200))
empty_wallet = make_wallet(0)
print(empty_wallet(0))
print(empty_wallet(1))