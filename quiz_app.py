# Simple Python Quiz App
# Author: Neeraja
# This program asks quiz questions and calculates score

print("Welcome to the Python Quiz App 🧠")

score = 0

print("\nQuestion 1:")
print("What is the output of: print(2 + 3)?")
print("a) 23")
print("b) 5")
print("c) Error")

answer1 = input("Your answer (a/b/c): ")

if answer1 == "b":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

print("\nYour current score is:", score)

print("\nQuestion 2:")
print("Which keyword is used to define a function in Python?")
print("a) func")
print("b) define")
print("c) def")

answer2 = input("Your answer (a/b/c): ")

if answer2 == "c":
    print("Correct ✅")
    score += 1
else:
    print("Wrong ❌")

print("\nFinal score:", score)

