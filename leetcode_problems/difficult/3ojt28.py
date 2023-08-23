# 28.Standardize mobile numbers when given N mobile numbers. Sort them in ascending order. Print them in the standard format.
def standardize_mobile(N):
    N.sort()
    SF = []
    for i in range(len(N)):
        SF.append("+91 "+N[i])
    return(SF)
List=["8095355871","9980132533","7123456789"]
 
print(standardize_mobile(List))

# def standardize(mob_nums):
#     n = len(mob_nums)

#     for passes in range(n - 1, 0, -1):
#         for i in range(passes):
#             if mob_nums[i] > mob_nums[i + 1]:
#                 mob_nums[i], mob_nums[i + 1] = mob_nums[i + 1], mob_nums[i]
# mob_nums = [766865, 769865, 767865, 764865, 762865, 761865]
# standardize(mob_nums)
# print(mob_nums)

