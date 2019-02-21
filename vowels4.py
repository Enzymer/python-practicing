vowels = ['a', 'e', 'i', 'o', 'u']
word = input("単語を入力して下さい。母音を探します。")
found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:
    if letter in vowels:
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'の出現回数は', v, '回。')

