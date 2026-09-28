quote = "To learn, one must be humble. But life is the great teacher."

print(f"Original String: {quote}")

for i, word in enumerate(quote.split(),1):
    word = word.strip('.').lower()
    print(f"Word {i}: '{word}' has {len(word)} characters.")


