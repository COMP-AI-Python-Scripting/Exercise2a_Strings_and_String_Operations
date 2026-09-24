def get_middle_three_characters(string1):
    print("Original String is", string1)

    # Find middle index
    middle_index = int(len(string1) / 2)

    # Slice string from (mid - 1) to (mid + 2)
    result = string1[middle_index - 1:middle_index + 2]
    print("Middle three chars are:", result)

get_middle_three_characters("jonathan")
get_middle_three_characters("albert")
get_middle_three_characters("rosalind")
