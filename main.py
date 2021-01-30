# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


##def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
##if __name__ == '__main__':
 ##   print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#formated strings
#first = 'Niko'
#last = 'Belic'
#poruka = first + ' [' + last + '] je koder'
#msg = f'{first} [{last}] je koder'
#print(poruka)


            #exercise 1
#house_value = 1000000
#credit = True
#if credit:
#    rata = 0.1 * house_value
#else:
#    rata= 0.2 * house_value
#print(f"rata: ${rata}")



            #exercise 2
#acc = 4
#if acc <= 3:                        # name = "J"
 #   print('not long enough sry')    #if len(name) <3:
#elif acc >= 50:
#    print('Too many chars sory')
#else:
#    print('Good name ;)')



            #exercise 3
#weight = int(input('Weight: '))
#unit = input('(L)bs or (K)g: ')
#if unit.upper() == 'L':
 #   converted = weight * 0.45
 #   print(f"You are {converted} kilos")
 #else:
 #   converted = weight / 0.45
 #   print(f"You are {converted} pounds")



            #exercise 4
secretNum = 55
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
     guess = int(input('Guess: '))
     guess_count += 1
     if guess == secretNum:
         print ('GZ buddy! :)')
         break
else:
     print('Sorry,failed guessing :| ')


