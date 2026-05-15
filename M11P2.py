# M11P2.py
# Enter a student's last name and three exam scores.
# Use a function to return total points and average exam score.


def compute_total_and_average(score1, score2, score3):
    total_points = score1 + score2 + score3
    average_score = total_points / 3

    return total_points, average_score


student_count = 0
response = input("Do you want to enter student exam scores? Enter Yes or No: ")

print()
print(f"{'Last Name':<15}{'Total Points':>15}{'Average':>15}")
print("-" * 45)

while response.lower() == "yes":
    last_name = input("Enter student's last name: ")
    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))
    score3 = float(input("Enter exam score 3: "))

    total_points, average_score = compute_total_and_average(score1, score2, score3)
    student_count = student_count + 1

    print(f"{last_name:<15}{total_points:>15.2f}{average_score:>15.2f}")

    response = input("Do you want to enter another student? Enter Yes or No: ")

print("-" * 45)
print(f"Number of students entered: {student_count}")
