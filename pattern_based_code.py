# PATTERN 1
# ****
# ****
# ****
# ****
#
# def print_star():
#     for i in range(0,4):
#             print("*"*4)
# print_star()

# PATTERN 2

# ****
# *  *
# *  *
# ****
# 4 i=0
# 2 i=1
# 2 i=2
# 4 i=3
# def print_star():
#     for i in range(0,4):
#         if i in (1,2):
#             print("* *")
#         else:
#             print("*"*4)
# print_star()
# ****
#  ****
#   ****
#    ****


# PATTERN 3
# i=0,1,2,3
# j=0, 1 space, 2 space, 3 space
# def print_star():
#     for i in range(0,4):
#             print(" "*i + "*"*4)
#
# print_star()

# PATTERN 4
#    ****
#   ****
#  ****
# ****
# def print_star():
#     for i in range(4,0,-1):
#         print(" "*i +"*"*4)
#
# print_star()

# PATTERN 5
#
# *
# **
# ***
# ****

# def print_star():
#     for i in range(1,5):
#         print("*"*i)
#
# print_star()

# PATTERN 6

# *
# ***
# *****
# *******
# 1,3,5,7
# def print_star():
#     for i in range(1,8):
#         if i==1:
#             print("*")
#         if i%2==0:
#             print("*"*i)
#
# print_star()

# Pattern 7
# Pyramid Star Pattern
#    *
#   ***
#  *****
# *******
#
# i=0,1,2,3
# space=3,2,1,0
# star=1,3,5,7

# Pyramid Star Pattern

#
# def print_star():
#     for i in range(0,5):
#         j=5-i
#         print(" "*j + "*"*(2*i+1))
# print_star()


# Inverted Pyramid Star Pattern
# *******
#  *****
#   ***
#    *
# i=0,1,2,3
# j=7,5,3,1
# space=0,1,2,3
# star=7,5,3,1
# def print_star():
#     for i in range(0,4):
#         j = 4-i
#         print(i*" " + "*"*(2*j-1))
# print_star()


# Pattern #1: Simple Number Triangle Pattern
#
# 1
#
# 2 2
#
# 3 3 3
#
# 4 4 4 4
#
# 5 5 5 5 5

def print_num_pattern(num):
    for i in range(num):
        for j in range(i):
            print(i,j)
            print(i, end=" ")
        print("")
print_num_pattern(6)




