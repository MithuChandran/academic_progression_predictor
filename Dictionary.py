# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Name: Mithuna Chandrasekaran
# Date:13/12/2022
#part4

#Initialize variables
exit_1="Y"
total_cre=0
progress=0
trailer=0
retriever=0
Excluded=0
pass_cre=0
defer_cre=0
fail_cre=0
pass_list=[]
defer_list=[]
fail_list=[]
id_list=[]
id_no=""
progress_outcome=[]
dictionary_new={}

credit = [0,20,40,60,80,100,120]

#part4
def dictionary(name):
    dictionary_new[id_no]=name+str(new_list).strip("][")    
    
    

def histogram(progress,trailer,retriever,Excluded):          #defyneing a function
    print ("-"*115)
    print("Histogram") 
    print ("Progress ",progress, ':  ',end='')          #printing 'progress' and starting the next print with the  same line by useing end=''
    for c in range(progress):                           # by using for loop we can count the stars and print it and useing end=''to print the stars in the same row
        print('*',end='')                               #useing end='' to print all stars in same row 
    print('\n')                                         #to start next progression outcome in next line  
    print ("Trailer ",trailer, ':   ',end='')
    for c in range (trailer):
        print ('*',end='')
    print('\n')
    print ("Retriver ",retriever, ':  ',end='')
    for c in range (retriever):
        print('*',end='')
    print('\n')
    print ("Excluded ",Excluded, ':  ',end='')
    for c in range (Excluded):
        print('*',end='')
    print('\n')

    print ('      \n')
    print (progress + trailer + retriever + Excluded,"Outcomes in total. ")
    print ("-"*115)
    
while exit_1=="Y":
    id_no=input("Please Enter your student ID: ")
    try:
        while True:
            try:
                  pass_cre = int(input("Please enter the pass Credits: "))             #prompt input form user  
            except ValueError:
                        print("Integer required")
                        continue
            else:
                  if pass_cre not in credit:
                        print("Out of range")
                  elif pass_cre in credit:
                        break

        
        
        while True:
            try:
                  defer_cre =int(input("Please enter the defer credits:"))             #prompt input form user 
            except ValueError:
                  print("integer required")
                  continue
            else:
                  if defer_cre not in credit:
                        print("out of range")
                  elif defer_cre in credit:
                        break

        
        
        while True:
            try:
                  fail_cre =int(input("Please enter the fail credits:"))              #prompt input form user 
            except ValueError:
                        print("integer required")
                        continue
            else:
                 if fail_cre not in credit:
                       print("out of range")
                 elif fail_cre in credit:
                       break

        
        
        while True:
            total_cre = pass_cre + defer_cre + fail_cre
            if total_cre != 120:
                  print("Total incorrect")
                  break
            new_list =[pass_cre,defer_cre,fail_cre]
        
        
            if pass_cre==120:
                print("Progress")
                progress=progress+1                                                   #modifying the progress outcome count inside progress condition
                dictionary("Progress - ")
            elif pass_cre==100:
                print("Progress(module trailer)")
                trailer=trailer+1                                                      #modifying the do not progress(module trailer) count inside the condition 
                dictionary("Progress(module trailer) - ")
                
            elif pass_cre!=120 and pass_cre!=100 and fail_cre >=0 and fail_cre <=60:                   
                print("Module retriever")
                retriever=retriever+1                                                 #modifying the  do not progress (module_retriver) count inside the condition
                dictionary("Module retriever - ")
            else:                                                                     #else will print the exclude outcome
                print("Exclude")
                Excluded=Excluded+1                                                   #modifying the  do not progress (module_retriver) count inside the condition
                dictionary("Excluded - ")
            break
#C
        print("Would you like to enter another set of data?")
        while True:
            exit_1 = input("Please enter 'y' to continue or else enter 'q' to quit the program : ")
            exit_1 = exit_1.upper()
            if exit_1=='Y':
                break
#D
            elif exit_1=='Q':
                histogram(progress,trailer,retriever,Excluded)                                                    #calling the function histogram
                total_cre = total_cre+1                                                                           #modifying the total no of students
                outcomes=[ 'Progress' , 'Trailer' ,' Retriever' , 'Excluded' ]
                total_outcomes= [ progress , trailer , retriever , Excluded ]
                break

            else :
                print ("Your input is wrong !")
                
            
    except ValueError:
      print("Integer Required")

print("")
print("part 4:")
for key, value in dictionary_new.items():
    print(key,":",value ,end=" ")
      
print("")   
print ("\nProgramme is Quited by user !\n")
