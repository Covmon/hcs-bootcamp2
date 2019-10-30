import csv

original = open("StudentsPerformanceOriginal.csv", "r")

reader = csv.DictReader(original)

new = open("StudentsPerformance.csv", "w")

writer = csv.writer(new)
writer.writerow(["gender", "race", "parental_education", "lunch", "prep", "score"])

for line in reader:
    gender = line["gender"]
    race = line["race"]
    parents = line["parental_education"]
    lunch = line["lunch"]
    prep = line["prep"]

    newline = []

    if gender == "female":
        newline.append(0)
    else:
        newline.append(1)

    if race == "group A":
        newline.append(0)
    elif race == "group B":
        newline.append(1)
    elif race == "group C":
        newline.append(2)
    else:
        newline.append(3)

    if parents == "some high school":
        newline.append(0)
    elif parents == "high school":
        newline.append(1)
    elif parents == "some college":
        newline.append(2)
    elif parents == "associate's degree":
        newline.append(3)
    elif parents == "bachelor's degree":
        newline.append(4)
    else:
        newline.append(5)

    if lunch == "free/reduced":
        newline.append(0)
    else:
        newline.append(1)

    if prep == "none":
        newline.append(0)
    else:
        newline.append(1)

    score = (int(line["math"]) + int(line["reading"]) + int(line["writing"])) / 3

    newline.append(score)

    writer.writerow(newline)

original.close()
new.close()