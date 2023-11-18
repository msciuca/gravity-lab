def calculate_average_time(time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8, time_9, time_10):

  # Create a list of time variables
  time_variables = [time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8, time_9, time_10]

  # Calculate the sum of the time variables
  sum_time = sum(time_variables)

  # Calculate the number of time variables
  num_time_variables = len(time_variables)

  # Calculate the average time
  average_time = sum_time / num_time_variables

  # Return the average time
  return average_time

time_1 = float(input("Enter time 1: "))
time_2 = float(input("Enter time 2: "))
time_3 = float(input("Enter time 3: "))
time_4 = float(input("Enter time 4: "))
time_5 = float(input("Enter time 5: "))
time_6 = float(input("Enter time 6: "))
time_7 = float(input("Enter time 7: "))
time_8 = float(input("Enter time 8: "))
time_9 = float(input("Enter time 9: "))
time_10 = float(input("Enter time 10: "))

average_time = calculate_average_time(time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8, time_9, time_10)

print("The average time is:", average_time)
