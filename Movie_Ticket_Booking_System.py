import copy
username='User'
password='1234'
Movies=['SVSC','MUFASA','ORANGE']
Price=[200,150,200]
Show_time={'11:00 AM':'SVSC','2:30 PM':'MUFASA','6:00 PM':'ORANGE','9:00 PM':'SVSC'}
Seats1={
    'A':[1,2,3,4,5,6,7,8,9],
    'B':[1,2,3,4,5,6,7,8,9],
    'C':[1,2,3,4,5,6,7,8,9],
    'D':[1,2,3,4,5,6,7,8,9],
    'E':[1,2,3,4,5,6,7,8,9]
    }
Seats11=copy.deepcopy(Seats1)
Seats2={
    'A':[1,2,3,4,5,6,7,8,9],
    'B':[1,2,3,4,5,6,7,8,9],
    'C':[1,2,3,4,5,6,7,8,9],
    'D':[1,2,3,4,5,6,7,8,9],
    'E':[1,2,3,4,5,6,7,8,9]
    }
Seats3={
    'A':[1,2,3,4,5,6,7,8,9],
    'B':[1,2,3,4,5,6,7,8,9],
    'C':[1,2,3,4,5,6,7,8,9],
    'D':[1,2,3,4,5,6,7,8,9],
    'E':[1,2,3,4,5,6,7,8,9]
    }
Seats4={
    'A':[1,2,3,4,5,6,7,8,9],
    'B':[1,2,3,4,5,6,7,8,9],
    'C':[1,2,3,4,5,6,7,8,9],
    'D':[1,2,3,4,5,6,7,8,9],
    'E':[1,2,3,4,5,6,7,8,9]
    }
Seats=[Seats1,Seats2,Seats3,Seats4]
def movies():
    print('*'*4,'In Cinemas','*'*4)
    for i in Movies:
        print(i)
    print('*'*20)
def nooftickets(t):
    if 1<=t<=4:
        return True
    else:
        return False
def show(mtime):
    if mtime=='11:00 AM':
        return Seats[0]
    elif mtime=='2:30 PM':
        return Seats[1]
    elif mtime=='6:00 PM':
        return Seats[2]
    elif mtime=='9:00 PM':
        return Seats[3]
    else:
        return None
def emptyseats(mtime):
    res=show(mtime)
    for i in res.items():
        print(i)
def countseats(mtime):
    cnt=0
    res=show(mtime)
    for i in res.values():
        a=len(i)
        cnt+=a
    return cnt
def upcase(s):
    return s.upper()
