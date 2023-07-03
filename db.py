import mysql.connector

db = mysql.connector.connect(host='localhost',user='root',password='apple')


# def findKthPositive(arr, k):
#     ls = [i for i in range(1,1001)]
#     em = [j for j in ls if j not in arr]
#     return em[k-1]
#
#
#
#
#
#
# arr = [2,3,4,7,11]
# # k = 5
#
# # print(findKthPositive(arr,k))
#
# def pivotIndex(nums):
#     for i in range(len(nums)):
#         sumleft = sum(nums[:i])
#         sumright = sum(nums[i+1:])
#         if sumleft == sumright:
#             return i
#
#     return -1
#
#
#
# nums = [-1,-1,0,1,1,0]
#
# # print(pivotIndex(nums))
#
# # def conse(s,k):
# #     vowels = ['a', 'e', 'i', 'o', 'u']
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # s = "aeiou"
# # k = 2
# # print(conse(s,k))
#
#
# def findMaxAverage(nums,k):
#     l = 0
#     r = 4
#     for i in range(  )
