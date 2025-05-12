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