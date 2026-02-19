def calculate_average(marks):
    return round(sum(marks) / len(marks), 2)

def find_topper(students):
    averages = {name: calculate_average(m) for name, m in students.items()}
    topper = max(averages, key=averages.get)
    return averages, topper

students = {
    "John": [85, 78, 92],
    "Alice": [88, 79, 95],
    "Bob": [70, 75, 80]
}

averages, topper = find_topper(students)
print(f"Average Marks: {averages}")
print(f"Top Performer: {topper}")
