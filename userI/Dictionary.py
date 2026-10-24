#student = {
##   "course": "B.Tech",
  #  "skill": "Python",
   # "goal": "Cloud Engineer"
#}
#print(student["name"])
#print(student["skill"])
#print(student["goal"])

#student = {
 #   "name": "Varsha",
  ## "goal": "Cloud Engineer"
#}
#student["skill"] = "AWS"
#print("name: " + student["name"])
#print("skill: " + student["skill"])
#print("goal: " + student["goal"])

#student = {
 #   "name": "Varsha",
  #  "skill": "AWS",
   # "goal": "Cloud Engineer"
#}
#student["skill"] = "Linux"
#student["city"] = "Punjab"
#print("name: " + student["name"])
##print("goal: " + student["goal"])
#print("city: " + student["city"])

#student = {
 #   "name": "Varsha",
  #  "skill": "Python",
   #     "city": "Punjab",
    #"goal": "Cloud Engineer"
#}  

#student = {
   #  "skill": "Python",
 #   "goal": "Cloud Engineer"
#}
#for key in student.keys():
    #print(key )

#student = {
 #   "name": "Varsha",
  #  "skill": "Python",
   # "goal": "Cloud Engineer"
#}
#for key,value in student.items():
 #   print(key + " : " + value)

#student = {
 #   "name": "Varsha",
  #  "skill": "Python",
   # "goal": "Cloud Engineer"
#}
#print(student.get("age",20))

students = [
    {"name": "Varsha", "marks": 90},
    {"name": "Aman", "marks": 85},
    {"name": "Riya", "marks": 95}
]

students[1]["marks"] = 92
students.append({"name": "Rahul", "marks": 88})
students.remove({"name": "Rahul", "marks":88})

for student in students:
    print(student["name"], student["marks"])