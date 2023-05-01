#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import date   #importing the datetime module for date of birth and to calculate age
from tabulate import tabulate #importing tabulate to make a table


#i have chosen to use the dictionary data structure for this particular question because it provides easy access to the attributes of the player and can be easily mapped with a key. i could enter just the id and immediately get all the information of the player.
player_data = {}
player_salaries = [400, 500, 700, 1000]  # Declared a list to store player salaries
player_rates = [30, 45, 60, 80]  # Declared another list to store player rates


#function to calculate rating of the player
def calculate_rating():
    print("Enter Player Data to get the salary of the player \n")  # prints message to enter data to get salary details

    while True:
        speed = float(input(
            "Enter value of speed of the player from 0 to 5 \n"))  # ask user to enter value of speed in a specfic range
        if speed <= 5 and speed >= 0:
            break
        else:
            print("The value you have entered is not valid.")

    while True:
        shooting = float(input(
            "Enter value of shooting of the player from 0 to 5 \n"))  # ask user to enter value of shooting in a specfic range
        if shooting <= 5 and shooting >= 0:
            break
        else:
            print("The value you have entered is not valid.")

    while True:
        passing = float(input(
            "Enter value of passing of the player from 0 to 5 \n"))  # ask user to enter value of passing of player in a specfic range
        if passing <= 5 and passing >= 0:
            break
        else:
            print("The value you have entered is not valid.")

    while True:
        defending = float(input(
            "Enter value of defending of the player from 0 to 5 \n"))  # ask user to enter value defending of player in a specfic range
        if defending <= 5 and defending >= 0:
            break
        else:
            print("The value you have entered is not valid.")

    while True:
        dribbling = float(input(
            "Enter value of dribbling of the player from 0 to 5 \n"))  # ask user to enter value of dribbling of the player in a specfic range
        if dribbling <= 5 and dribbling >= 0:
            break
        else:
            print("The value you have entered is not valid.")

    while True:
        physicality = float(input(
            "Enter value of physicality of the player from 0 to 5 \n"))  # ask user to enter value of physicality in a specfic range
        if physicality <= 5 and physicality >= 0:
            break
        else:
            print("The value you have entered is not valid.")
            continue

    sum_of_skills = int(
        speed + shooting + passing + defending + dribbling + physicality)  # here I calculated the sum of all the skills of player data entered above in the programme
    print(f'The sum of the skills are {sum_of_skills}\n')  # print sum of skills on output screen

    #making this variable global so it can be accessed in other functions
    global overall_rating
    overall_rating = int(
        (sum_of_skills * 100) / 30)  # here I calculated the overall rate of the player using the given formula

    print(f'The Overall rate of the player is {overall_rating}\n')  # print the overall rate on output screen


#function to calculate salary
def calculate_salary():

    global player_salary
   

    if overall_rating <= player_rates[
        0]:  # if overall rate is less or less then equal to Player rates which is first index element that is 30
        player_salary = player_salaries[0]  # then print salary is 400

    elif overall_rating > player_rates[0] and overall_rating <= player_rates[
        1]:  # if overall rate is greater than player rates which is zero index element and less than and equal to first index element
        player_salary = player_salaries[1], player_salaries[0]  # then print salary is 500, 400

    elif overall_rating > player_rates[1] and overall_rating <= player_rates[
        2]:  # if overall rate is greater than player rates which is first index element and less than and equal to second index element
        player_salary = player_salaries[2], player_salaries[1]  # then print salary is 700,500

    elif overall_rating > player_rates[2] and overall_rating <= player_rates[
        3]:  # if overall rate is greater than player rates which is second index element and less than and equal to third index element
        player_salary = player_salaries[3], player_salaries[2]  # then print salary is 1000, 700

    elif overall_rating > player_rates[3]:  # if overall rate is greater then player rates third index element
        player_salary = player_salaries[3]  # then print salary is 1000

    else:  # if input details does not match with any condition then print a message on user screen invalid input so that he/she will enter correct input values again
        print("Invalid Input: Try Again from start")


#the main function to run the program
def main():
    print("Welcome to my football club!\n")
    player_num = int(input("Enter the number of players whom data you want to enter: "))
    #getting data for players
    for i in range(player_num):
        while True:
            player_id = input("Enter a 2 digit player ID: ")

            if (len(player_id)) == 2 and player_id.isdigit(): #error handling for user id
                break
            else:
                print("The Player ID you have entered is not valid.")

        player_name = input("Enter player name: ")

        date_of_birth = input("Enter your date of birth (YYYY/MM/DD)- ")

        calculate_rating()

        calculate_salary()

        #function to calculate age of the player
        def calculate_age(birthdate):

            today = date.today()
            age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

            return age

        #here, i take the input from the user which was in form of a string and store it in a list and then access it via indexing to minus it with the current year
        age_list = date_of_birth.split("/")
        year = age_list[0] #accessing the year the user entered
        month = age_list[1] #accessing the month the user entered
        day = age_list[2] #accessing the day the user entered
        player_age = calculate_age(date(int(year), int(month), int(day)))

        #setting a key and storing all the data in the dictionary
        player_data[player_id] = player_name, date_of_birth, player_age, overall_rating, player_salary


    #creating a table by first making colomns using headers and the tabulate function
    headers = ["UID", "Name", "D.O.B", "Age", "Score", "Salary Range"]
    table = tabulate([(i,) + player_data[i] for i in player_data], headers=headers)
    print(table)

    #creating a new text file and storing the data inside it.
    with open("C:\\Users\\MUHAMMAD HASNAIN\\Desktop\\player_data.txt", "w") as f: #enter the directory where you want to save text file
        f.write(table)
        f.close()


main()


# In[ ]:




