# Added for Data warehouse purposes:
# - Location moved to rent as City -> District (from dictionary) v
# - Employee age v
# - Task cost v
# - Proper categories to payments/repairs v  
# - Days of delay in payment v
# - Client age instead of birthday v
# - Add client category to user experience v
# - Add to rent: rent duration, wait time v
# - Think about review category, age category and length category 
#   in terms of payment (there might be payments without this data)
# Generator for T1 

import numpy as np
import random
random.seed(1001)
import pandas as pd
payments = 0 

# open file and append 
f = open("bulk/carsT1.bulk", "w")
v = open("txt/vins.txt","r")

# define cars models dictionary
cars_dict = {'Opel':['Astra','Corsa','Zafira'],'Renault':['Clio','Megane','Zoe'],'Hyundai':['i20','i30','Tucson'],'Kia':['Rio','Ceed','Sorento'],
'Mercedes':['C200d','GLC200d','E63s']}

# create 350 cars
for i in range(350):
    random.seed(i)
    # put car id in front
    f.write(str(i)+';')

    # get the vin from txt file 
    vin = v.readline()
    vin = vin[:-1]
    
    f.write(str(vin)+';')
    # generate car model 
    brand = random.choice(list(cars_dict))
    model = random.choice(cars_dict[brand])
    # generate production year 
    year = random.randint(2020,2021)
    # generate fuel level
    fuel = random.randint(1,500)
    # generate door status 
    door = random.randint(0,3)
    # generate warning lights 
    warning = 0
    # generate location 
    loc_lat = round(random.uniform(49,54),5)
    loc_long = round(random.uniform(17,23),5)
    # mileage generator
    mileage = random.randint(20,35000)
    #power generator 
    if model == 'Corsa' or model == 'Clio' or model == 'i20' or model == 'Rio':
        power = 85
        price_list = 0
    elif model == 'Astra' or model == 'Megane' or model == 'i30' or model == 'Ceed':
        power = 125
        price_list = 1
    elif model == 'Zafira' or model == 'Zoe' or model == 'Tucson' or model == 'Sorento':
        power = 160
        price_list = 2
    else:
        power = 220
        price_list = 3
    # drive type generator 
    if brand == 'Mercedes':
        drive = 'AWD'
    else:
        drive = 'FWD'

    # put data into bulk 
    f.write(str(price_list) + ';' + str(brand) + ' ' + str(model) + ';' + str(year) + ';' + str(fuel) + ';' + str(door) + ';' + str(warning) + ';')
    f.write(str(mileage) + ';' + str(power) + ';' + str(drive))
    #f.write(str(cars_dict[brand])+';'+str(cars_dict[brand][model])+';')

    # price list id from 1 to 4 

    # endline after every car
    f.write('\n')


#open and read the file after the appending:
#f = open("cars.bulk", "r")
#print(f.read())

# generating customers 
import random
random.seed(1001)
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
months = ['01','02','03','04','05','06','07','08','09','10','11','12']
fnames = open('txt/cust_name.txt','r')
fpesel = open('txt/cust_pesel.txt','r')
#fmail = open('txt/cust_mail.txt','r')
f = open('bulk/customersT1.bulk','w')

# e_mail

for i in range(0,500):
    customerid = i
    name = fnames.readline()
    name = name[:-1]
    pesel = fpesel.readline()
    pesel = pesel[:-1]
    #email = fmail.readline()
    email = 'test'+str(i)+'@gmail.com'

    login = name[:5].lower()
    password = random.choice(letters)+str(random.randint(1000,9999))

    driver_num = str(random.randint(10000,99999))+'/'+str(random.randint(10,99))+'/'+str(random.randint(1000,9999))
    id_number = random.choice(letters)+random.choice(letters)+str(random.randint(1000,9999))

    card_number = random.randint(1000000000000000,9999999999999999)
    card_m = random.choice(months)
    #if card_m < 10:
    #    card_m = '0'+str(card_m)
    card_expire = str(card_m)+'/'+str(random.randint(23,27))
    card_ccv = random.randint(100,999)

    gender = random.randint(0,1)

    # changed birthdate to just age 
    birthdate = random.randint(20,70)

    reg_date = str(random.randint(2021,2022))+'-'+str(random.choice(months))+'-'+str(random.randint(10,28))

    f.write(str(customerid)+';'+str(name)+';'+str(pesel)+';'+str(email)+';'+str(login)+';'+str(password)+';'+
    str(driver_num)+';'+str(id_number)+';'+str(card_number)+';'+str(card_expire)+';'+str(card_ccv)+';'+
    str(gender)+';'+str(birthdate)+';'+str(reg_date)+'\n')

