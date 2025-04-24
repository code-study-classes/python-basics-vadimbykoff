def is_weekend(day):
    return day == 6 or day == 7


def get_discount(amount):
    if amount >= 5000:
        return amount * 0.10
    elif amount >= 1000:
        return amount * 0.05
    return 0


def describe_number(n):
    n_str = str(n)
    parity = "четное" if n % 2 == 0 else "нечетное"
    length = len(n_str)
    return f"{parity} {length}-значное число"


def convert_to_meters(unitNumber, lengthInUnits):
    units = {1: 0.1, 2: 1000, 3: 1, 4: 0.001, 5: 0.01}
    return lengthInUnits * units[unitNumber]


def describe_age(age):
    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "", "двадцать", "тридцать", "сорок", "пятьдесят", "шестидесят", "семьдесят", "восемьдесят", "девяносто"]
    
    if age < 20:
        return ones[age] + " лет"
    return tens[age // 10] + " " + ones[age % 10] + " лет"