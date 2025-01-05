import csv

# Data to write to CSV
data = [
    ["category", "score"],
    ["IAM", 75],
    ["Detection", 60],
    ["Data Protection", 85],
    ["Infrastructure Protection", 70],
    ["Incident Response", 65],
]

# File name
csv_filename = "./locales/security_posture.csv"

# Writing data to CSV
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{csv_filename}' created successfully!")
