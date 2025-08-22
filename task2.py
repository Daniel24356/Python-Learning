import re

# #3
# def groupAnagrams(sentences):
#     groups = {}

#     for s in sentences:
#         # normalize the sentences
#         cleaned = re.sub(r'[^a-z]', '', s.lower())
#         # sort the normalized sentence
#         key = ''.join(sorted(cleaned))
#         # if the key doesnt exist in groups:
#         if key not in groups:
#             groups[key] = [] #create one
#         groups[key].append(s) # if it exists, add the sentence

#     return list(groups.values()) # return the list of values


# print(groupAnagrams(['Listen to me', 'Enlist to me', 'The eyes', 'They see']))


# #4
# def rankStudentsByAvgScore(dicts):
#     students = []
#     for name, scores in dicts.items():
#         avg = sum(scores) / len(scores)
#         students.append((name, round(avg, 2)))
    
#     #sort by descending order (-x[1]) and if avg is equal sort name by aplabetical order(x[0])
#     sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
#     return sorted_students

# print(rankStudentsByAvgScore({'Alice':[90,85,88], 'Bob':[90,85,88], 'Charlie':[95,80,85]}))
   
# #5
# def assignIdtoUniqWord(sentence):
#     words = sentence.split()
#     mapping = {}
#     encoded = []
#     current_id = 1

#     for word in words:
#         if word not in mapping:     
#             mapping[word] = current_id
#             current_id += 1
#         encoded.append(mapping[word])

#     id_to_word = {v: k for k, v in mapping.items()}
#     return encoded, id_to_word


# print(assignIdtoUniqWord('the cat sat on the mat'))

# #1
# #dont understand question
# # def word_ladder(start, end, dictionary):

# #2
# #dont understand question
# # def snake_game(grid, start, directions, food):