# generating employees 
# employeeid, name, pesel, driver_number
# id_number, position 
pos = ['manager','cleaner','driver','agent']
f = open('bulk/employeesT1.bulk','w')
namez = open('txt/names.txt','r',encoding='utf-8')
peselz = open('txt/pesele.txt','r',encoding='utf-8')
import random 
random.seed(1001)
for i in range (0,50):
     # get the name from txt file 
    name = namez.readline()
    name = name[:-1]
    # get the pesel from txt file
    pesel = peselz.readline()
    pesel = pesel[:-1]
    # get driver num
    num1=random.randint(10000,99999)
    num2=random.randint(10,99)
    num3=random.randint(1000,9999)
    driver_num = str(num1)+'/'+str(num2)+'/'+str(num3)
    # get id num
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sign1 = random.choice(letters)
    sign2 = random.choice(letters)
    num4 = random.randint(10000,99999)
    id_number = str(sign1)+str(sign2)+str(num4)
    # position gen 
    position = random.choice(pos)
    emp_age = random.randint(20,45)

    f.write(str(i)+';'+name+';'+str(pesel)+';'+str(driver_num)+';'+str(id_number)+';'+str(position)+';'+str(emp_age)+'\n')

import random 
random.seed(1001)
file = open('bulk/PListT1.bulk','w')
# price list generating for 4 classes of cars 
# attributes: price_listID, hour_price, mileage_price,
# starting_fee, date of start, date of finish 
temp = [1.0,1.5,2,2.5]
date = ['2021-01-01','2021-04-01','2021-07-01','2021-10-01',
        '2021-03-31','2021-06-30','2021-09-30','2021-12-31',
        '2022-01-01','2022-04-01','2022-07-01','2022-10-01',
        '2022-03-31','2022-06-30','2022-09-30','2022-12-31']
for y in range(0,2):
    for i in range(0,4):
        id = i+4*y 
        h_price = random.randint(i*10+30,i*10+40)
        m_price = temp[i]
        s_fee = random.randint(1,3) + 0.5
        date_s = date[i+8*y]
        date_f = date[i+4 + 8*y]
        file.write(str(id)+';'+str(h_price)+';'+str(m_price)+';'
        +str(s_fee)+';'+date_s+';'+date_f+'\n')
file.close()

# generating rents with payment and user experiences 
# 
import random
random.seed(1001)
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
MM = ['01','02','03','04','05','06','07','08','09','10','11','12']
stat= ['canceled','completed']
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

rf = open('bulk/rentsT1.bulk','w')
pf = open('bulk/paymentsT1.bulk','w')
pf2 = open('bulk/invoicesT1.csv','w')
uxf = open('bulk/uxT1.bulk','w')

init_year = 2021
init_month = 1 
init_day = 1
rows = 0
cars_num = 350
customers_num = 500
caryear= [0]*cars_num
carday=[0]*cars_num
carmonth=[0]*cars_num
user_exp_num = 0
payment_num = 0
invoiceid = 0

