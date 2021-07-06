import sys
N = int(sys.stdin.readline())

b = [0] + [int(sys.stdin.readline()) for i in range(N)]


def DFS():
    result_list = []
    for i in range(1, len(b)):
        visited = [False] * (N+1)
        temp_set_1, temp_set_2 = set(), set()
        need_visit = [i]
        while need_visit:
            temp = need_visit.pop()
            if visited[temp] == False:
                need_visit.append(b[temp])
                temp_set_1.add(temp)
                temp_set_2.add(b[temp])
                visited[temp] = True
            if temp_set_1 == temp_set_2:
                result_list.extend(list(temp_set_2))
    result_list = sorted(list(set(result_list)))
    print(len(result_list))
    for i in result_list:
        print(i)
    return


DFS()


# import sys
# N = int(sys.stdin.readline())


# a = [0] + [i+1 for i in range(N)]
# b = [0] + [int(sys.stdin.readline()) for i in range(N)]


# def DFS():
#     result_list = set()

#     for i in range(1, len(b)):
#         visited = [False] * (N+1)
#         temp_list = []
#         need_visit = [i]
#         while need_visit:
#             temp = need_visit.pop()
#             if visited[temp] == False:
#                 need_visit.append(b[temp])
#                 temp_list.append(b[temp])
#                 visited[temp] = True
#             if b[temp] == i:
#                 result_list.update(temp_list)
#                 break
#     # print(result_list)
#     result_list = sorted(list(result_list))
#     # result_list.sort()
#     print(len(result_list))
#     for i in result_list:
#         print(i)
#     # print(result_list)
#     return


# DFS()
# # print(a, b)
