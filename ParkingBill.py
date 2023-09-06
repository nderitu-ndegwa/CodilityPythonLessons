from datetime import datetime

def solution(E, L):
    entry_time = datetime.strptime(E, '%H:%M')
    exit_time = datetime.strptime(L, '%H:%M')
    
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