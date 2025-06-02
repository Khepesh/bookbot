from collections import Counter

def get_word_count ( text ):
    words = text.split()
    return len(words)

def get_character_count ( text ):
    counts = {}
    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts