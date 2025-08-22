# #1. Digit Classifier
# def digitClassifier(number):
#     if(number == 0):
#         print("Zero")
#     elif(number%2 == 0 and number%3 == 0):
#         print("Even and divisible by 3")   
#     elif(number%2 == 0):
#         print("Even")
#     else:
#         print("Odd")

# digitClassifier(9)        

# # 2. Reverse Engineering
# def reverseEngineering(number):
#     reversedNum = 0
#     number = abs(number)
#     while number > 0:
#         reversedNum = reversedNum * 10 + number % 10
#         number //= 10
#     return reversedNum
# print(reverseEngineering(1234))

# # 3. List Compression
# def listCompression(values):
#     result = []
#     for value in values:
#         if value % 2 == 0:
#             result.append(value * 2)
#     return result

# print(listCompression([2,3,4,5,6]))

# # 4. Collatz Conjecture
# def collatConjecture(n):
#     steps = 0
#     while n != 1:
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3 * n + 1
#         steps += 1
#     return steps

# print(collatConjecture(6))

# # 5. Second Largest
# #   def secondLargest(values):
      
# # 6. Missing Number in Sequence
# def missingNumInSeq(values):
#     for i in range(len(values) - 1):  
#         if values[i+1] - values[i] != 1:
#             return values[i] + 1
#     return None 
         
# print(missingNumInSeq([1,2,3,4,5,6,7,9]))        

# # 7. Palindrome Checker
# def palindromeChecker(numberList):
#       last = len(numberList) - 1
#       for i in range(len(numberList) // 2):
#         if numberList[i] != numberList[last - i]:
#             return False
#       return True

# print(palindromeChecker([4,3,4,3,4]))

# # 8. Count Digits Without String Conversion
# # def countDigitsWithoutConv():

# # 9. Unique Elements Only
# def uniqueElementsOnly(values):
#     return len(values) == len(set(values))

# print(uniqueElementsOnly(["1","2","3","4","5","5","5"]))


# # 10. Maximum Difference
# def maximumDiff(values):
#     sorted_list = sorted(values)
#     return sorted_list[-1] - sorted_list[0]
    
# maximumDiff([2,4,5,6,8,9])

