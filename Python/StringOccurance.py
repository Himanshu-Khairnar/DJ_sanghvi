def word_occurrences():
    text = input("Enter a string: ")

    words = text.lower().split()

    word_count = {}

    for word in words:
        word = word.strip(",.!?;:")  
        word_count[word] = word_count.get(word, 0) + 1


    print("\n--- Word Occurrences ---")
    for word, count in word_count.items():
        print(f"{word} : {count}")



word_occurrences()
