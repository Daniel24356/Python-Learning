# def extract_vowels(lists):
#     array = []
#     vowels = "aeiouAEIOU"
#     for i in range(len(lists)):
#         for j in range(len(lists[i])):
#             if(lists[i][j] in vowels):
#                 array.append(lists[i][j])
#     return array

# print(extract_vowels(["cat", "apple"]))

# def findAllEvenNumber(lists):
#     array = []
#     for i in range(len(lists)):
#         for j in range(len(lists[i])):
#             if(lists[i][j] % 2 == 0):
#                 array.append(lists[i][j])
#     return array

# print(findAllEvenNumber([[1,2,3],[4,5,6]]))


# def matrix_to_string(lists):
#     empty_string = ""
#     for i in range(len(lists)):
#         for j in range(len(lists[i])):
#             empty_string += lists[i][j]           
#     return empty_string

# matrix_to_string([['H','i'],['!']])        

# def flatten_list(lists):
#     array = []
#     for i in range(len(lists)):
#         for j in range(len(lists[i])):
#             array.append(lists[i][j])
#     return array

# flatten_list([[1,2],[3,4]])        

# def count_zeros(lists):
#     sum = 0
#     for i in range(len(lists)):
#         for j in range(len(lists[i])):
#             if lists[i][j] == 0:
#                 sum = sum + 1
#     return sum   

# count_zeros([[0,1,0],[2,0,3]])           

# def reverseSentence(str):
#     lists = str.split(' ')
#     array = []
#     last = len(lists) - 1
#     for i in range(len(lists)):
#         array.append(lists[last-i])
#     return " ".join(array)    

# print(reverseSentence("I love Python"))

# def removeDuplicates(lists):
#     i = 0
#     while i < len(lists) - 1:
#         if lists[i] == lists[i+1]:
#             lists.pop(i)
#         else:
#             i += 1
#     return lists

# print(removeDuplicates([1, 2, 4, 3, 2, 4, 5]))



# def countCharFreq(s):
#     for i in range(len(s)):
#         count = 0
#         for j in range(len(s)):
#             if s[i] == s[j]:
#                 count += 1
#         print(f"{s[i]}: {count}")

# countCharFreq("banana")

# def mergeTwoSortedList(list1, list2):
#     singleList = list1 + list2
#     for i in range(len(singleList) -1):
#         if(singleList[i] > singleList[i+1]):
#             singleList[i+1] = singleList[i]
#             singleList[i] = singleList[i + 1]
#     return singleList

# print(mergeTwoSortedList([1, 3, 5],[2, 4, 6]))       

# def longestWordInString(text):
#     words = text.split(' ')
#     i = 0
#     while i < len(words) - 1:  # use while since we might pop
#         if len(words[i]) < len(words[i + 1]):
#             words.pop(i)  # remove current if shorter
#         elif len(words[i]) == len(words[i + 1]):
#             words.pop(i + 1)  # remove the later one if same length
#         else:
#             i += 1  # move forward only if nothing removed
#     return words[0]  # only one word should remain

# print(longestWordInString("The quick brown fox jumps over the lazy dog"))
       

# from typing import Counter


# def countCharFreq(s):
#     return dict(Counter(s))

# print(countCharFreq("banana"))

# def longestWordInString(sentence):
#     words = sentence.split()
#     return max(words, key=len)

# print(longestWordInString("I love programming in Python"))
# # # Output: programming

# def minimumOutput(lists):
#     min_value = min(lists)
#     day = lists.index(min_value)
#     return f"Lowest yield: {min_value} bag on day {day}"

# print(minimumOutput([45, 60, 38, 55, 70, 42, 39, 48]))    




            




    