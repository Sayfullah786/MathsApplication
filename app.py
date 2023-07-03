# from flask import Flask,render_template,request
# import json
# app = Flask(__name__)
#
# @app.route('/')
# def login():
#     return render_template('index.html')
#
# @app.route('/question', methods=['GET', 'POST'])
# def quiz():
#     with open('quiz.json') as file:
#         quiz_data = json.load(file)
#
#     if request.method == 'POST':
#         user_answers = request.form  # Get the submitted form data
#         correct_count = calculate_correct_answers(user_answers, quiz_data)  # Calculate the number of correct answers
#         return render_template('result.html', correct_count=correct_count)
#
#     return render_template('quiz.html', quiz_data=quiz_data)
#
#
# def calculate_correct_answers(user_answers, quiz_data):
#     correct_count = 0
#     for i, question in enumerate(quiz_data['questions']):
#         correct_answer = question['correct_answer']
#         user_answer = user_answers.get(str(i))  # Get the user's answer for each question
#         if user_answer == correct_answer:
#             correct_count += 1
#
#     return correct_count
#
# if __name__ == '__main__':
#     app.run()
#








class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self,value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)






#
#
# Tree = Node(5)
# Tree.insert(6)


# def findmax(nums,k):
#     averages = []
#     for i in range(len(nums) - k + 1):
#         subarray = float(sum(nums[i:i + k]) / k)
#         averages.append(subarray)
#     return float(max(averages))
#
#
#
#
#
#
# nums = [1,12,-5,-6,50,3]
# k = 4
# print(findmax(nums,k))




# print(Tree.right.value)





# def removestars(s):
#     stack = []
#     for char in s:
#         if char == '*':
#             stack.pop(-1)
#         else:
#             stack.append(char)
#     return ''.join(stack)
#
#
#
#
#
# s = "erase*****"
#
# print(removestars(s))
#


# def contains(nums,k):
#    for i in range(0,len(nums)):
#        for j in range(i+1,len(nums)):
#            if nums[i] == nums[j]:
#                diff = abs(i - j)
#                print(diff)
#                if diff <= k:
#                    return True
#                else:
#                    return False
#
# def setway(nums):
#     numsa = set(nums)
#     nu = list(numsa)
#     if nu == nums:
#         return False
#     else:
#         return True
#
#
#
# # print(setway([1,2,3,4]))
#
# # def isaliensorted(words,order):
# #
# #
# #
# # words = ["hello", "leetcode"]
# #
# # order = "hlabcdefgijkmnopqrstuvwxyz"
# # print(isaliensorted(words,order))
#
#
#
# def getlucky(s,k):
#     alp = "abcdefghijklmnopqrstuvwxyz"
#     dig = ''
#     for letter in s:
#         dig += (str(alp.index(letter)+1))
#     curr = [int(i) for i in dig]
#
#     for i in range(k):
#         curr = sum(curr)
#         curr = [int(i)for i in str(curr)]
#
#     ls = [str(i) for i in curr]
#     x = "".join(ls)
#
#     return int(x)
#
#
#
# # print(getlucky(s = "zbax", k = 2))
#
# def maxsubarray(nums):
#     maxsub = nums[0]
#     cursum = 0
#     for num in nums:
#         if cursum < 0:
#             cursum = 0
#         print(cursum)
#         cursum += num
#         maxsub = max(maxsub,cursum)
#
#     return maxsub
#
#
#
#
#
#
#
#
#
#
# # print(maxsubarray(nums = [-2,1,-3,4,-1,2,1,-5,4]))
#
#
# # def degreearray(nums):
#
#
# def wordpattern(pattern,s):
#     s = s.split(' ')
#     pattern = [i for i in pattern]
#     if len(s) != len(pattern):
#         return False
#
#     dictionary = {}
#     maped = set()
#     for i in range(len(pattern)):
#         if pattern[i] not in dictionary:
#             if s[i] in maped:
#                 return False
#             dictionary[pattern[i]] = s[i]
#             maped.add(s[i])
#         else:
#             if dictionary[pattern[i]]!= s[i]:
#                 return False
#     return True
#
#
#
# pattern = "baad"
# s = "dog cat cat dog"
# # print(wordpattern(pattern,s))
#
#
# def twosumhash(nums,target):
#     hashmap ={}
#     for i,j in enumerate(nums):
#         diff = target - j
#         if diff in hashmap:
#             return [hashmap[diff], i]
#         else:
#             hashmap[j] = i
#     return
#
#
#
#
# # print(twosumhash(nums=[2,7,11,13],target=9))
# from collections import Counter
# def majority(nums):
#     x = len(nums)
#     n = Counter(nums)
#
#     y = max(n.values())
#     if y > (x/2):
#         for key, value in n.items():
#             if value == y:
#                 return key
#
#
#
#
#
# # print(majority([3,2,3]))
#
# def smallestnumber(nums1,nums2):
#     commons = [i for i in nums1 if i in nums2]
#     ls = []
#     mew = []
#     ls.append(min(nums1))
#     ls.append(min(nums2))
#     result = int(''.join(map(str, ls)))
#     reversed_num = int(str(result)[::-1])
#     mew.append(reversed_num)
#     mew.append(result)
#     if len(commons) >= 1:
#         com = min(commons)
#         mew.append(com)
#
#     return min(mew)
#
#
# nums1 = [3,5,2,6]
# nums2 = [3,1,7]
# # print(smallestnumber(nums1,nums2))
#
# def longestcommonprefix(strs):
#     res = ""
#     prefix = strs[0]
#
#
#
#
#
#
#
#
#
# #
# # strs = ["flower","flow","flight"]
# # print(longestcommonprefix(strs))
#
#
# def commonfactors(a,b):
#     factors = []
#     for i in range(1,b+1):
#         if b % i == 0 and a % i == 0:
#             factors.append(i)
#     return len(factors)
#
#
# print(commonfactors(a = 25, b = 30))

