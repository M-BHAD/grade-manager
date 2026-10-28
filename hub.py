while True:
    name=input("Enter your name: ")
    print("Welcome",name)

    while True:
        m1=int(input("English marks: "))
        m2=int(input("Hindi marks: "))
        m3=int(input("Maths marks: "))
        m4=int(input("Science marks: "))
        m5=int(input("computer marks: "))
        if  (0 <= m1 <= 100 and
            0 <= m2 <= 100 and
            0 <= m3 <= 100 and 
            0 <= m4 <= 100 and 
            0 <=m5<= 100):
            print("All marks are valid!")
            break
        else:
            print("Invalid marks! Enter again.")
    total=m1+m2+m3+m4+m5
    avg=total/5
    percentage=(total/500)*100


    if percentage>=90:
        grade="A+"
    elif percentage>=80:
        grade="A"
    elif percentage>=70:    
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage>=50:
        grade="D"
    else:
        grade="Fail"

    print("\n================STUDENT RESULT==================")
    print("Student Name: ",name)
    print("Total Marks: ",total,"/500")
    print("Percentage: ",percentage,"%")
    print("Grade: ",grade)
    print("===================================================")
   
    again=input("Add another student?(yes/no) : ").lower()
    if again == "no":
        print("Thank you for using Student Grade Manager!")
        break

        
  

    