while rows<1000000:
    # rents:
    # v status, v rentid, v start_date, v finish_date, v customerid, v carid
    # v initial_mileage, v final_mileage
    for i in range(0,cars_num):
        # get car's last rent date 
        if caryear[i]==0:
            caryear[i]=init_year
            carday[i] = init_month
            carmonth[i] = init_day
        # generate rent details for car 
        wait_time = random.randint(1,5)
        prob = random.random()
        if prob<0.05:
            duration = random.randint(5,15)
        elif prob<0.2:
            duration = random.randint(2,4)
        else:
            duration = 1
        if random.random()<0.02:
            status = 'canceled'
        else:
            status = 'completed'
        rentid = rows
        rows = rows+1
        # geting start day, month and year of rent by 
        # checking the waiting time of a car and it's 
        # last rent details 
        start_day = carday[i]+wait_time
        start_month = carmonth[i]
        start_year = caryear[i]
        if start_day>month_days[carmonth[i]-1]:
            start_day = start_day % month_days[carmonth[i]-1]
            start_month = carmonth[i]+1
            if start_month > 12:
                start_month = 1
                start_year = caryear[i]+1
        else: 
            start_month = carmonth[i]
            start_year = caryear[i]

        # same as start day for finish date in 
        finish_day = start_day + duration 
        if finish_day > month_days[start_month-1]:
            finish_day = finish_day % month_days[start_month-1]
            finish_month = start_month + 1
            finish_year = start_year
            if finish_month > 12:
                finish_month = 1
                finish_year = start_year + 1 
        else:
            finish_month = start_month
            finish_year = start_year

        customerid = random.randint(0,customers_num-1)
        final_mileage = random.randint(50,250)*duration 
        # payment 
        for y in range(duration):
            paymentid = payment_num
            payment_num += 1
            cost = (final_mileage/duration) * 1.5
            issue_year = start_year
            issue_month = start_month
            issue_day = start_day+y+1  
            if issue_day > month_days[issue_month-1]:
                issue_day=issue_day%month_days[issue_month-1]+1
                issue_month +=1
                if issue_month >12:
                    issue_month = 1
                    issue_year +=1
            delay = 0
            if random.random()<0.1:
                delay = random.randint(1,2)
            
            pay_year = issue_year
            pay_month = issue_month
            pay_day = issue_day + delay + 1
            if pay_day > month_days[pay_month-1]:
                pay_day=1%month_days[pay_month-1]+1
                pay_month +=1
                if pay_month >12:
                    pay_month = 1
                    pay_year +=1
            if issue_day < 10:
                issue_day = '0'+str(issue_day)
            if pay_day < 10:
                pay_day = '0'+str(pay_day)
            if issue_month < 10:
                issue_month = '0'+str(issue_month)
            if pay_month < 10:
                pay_month = '0'+str(pay_month)
            pf2.write(str(issue_year)+'-'+str(issue_month)+'-'+str(issue_day)+';'+str(pay_year)+'-'+str(pay_month)+'-'+str(pay_day)+';'+
            str(invoiceid)+';'+str(rentid)+';'+str(paymentid)+';'+str(customerid)+';'+str(cost)+';'+str(delay)+';'+str('0,23\n'))   
            invoiceid+=1
        # issue date;pay date;invoice id;rent id;payment id;customer id;cost;delay;tax
        #hours generation 
        start_hour = str(random.randint(0,23))+':'+str(random.randint(10,59))+':'+str(random.randint(10,59))
        finish_hour = str(random.randint(0,23))+':'+str(random.randint(10,59))+':'+str(random.randint(10,59))

        car_id = i

        initial_mileage = 0

        caryear[i]=finish_year
        carday[i] = finish_day
        carmonth[i] = finish_month

        if start_day >0 and start_day < 10:
            start_day = '0'+str(start_day)
        if start_month >0 and start_month < 10:
            start_month = '0'+str(start_month)
        if finish_day >0 and finish_day < 10:
            finish_day = '0'+str(finish_day)
        if finish_month >0 and finish_month < 10:
            finish_month = '0'+str(finish_month)
            
        # Rent loc moved from car 
        locdict = {'Gdansk':['Srodmiescie','Wrzeszcz'],'Krakow':['Kazimierz','Lagiewniki'],
                   'Warszawa':['Praga','Sadyba'],'Wroclaw':['Lesnica','Biskupin']}
        loccity = random.choice(list(locdict))
        locdistrict = random.choice(locdict[loccity])
        # v status, v rentid, v start_date, v finish_date, v customerid, v carid
        # v initial_mileage, v final_mileage
        if locdistrict=='Srodmiescie':
            locNo = 1
        elif locdistrict=='Wrzeszcz':
            locNo = 2
        elif locdistrict=='Kazimierz':
            locNo = 3
        elif locdistrict=='Lagiewniki':
            locNo = 4
        elif locdistrict=='Praga':
            locNo = 5
        elif locdistrict=='Sadyba':
            locNo = 6
        elif locdistrict=='Lesnica':
            locNo = 7
        else:
            locNo = 8
        rf.write(str(status)+';'+str(rentid)+';'+str(start_year)+'-'+str(start_month)+'-'+str(start_day)+
        ' '+str(start_hour)+';'+str(finish_year)+'-'+str(finish_month)+'-'+str(finish_day)+' '+str(finish_hour)+';'+
        str(customerid)+';'+str(car_id)+';'+str(initial_mileage)+';'+str(final_mileage)+';'+str(loccity)+';'+str(locdistrict)+';'+str(locNo)
        +';'+str((wait_time*24)-random.randint(0,10))+';'+str((duration*24)-random.randint(0,12))+';1\n')

        # payment 
        for y in range(duration):
            paymentid = payment_num
            cost = (final_mileage/duration) * 1.5
            pf.write(str(payments)+';'+str(rentid)+';'+str(cost)+'\n')       
            payments+=1 
            
        if status == 'completed':
            # generate user experience 
            if random.random() > 0.5:
                uxid = user_exp_num
                user_exp_num += 1
                content = random.choice(['Good service','Bad service','Its ok'])
                if content == 'Good service':
                    rating = random.randint(8,10)
                    type_of_ux = 'opinion'
                elif content == 'Its ok':
                    rating = random.randint(5,7)
                    type_of_ux = 'opinion'
                else:
                    rating = random.randint(1,4)
                    if rating == 4:
                        type_of_ux = 'collision'
                    else:
                        type_of_ux = 'complaint'

                cust_type = ''
                if random.random()<0.2:
                    cust_type = 'New'
                else:
                    cust_type = 'Regular'
                uxf.write(str(uxid)+';'+str(rentid)+';'+str(content)+';'+str(rating)+';'+str(type_of_ux)+';'+str(cust_type)+'\n')

