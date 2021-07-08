n = input()
half = len(n)//2

first = sum(list(map(int,n[:half])))
second = sum(list(map(int,n[half:])))

if (first == second): print("LUCKY")
else: print("READY")