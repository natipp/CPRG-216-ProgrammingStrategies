print("Welcome to Circle Phones's Profit calculator.")
print('''You can calculate the profit of the company according to a specific day 
or by a week or divide the week into weekdays and weekend''')
print('''1 - For specific Day
2 - For the Week
3 - For Week Business Days
4 - For Weekend days
0 - Exit
''')
time = int(input('Which time period do you want to enter: '))

apple_iphone = 120.45
android_phone = 99.5
apple_tablet = 75.69
android_tablet = 65.73
windows_tablet = 51.49
api = 0
anp = 0
apt = 0
ant = 0
wt = 0
total = 0
quantity_sold = 0
day = 0

while(True):
     if time == 0:
          print('Program End!')
          break
     elif time == 1:
          number = int(input('Enter product number 1-5, or enter 0 to stop:')) 
          if number == 0:
            break
          quantity_sold = int(input('Enter quantity sold:'))
          if number == 1:
           api = quantity_sold * apple_iphone
           total += api
          elif number == 2:
           anp = quantity_sold * android_phone
           total += anp
          elif number == 3:
           apt = quantity_sold * apple_tablet
           total += apt
          elif number == 4:
           ant = quantity_sold * android_tablet
           total += ant
          elif number == 5:
           wt = quantity_sold * windows_tablet
           total += wt
          else:
            print('Invalid input, please enter a valid number')
          print('You total profit for today is:',total)
          if total < 10000:
            print("We didn't reach our goal for this period. More hard work needed. ")
          elif total > 10000:
            print('You did well this period! Keep up the great work!')
     elif time == 2:
        print('For Monday')
        number = int(input('Enter product number 1-5, or enter 0 to stop:')) 
        if number == 0:
            break
        quantity_sold = int(input('Enter quantity sold:'))
        if number == 1:
           api = quantity_sold * apple_iphone
           total += api
        elif number == 2:
           anp = quantity_sold * android_phone
           total += anp
        elif number == 3:
           apt = quantity_sold * apple_tablet
           total += apt
        elif number == 4:
           ant = quantity_sold * android_tablet
           total += ant
        elif number == 5:
           wt = quantity_sold * windows_tablet
           total += wt
        else:
            print('Invalid input, please enter a valid number')
        print('You total profit for today is:',total)
        if total < 10000:
            print("We didn't reach our goal for this period. More hard work needed. ")
        elif total > 10000:
            print('You did well this period! Keep up the great work!')
     elif time == 3:
        if day < 0:
           print('for Monday')
        if day == 5:
         number = int(input('Enter product number 1-5, or enter 0 to stop:')) 
         if number == 0:
            break
         quantity_sold = int(input('Enter quantity sold:'))
         if number == 1:
           api = quantity_sold * apple_iphone
           total += api
         elif number == 2:
           anp = quantity_sold * android_phone
           total += anp
         elif number == 3:
           apt = quantity_sold * apple_tablet
           total += apt
         elif number == 4:
           ant = quantity_sold * android_tablet
           total += ant
         elif number == 5:
           wt = quantity_sold * windows_tablet
           total += wt
         else:
            print('Invalid input, please enter a valid number')
         day += 1
        print('You total profit for today is:',total)
        if total < 10000:
            print("We didn't reach our goal for this period. More hard work needed. ")
        elif total > 10000:
            print('You did well this period! Keep up the great work!')
     elif time == 4:
        if day < 0:
           print('for Monday')
        if day == 2:
         number = int(input('Enter product number 1-5, or enter 0 to stop:')) 
         if number == 0:
            break
         quantity_sold = int(input('Enter quantity sold:'))
         if number == 1:
           api = quantity_sold * apple_iphone
           total += api
         elif number == 2:
           anp = quantity_sold * android_phone
           total += anp
         elif number == 3:
           apt = quantity_sold * apple_tablet
           total += apt
         elif number == 4:
           ant = quantity_sold * android_tablet
           total += ant
         elif number == 5:
           wt = quantity_sold * windows_tablet
           total += wt
         else:
            print('Invalid input, please enter a valid number')
         day += 1
        print('You total profit for today is:',total)
        if total < 10000:
            print("We didn't reach our goal for this period. More hard work needed. ")
        elif total > 10000:
            print('You did well this period! Keep up the great work!')
     else:
        print('Invalid input, please enter a valid number')


 