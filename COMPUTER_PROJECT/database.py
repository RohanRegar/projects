import mysql.connector as mc
con=mc.connect(host="localhost",user="root",passwd="",database='test')
cur=con.cursor()

q="create table hotel1 (SlNo int(3) Primary Key, Name_Of_Dish varchar(30), Price int(11), Veg_or_Nonveg varchar(10))"
cur.execute(q)

cur.execute("insert into hotel1 values({},'{}',{},'{}')".format(1,'Chicken Tikka',80,'Non-Veg'))
cur.execute("insert into hotel1 values({},'{}',{},'{}')".format(2,'Chicken Pasta',80,'Non-Veg'))
cur.execute("insert into hotel1 values({},'{}',{},'{}')".format(3,'Masala Dosa',60,'Veg'))
cur.execute("insert into hotel1 values({},'{}',{},'{}')".format(4,'Pav Bhaji',50,'Veg'))
cur.execute("insert into hotel1 values({},'{}',{},'{}')".format(5,'Veg Noodles',80,'Veg'))

q="create table hotel2 (SlNo int(3) Primary Key, Name_Of_Dish varchar(30), Price int(11), Veg_or_Nonveg varchar(10))"
cur.execute(q)

cur.execute("insert into hotel2 values({},'{}',{},'{}')".format(1,'Chicken Burger',170,'Non-Veg'))
cur.execute("insert into hotel2 values({},'{}',{},'{}')".format(2,'Chicken Sausage Burger',200,'Non-Veg'))
cur.execute("insert into hotel2 values({},'{}',{},'{}')".format(3,'Aloo Tikki Burger',150,'Veg'))
cur.execute("insert into hotel2 values({},'{}',{},'{}')".format(4,'Paneer Burger',170,'Veg'))
cur.execute("insert into hotel2 values({},'{}',{},'{}')".format(5,'Extra Cheese Paneer Burger',190,'Veg'))

q="create table hotel3 (SlNo int(3) Primary Key, Name_Of_Dish varchar(30), Price int(11), Veg_or_Nonveg varchar(10))"
cur.execute(q)

cur.execute("insert into hotel3 values({},'{}',{},'{}')".format(1,'Orange Juice',20,'Veg'))
cur.execute("insert into hotel3 values({},'{}',{},'{}')".format(2,'Chicken Soup',40,'Non-Veg'))
cur.execute("insert into hotel3 values({},'{}',{},'{}')".format(3,'Samosa Chaat',30,'Veg'))
cur.execute("insert into hotel3 values({},'{}',{},'{}')".format(4,'Papri Chaat',25,'Veg'))
cur.execute("insert into hotel3 values({},'{}',{},'{}')".format(5,'Cheese Toast',25,'Veg'))

q="create table history (Username varchar(30) Primary Key,Password varchar(30), Date_Ordered date, Time_Ordered time, Name_Of_Dish char(30), Price int(4), Rating int(2))"
cur.execute(q)


con.commit()
con.close()
