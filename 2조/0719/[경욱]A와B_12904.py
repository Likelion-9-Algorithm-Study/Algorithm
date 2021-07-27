import sys
input = sys.stdin.readline
s = input().strip()
t = input().strip()

while True:
    if t[-1] == "A":
        t = t[:-1]
    elif t[-1] == "B":
        t = t[:-1]
        t = "".join(reversed(t))
    if t == s:
        print(1)
        break
    elif t != s and len(t) == len(s):
        print(0)
        break
# import sys
# input = sys.stdin.readline
# s = input().strip()
# t = input().strip()


# def bfs(s):
#     need_visit = [s]
#     while need_visit:
#         temp_list = set()
#         for i in need_visit:
#             a = i + "A"
#             b = "".join(reversed(i)) + "B"
#             if a == t or b == t:
#                 return 1

#             # if len(a) > len(t) or len(b) > len(t):
#             #     return 0
#             temp_list.add(a)
#             temp_list.add(b)
#         need_visit = list(temp_list)
#     return 0


# result = bfs(s)
# print(result)

# b
# ba-1 / bb
# baa / abb-1 / bba / bbb
# baaa / aabb / abba-1 / bbab /bbaa / abbb / bbbb /bbba
# abba

