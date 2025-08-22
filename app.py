weight = int(input("Weight:"))
unit = input("(K)g or (L)bs:")

if unit.upper() == 'L':
    convert = weight / 0.46
    print("Weight in kg:" + str(convert))
else:
# #     convert = weight * 0.46
# #     print("Weight in lbs:" + str(convert))

# # numbers = [1,2,3,4,5]
# # for item in numbers:
# #     print(item)

# # i = 0
# # while i < len(numbers):
# #     print(numbers[i])
# #     i = i + 1

# # numbers = range(5, 10, 2)
# # for number in numbers:
# #     print(number)

# # sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# # print(sentence)

# first = 'first'
# mutiline = 'I am good'
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(mutiline.title())
# print(mutiline.replace("good", "ok"))

# print(len(mutiline))
# mutiline += '              '
# print(len(mutiline))
# print(len(mutiline.strip()))
# print(len(mutiline.lstrip()))
# print(len(mutiline.rstrip()))

# title = "menu".upper()
# print(title.center(20,"="))
# print("Coffee".ljust(16,".") + '$1'.rjust(4))
# print("Muffin".ljust(16,".") + '$2'.rjust(4))
# print("Cheesecake".ljust(16,".") + '$4'.rjust(4))

# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])

# print(first.startswith("f"))
# print(first.endswith("t"))

# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# gpa = 3.28
# print(abs(gpa))
