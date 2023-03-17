def count_letters_digits(sentence):
    letter_count = 0
    digit_count = 0

    for char in sentence:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            continue
    
    return [letter_count,digit_count]

print(count_letters_digits("Infosys 123"))
print(count_letters_digits("ABCDEFGH"))



