
s = input()
s_lower = s.lower()
n = s_lower.count('a')
if n > 0:
    print(f'A letra "a" acontece {n} vezes na string {s}')
else:
    print(f'A letra "a" não faz parte da string {s}')
