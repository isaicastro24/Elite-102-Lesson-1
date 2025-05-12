import random
import mysql.connector

connection = mysql.connector.connect() #gets out sql table
cursor = connection.cursor() #allows us to manipulate sql table



#data used to refernece
account_pin = input("Enter your account PIN: ")
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')


# Main menu
menu = '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Welcome to Steal Money Bank!

1. Check Balance
2. Make a Deposit
3. Withdraw Cash
4. Change PIN
5. Show Account Number
6. Change First Name
7. Change Last Name
8. Delete account
9. Log Out
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
    print("Thank you for creating your account!")
    print("Returning to main menu")


#check total $ amount in account
def total_money_in_account():
    cursor = connection.cursor()
    see_money = ("SELECT totalMoney FROM userinfo WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(see_money,(account_pin, first_name, last_name))
    for totalmoney in cursor:
        print("Your total balance is: " + str(totalmoney[0]))
    cursor.close()

#updates current money with deposit made into account
def making_deposit():
    cursor = connection.cursor()
    deposit = float(input("Enter amount to deposit: "))
    get_total_money = ("SELECT totalMoney FROM userinfo WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(get_total_money, (account_pin, first_name, last_name))
    for amts in cursor:
        amt = float(str(amts[0]))
    money = deposit + amt
    new_money = ("UPDATE userinfo SET totalMoney = %s WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(new_money, (money, account_pin, first_name, last_name))
    connection.commit()
    print("Your new total balance is: " + str(money))
    cursor.close()

# updates current money with money being withdrawn(subtracted)
def withdraw_money():
    cursor = connection.cursor()
    withdraw = float(input("Enter amount to withdraw: "))
    get_total_money = ("SELECT totalMoney FROM userinfo WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(get_total_money, (account_pin, first_name, last_name))
    for amts in cursor:
        amt= float(str(amts[0]))
    money = amt - withdraw
    new_money = ("UPDATE userinfo SET totalMoney = %s WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(new_money, (money, account_pin, first_name, last_name))
    connection.commit()
    print("Your new total balance is: " + str(money))
    cursor.close()

#allows users to change their pin
def changing_pin():
    cursor = connection.cursor()
    new_pin = input("Enter your new pin: ")
    update_pin = ("UPDATE userinfo SET pin = %s WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(update_pin, (new_pin, account_pin, first_name, last_name))
    connection.commit()
    print("PIN updated")
    cursor.close()
    print('Log back in using your new pin')
    exit()

#shows a user's account number
def show_account_num():
    cursor = connection.cursor()
    account_num = ("SELECT accountNumber FROM userinfo WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(account_num, (account_pin, first_name, last_name))
    for num in cursor:
        print("You account number is: " + str(num[0]))
        cursor.close()
        print('Please log back in for safety issues')
        exit()

#allows users to change first name
def changing_first():
    cursor = connection.cursor()
    new_first = input("Enter your new first name: ")
    update_first = ("UPDATE userinfo SET firstName = %s WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(update_first, (new_first, account_pin, first_name, last_name))
    connection.commit()
    print("First name updated")
    cursor.close()
    print('Log back in using your new first name')
    exit()

#allows user to change their last name
def changing_last():
    cursor = connection.cursor()
    new_last = input("Enter your new last name: ")
    update_last = ("UPDATE userinfo SET lastName = %s WHERE pin = %s AND firstName = %s AND lastName = %s")
    cursor.execute(update_last, (new_last, account_pin, first_name, last_name))
    connection.commit()
    print("Last name updated")
    cursor.close()
    print('Log back in using your new last name')
    exit()

#user can delete account or not, either ways, will be logged out of system
def deleting_account():
    cursor = connection.cursor()
    caution = input("Would you like to proceed (yes/no): ").lower()
    if caution == 'yes':
        delete_account = ("DELETE FROM userinfo WHERE pin = %s AND firstName = %s AND lastName = %s")
        cursor.execute(delete_account, (account_pin, first_name, last_name))
        connection.commit()
        print("Account deleted")
        print('Logging out...')
        exit()
    else:
        print('Thank you for staying with us!')
        print('Please log back in for safety issues')
        exit()

#checking if a account already exists
new_user = input('Are you a new Steal Money Bank user? (yes/no): ').lower()
while new_user == 'yes':
    create_new_user()
    new_user = input('Are you a new Big Bank user: ')   

#runs entire banking system
using_menu = int(input(menu))
while using_menu != 9:
    if using_menu == 1:
        total_money_in_account()
        using_menu = int(input(menu))
    elif using_menu == 2:
        making_deposit()
        using_menu = int(input(menu))
    elif using_menu == 3:
        withdraw_money()
        using_menu = int(input(menu))
    elif using_menu == 4:
        changing_pin()
        using_menu = int(input(menu))
    elif using_menu == 5:
        show_account_num()
        using_menu = int(input(menu))
    elif using_menu == 6:
        changing_first()
        using_menu = int(input(menu))
    elif using_menu == 7:
        changing_last()
        using_menu = int(input(menu))
    elif using_menu == 8:
        deleting_account()
        using_menu = int(input(menu))
    else:
        print('Thank you for using for using Steal Money Bank! Have a great day!')
        exit()
