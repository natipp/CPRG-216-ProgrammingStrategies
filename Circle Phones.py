print("Welcome to Circle Phones's Profit calculator.")

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


while(True):
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


