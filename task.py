def exceedLimit(litrs):
    sum = 0
    for litre in litrs:
        sum += litre
        if (sum > 10000):
            return "Capacity exceeded"
    return "Capacity not exceeded"    

print(exceedLimit([1200,1800,1500,2000,1750,1400,1650]))

# def exceedFive(values):
#     sorted_array = sorted(values)
#     array = []
#     for value in values:
#         if(value > 5):
#             array.append(value)
#     return array   


# def duplicateZero(values):
#      for i in range(len(values)):
    
#          for j in range(len(values[i])):
#              if(values[i][j] and values[i][j+1] == 0):
#                  return values[i]
         
          

         
# # def averageRoute(lists):
# #     for i in range()

        