# def maxprofit(prices):
#     max_profit = 0
#     for i in range(len(prices)-1):
#         for j in range(i+1,len(prices)-1):
#             max_profit = max(max_profit,prices[j] -  prices[i])
#     return max_profit
#
#
# # prices = [1,2]
# # print(maxprofit(prices))
#
# from collections import Counter
# def groupanagrams(strs):
#     matrix = []
#     master = []
#     extra = []
#     for i in range(len(strs)-1):
#         for j in range(i+1,len(strs)-1):
#             if Counter(strs[i]) == Counter(strs[j]):
#                 matrix.append(strs[i])
#                 matrix.append(strs[j])
#
#
#     return matrix,extra
#
# strs = ["eat","tea","tan","ate","nat","bat"]
# # print(groupanagrams(strs))
#
#
# def searchRange(nums,target):
#     if target not in nums:
#         return [-1,-1]
#     low = 0
#     high = len(nums)
#     while low < high:
#         mid = (low+ high) //2
#         print(mid)
#         if nums[mid] == target:
#             return mid
#         elif  nums[high] > target:
#             high -= 1
#         else:
#             low +=1
#     return low,high
# # nums = [5,7,7,8,8,10]
# # target= 8
# # print(searchRange())
#
# def binary(nums,target):
#     if target not in nums:
#         return [-1,-1]
#     if len(nums) == 1 and target == 1:
#         return [0,0]
#
#
#     low,high = 0,len(nums)-1
#     while low != high:
#         if nums[low] < target:
#             low+=1
#         if nums[high]> target:
#             high-=1
#
#         if nums[high] == target and nums[low]==target:
#             return low,high
#
# # nums = [1]
# # target = 1
# # print(binary(nums,target))
#
#
# # def maxarea(height):
# #     low = 0
# #     top = len(height)-1
# #     ls = []
# #     while low < top:
# #         if height[low] < height[top]:
# #             area = height[low] * (top - low)
# #             ls.append(area)
# #
#
#
# def heighchecker(heights):
#
#     copy = sorted(heights)
#     count = 0
#     for i in range(len(heights)):
#         if heights[i] != copy[i]:
#             count+=1
#     return count, heights,copy
#
#
#
# # heights = [1,1,4,2,1,3]
# # print(heighchecker(heights))
#
# import re
#
# def ispalindrome(s):
#
#
#     s = re.sub(r"[^a-zA-Z0-9\\s+]", '', s)
#
#     s = s.strip()
#     x = ''.join(s.split(' ')).lower()
#     return x == x[::-1]
#
# # s = "ab_a"
#
# # print(ispalindrome(s))
#
#
# def strStr(haystack,needle):
#     stock = []
#
# haystack = "sadbutsad"
# needle = "sad"
#
# # print(strStr(haystack,needle))
#
# def reversestring(s):
#     s = s.strip()
#     s = s.split(' ')
#     s = [item for item in s if item.strip()]
#     s = [item + ' ' for item in s]
#
#
#
#
#
#
#     x = ''.join(s[::-1])
#     return x.strip()
# # s = "the sky is blue"
# # print(reversestring(s))
#
# def searchmatrix(matrix,target):
#     for ls in matrix:
#         print(ls[0])
#         for num in range(0,len(ls)):
#             print(num)
#             if ls[num]==target:
#                 return True
#     return False
#
# # matrix = [[1]]
# # target = 1
# # print(searchmatrix(matrix,target))
#
# def longestsubstring(s):
#     charset = set()
#     count = 0
#     for i in s:
#         if i in charset:
#             count = 0
#         else:
#             charset.add(i)
#     return charset
#
# # print(longestsubstring(s = "pwwkew"))
#
# def rotate(nums,k):
#     k = k % len(nums)
#     nums[:] = nums[len(nums)-k:] + nums[0:len(nums)-k]
#     return nums
# #
# #
# #
# #
# # nums = [1,2,3,4,5,6,7]
# # k = 3
# # print(rotate(nums,k))
#
# def uniqueoccurences(arr):
#     num = []
#     k = set(arr)
#     for i in k:
#         num.append(arr.count(i))
#
#
#     dif = sorted(set(num))
#
#     return sorted(num) == dif
#
# print(uniqueoccurences(arr = [1,2,2,1,1,3]))

from collections import Counter
# def makeequal(words):
#
#
#
# print(makeequal(words = ["abc","aabc","bc"]))

