from datetime import datetime

def solution(E, L):
    
    en_time = datetime.strftime(E, '%H:%M')
    ex_time = datetime.strftime(L, '%H:%M')
    
    parked_minutes = (ex_time - en_time).seconds / 60

    parked_full_hours = parked_minutes // 60
    rem_minutes = parked_minutes % 60

    ent_fee = 2