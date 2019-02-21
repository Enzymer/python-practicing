vowels = ['a', 'e', 'i', 'o', 'u']
word = input("単語を入力して下さい。母音を探します。")
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'の出現回数は', v, '回。')


