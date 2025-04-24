def extract_file_name(full_file_name):
    return full_file_name.split('/')[-1].split('.')[0]


def encrypt_sentence(sentence):
    even_chars = [sentence[i] for i in range(0, len(sentence), 2)]
    odd_chars = [sentence[i] for i in range(1, len(sentence), 2)][::-1]
    return ''.join(even_chars + odd_chars)


def check_brackets(expression):
    stack = []
    for i, char in enumerate(expression):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if not stack:
                return i + 1
            stack.pop()
    return -1 if stack else 0


def reverse_domain(domain):
    return '.'.join(domain.split('.')[::-1])


def count_vowel_groups(word):
    vowels = 'aeiouy'
    word = word.lower()
    count = 0
    in_group = False
    for char in word:
        if char in vowels:
            if not in_group:
                count += 1
                in_group = True
        else:
            in_group = False
    return count