# from django.test import TestCase
import collections
import random

# Create your tests here.
# # 汉诺塔原理
# def hannoi(n, a, b, c):
#     if n > 0:
#         hannoi(n - 1, a, c, b)
#         print("from %s move %s", (a, c))
#         hannoi(n - 1, b, a, c)
#
#
# print(hannoi(64, "a", "b", "c"))
#
#
# # 顺序查找
# def liner_search(list, val):
#     for index, v in enumerate(list):
#         if v == val:
#             return index
#         else:
#             return None


# 二分查找法  对有序的数据进行查找
# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:  # 候选区有值
#         mid = (left + right) // 2
#         if li[mid] == val:
#             return mid
#         elif li[mid] > val: #待查找的值在左侧
#             right = mid - 1
#         else:  # li[mid]>val: #待查找的值在右侧
#             left = mid + 1
#     else:
#         return None
#
#


# li = [1, 3, 4, 6, 7, 8, 9, 10]
# print(binary_search(li, 7))


# 冒泡排序
list = [random.randint(0, 15) for w in range(15)]


# print(list)
# def maop(list):
#     n = len(list)
#     for x in range(n-1):
#         exchange = False # 增加标签判断。如果发现一次比较中没有发生位移变化。那么代表全部有序
#         for y in range(n - x - 1):
#             if list[y] > list[y+1]:
#                 list[y], list[y+1] = list[y+1], list[y]
#                 exchange = True
#         if not exchange:
#             return list
# print(maop(list))

# 选择排序

# def choice_sort(list):
#     for x in range(len(list)-1):
#         min_loc = x
#         for j in range(x+1,len(list)):
#             if list[j]<list[min_loc]:
#                 min_loc = j
#         if min_loc !=x:
#             list[x],list[min_loc] = list[min_loc],list[x]
#     return list
#
# print(choice_sort(list))


# 插入排序

# def insert_sort(list):
#     for x in range(1, len(list)):
#         tmp = list[x]
#         j = x - 1
#         while j >= 0 and tmp < list[j]:
#             list[j + 1] = list[j]
#             j -= 1
#         list[j + 1] = tmp
#     return list
#
#
# print(insert_sort(list))


# 快速排序
# def partiton(list, left, right):
#     print(list)
#     tmp = list[left]
#     while left < right:
#         while left < right and tmp <= list[right]:
#             right -= 1
#         list[left] = list[right]
#         print(list, "left")
#         while left < right and tmp >= list[left]:
#             left += 1
#         list[right] = list[left]
#         print(list, "right")
#     list[left] = tmp
#     print(list, "最终")
#     return left
#
#
# def quick_sort(list, left, right):
#     if left < right:
#         mid = partiton(list, left, right)
#         quick_sort(list, 0, mid - 1)
#         quick_sort(list, mid + 1, right)
#     return list
#
#
# print(quick_sort(list, 0, len(list) - 1))

# 斐波那契数列 爬楼梯。一次上1层或2层一共多少种 f(n) = f(n-1)+f(n-2)
# def palo(n):
#     if n <= 3: return n
#     sum = 0
#     for i in range(3,n):
#         sum += (i-1) + (i-2)
#     return sum
#
#
# print(palo(5))

# 一次性买卖股票最大利润
# def maxOrifit(pirces):
#     min_price = pirces[0]
#     max_profit = 0
#     for price in pirces:
#         min_price = min_price if min_price<price else price
#         max_profit = max_profit if max_profit>price-min_price else price - min_price
#     return max_profit
# print(maxOrifit(list))


# 替换字符串中的内容
# def replacess(s:str):
#     return "%20".join(s.split(" "))
#
# print(replacess("We are happy."))


# class Solution:
#     def fib(n):
#         dp = [1,1, 2]
#         for i in range(3, n+1 ):
#             dp.append(dp[i - 1] + dp[i - 2])
#             print(dp)
#         return dp[n] % 1000000007
#
# print(Solution.fib(0))
# li = []
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# len1 = matrix[2][::-1]
#
# # for i in range(len(len1)):
# #     li.append(len1[i])
# li.append(len1[-1])
# print(li)
#
# class Node(object):
#     def __init__(self, item):
#         self.elem = item
#         self.lchild = None
#         self.rchild = None
#
#
# class Tree(object):
#     def __init__(self):
#
#         self.root = None
#
#     def add(self,item):
#         node = Node(item)
#         if self.root is None:
#             self.root = node
#             return
#         queue = [self.root]
#
#         while queue:
#             cur_node = queue.pop(0)
#             if cur_node.lchild is None:
#                 cur_node.lchild = node
#                 return
#             else:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is None:
#                 cur_node.rchild = node
#                 return
#             else:
#                 queue.append(cur_node.rchild)
#
#     def breadth_travel(self):
#         """广度遍历"""
#         if self.root is None:
#             return
#         queue = [self.root]
#         cur_node = queue.pop(0)
#         print(cur_node.elem, end=" ")
#         while queue:
#             if cur_node.rchild is not None:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is not None:
#                 queue.append(cur_node.rchild)
#
#     """先序遍历"""
#
#     def preorder(self, node):
#         if node is None:
#             return
#         print(node.elem, end=" ")
#         self.preorder(node.lchild)
#         self.preorder(node.rchild)
#     """中序遍历"""
#
#     def inorder(self, node):
#         if node is None:
#             return
#
#         self.inorder(node.lchild)
#         print(node.elem, end=" ")
#         self.inorder(node.rchild)
#     """后序遍历"""
#
#     def postorder(self, node):
#         if node is None:
#             return
#
#         self.postorder(node.lchild)
#         self.postorder(node.rchild)
#         print(node.elem, end=" ")
#
#
#
#
# if __name__ == "__main__":
#     tree = Tree()
#     tree.add(0)
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(4)
#     tree.add(5)
#     tree.add(6)
#     tree.add(7)
#     tree.add(8)
#     tree.add(9)
#     tree.breadth_travel()
#     print(" ")
#     tree.preorder(tree.root)


