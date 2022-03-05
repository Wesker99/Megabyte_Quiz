print("Welcome to The Megabyte Quiz")

playing = input("Are you going to play? ")

score = 0

if playing.lower() != "yes":
     quit()

print("okay! Let's play")

answer = input("what does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct answer !")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("correct answer !")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does RAM stands for? ")
if answer.lower() == "random access memory":
    print("correct answer !")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does ROM stands for? ")
if answer.lower() == "read only memory":
    print("correct answer !")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does PSU stands for? ")
if answer.lower() == "power supply unit":
    print("correct answer !")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does SSD stands for? ")
if answer.lower() == "solid state drive":
    print("correct answer !")
    score += 1
else:
    print("Incorrect answer")

answer = input("what does OS stands for? ")
if answer.lower() == "operating system":
    print("correct answer !")
    score += 1
else:
    print("Incorrect answer")

print("Your " + str(score) + " Questions are Correct!")
print("You Scored " + str((score/7) * 100) + "%.")