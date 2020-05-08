s = input()

a = len(s)

for i in range(a//2):
    if s[i] != s[-1-i]:
        print("It's not palindrome")
        quit()

print("It's palindrome")
