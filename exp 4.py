from itertools import permutations

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

letters = list(set(word1 + word2 + result))

if len(letters) > 10:
    print("Too many unique letters!")
else:
    for p in permutations(range(10), len(letters)):
        d = dict(zip(letters, p))

        if d[word1[0]] == 0 or d[word2[0]] == 0 or d[result[0]] == 0:
            continue

        n1 = int(''.join(str(d[ch]) for ch in word1))
        n2 = int(''.join(str(d[ch]) for ch in word2))
        n3 = int(''.join(str(d[ch]) for ch in result))

        if n1 + n2 == n3:
            print("\nSolution Found")
            print(word1, "=", n1)
            print(word2, "=", n2)
            print(result, "=", n3)
            break
