
def sum_even_digits(number: int) -> int:
    number = abs(number)  # игнорируем знак числа
    total = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            total += int(digit)
    return total


def count_vowel_triplets(text: str) -> int:
    vowels = "aeiouyAEIOUY"
    count = 0
    for i in range(len(text) - 2):
        if text[i] in vowels and text[i + 1] in vowels and text[i + 2] in vowels:
            count += 1
    return count


def find_fibonacci_index(number: int) -> int:
    a, b = 0, 1
    index = 1
    while b < number:
        a, b = b, a + b
        index += 1
    return index if b == number else -1


def remove_duplicates(string: str) -> str:
    if not string:
        return ""
    result = [string[0]]
    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            result.append(string[i])
    return "".join(result)