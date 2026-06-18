def count_vowels(word: str) -> int:
    """
    计算单词中元音字母的数量
    """
    vowel_count = 0
    for letter in word:
        if letter.lower() in "aeiou":
            vowel_count += 1
    return vowel_count

from itertools import groupby
words: list[str] = ['cat', 'dog', 'elephant', 'mood', 'banana', 'mate']
sorted_words: list[str] = sorted(words, key=count_vowels) # 按照元音字母数量排序
grouped: groupby = groupby(sorted_words, key=count_vowels) # 按照元音字母数量分组

for vowel, group in grouped:
    print(f'{vowel=},{list(group)}')
"""
vowel=1,['cat', 'dog']
vowel=2,['mood', 'mate']
vowel=3,['elephant', 'banana']
"""