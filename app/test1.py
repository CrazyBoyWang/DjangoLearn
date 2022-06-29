import random
import heapq

list = [random.randint(0, 15) for w in range(15)]
print(list, "初始列表")


# def maop(list):
#     for i in range(len(list)-1):
#         for j in range(len(list)-1-i):
#             print(list,"循环{0}".format(j))
#             if list[j]>list[j+1]:
#                 list[j],list[j+1] = list[j+1],list[j]
#     return list


#
# def maop(list):
#     for i in range(len(list)):
#         for j in range(len(list)-1):
#             print(list, "循环{0}".format(j))
#             if list[i]<list[j]:
#                 list[i], list[j] = list[j], list[i]

# return list

# print(maop(list),"排序后列表")

#
# def insert_sort(list):
#     for i in range(1,len(list)):
#         temp = list[i]
#         j = i-1
#         while j>=0 and temp<list[j]:
#             list[j+1] = list[j]
#             j-=1
#         list[j+1] = temp
#     return list
#
# print(insert_sort(list))
#


# def sift(list,low,high):
#     """
#     :param list: 列表
#     :param low: 堆的跟节点位置
#     :param high: 堆的最后一个元素的位置
#     :return:
#     """
#     i = low #i最开始指向跟节点
#     j = 2 * i +1 # 最近的左子节点
#     tmp = list[low] #把堆顶存起来
#     while j<=high: # 只要j位置有数，就会循环下去
#         if j<=high<=high and list[j+1]>list[j]:# 如果右边有，并且大于左边
#             j = j+1 #指向右子节点
#         if list[j]>tmp:
#             list[i] = list[j]
#             i = j   #往下一层
#             j = 2 *i +1
#         else:
#             list[i] = tmp
#             break
#
#     else:
#         list[i] = tmp
#
#
# def heap_sort(list):

# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1  # left = 2*i + 1
#     r = 2 * i + 2  # right = 2*i + 2
#
#     if l < n and arr[i] < arr[l]:
#         largest = l
#
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # 交换
#
#         heapify(arr, n, largest)
#
#
# def heapSort(arr):
#     n = len(arr)
#
#     # Build a maxheap.
#     for i in range(n, -1, -1):
#         heapify(arr, n, i)
#
#         # 一个个交换元素
#     for i in range(n - 1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]  # 交换
#         heapify(arr, i, 0)
#
#
# arr = list
# heapSort(arr)
# n = len(arr)
# print("排序后")
# for i in range(n):
#     print("%d" % arr[i])


# def heapfy(list, n, i):
#     largest = i  # 定义根节点
#     l = 2 * i + 1  # 左子节点
#     r = 2 * i + 2  # 右子节点
#     if l < n and list[largest] < list[l]:
#         largest = l
#     if r < n and list[largest] < list[r]:
#         largest = r
#     if largest != i:
#         list[i], list[largest] = list[largest], list[i]
#         heapfy(list, n, largest)
#
#
# def heapSort(list):
#     n = len(list)
#     for i in range(n, -1, -1):  # 自底向上建堆
#         heapfy(list, n, i)
#
#     for i in range(n - 1, -1, -1):
#         list[i], list[0] = list[0], list[i]  # 交换
#         heapfy(list, i, 0)
#     return list
#
#
# print(heapSort(list))
#
# def kuaisu(list,left,right):
#     while left<right:
#         temp = list[left]
#         while left<right and temp <=list[right]:
#             right-=1
#         list[left] = list[right]
#         while left<right and temp >= list[left]:
#             left+=1
#         list[right] = list[left]
#         list[left] = temp
#         return left
#
# def quick_sort(list,left,right):
#     if left<right:
#         mid = kuaisu(list,left,right)
#         quick_sort(list,0,mid-1)
#         quick_sort(list,mid+1,right)
#     return list
# print(quick_sort(list,0,len(list)-1))

