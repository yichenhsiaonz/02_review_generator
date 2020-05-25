def return_input(question):

    input_loop = ""
    while input_loop == "":

        user_input = input(question)
        # does not allow for blanks

        if user_input.strip() == "":
            print("Enter something!!!")

        # returns everything else

        else:
            return user_input

testing_loop = ""
while testing_loop == "":

    title = return_input("Please enter the title: ")
    author = return_input("Please enter the author: ")

    print()
    print("Title: {}".format(title))
    print("Author: {}".format(author))
