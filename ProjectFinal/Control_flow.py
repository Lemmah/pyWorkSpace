from list_display import list_of_skills
from dict_response import dict_response
from manipulate_dic import manipulate_dic
response = 2

while response == 2:
    print("Welcome to Skill-Learning Progress Evaluation")
    print("What action do you want to be performed?\n\t1. Output list\n\t2. Evaluate progress\n\t3. Check progress")
    action = int(
        input("Give your response in terms of the number of the action as listed: "))
    if not isinstance(action, int):
        print("Invalid input. Only numbers allowed")

    elif int(action) < 1:
        print("Invalid input!")

    elif int(action) > 3:
        print("Invalid input!")

    else:
        if int(action) == 1:
            print(list_of_skills())

        elif int(action) == 2:
            dict_response()
            manipulate_dic()

        elif int(action) == 3:
            manipulate_dic()

    response = int(
        input("Do you want to exit?\n\t1.\
         Yes\n\t2. No\n\nEnter your response:\t"))
