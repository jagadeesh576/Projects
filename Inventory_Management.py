veg=['potato','tomato','brinjal','carrot','beetroot','cabbage','cauliflower','cucumber','beans','ladiesfinger','brocolli','banana','radish','capsicum','onion']
quantity=[8,15,10,5,3,20,18,7,5,13,5,15,7,6,50]
cost_price=[25,17,12,46,44,25,26,29,20,13,52,5,14,27,35]
sell_price=[30,20,15,50,50,30,30,35,25,20,55,10,20,35,40]
s_no=[]
name=[]
m_no=[]
s_cart=[]
i_qnt=[]
i_profit=[]
password='abc1234'
profit=0
while True:
    print('Choose one Option')
    print('1. ShopKeeper')
    print('2. Customer')
    ask=int(input('Who are you? '))
    if ask==1:
        Pass=input('Enter the password to get access: ')
        if Pass==password:
            print('What do you want to do? ')
            print('1. Update Inventory')
            print('2. View Inventory')
            print('3. View User details')
            print('4. View Report')
            print('5. Exit')
            action=int(input('Which operation would you like to perform? '))
            # Upadting Inventory
            if action==1:
                print('Select one operation')
                print('1. Add')
                print('2. Remove')
                print('3. Update')
                op=int(input('Which operation would you like to perform? '))
                # Adding vegetables
                if op==1:
                    n=int(input('How many varieties of vegetables would you like to add? '))
                    for i in range(n):
                        while True:
                            veggie=input('Which vegetable would you like to add to your list? ')
                            if veggie.isalpha():
                                veg.append(veggie)
                            else:
                                print('Please enter a valid vegetable name.')
                        print(veggie,'is added to Inventory.')
                        while True:
                            qnty=float(input('Please specify the quantity for the new vegetable (in kilograms): '))
                            if qnty>0:
                                quantity.append(qnty)
                                break
                            else:
                                print('Please enter valid quantity.')
                        print(qnty,'Kgs quantity of',veggie,'is added to Quantity data.')
                        while True:
                            cost=int(input('Enter cost price of new vegetable: '))
                            if cost>0:
                                cost_price.append(cost)
                            else:
                                print('Please enter a valid cost price.')
                        print(cost,'cost price of',veggie,'is added to Cost_Price data.')
                        while True:
                            sell=int(input('Enter selling price of new vegetable: '))
                            if sell>0:
                                sell_price.append(sell)
                            else:
                                print('Please enter valid selling price.')
                        print(sell,'selling price of',veggie,'is added to Selling_price data.')
                # Removing vegetables
                elif op==2:
                    while True:
                        veggie=input('Which vegetable you want to remove? ')
                        if veggie.isalpha():
                            break
                        else:
                            print('Please enter a valid vegetable name.')
                    if veggie in veg: 
                        idx=veg.index(veggie)
                        veg.pop(idx)
                        quantity.pop(idx)
                        cost_price.pop(idx)
                        sell_price.pop(idx)
                        print(veggie,'and all the data of',veggie,'is removed from Inventory.')
                    else:
                        print(veggie,'is not available.')
                        
                # Updating vegetables
                elif op==3:
                    while True:
                        veggie=input('Which vegetable you want to update? ')
                        if veggie.isalpha():
                                break
                        else:
                            print('Please enter a valid vegtable name.')
                    if veggie in veg:
                        idx=veg.index(veggie)
                        v=input('Enter new vegetable name you want to add: ')
                        veg[idx]=v
                        while True:
                            qnty=float(input('Enter the quantity: '))
                            if qnty>0:
                                quantity[idx]=quantity[idx]+qnty
                            else:
                                print('please eanter a valid quantity.')
                        print(qnty,'Kgs of',veggie,'is modified in Quantity data.')
                        while True:
                            cost=float(input('Enter cost price: '))
                            if cost>0:
                                cost_price[idx]=cost
                            else:
                                print('Please enter a valid cost price.')
                        print(cost,'cost price of',veggie,'is added to Cost_Price data.')
                        while True:
                            sell=float(input('Enter the selling price: '))
                            if sell>0:
                                sell_price[idx]=sell
                            else:
                                print('Please enter a valid selling price.')
                        print(sell,'selling price of',veggie,'is added to Selling_price data.')
                    else:
                        print(veggie,'is not available.')
                else:
                    print(op,'?')
                    print('Sorry, there is no such operation.')
                    print('Please choose a valid operation.')
            # View Inventory
            elif action==2:
                print('*'*4,'IVENTORY DETAILS','*'*4)
                print('*'*4,'Vegetable','Quantity','Cost Price','Selling Price','*'*4)
                for a,b,c,d in zip(veg,quantity,cost_price,sell_price):
                    print(a,b,c,d)
                print('*'*27)
            # View User Details
            elif action==3:
                print('*'*4,'CUSTOMER DETAILS','*'*4)
                print('*'*4,'S.No','Name','Moblie Number','*'*4)
                for a,b,c in zip(s_no,name,m_no):
                    print(a,b,c)
                print('*'*26)
            # View Report
            elif action==4:
                for a,b in zip(veg,quantity):
                    print(a,b)
                    print()
                print('*'*4,'ITEM WISE PROFIT','*'*4)
                print('Vegetable','Quantity Sold','Profit')
                # Item wise profit
                # To display the vegetables sold in a day
                for c,d,e in zip(s_cart,i_qnt,i_profit):
                    iprofit=sum(i_profit)
                    print(c,d,'Kgs',e)
                print('*'*26)
                print('*'*4,'TOTAL PROFIT','*'*4)
                print('Today profit is',iprofit)
                print('*'*21)
            # Exiting (Closing the store)
            elif action==5:
                print('*'*4,'Closing the shop','*'*4)
                break
            else:
                print(action,'?')
                print('Sorry, there is no such operation.')
                print('Please, choose a valid option.')
        else:
            print('Incorrect Password.')
    # Customer (Buying vegetables)
    elif ask==2:
        print('*'*4,'Vegetables available in Inventory','*'*4)
        for i in veg:
            print(i)
        print('*'*43)
        cart=[]
        weight=[]
        bill=0
        s_no_cnt=0
        while True:
            print('Which operation would you like to perform? ')
            print('1. Add to cart') 
            print('2. Remove from cart')
            print('3. Modify Cart')
            print('4. View Cart')
            print('5. Billing')
            print('6. Exit')
            action=int(input('Please choose one of the following options: '))
            # To add into cart
            if action==1:
                while True:
                    veggie=input('Which vegetable would you like to purchase? ')
                    if veggie.isalpha():
                        if veggie in veg: #Tomato
                            while True:
                                qnty=float(input('Please enter the quantity you would like to purchase (in kilograms): ')) #5
                                if qnty>0: #10>0 and 10.isdidgit() - T and T - T
                                    break
                                else:
                                    print('Please eneter a valid quantity.')
                                    # Extracting the index of vegetable
                            idx=veg.index(veggie) #veg.index(Tomato)
                            if qnty<=(quantity[idx]): #1<=15 - T
                                if veggie in cart:
                                    cidx=cart.index(veggie)
                                    weight[cidx]=weight[cidx]+qnty
                                    print(veggie,'is added to cart.')
                                else:
                                    cart.append(veggie)
                                    weight.append(qnty)
                            else:
                                print('Insufficient stock.')
                        else:
                            print(veggie,'is not available.')
                    else:
                        print('Please enter a valid vegetable name.')
                    ch=input('Do you want to purchase more? (yes/no): ')
                    if ch=='no':
                        break
            # To remove from cart
            elif action==2:
                while True:
                    veggie=input('Enter vegetable name you want to remove: ')
                    if veggie.isalpha():
                        break
                    else:
                        print('Please enter a valid vegetable name.')
                if veggie in cart:
                    idx=cart.index(veggie)
                    cart.pop(idx)
                    weight_removed=weight.pop(idx)
                    item_idx=veg.index(veggie)
                    quantity[item_idx]=quantity[item_idx]+weight_removed
                    print(veggie,'and all the data of',veggie,'is removed from cart.')
                else:
                    print(veggie,'is not available in cart.')
            #Modify the cart
            elif action==3:
                while True:
                    veggie=input('Enter vegetable  name you want to modify: ')
                    if veggie.isalpha():
                        break
                    else:
                        print('Please enter a valid vegetable name.')
                if veggie in cart:
                    idx=cart.index(veggie)
                    while True:
                        qnty=float(input('Enter quantity you want: '))
                        if qnty>0:
                            weight[idx]=qnty
                            break
                        else:
                            print('Please enter a valid quantity.')
                    print(veggie,'is modified.')
                else:
                    print(veggie,'is not available in cart')
            # View Cart
            elif action==4:
                print('*'*4,'ITEMS IN CART','*'*4)
                print('Vegatable','Quantity')
                for a,b in zip(cart,weight):
                    print(a,b,'Kgs')
                print('*'*18)
            # Billing
            elif action==5:
                # Customer details
                name1=input('Enter customer name: ')
                if name1 in name:
                    idx=name.index(name1)
                    print('*'*4,'CUSTOMER DETAILS','*'*4)
                    print('S_No: ',s_no[idx])
                    print('Name: ',name[idx])
                    print('Moblie Number: ',m_no[idx])
                    print('*'*26)
                else:
                    name.append(name1)
                    while True:
                        mno=input('Enter customer mobile number: ')
                        if len(mno)==10 and mno.isdigit():
                            m_no.append(mno)
                            break
                        else:
                            print('Please enter a valid number')
                    s_no.append(len(s_no)+1)
                # View User Details for billing
                print('*'*4,'CUSTOMER DETAILS','*'*4)
                m=len(s_no)
                print('S.No:',m)
                print('Name:',name1)
                print('Mobile Number:',mno)
                print('*'*26)
                # Displaying vegtables bought by a person
                print('*'*4,'VEGETABLES IN BAG','*'*4)
                # Displaying vegetables and it's quantity after closing the bill
                # Adding them to report
                for a,b in zip(cart,weight):
                        if a in s_cart:
                            didx=s_cart.index(a)
                            vidx=veg.index(a)
                            i_qnt[didx]=i_qnt[didx]+b
                            quantity[vidx]=quantity[vidx]-b
                            i_profit[didx]=i_profit[didx]+(e*sell_price[vidx]-cost_price[vidx])
                            
                        else:
                            vidx=veg.index(a)
                            s_cart.append(a)
                            i_qnt.append(b)
                            quantity[vidx]=quantity[vidx]-b
                            i_profit.append(b*(sell_price[vidx]-cost_price[vidx]))
                        print(a,b,'Kgs')
                for c, d in zip(cart, weight):  
                    vegidx = veg.index(c)  
                    bill = bill + (d*sell_price[vegidx])  
                    profit=profit+(d*(sell_price[idx]-cost_price[idx]))
                print('*'*4,'Thanks for Visiting','*'*4)
                print('The total amount to be paid is: ',bill)
                # Discount
                if 250<=bill<500: #40
                    print('The amount to be paid after applying the discount is',bill-(bill*0.05))
                elif 500<=bill<1000:
                    print('The amount to be paid after applying the discount is',bill-(bill*0.10))
                elif 1000<=bill<2000:
                    print('The amount to be paid after applying the discount is',bill-(bill*0.15))
                elif bill>=2000:
                    print('The amount to be paid after applying the discount is',bill-(bill*0.20))
                else:
                    print('No discount!')
                cart=[]
                weight=[]
                bill=0
            #Exiting from customer
            elif action==6:
                print('Exiting...')
                break
            else:
                print(action,'?')
                print('Sorry, there is no such option.')
                print('Please choose the correct option.')
    else:
        print(ask,'?',sep='')
        print('Sorry, there is no such option.')
        print('Please choose the correct option.')
