student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print(range(1, 10))

# total_score = sum(student_scores)
# print(total_score)

# sum = 0
# for score in student_scores:
#     sum = sum + score
# print(sum)

# print(max(student_scores))

# Find the largest number using for loop
large = 0
for score in student_scores:
     if large<score:
         large = score
print(large)
