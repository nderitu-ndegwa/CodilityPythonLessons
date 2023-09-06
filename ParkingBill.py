from datetime import datetime

def solution(E, L):
    entry_time = datetime.strptime(E, '%H:%M')
    exit_time = datetime.strptime(L, '%H:%M')
    
    parked_minutes = (exit_time - entry_time).seconds / 60
    
    parked_full_hours = parked_minutes // 60
    rem_minutes = parked_minutes % 60

    parking_bill = 2
    
    if parked_full_hours > 0 or (parked_minutes // 60) < 1:
        parking_bill += 3
        
    if parked_full_hours > 1:
        parking_bill += (parked_full_hours - 1) * 4
        
    if rem_minutes > 0 and parked_full_hours > 1:
        parking_bill += 4
        
    return int(parking_bill)