def main():
    while True:
        print('Choose one option')
        print('1. Owner')
        print('2. Customer')
        print('3. Exit')
        n=int(input('Enter an option: '))
        if 1<=n<=3:
            if n==1:
                user=input('Enter user name: ')
                Pass=input('Enter password: ')
                if username==user and password==Pass:
                    while True:
                        print('Choose one option')
                        print('1. Add new movie')
                        print('2. Update movie price')
                        print('3. Update available seats')
                        print('4. Display all Movies')
                        print('5. Return to main Menu')
                        op=int(input('What do you want to perform: '))
                        if 1<=op<=5:
                            if op==1:
                                if 1<=len(Movies)<=3:
                                    mtime=input('Enter show time: ')
                                    user=input('Enter the movie name: ')
                                    mname=upcase(user)
                                    mprice=int(input('Enter the price of movie: '))
                                    if mtime in Show_time.keys():
                                        if mname in Movies:
                                            print(mname,'is available')
                                            print('A movie name is allowed only once')
                                        else:
                                            Movies.append(mname)
                                            Price.append(mprice)
                                            Show_time[mtime]=mname
                                            print(mname,'is added')
                                    else:
                                        print('Please enter a valid show time')
                                else:
                                    print('Maximum Limit reached')
                                    print('Do you want to update the existing movie? (yes/no): ')
                                    user=input('Enter your choice: ')
                                    choice=upcase(user)
                                    if choice=='YES':
                                        user=input('Which movie you want to update? ')
                                        oldmovie=upcase(user)
                                        if oldmovie in Movies:
                                            idx=Movies.index(oldmovie)
                                            user=input('Enter new movie name: ')
                                            newmovie=upcase(user)
                                            newprice=int(input('Enter the price of movie: '))
                                            if newmovie in Movies:
                                                print('Movie is already available')
                                            else:
                                                Movies[idx]=newmovie
                                                Price[idx]=newprice
                                                print(newmovie,'is updated with',oldmovie)
                                        else:
                                            print('Movie deos not exist')
                                    else:
                                        continue
                            elif op==2:
                                user=input('Enter movie name to update price: ')
                                mname=upcase(user)
                                if mname in Movies:
                                    idx=Movies.index(mname)
                                    newprice=int(input('Enter the new price: '))
                                    Price[idx]=newprice
                                    print('Price of',mname,'is updated')
                                else:
                                    print('Movie is not available')
                            elif op==3:
                                mtime=input('Enter show time: ')
                                if mtime in Show_time:
                                    if mtime=='11:00 AM':
                                        Seats1.clear()
                                        Seats1.update(copy.deepcopy(Seats11))
                                    elif mtime=='2:30 PM':
                                        Seats2.clear()
                                        Seats2.update(copy.deepcopy(Seats11))
                                    elif mtime=='6:00 PM':
                                        Seats3.clear()
                                        Seats3.update(copy.deepcopy(Seats11))
                                    elif mtime=='9:00 PM':
                                        Seats4.clear()
                                        Seats4.update(copy.deepcopy(Seats11))
                                    print(mtime,'show seats are updated')
                                else:
                                    print('Please enter an appropriate show time')
                            elif op==4:
                                movies()
                            elif op==5:
                                break
                            
                        else:
                            print('Please select appropriate option')
                else:
                    print('Invalid username or password')
            elif n==2:
                while True:
                    print('Choose one option: ')
                    print('1. Display Available Movies')
                    print('2. Select Movie to Book Tickets')
                    print('3. Check seat availability')
                    print('4. Return to Main Menu')
                    op=int(input('Choose one option: '))
                    if 1<=op<=4:
                        if op==1:
                            movies()
                        elif op==2:
                            print(Show_time)
                            user=input('Enter one movie name: ')
                            mname=upcase(user)
                            mtime=input('Enter show time: ')
                            if mname in Movies:
                                if Show_time[mtime]==mname:
                                    tickets=int(input('Enter number of tickets: '))
                                    res=nooftickets(tickets)
                                    if res==True:
                                        available_seats=countseats(mtime)
                                        if tickets<=available_seats:
                                            emptyseats(mtime)
                                            user=input('Choose a row: ')
                                            row=upcase(user)
                                            seats=list(map(int,input('Enter seat numbers: ').split()))
                                            if tickets==len(seats):
                                                res=show(mtime)
                                                if row in res.keys():
                                                    for i in seats:
                                                        if i in res[row]:
                                                            res[row].remove(i)
                                                    print('Booking Confirmed')  
                                                else:
                                                    print('The seats you choosen are not available')
                                            else:
                                                print('You are entered wrong seat count please enter same as begining count ')
                                        else:
                                            print(tickets,'tickets is not available')
                                    else:
                                        print('You can only book from 1 to 4 seats only')
                                else:
                                    print('This movie is not available for this show')
                            else:
                                print(mname,'Movie is not availble')
                        elif op==3:
                            print(Show_time)
                            Time=input('Please enter the showtime you would like to check: ')
                            if Time in Show_time:
                                tickets=int(input('Enter number of tickets: '))
                                res=nooftickets(tickets)
                                if res==True:
                                    available_seats=countseats(Time)
                                    if tickets<=available_seats:
                                        print(tickets,'tickets are available for this show')
                                    else:
                                        print('Seats not available')
                                else:
                                    print('You can only book from 1 to 4 seats only')
                            else:
                                print('No show at the time you mentioned')
                        elif op==4:
                            break
                    else:
                        print('Please select appropriate option')
            elif n==3:
                break
        else:
            print('Please select appropriate option')
main()
