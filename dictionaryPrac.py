def countWordFreq(str):
    str_lists = str.lower().split(" ")
    # count = 1
    dic = {}
    for list in str_lists:
        if list not in dic:
            dic[list] = 0
        dic[list] += 1
    return dic 

# print(countWordFreq("I love Python and I love coding"))

# def mostFreqChar(str):
#     dic = {}
#     # count = 0
#     for char in str:
#         if char not in dic:
#             dic[char] = 0
#         dic[char] += 1
#     return max(dic, key=dic.get) # the max is acting as a loop. it loops through the dic and the key gets the max value and it returns the key with that max value

# print(mostFreqChar("banana"))

# def groupWordsByFirstLetter(lists):
#     dic = {}
#     for list in lists:
#         if list[0] not in dic:
#             dic[list[0]] = []
#         dic[list[0]].append(list)
#     return dic

# print(groupWordsByFirstLetter(["apple", "ant", "banana", "ball", "cat"]))

# def invertDic(d):
#     return {v: k for k, v in d.items()}

# print(invertDic({1: 'a', 2: 'b', 3: 'c'}))

# def countCharFreq(lists):
#     count = 0
#     dic = {}
#     for i in lists:
#         for j in i:
#             if j not in dic:
#                 dic[j] = 0
#             dic[j] += 1  
#     return dic          

        
# print(countCharFreq(["cat", "dog", "cow"]))   


# def mergeTwoDict(a, b):




















