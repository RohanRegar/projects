import datetime
import random
import csv
account=open('account.csv','a+',newline='')
                                 
import mysql.connector as mc
con=mc.connect(host="localhost",user="root",passwd="",database='test')
cur=con.cursor()

def createaccount():
    wf=csv.writer(account)
    name=eval(input('Enter the name'))
    mobile=eval(input('Enter the mobile'))
    global user
    global passwd
    user=eval(input('Enter the userid'))
    passwd=eval(input('Enter the password'))
    preference=eval(input('Enter your preference. For non-veg type Non-Veg\nFor veg press Veg\nFor both press ANY'))
    wf.writerow([name,mobile,user,passwd,preference])

def verify(user,passwd):
    flag=0
    r=csv.reader(account)
    account.seek(0)
    for data in r:
        if (user in data) and (passwd in data):
            
            flag=1
            break
    return flag
def drawtable(hotel):
    print(65*'-')
    print('|SlNo',4*' ','|','Name Of Dish',15*' ','|','Price',3*' ','|','Type',2*' ','|')
    print(65*'-')
    for data in hotel:
        slno=str(data[0])
        dish=data[1]
        price=str(data[2])
        x=data[3]
        while len(slno)<8:
            slno+=' '
        while len(dish)<28:
            dish+=' '
        while len(price)<9:
            price+=' '
        while len(x)<7:
            x+=' '
        
        print('|',slno,'|',dish,'|',price,'|',x,'|')
    print(65*'-')

def preference(user):
    r=csv.reader(account)
    account.seek(0)
    for data in r:
        if (user in data):
            x=data[4]
    return x
    
def display(preference):
    if preference!='ANY':
        print("\t\t\t\thotel 1")
        cur.execute("select * from hotel1 where Veg_or_Nonveg='{}'".format(preference))
        rows=cur.fetchall()
        hotel=[]
        for R in rows:
            hotel.append(R)
        drawtable(hotel)
        print("\t\t\t\thotel2")
        cur.execute("select * from hotel2 where Veg_or_Nonveg='{}'".format(preference))
        rows=cur.fetchall()
        hotel=[]
        for R in rows:
            hotel.append(R)
        drawtable(hotel)
        print("\t\t\t\thotel3")
        cur.execute("select * from hotel3 where Veg_or_Nonveg='{}'".format(preference))
        rows=cur.fetchall()
        hotel=[]
        for R in rows:
            hotel.append(R)
        drawtable(hotel)
    else:
        print("Menu hotel1")
        cur.execute("select * from hotel1")
        rows=cur.fetchall()
        hotel=[]
        for R in rows:
            hotel.append(R)
        drawtable(hotel)
        print("menu hotel2")
        cur.execute("select * from hotel2")
        rows=cur.fetchall()
        hotel=[]
        for R in rows:
            hotel.append(R)
        drawtable(hotel)
        print("menu hotel3")
        cur.execute("select * from hotel3")
        rows=cur.fetchall()
        hotel=[]
        for R in rows:
            hotel.append(R)
        drawtable(hotel)

def time(x=' '):
    now=datetime.datetime.now()
    dt_string = now.strftime("%H:%M")
    
    minutes=int(dt_string[3:5])+30
    hour=int(dt_string[0:2])

    if x==' ':
        if minutes>60:
            minutes=str(minutes-60)
            if len(minutes)<2:
                minutes='0'+minutes
            hour=str(hour+1)
        else:
            minutes=str(minutes)
            hour=str(hour)
        return (hour+':'+minutes)
    else:
        return dt_string
    
def bank(user):
    r=csv.reader(account)
    account.seek(0)
    for data in r:
        if (user in data):
            x=data[5]
    return x
    
def date():
    now=datetime.datetime.now()
    dt_string = now.strftime("%d-%m-%y")
    return dt_string

while True:
    prompt1=eval(input('''1)For creating a new account press 1\n2)For logging in press 2:-\n'''))
    print()
    if prompt1==1:
        createaccount()
    elif prompt1==2:
        user=eval(input('Enter the userid:-'))
        passwd=eval(input('Enter the password:-'))
        if verify(user,passwd)==1:
            print('Login success\n')
        else:
            print('Incorrect details\n')
            break
    #display the hotels...
    while True:
        prompt2=eval(input('''1)For displaying restaurants based on your profile\n2)For displaying all restaurants:-'''))
        if prompt2==2:
            display('ANY')
            print()
            break
        elif prompt2==1:
            x=preference(user)
            display(x)
            print()
            break
        else:
            print('Enter correct option')
    while True:
        hotel=eval(input('''Enter the name of the restaurant of your choice:-'''))
        dish=eval(input('''Enter the serial number of the dish of the restaurant:-'''))
        if hotel=='hotel1':
             cur.execute("select Name_of_dish,Price from hotel1 where SlNo={}".format(dish))
             break
        elif hotel=='hotel2':
             cur.execute("select Name_of_dish,Price from hotel2 where SlNo={}".format(dish))
             break
        elif hotel=='hotel3':
             cur.execute("select Name_of_dish,Price from hotel3 where SlNo={}".format(dish))
             break
        else:
            print('Enter the correct restaurant name')
    data=cur.fetchall()
    nameofdish,price=data[0]
        
    while True:
        prompt3=eval(input('1)For takeaway press 1\n2)For dine-in press 2\n3)For delivery press 3'))
        if prompt3==1:
            print('Your order of',nameofdish,'price',price,'will be ready after 30 minutes within',time())
            break
        elif prompt3==2:
            print('Table',random.randint(1,20),'has been reserved for your order of',nameofdish,' price',price,'and will be ready within',time())
            break
        elif prompt3==3:
            print('Your order of',nameofdish,'price',price,'will be delivered to your address within 30 minutes before',time(),'\n')
               
            break
        else:
            print('Enter the correct option')

    rating=eval(input('Enter your rating out of 10'))
    q="insert into History values ('{}','{}','{}','{}','{}',{},{})".format(user,passwd,date(),time('current'),nameofdish,price,rating)
    cur.execute(q)
    con.commit()
    break
        
            
account.close()
con.close()
