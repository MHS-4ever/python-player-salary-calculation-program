# python-player-salary-calculation-program
This respiratory contain a .py file containing the code for player salary calculation according to his skills and the complete documentation of the code.
Importing Modules: The first two lines of the code are importing the necessary modules that will be used throughout the program. The datetime module is imported to calculate the age of the player using their date of birth, and the tabulate module is imported to display the data in a tabular format.

Initializing Variables: Two lists are declared in this part of the code, player_salaries and player_rates. These lists store the salaries and the corresponding player rates, respectively.

Function to Calculate Player Rating: The calculate_rating() function is defined in this part of the code. It prompts the user to input the player's skills in the range of 0 to 5, and then it calculates the overall rating of the player based on the given formula. It also prints the sum of the skills and the overall rating on the output screen.

Function to Calculate Player Salary: The calculate_salary() function is defined in this part of the code. It calculates the salary of the player based on their overall rating. The salary is determined by looking up the player rates in the player_rates list and then matching them with the corresponding salary values in the player_salaries list. Finally, the function sets the player_salary variable to the appropriate value.

Main Function: The main() function is defined in this part of the code. It prompts the user to enter the player's name, date of birth, and skill levels. It then calculates the player's age based on their date of birth and calls the calculate_rating() and calculate_salary() functions to determine the player's overall rating and salary, respectively. Finally, it displays all the information in a table using the tabulate module.

Creating Player Data: In this part of the code, a dictionary named player_data is created to store all the player information. The player_id is used as the key, and the player's name, date of birth, age, overall rating, and salary are stored as values.

Output: The final part of the code displays the player data in a tabular format using the tabulate module. The table shows the player's name, date of birth, age, overall rating, and salary.
