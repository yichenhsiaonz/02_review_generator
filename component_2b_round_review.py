import math


def return_input(question):
    rounding = ""
    default = ""

    input_loop = ""
    while input_loop == "":
        try:

            user_input = float(input(question))

            if user_input == "":
                print("Enter something!!!")
            elif user_input > 5:
                return [5, ""]
            elif user_input < 1:
                return [1, ""]
            elif user_input % 1 != 0:
                while rounding == "":
                    rounding = input("Would you like to round up or down?: ")
                    if rounding == "up":
                        default = "Because it is worth more than a {}".format(math.floor(user_input))
                        user_input = math.ceil(user_input)
                        rounding_loop = 1
                    elif rounding == "down":
                        default = "Because it is not worth a {}".format(math.ceil(user_input))
                        user_input = math.floor(user_input)
                        rounding_loop = 1
                    else:
                        print("Please enter \"up\" or \"down!!!\"")
            else:
                return [user_input, ""]

            input_loop = 1
        except ValueError:
            print("Only numbers!!!")

    reason = input("Why did you decide to round {}?: ".format(rounding))
    if reason.strip() == "":
        reason = default

    return [user_input, reason]

testing_loop = ""
while testing_loop == "":

    # condition of 0 shows that program isn't asking for author
    rating = return_input("Please enter the rating: ")
    print("Rating: {:.0f}".format(rating[0]))
    if rating[1] != "":
        print("Reason: {}".format(rating[1]))
    print()
