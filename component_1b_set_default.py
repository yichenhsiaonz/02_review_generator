def return_input(question, condition):

    input_loop = ""
    while input_loop == "":

        user_input = input(question)

        # returns anonymous if no author name entered

        if condition == 1 and user_input.strip() == "":
            return "Anonymous"

        # does not allow for blanks when not asking for author

        elif user_input.strip() == "":
            print("Enter something!!!")

        # returns everything else

        else:
            return user_input

testing_loop = ""
while testing_loop == "":

    # condition of 0 shows that program isn't asking for author
    title = return_input("Please enter the title: ", 0)

    # condition of 1 shows that program is asking for author
    author = return_input("Please enter the author: ", 1)

    print()
    print("Title: {}".format(title))
    print("Author: {}".format(author))
