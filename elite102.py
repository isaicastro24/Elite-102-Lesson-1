import random
import mysql.connector

connection = mysql.connector.connect()
cursor = connection.cursor()



# Main menu
menu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Steal Money Bank!

1. Check Balance
2. Make a Deposit
3. Withdraw Cash
4. Change Account Information
5. Delete account
6. Log Out
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
# Account settings menu
account_menu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to the Steal Money Bank Account Menu!

1. Change PIN
2. Change First Name
3. Change Last Name
4. Show Account Number
5. Exit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''

# allows user to create a user(which is then supposed to update in database)

def create_new_user():

    #creating account
    create_pin = input("Enter a PIN: ")
    create_account_num = random.randint(1, 1000000)
    deposit = input("Enter an amount to deposit: ")
    new_first_name = input("Enter your first name: ")
    new_last_name = input("Enter your last name: ")

    #transfer data to sql
    data_insertion = ("INSERT INTO userinfo" 
                    "(pin, accountNumber, totalMoney, firstName, lastName)" 
                    "VALUES (%s, %s, %s, %s, %s)")
    data_insert = (create_pin, create_account_num, deposit, new_first_name, new_last_name)

    #add data to sql
    cursor.execute(data_insertion, data_insert)
    connection.commit()
    cursor.close()
    
    #friendly bank talk
    print("Thank you for creating you account!")
    print("Returning to main menu")
