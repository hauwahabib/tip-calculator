print("Tip Calculator")
print()
myBill = float(input("How much did you spend?"))
print()
percentage = int(input("What percentage do you want to tip?"))
print()
numberOfPeople = int(input("How many people in your group?"))
print()
answerOne = percentage / 100 * myBill 
answer = answerOne + myBill
print()
print("You all owe", answer)