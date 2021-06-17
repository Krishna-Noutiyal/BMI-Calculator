"""
This program Shows your BMI and 
Suggests you some exercises and diets to follow
"""
# Welcome message
print("\n\n\tHello And Welcome to BMI Calculator\n\n\tThis program shows your BMI and suggests you diets and exercises")
while True:
    try:

        
        def read(file_name, file):

            if file_name == "1" or file_name == "yes" or file_name == "Yes" or file_name == "y" or file_name == "Y":
                
                with open(f"{file}", "r") as f:
                    #Storing the file lines as list in variable
                    line = f.readlines()

                    # For loop to print lines
                    for i in line:
                        print(i) 
        
        def underweight():
            
            with open("Underweight Diet and Exercises.txt", "w+") as n:
                lines = [
                    "\n\tHello and Welcome your BMI is underweight",
                    "\n\n\tYou need to increase your body weight and size",
                    "\n\n\t\tTry these exercises:-",
                    "\n\n\t\t\t1) Running",
                    "\n\t\t\t2) Jumping Jacks",
                    "\n\t\t\t3) Criss Cross",
                    "\n\t\t\t4) Pullups",
                    "\n\t\t\t5) And some regular straching",

                    "\n\n\tYou should also increase protein and fat in your diet",
                    "\n\n\t\t\tYou can eat fatty food twice or thrise a week",
                    "\n\t\t\tBut don't eat to much fatty food it my cause obese",


                ]
                n.writelines(lines)

                #Successful msg
                print("\n\nYour exercise and diet plan is created succesfully")
                
            # Asking user to print the file
            print("\n\n\n\t\tDo you want to see what exercises and foods you should do and eat")
            print_or_not = input("\n\n\t\t\t1) Yes \n\t\t\t2) No:\n\n\t\t\t")

            file = "Underweight Diet and Exercises.txt"

            # Calling the read function
            read(print_or_not,file)

        def normal():
            with open("Normal Diet and Exercises.txt", "w+") as n:
                lines = [
                    "\n\tHello and Welcome your BMI is normal",
                    "\n\n\tYou need to maintain your body weight and size",
                    "\n\n\t\tTry these exercises:-",
                    "\n\n\t\t\t1) Running",
                    "\n\t\t\t2) Burpees",
                    "\n\t\t\t3) Squads",
                    "\n\t\t\t4) Pushups",
                    "\n\t\t\t5) And some regular straching",

                    "\n\n\tYou should also maintain a healthy diet",
                    "\n\n\t\t\tYou can eat oily food twice or thrise a week",
                    "\n\t\t\tBut don't eat to much oily food it my cause obese",


                ]
                n.writelines(lines)

                #Successful msg
                print("\n\nYour exercise and diet plan is created succesfully")
                
            
            # Asking user to print the file
            print("\n\n\n\t\tDo you want to see what exercises and foods you should do and eat")
            print_or_not = input("\n\n\t\t\t1) Yes \n\t\t\t2) No:\n\n\t\t\t")

            file = "Normal Diet and Exercises.txt"

            # Calling the read function
            read(print_or_not,file)

        def obese():
            with open("Obese Diet and Exercises.txt", "w+") as n:
                lines = [
                    "\n\tHello and Welcome your BMI is Obese",
                    "\n\n\tYou need to reduce your body weight and figure",
                    "\n\n\t\tTry these exercises:-",
                    "\n\n\t\t\t1) Running",
                    "\n\t\t\t2) Burpees",
                    "\n\t\t\t3) Squads",
                    "\n\t\t\t4) Pushups",
                    "\n\t\t\t5) Exercises that reduces fat",
                    "\n\t\t\t6) And some regular straching",

                    "\n\n\tYou should also maintain a healthy diet",
                    "\n\n\t\t\tYou should exteremly avoid fatty and oily food ",
                    "\n\t\t\tIf you are doing the listed exercises and trying to avoid fatty and oily food ",
                    "\n\t\t\tAs mentioned above you can eat fast food ones a week on sunday",
                    "\n\t\t\tBut don't eat to much oily food it my cause obese",


                ]
                n.writelines(lines)

                #Successful msg
                print("\n\nYour exercise and diet plan is created succesfully")

            
            # Asking user to print the file
            print("\n\n\n\t\tDo you want to see what exercises and foods you should do and eat")
            print_or_not = input("\n\n\t\t\t1) Yes \n\t\t\t2) No\n\n\t\t\t: ")

            file = "Obese Diet and Exercises.txt"

            # Calling the read function
            read(print_or_not,file)

        def creat_retrive(): 
            """ This function Shows a dialog asking you to create the file """
            print("\n\n\t\t\tDo you want to get an exercise and diet plan")            
  

        # Asking user if he\she want's to chech there BMI and creat suitable exercise and diet plan
        print("\n\n\t\tWhat you want to do \n\n\t\t1) Check your BMI and create suitable exercise and diet plan \n\n\t\t2) View your exesting plan")
        crt_view = int(input("\n\n\t\tEnter 1 or 2 as above: "))

        if crt_view == 1:
        
            # Asking user to enter weight
            weight = int(input("\n\n\t\tPlease enter your weight in Kg: "))

            # Asking user to enter height
            print("\n\n\tI will also need your height in meters")

            height = float(input("\n\n\t\tPlease enter your height in Meters: "))

            # Rounding the square of height
            square = round(height**2)
            # Rounding the BMI
            Bmi = round(weight / square)
            # print(Bmi)



            # If bmi is normal
            if 18.5 <= Bmi <= 24.9:
                print("\n\n\t\t\tCongratulation!! Your Normal")
                print("\n\t\t\t\tYour BMI is", Bmi)

                # Adding a dialoge box 
                creat_retrive()

                #Askes user to creat exercise and diet file
                crt_ret = input("\n\t\t\tPress y if you agree or enter to exit: ")  
                if crt_ret == "y" or crt_ret =="Y":
                    #funtion to create a Normal BMI file
                    normal()

                else:
                    break

            # If bmi is underweight
            elif 12<= Bmi < 18.5:
                print("\n\n\t\t\tSorry!! Your Underweight")
                print("\n\t\t\t\tYour BMI is", Bmi)

                # Adding a dialoge box 
                creat_retrive()

                #Askes user to creat exercise and diet file
                crt_ret = input("\n\t\t\tPress y if you agree or enter to exit: ")  
                if crt_ret == "y" or crt_ret =="Y":
                    #funtion to create a Normal BMI file
                    underweight()
                else:
                    break

            # If bmi is obese
            elif 24.9 < Bmi <= 30:
                print("\n\n\t\t\tSorry!! but your are Obese")
                print("\n\t\t\t\tYour BMI is", Bmi)
                
                # Adding a dialoge box 
                creat_retrive()

                #Askes user to creat exercise and diet file
                crt_ret = input("\n\t\t\tPress y if you agree or enter to exit: ")  
                if crt_ret == "y" or crt_ret =="Y":
                    #funtion to create a Normal BMI file
                    obese()

                else:
                    break

            # If bmi is exteremly obese
            elif 30 < Bmi <= 40:
                print("\n\n\t\t\tSorry!! but your are Extremely Obese")
                print("\n\t\t\t\tYour BMI is", Bmi)
                
                # Adding a dialoge box 
                creat_retrive()

                #Askes user to creat exercise and diet file
                crt_ret = input("\n\t\t\tPress y if you agree or enter to exit: ")  
                if crt_ret == "y" or crt_ret =="Y":
                    #funtion to create a Normal BMI file
                    obese()

                else:
                    break

            # If bmi is very exteremly obes
            elif 40 < Bmi <= 80:
                print("\n\n\t\t\tYour are probably lying you can't have a BMI of", Bmi)
                print("\n\n\t\t\tIn case you are not lying my friend your are actually very Obese")
                
                # Adding a dialoge box 
                creat_retrive()

                #Askes user to creat exercise and diet file
                crt_ret = input("\n\t\t\tPress y if you agree or enter to exit: ")  
                if crt_ret == "y" or crt_ret =="Y":
                    #funtion to create a Normal BMI file
                    obese()

                else:
                    break

            # If bmi is touching world record
            elif 80 < Bmi <= 200:
                print("\n\n\t\t\tYou just can't have a BMI of", Bmi) 
                print("\n\n\t\t\tHow is this even possible", Bmi) 
                print("\n\n\t\t\tIn case you are not lying my friend, your are actually 1 of the worlds most Obesed person")
                
                # Adding a dialoge box 
                creat_retrive()

                #Askes user to creat exercise and diet file
                crt_ret = input("\n\t\t\tPress y if you agree or enter to exit: ")  
                if crt_ret == "y" or crt_ret =="Y":
                    #funtion to create a Normal BMI file
                    obese()

                else:
                    break

            # If bmi is probably fake
            elif 200 < Bmi :
                print("\n\n\t\t\tAah! Now you are actually lying you can't have a BMI of", Bmi) 
                print("\n\n\t\t\tBecause the person with world record of 'Highest BMI ever' has a BMI of: 204") 
                print("\n\n\n\t\t\t\tPlease tell as many lies as you can digest !")
            
            # If bmi is verry verry underweight
            else:
                print("\n\n\n\t\t\t\tPlease tell as many lies as you can digest !")
        
        elif crt_view == 2:
            
            try:
                Bmi = int(input("\n\n\tEnter Your BMI: "))
                e = input("\n\n\t\t\tPress enter to print your plan: ")
                # If bmi is normal
                if 18.5 <= Bmi <= 24.9:

                    with open("Normal Diet and Exercises.txt", "r") as n:

                        #Storing the file lines as list in variable
                        line = n.readlines()

                        # For loop to print lines
                        for i in line:
                            print(i) 
                
                # If bmi is underweight                
                elif 12<= Bmi < 18.5:
                    with open("underweight Diet and Exercises.txt", "r") as n:

                        #Storing the file lines as list in variable
                        line = n.readlines()

                        # For loop to print lines
                        for i in line:
                            print(i) 
                
                # If bmi is obese                
                elif 24.9< Bmi <=200:

                    with open("Obese Diet and Exercises.txt", "r") as n:

                        #Storing the file lines as list in variable
                        line = n.readlines()

                        # For loop to print lines
                        for i in line:
                            print(i) 

                # If bmi is kinda SuS
                else:
                    print("\n\n\n\t\t\t\tPlease tell as many lies as you can digest !")
            
            except Exception as e:
                print("\n\n\tYou have not created any type of exercise or diet plan")
                # print(e)
    
    
                # Asking user to continue or exit
                a = input("\n\n\t\tPress y to continue or enter to exit: ")
                if a == "y" or a == "Y":
                    continue
                else:
                    break

        
    except Exception as e:
        print("\n\n\tYou did someting wrong please try again")
        # print(e)
    
    
    # Asking user to continue or exit
    a = input("\n\n\t\tPress y to continue or enter to exit: ")
    if a == "y" or a == "Y":
        continue
    else:
        break


    