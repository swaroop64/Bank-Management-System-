print('-'*20)

#decalring some customer details
cust_names = ['Swaroop', 'Bhanu', 'Yaswanth', 'Sofia']
cust_pins = [1234,2345,3456,4567]
cust_bal = [10000,5000,8000,4000]

deposition = 0
withdrawal = 0
balance = 0
counter_1 = 1
counter_2 = 4
i = 0

#to run the program continously,
while True:
    #to display the menu
    print("-"*15)
    print('-----Welcome to Python Bank-----')
    print('*'*32)
    print('>> 1. Open a new account')
    print('>> 2. Withdraw money')
    print('>> 3. Deposit money')
    print('>> 4. Check balance')
    print('>> 5. Exit')
    print('-'*32)

    #taking the input of menu from users;
    choice = int(input("Enter your choice from the menu: "))
    #let's  define the working of the menu;
    if choice == 1:
        print(f'Choice of the customer is: {choice}')
        #the below line will take the no. of customers from user
        NOC = eval(input('Number of Customers:'))
        i = i + NOC
        #we use if condition to restrict the no. of new accounts to 4.
        if i > 5:
            print('\n')
            print('Sorry, you can not open more than 5 accounts')
            i = i - NOC
        else:
            while counter_1 <= i:
                #the below line will take the name of the customer from user
                cust_names.append(input('Please enter your full name: '))
                #the below line will take the pin of the customer from user
                cust_pins.append(eval(input('Please enter your pin: ')))
                #the below line will take the balance of the customer from user
                balance = 0
                deposition = eval(input('Please input a value to be deposited to start an account:'))
                balance = balance + deposition
                cust_bal.append(balance)
                print('\nName = ', end = " ")
                print(cust_names[counter_2])
                print('\nPIN = ',end = ' ')
                print(cust_pins[counter_2])
                print('\nBalance = ',end = ' ')
                print(cust_bal[counter_2], end = ' ')
                print('-/Rs')
                counter_1 = counter_1 + 1
                counter_2 = counter_2 + 1
                print('\nYour Name is now added to the customers system')
                print("Your pin is added to customer system")
                print("Your balance is added to customer system")
                print("----New account created successfully !----")
                print("\n")
                print("Your name is avalilable on the customers list now : ")
                print(cust_names)
                print("\n")
                print("Note! Please remember the Name and Pin")
                print("-"*34)

                #now the below statement will help you to go back to the start menu
        mainmenu = input('Please press the "ENTER" key  to go back to the Main Menu to perform another function or exit..')
    elif choice == 2:
        j = 0
        print(f'Choice of the customer is: {choice}')
        #we use while loop to avoid/prevent the user using the account if the U_name or PIN is wrong
        while j < 1:
            k = -1
            name = input('Please input your Name: ')
            pin = eval(input('Please input your PIN: '))
            #we use while loop, to keep the function running when variable k is smaller than length of the cust_names list
            while k < len(cust_names) - 1:
                k += 1
                #we use if condition to check if the name and pin are correct and matches
                if cust_names[k] == name and cust_pins[k] == pin:
                    j = j + 1
                    #these few statements  will show the balance taken from the list
                    print('Your Current balance: ', end = ' ')
                    print(cust_bal[k], end = ' ')
                    print('-/Rs\n')
                    balance = (cust_bal[k])
                    #these few statements will help you to withdraw money from the account
                    withdraw = eval(input('Please enter the amount you want to withdraw: '))
                    if withdraw > balance:
                        deposition = eval(input('Please deposit a higher value. \nInsuffifient Funds'))
                        #update the balance
                        balance = balance + deposition
                        print('your Current Balance:', end = ' ')
                        print(balance, end = ' ')
                        print('-/Rs\n')     # 1000-200=800
                        print('-----Withdrawal Successfull!-----')
                        cust_bal[k]=balance
                        print('Your Balance:', balance, end=' ')
                        print("-/Rs\n\n")
                    else:
                        balance = balance - withdraw
                        print('\n')
                        print('-----Withdraw Successful!-----')
                        cust_bal[k] = balance
                        print('Your New Balance:', balance, end=' ')
                        print("-/Rs\n\n")
            if j < 1:
                print('Your name and pin does not match!\n')
                break
        mainmenu = input('Please press the "ENTER" key  to go back to the Main Menu to perform another function or exit..')
    elif choice == 3:
        print(f'Choice of the customer is: {choice}')
        n = 0
        # The while loop below would work when the pin or the username is wrong.
        while n < 1:
            k = -1
            name = input("Please input Name: ")
            pin = eval(input("Please input PIN: "))
            # The while loop below will keep the function running to find the correct user.
            while k < len(cust_names) - 1:
                k = k + 1
                # The two if conditions below would find whether both the pin and the name is correct.
                if name == cust_names[k]:
                    if pin == cust_pins[k]:
                        n = n + 1
                        # These statements below would show the customer balance and update list values according to
                        # the deposition made.
                        print("Your Current Balance: ", end=" ")
                        print(cust_bal[k], end=" ")
                        print("-/Rs")
                        balance = (cust_bal[k])
                        # This statement below takes the depositionn from the customer.
                        deposition = eval(input("Enter the value you want to deposit : "))
                        balance = balance + deposition # 1000+500=1500
                        cust_bal[k] = balance
                        print("\n")
                        print("----Deposition successful!----")
                        print("Your New Balance: ", balance, end=" ")
                        print("-/Rs\n\n")
            if n < 1:
                print("Your name and pin does not match!\n")
                break
            # This statement below helps the user to go back to the start of the program (main menu).
        mainmenu = input('Please press the "ENTER" key  to go back to the Main Menu to perform another function or exit..')
    elif choice == 4:
        print(f'Choice of the customer is: {choice}')
        k = 0
        print('Customer name list and balances mentioned below:')
        print('\n')
        while k < len(cust_names) - 1:
            print(f'Customer Name: {cust_names[k]}')
            print(f'Customer Balance: {cust_bal[k]}')
            print('-/Rs')
            print('\n')
            k = k + 1
        mainmenu = input('Please press the "ENTER" key  to go back to the Main Menu to perform another function or exit..')
    elif choice == 5:
        print(f'Choice of customer is: {choice}')
        print('Thank you for using our banking system!\n')
        print('Please Visit Again\n')
        break
    else:
        print('Invalid choice. Please choose a valid option.\n')
        print('\nPlease Try Again')
        mainmenu = input("Please press the Enter key to go back to main menu and perform another action or exit...")