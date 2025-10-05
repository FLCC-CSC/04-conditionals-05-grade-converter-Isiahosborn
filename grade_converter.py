# FILE NAME - grade_converter.py

# NAME: Isiah Osborn
# DATE: 2025-10-05
# BRIEF DESCRIPTION:
#   Read a numerical grade and print the corresponding letter grade.
#   >100 => A+, 90–100 => A, 80–89 => B, 70–79 => C, 65–69 => D, else F.

########## ENTER YER CODE BELOW THIS LINE ##########

print("===== Grade Converter =====")
percent = int(input("Enter a numerical grade (1-100): ").strip())

if percent > 100:
    print("A+")
elif percent >= 90:
    print("A")
elif percent >= 80:
    print("B")
elif percent >= 70:
    print("C")
elif percent >= 65:
    print("D")
else:
    print("F")

########### END YER CODE ABOVE THIS LINE ###########

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
===== Grade Converter =====
Enter a numerical grade (1-100): 101
A+
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): -78
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 64
F
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 65
D
'''


'''
===== Grade Converter =====
Enter a numerical grade (1-100): 66
D
'''

########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What is something you would tell a future student to be careful about when
   doing this lab?







'''
