quote = "To learn, one must be humble. But life is the great teacher."

print(f"Original String: {quote}")

for word in quote.split():
    word = word.strip('.').lower()
    print(f"Word {word} has {len(word)} characters.")


