# # Start with this basic structure
# music_library = {
#     "rock": [
#         {"title": "Bohemian Rhapsody", "artist": "Queen", "duration": 354},
#         {"title": "Stairway to Heaven", "artist": "Led Zeppelin", "duration": 482}
#     ],
#     "pop": [
#         {"title": "Shape of You", "artist": "Ed Sheeran", "duration": 234},
#         {"title": "Blinding Lights", "artist": "The Weeknd", "duration": 201}
#     ],
#     "hip-hop": [
#         {"title": "Lose Yourself", "artist": "Eminem", "duration": 326}
#     ]
# }

# # Task 1: Add a new song to the "rock" genre
# title=input("Song Title: ")
# artist=input("Artist: ")
# duration=input("Duration: ")

# music_library["rock"].append({
#     "title": f"{title}",
#     "artist": f"{artist}",
#     "duration": f"{duration}"  # Just an example duration
# })

# # Task 2: Print all songs in the "pop" genre
# print(music_library["rock"])

# # Task 3: Calculate the total duration of all songs in "hip-hop"

# total=0
# for song in music_library["hip-hop"]:
#     total += song["duration"]

# print(total)

# Start with this basic structure
school = {
    "Computer Science": {
        "chair": "Dr. Jane Smith",
        "courses": {
            "CS101": {"name": "Intro to Programming", "instructor": "Dr. Brown", "credits": 3},
            "CS201": {"name": "Data Structures", "instructor": "Dr. Green", "credits": 4}
        }
    },
    "Mathematics": {
        "chair": "Dr. Tom Johnson",
        "courses": {
            "MATH101": {"name": "Calculus I", "instructor": "Dr. White", "credits": 4},
            "MATH205": {"name": "Linear Algebra", "instructor": "Dr. Brown", "credits": 3}
        }
    }
}

# Task 1: Add a new course "CS301: Database Systems" to Computer Science
# taught by "Dr. Lee" with 4 credits
school["Computer Science"]["courses"]["CS301"]={"name": "Database Systems", "instructor": "Dr. Lee", "credits": 4}
print(school)

# Task 2: Find and print all courses taught by "Dr. Brown"
for department in school.values():
    for course_code, course_info in department["courses"].items():
        if course_info["instructor"]=="Dr. Brown":
            print(f"{course_code}: {course_info["name"]} ({course_info["credits"]} credits)")


# Task 3: Print a formatted list of all departments and their courses
# Your code here