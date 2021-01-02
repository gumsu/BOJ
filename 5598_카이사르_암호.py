a = input()

tmp = ''
for i in a:
    tmp += chr((ord(i) -65 -3 + 26) % 26 + 65)
print(tmp)