group = str(input("Введите группу: "))
def entry_message():
    if group == "Т118":
        return ("Т118: вход разрешён")
    else:
        return ("Обратитесь к куратору")
check_entry = entry_message
print(check_entry())
print(type(check_entry("Т118")))

#==========================================================================

def standard_fare(km): return 500+100*km
def student_fare(km): return 300+70*km
def trip_cost(km, tariff): return tariff(km)
print (trip_cost(10, standard_fare))
print (trip_cost(10, student_fare))
print (trip_cost(0, standard_fare))
print (trip_cost(0, student_fare))
print(trip_cost(1, standard_fare))
print(trip_cost(1, student_fare))

#==========================================================================

def make_discount(amount):
    def discount(price):
        result = price - amount
        if result < 0:
            return 0
        return result
    return discount
discount_0 = make_discount(500)
discount_100 = make_discount(100)
discount_300 = make_discount(300)
print(discount_100(250))
print(discount_300(250))
print(discount_100(100))
print(discount_100(0))
print(discount_300(500))
print(discount_100(500))
print(discount_0(500))
print(discount_100(101))
print(discount_100(99))
#1 0
print(type(discount_100(100)))
print(type(discount_100(250)))

#==========================================================================

def check_case(function, value, expected):
    actual = function(value)
    return actual == expected
def ekeb_price(price):
    if price >= 1000:
        return price - 100
    return price
discount_100 = check_case(ekeb_price, 250, 150)
print(discount_100)
print (check_case (ekeb_price, 999, 999))
print(check_case (ekeb_price, 1000, 900))
print (check_case (ekeb_price, 1001, 901))
print()
def wrong_price(price):
    return price - 100
print (check_case (wrong_price, 999, 999))
print(check_case (wrong_price, 1000, 900))
print (check_case (wrong_price, 1001, 901))