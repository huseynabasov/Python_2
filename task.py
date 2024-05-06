import math
# Task 7
# nums1 = [1, 2, 3, 4, 5]
# nums2 = [4, 5, 6 7, 8]
# result = []
# for i in range(0, len(nums1)):
#     result.append((nums1[i] + nums2[i]) / 2)
# print (f"Verilen listlerin ortalamasi :  {result}")
# -------------------------------------------------------------------------------------------------
# Task 6
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# print([x.lower().split()[0] for x in names])
# -------------------------------------------------------------------------------------------------
# Task 5
# mylist=['sentyabr','avqust','yanvar']
# print([f"{newList} : {len(newList)}" for newList in mylist])
# -------------------------------------------------------------------------------------------------
# Task 2
# my_list = [22, 11, 22, 44, 55, 7, 4, 4, 7, 1, 2, 3, 8, 9]
# print(list({x for x in my_list}))
# -------------------------------------------------------------------------------------------------
# Task 4
# eded = int(input("Reqemi daxil edin: "))
# print(f"Bolenleri tapilacaq reqem {eded} :  {[i for i in range(1, eded + 1) if eded % i == 0]}")

# Task 1
# def kvadrat(input_list):
#     return [
#         num
#         for num in input_list
#         if any(
#             num == i**2 or num == -(i**2) for i in range(1, int(abs(num) ** 0.5) + 1)
#         )
#     ] 
# my_list = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# kvadratEded = kvadrat(my_list)
# print(f"Listdeki bir reqemin kvadrati olan reqemler: {kvadratEded}")
# -------------------------------------------------------------------------------------------------
# Task 2
# def cem(cemlist):
#     return math.prod(cemlist)

# newlist = []
# for i in range(1,5):
#     list=int(input("Reqem daxil edin: "))
#     newlist.append(list)  
# print(f"Verilen reqemler listi: {newlist} ----- Verilen listdeki reqemlerin hasili: {cem(newlist)}")