import random
random.seed(1001)
month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
# generate repairs file 
year = 2021
day = 1
month = 1
invoice_num = 0
cars_num = 350
f = open('bulk/repairsT1.bulk','w')
while year<2059:
    wait = random.randint(14,20)
    day +=wait 
    if day > month_days[month-1]:
        day = day % month_days[month-1]+1
        month +=1 
        if month > 12:
            month = 1
            year+=1
    date = str(year)+'-'+str(month)+'-'+str(day)
    carid = random.randint(0,cars_num-1)
    name = 'waorkshop' + str(random.randint(1,10))
    price = random.randint(200,1000)
    tax = '23%'
    status = 'paid'
    type_of_repair = random.choice(['washing','fueling','lacquering','repair','clutch repair'])
    f.write(str(date)+';'+str(date)+';0;'+str(invoice_num)+';'+str(carid)+';'+str(name)+';'+str(price)+';'+str(tax)+';'+str(status)+';'+str(type_of_repair)+'\n')
    invoice_num+=1

import random 
random.seed(1001)
f = open('bulk/tasksT1.bulk','w')

for i in range(0,1000):
    taskid = i
    employeeid = random.randint(0,49)
    carid = random.randint(0,349)
    priority = random.randint(1,5)
    task_type = random.choice(['cleaning','fueling','repairing','relocating'])
    task_cost = random.randint(50,250)
    f.write(str(taskid)+';'+str(employeeid)+';'+str(carid)+';'+str(priority)+';'+str(task_type)+';'+str(task_cost)+'\n')




