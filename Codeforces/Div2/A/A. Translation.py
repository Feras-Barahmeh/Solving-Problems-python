s1 = input()
s2 = input()
s2 = [x for x in s2]
s2.reverse()
s1 = [y for y in s1]
print("YES" if s2 == s1 else "NO")



