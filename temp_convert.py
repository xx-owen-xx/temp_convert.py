# Author: Owen Fissel
# username: xx-owen-xx
# date: 06/23/25
# task: prompt user to input a temperature in celcius and then convert that temperature to fahrenheit
 

#prompts user to input 5 numbers
num_1 = float(input('input one number: '))
num_2 = float(input('input one number: '))
num_3 = float(input('input one number: '))
num_4 = float(input('input one number: '))
num_5 = float(input('input one number: '))

#divides the inputs by 5 (the number of inputs) giving us the mean or average
average =((num_1 + num_2 + num_3 + num_4 + num_5) / 5)
#prints the result (average)
print('The average of those numbers:\n',(average))
