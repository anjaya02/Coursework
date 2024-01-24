# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2052383
# Date: 22.11.2023

while True:
    try:
        pass_credits = int(input("Please enter your credits at pass:"))

        if pass_credits not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range")
        else:
            defer_credits = int(input("Please enter your credits at defer:"))
            if defer_credits not in [0, 20, 40, 60, 80, 100, 120]:
                print("Out of range")
            else:
                fail_credits = int(input("Please enter your credits at fail:"))
                if fail_credits not in [0, 20, 40, 60, 80, 100, 120]:
                    print("Out of range")
                elif pass_credits + defer_credits + fail_credits != 120:
                    print("Total incorrect")
                else:
                    if pass_credits == 120:
                        print("Progress")
                    elif pass_credits == 100:
                        print("Progress (module trailer)")
                    elif pass_credits == 80 or pass_credits == 60:
                        print("Do not progress - Module retriever")
                    elif pass_credits == 40 and fail_credits != 80:
                        print("Do not progress - Module retriever")
                    elif pass_credits == 20 and fail_credits < 80:
                        print("Do not progress - Module retriever")
                    elif pass_credits == 0 and fail_credits < 80:
                        print("Do not progress - Module retriever")
                    else:
                        print("Exclude")

                    choice = input("Would you like to enter another set of data?"
                                   "\nEnter 'y' for yes or 'q' to quit and view results:")
                    if choice.lower() == "q":
                        break
                    elif choice.lower() != "y":
                        print("Invalid input. Please enter 'y' for yes or 'q' to quit.")
    except ValueError:
        print("Integer required")
