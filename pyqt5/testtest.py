import datetime

def current_month_weeks():
    current_date = datetime.date.today()
    current_date = datetime.date(2023, 8, 20)  # test test test 

    start_date = datetime.date(current_date.year, current_date.month, 1)
    end_date = start_date + datetime.timedelta(days=31)
    
    current_week = 1
    week_to_check = (current_date.day - 1) // 7 + 1  # 현재 날짜가 속한 주차 계산
    is_in_week = False
    
    while start_date < end_date:
        if start_date.month != current_date.month:
            break
            
        if current_week == week_to_check:
            is_in_week = True
            break
        
        start_date += datetime.timedelta(weeks=1)
        current_week += 1
    
    if is_in_week:
        print(f"{start_date.strftime('%m월')} {week_to_check}주차")

current_month_weeks()
