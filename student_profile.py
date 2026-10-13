
student = {
    "name": "Krishnasree",
    "branch": "Electronics and Communication Engineering",
    "college": "RMK Engineering College",
    "interests": ["AI/ML", "IoT", "Embedded Systems"]
}

print("=== Student Profile ===")
print("Name:", student["name"])
print("Branch:", student["branch"])
print("College:", student["college"])

print("\nTechnical Interests:")
for interest in student["interests"]:
    print("-", interest)
