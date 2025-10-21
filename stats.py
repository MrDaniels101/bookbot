def text_count(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    counts = {}
    for char in text.lower():
        if char in counts:
            counts[char] += 1   
        else:
            counts[char] = 1
    return counts


def by_num(item):
    return item["num"]

def sorted_chars(char_counts):
    results = []
    for char, num in char_counts.items():
        if char.isalpha():
            results.append({"char":char, "num":num})
    results.sort(key=by_num, reverse=True)
    return results