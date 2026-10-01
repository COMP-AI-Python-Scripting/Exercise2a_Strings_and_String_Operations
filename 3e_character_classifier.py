def count_characters_digits_symbols(sample):
    character_count = 0
    digit_count = 0
    symbol_count = 0
    for character in sample:
        if character.isalpha():
            character_count += 1
        elif character.isdigit():
            digit_count += 1
        # if it is not letter or digit then it is a special symbol
        else:
            symbol_count += 1

    print(f"Characters = {character_count}, Digits = {digit_count}, Symbol = {symbol_count}")

sample_str = "Lfg143~@dr&&21ccx"
print(f"For input '{sample_str}':")
count_characters_digits_symbols(sample_str)
