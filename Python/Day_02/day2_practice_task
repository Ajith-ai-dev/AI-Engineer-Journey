'''
1. Write a program that demonstrates all of the following:

- Create one list.
- Create two variables referring to that list.
- Mutate the list.
- Rebind one variable.
- Print:
    - both variables
    - id()
    - ==
    - is
'''

exam_scores = [90, 83, 79]
scores_copy1 = exam_scores
scores_copy2 = exam_scores

# Mutating the list
scores_copy1.append(100)

# Rebinding creates a new list instead of modifying the shared one
scores_copy2 = [90, 83, 79, 100]

print("exam_scores:", exam_scores)
print("scores_copy1:", scores_copy1)
print("scores_copy2:", scores_copy2)

# printing identity(id) of the lists
print("scores_copy1 id:", id(scores_copy1))
print("scores_copy1 id:", id(scores_copy2))

# equality returns True if contents are matched, is returns True if identities are matched
print(scores_copy1 == scores_copy2)
print(scores_copy1 is scores_copy2)
