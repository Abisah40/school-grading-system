score = int(input("enter your score:"))
name =input("enter your name:")
if score >= 70 and score <= 100:
    print(f"{name},your score is {score} and your grade is A")
elif score >=60 and score < 70:
    print(f"{name},your score is {score} and your grade is B")
elif score >= 50 and score < 60:
    print(f"{name},your score is {score} and your grade is C")
elif score >=40 and score < 50:
    print(f"{name},your score is {score} and your grade is D")
elif score >= 30 and score < 40:
    print(f"{name},your score is {score} and your grade is E")
else:
    print(f"{name},your score is {score},your grade is F and you fail...")