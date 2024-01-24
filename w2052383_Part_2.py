# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2052383
# Date: 22.11.2023
progress_data = []
module_trailer_data = []
module_retriever_data = []
exclude_data = []

progress_count = 0
module_trailer_count = 0
module_retriever_count = 0
exclude_count = 0

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
                    data = [pass_credits, defer_credits, fail_credits]
                    if pass_credits == 120:
                        print("Progress")
                        progress_count += 1
                        progress_data.append(data)
                    elif pass_credits == 100:
                        print("Progress (module trailer)")
                        module_trailer_count += 1
                        module_trailer_data.append(data)
                    elif pass_credits == 80 or pass_credits == 60:
                        print("Do not progress - Module retriever")
                        module_retriever_count += 1
                        module_retriever_data.append(data)
                    elif pass_credits == 40 and fail_credits != 80:
                        print("Do not progress - Module retriever")
                        module_retriever_count += 1
                        module_retriever_data.append(data)
                    elif pass_credits == 20 and fail_credits < 80:
                        print("Do not progress - Module retriever")
                        module_retriever_count += 1
                        module_retriever_data.append(data)
                    elif pass_credits == 0 and fail_credits < 80:
                        print("Do not progress - Module retriever")
                        module_retriever_count += 1
                        module_retriever_data.append(data)
                    else:
                        print("Exclude")
                        exclude_count += 1
                        exclude_data.append(data)

                    choice = input("Would you like to enter another set of data?"
                                   "\nEnter 'y' for yes or 'q' to quit and view results:")
                    if choice.lower() == "q":
                        print("-----------------------------------------")
                        print("Part 2:")
                        for data in progress_data:
                            print(f"Progress - {data[0]}, {data[1]}, {data[2]}")

                        for data in module_trailer_data:
                            print(f"Progress (module trailer) - {data[0]}, {data[1]}, {data[2]}")

                        for data in module_retriever_data:
                            print(f"Do not progress - Module retriever - {data[0]}, {data[1]}, {data[2]}")

                        for data in exclude_data:
                            print(f"Exclude - {data[0]}, {data[1]}, {data[2]}")
                        print("-----------------------------------------")
                        break
                    elif choice.lower() != "y":
                        print("Invalid input. Please enter 'y' for yes or 'q' to quit.")
    except ValueError:
        print("Integer required")
# data[0] represents the number of credits at pass.
# data[1] represents the number of credits at defer.
# data[2] represents the number of credits at fail.
