#Python Datatypes
#1. Integer
score = 100

#2. String
name = "Adam"

#3. Bool
status = True

#4. Dict
person  = {"name" : "Adam", "age" : 25}

#5. Float
cost = 15.4

#6. Tuple
account_details = ("9876543210", "IFSC654")

#7. List
technologies = ["Python", "HTML", "CSS" ,"JS"]


print(technologies[2])

#8. Set
Students = {"1", "2", "3"}


UniversityData = {
    "AI_ML" : ["Adam" , "Sam"],
    "CIVIL" : {
        "SECTION_A" : ["David", "john"],
        "SECTION_B" : ["Thanu", "Saad"]
    }
}



#=========================CRUD ON DICT
person= {
    
}

#craete
person['name'] = "Adam"
person['phone'] = "9876543210"

#read
print(person['name'])

#update
person['name'] = "MR. Adam"

#delete
person.pop("name")



print(person)


#===========================CRUD ON LIST



todos = []

#create
todos.append("Code")

print(todos)

#read
print(todos[0])


#update
todos[0] = "Programming"


#remove
todos.remove("Programming")
print(todos)
