# Calender
# date+monthcode+last_two_digits+century_code+number_of_leapyears (if leap year and date after feb 29 include year else (year-1))
m_code={'01':1,'02':4,'03':4,'04':0,'05':2,'06':5,'07':0,'08':3,'09':6,'10':1,'11':4,'12':6}
week_code={1:'Sunday',2:'Monday',3:'Tuesday',4:'Wednesday',5:'Thursday',6:'Friday',0:'Saturday'}
x=input('Enter the date to find the day (dd/mm/yyyy): ')
date=int(x[:2])
month=x[3:5]
year=int(x[6:])
valid_date=False
if month in m_code.keys():
    if month in ['01','03','05','07','08','10','12'] and 1<=date<=31:
        valid_date=True
    elif month in ['04','06','09','11'] and 1<=date<=30:
        valid_date=True
    elif month=='02':
        if (year%4==0 and year%100!=0) or (year%400==0):
            if 1<=date<=29:
                valid_date=True
        elif 1<=date<=28:
            valid_date=True
def isleapyear():
    leapyears=(year%100)//4
    if (year%4==0 and year%100!=0) or (year%400==0):
        if month=='01' or month=='02':
            leapyears-=1 
    return leapyears
def monthcode():
    return m_code[month]
def centurycode():
    cen_code=((3 - ((year // 100) % 4)) * 2) % 7
    return cen_code
def main():
    if valid_date:
        moncode=monthcode()
        no_of_leapyears=isleapyear()
        c_code=centurycode()
        s=date+moncode+(year%100)+c_code+no_of_leapyears
        avg=s%7 #Return Remainder
        print(week_code[avg])
    else:
        print('Invalid date, Please enter a valid date')
main()
