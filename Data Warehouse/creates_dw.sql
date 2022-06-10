-- dimensions
create table payment_category(
	category_id int primary key,
	category varchar(20)
);

create table junk(
	junk_id int primary key,
	length_category varchar(10),
	review_category varchar(10),
	age_category varchar(20)
);

create table date(
	date_id int primary key,
	date date,
	year int,
	month varchar(10),
	season varchar(10)
);

create table rental_place(
	place_id int primary key,
	city varchar(20),
	district varchar(20),
	locationNo numeric
);

create table customer(
	customer_id int primary key,
	name_and_surname varchar(50),
	age_category varchar(20)
);

create table report(
	report_id int primary key,
	type varchar(20),
	client_category varchar(10)
);

create table employee(
	employee_id int primary key,
	name_and_surname varchar(50),
	age_category varchar(20),
	position varchar(20)
);

create table car(
	car_id int primary key,
	type_of_drive varchar(3),
	power_category varchar(19)
);

create table time(
	time_id int primary key,
	hour numeric,
	minute numeric
);
-- facts
create table rent(
	finish_date_id int foreign key references date,
	start_date_id int foreign key references date,
	car_id int foreign key references car,
	customer_id int foreign key references customer(customer_id),
	report_id int foreign key references report(report_id),
	place_id int foreign key references rental_place(place_id),
	start_time_id int foreign key references time(time_id),
	finish_time_id int foreign key references time(time_id),
	cost money,
	wait_hours int,
	rent_duration int,
	rentNo int
);

create table task(
	employee_id int foreign key references employee(employee_id),
	car_id int foreign key references car(car_id),
	cost money
);

create table payment(
	issue_date_id int foreign key references date(date_id),
	pay_date_id int foreign key references date(date_id),
	category_id int foreign key references payment_category(category_id),
	car_id int foreign key references car(car_id),
	
	value money,
	delay_days int
);

-- testing purposes 
--insert into rental_place(place_id,city,district,locationNo)values(1,'Gdansk','Suchanino',1); 
--select * from rental_place;
--drop table rental_place;