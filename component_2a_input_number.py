def return_input(question):

    input_loop = ""
    while input_loop == "":
        try:

            user_input = float(input(question))

            if user_input == "":
                print("Enter something!!!")
            elif user_input > 5:
                return 5
            elif user_input < 1:
                return 1
            else:
                return user_input

        except ValueError:
            print("Enter a number!!!")

testing_loop = ""
while testing_loop == "":

    number = return_input("Please enter the rating: ")
    print("Rating: {}".format(number))
    print()
