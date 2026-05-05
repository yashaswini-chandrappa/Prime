'''Q5. Create a dictionary where:
•Keys = studentnames
•Values = marks(integer)
Write a menu-based program where user presses a key (ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ)depending on the operation they want to perform on the dictionary: 
1.-Add a student - A
2.-Updatemarks-B 
3.-Search for a student-C
4.-Display all students and marks-D'''

'''Important concept in dictionary'''

dict = {"Anju": [90,23,12,54],"Theju": [90,25,78,34],"Sanju":[90,100,93,95],"Sagar":[49,46,12,89]}
options = input("Provide input as 'A' - Add a student \n 'B' - Update Marks \n 'C' - Search for a student \n 'D' - Display all students and marks\n : ")
match options:
    case "A":
        add_student = input("Provide the name of the student to be added : ")
        marks = list(map(int, input("Provide marks (comma separated): ").split(",")))
        dict[add_student] = marks
        print(dict)
    case "B":
        name = input("Enter the student name for updating the marks :")
        if name in dict:
            marks = list(map(int, input("Provide marks (comma separated): ").split(",")))
            dict[name]=marks
            print(dict)
        else:
            print("Student not found")
    case "C":
        search = input("Provide the student name to search : ")
        search_result =  dict.get(search)
        print(search_result)
    case "D":
        print(dict.items())