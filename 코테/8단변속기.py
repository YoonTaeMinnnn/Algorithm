import sys
input = sys.stdin.readline

l = list(map(int, input().split()))
com = [i for i in range(1, len(l)+1)]
com2 = [i for i in range(len(l), 0, -1)]


if l == com:
    print("ascending")
elif l == com2:
    print("descending")
else:
    print("mixed")