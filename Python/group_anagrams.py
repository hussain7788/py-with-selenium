from collections import defaultdict

def group_anagrams(words):
    anagram_groups = defaultdict(list)
    import pdb;pdb.set_trace()
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)

    result = [group for group in anagram_groups.values() if len(group) > 1]
    return result

input_words = ['eat', 'tae', 'save', 'vase', 'avse']
output_groups = group_anagrams(input_words)
print(output_groups)