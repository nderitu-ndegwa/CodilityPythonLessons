'''
TASK:



You parked your car in a parking lot and want to compute the total cost of the ticket. The billing rules are as follows:

        The entrance fee of the car parking lot is 2;
        The first full or partial hour costs 3;
        Each successive full or partial hour (after the first) costs 4.

You entered the car parking lot at time E and left at time L. In this task, times are represented as strings in the format "HH:MM" (where "HH" is a two-digit number between 0 and 23, which stands for hours, and "MM" is a two-digit number between 0 and 59, which stands for minutes).

Write a function:

    def solution(E, L)

that, given strings E and L specifying points in time in the format "HH:MM", returns the total cost of the parking bill from your entry at time E to your exit at time L. You can assume that E describes a time before L on the same day.

For example, given "10:00" and "13:21" your function should return 17, because the entrance fee equals 2, the first hour costs 3 and there are two more full hours and part of a further hour, so the total cost is 2 + 3 + (3 * 4) = 17. Given "09:42" and "11:42" your function should return 9, because the entrance fee equals 2, the first hour costs 3 and the second hour costs 4, so the total cost is 2 + 3 + 4 = 9.

Assume that:

        strings E and L follow the format "HH:MM" strictly;
        string E describes a time before L on the same day.

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

'''


from datetime import datetime

def solution(E, L):
    entry_time = datetime.strptime(E, '%HH:%MM')
    exit_time = datetime.strptime(L, '%HH:%MM')
    
    #Get total minutes
    parked_minutes = (exit_time - entry_time).seconds / 60
    
    #Conversion to hours and remainder in minutes
    parked_full_hours = parked_minutes // 60
    rem_minutes = parked_minutes % 60

    #Initial parking fee
    parking_bill = 2
    
    #Up to 1 hour or less
    if parked_full_hours > 0 or (parked_minutes // 60) < 1:
        parking_bill += 3
    
    #Additional hours after the first one hour 
    if parked_full_hours > 1:
        parking_bill += (parked_full_hours - 1) * 4
    
    #All additional minutes after the first one hour
    if rem_minutes > 0 and parked_full_hours > 1:
        parking_bill += 4
        
    return int(parking_bill)