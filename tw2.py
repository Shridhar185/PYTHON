#store in dictionary
#1.display course with highest registrations
#2.by course code display details
#3.disply details of all courses 


""" def addCourse(courses):
    courseCode=input("coursecode: ")  #it is the key 
    if courseCode not in courses:
        courseName=input("enter course name: ")
        faculty=input("faculty: ")
        noOfRegs=int(input("no of register: "))
        courses[courseCode]=[courseName,faculty,noOfRegs]
    else:
        print("courses already present ")
   
def dispAll(courses):
    if len(courses)==0:
        print("no course")
        return
    for code in courses:                #here key as an indexnumber 
        print(code,'', courses[code] )  #similar as i and a[i]
        
def dispOne(courses):
    code=input("enter code to search ")
    if code in courses:
        print("the course is ")
        print(code,": ",courses[code])
    else:
        print("course with this code is not present")
 
def noOfRegs(courses):
    if len(courses)==0:
        print("no course")
        return
    regs=[]
    for values in courses:
        regs.append(values[2]) # the regs value is at index 2 for key values
    
    code=max(regs)
    for course in courses:
        if course[2]==code:
            print("course with highest regist:",course)
         
    
def main():
    courses={}
    while(1):
        print("1.add course \n2.display all \n3.display particular course \n4.course with highest registrations \n5.exit")
        opt=int(input("Enter option: "))
        if opt==1:
            addCourse(courses)
        elif opt==2:
            dispAll(courses)
        elif opt==3:
            dispOne(courses)
        elif opt==4:
            noOfRegs(courses)
        elif opt==5:
            break
        

if __name__=='__main__':
    main()
 """






def addCourse(courses):
    courseCode=input("coursecode: ")  #it is the key 
    if courseCode not in courses:
        courseName=input("enter course name: ")
        faculty=input("faculty: ")
        course={"course: ":courseName,"fac: ":faculty}
        courses[courseCode]=course
    else:
        print("courses already present ")
   
def dispAll(courses):
    if len(courses)==0:
        print("no course")
        return
    co=input("enter cdoe :" )
    for co in courses:                #here key as an indexnumber 
        print("code: ",co)  #similar as i and a[i]
        print("course : ",courses["courseName"])
 
def main():
    courses={}
    while(1):
        print("1.add course \n2.display all \n3.display particular course \n4.course with highest registrations \n5.exit")
        opt=int(input("Enter option: "))
        if opt==1:
            addCourse(courses)
        elif opt==2:
            dispAll(courses)
         
        elif opt==5:
            break
        

if __name__=='__main__':
    main()









    