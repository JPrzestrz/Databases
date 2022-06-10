-- Task III from DATABASES 

-- Tasks to complete: 
-- their number: from 7 to 10,
-- at least 1 query using a view = 1/1
---at least 2 queries using joins = 2/2
-- at least 2 queries with subqueries = 2/2
-- at least 2 queries using aggregate functions 2/2
-- at least 2 queries using grouping = 2/2
-- at least 1 query with ordering 1/1 <v> 

-- 1 select car's name and engine volume and it's sum of cost of all the repairs 
-- it had in warehouse grouped by name and ordered by sum of costs <comp>
-- grouping, aggregate, ordering
select car.model_name, car_variant.engine_volume, sum(repair.cost) as "Sum of costs"
   from car,car_variant, customer, service, repair
   where (car.variant_id=car_variant.variant_id 
      and car.customer_id = customer.person_id 
	  and customer.person_id = service.customer_id
	  and service.service_id = repair.service_id
	  and car_variant.engine_volume > 1400)
   group by car.model_name,car_variant.engine_volume
   order by "Sum of costs";

-- 2 select name of clients along with number of their visits in workshop and sum 
-- and average cost of visits <?>
-- group by, aggregate func 
select customer.name, customer.times_in_workshop, sum(repair.cost) as "Sum of costs",  sum(repair.cost)/customer.times_in_workshop as "Average cost"
   from customer, car, service, repair
   where customer.person_id = car.customer_id
      and service.customer_id = customer.person_id
	  and service.service_id = repair.service_id
   group by customer.name,customer.times_in_workshop;

-- 3 select cars that their production year is higher than average production year along with
-- their owners and order them by their engine volume <comp>
-- order, aggregate, subquerry, 
select c.model_name, c.color, cm.production_year, cv.engine_volume, cr.name as "owner name"
   from car_model as cm, car as c, car_variant as cv, customer as cr
   where c.variant_id=cv.variant_id 
      and cv.model_id=cm.model_id 
	  and c.customer_id = cr.person_id
	  and cm.production_year > 
	     (
	        select avg(production_year)
		       from car_model
		 )
	order by cv.engine_volume desc;

-- 4 select parts name and it's total cost along with difference of total cost and 
-- average cost of all the repairs. 
-- aggr, subquerry, ord, grp
select pc.part_name,sum(pis.cost) as "total_cost", sum(pis.cost) - (
         select avg(cost)
	        from repair
	  ) as "difference_from_avg"
   from parts_in_stock as pis, parts_catalog as pc, parts_used as pu, repair as r
   where pis.part_id = pc.part_id
      and pis.id = pu.id
	  and pu.repair_id = r.repair_id
   group by pc.part_name
   order by "total_cost" desc

-- 5 select all the female customers and their cars 
-- and number of times they had any service in our workshop 
-- aggr, joins, group by 
select c.name, p.email, car.model_name, count(s.type_of_service) as "times_serviced"
   from customer as c
      left join car
	     on car.customer_id = c.person_id
	  left join people as p
	     on p.person_id = c.person_id
	  left join service as s
	     on s.vin = car.vin
   where p.gender=1
   group by c.name, p.gender, p.email, car.model_name;

-- 6 select 3 mechanics that had the most repairs and then the most expensive part used
-- write their names and pesel and number of their repairs and maximum total cost of part used in repair
select top 3 m.name as mechanic_name, p.pesel, count(r.service_id) as times_repairing, max(pu.total_cost) as most_expensive_part
   from mechanic as m
      left join people as p
	     on p.person_id = m.person_id
      left join repair as r 
	     on r.employee_id = m.person_id
	  left join parts_used as pu
	     on pu.repair_id = r.repair_id
   group by m.name, p.pesel
   order by times_repairing desc, most_expensive_part desc;

-- 7 select and group drive types and transmissions of cars with their 
-- average cost of parts, number of parts to this car that workshop 
-- has in the stock and total value of parts to this car that has avg cost 
-- of parts higher than the avg cost of parts in the stock
select cv.drive_type, cv.transmission, avg(pis.cost) as average_cost, sum(pis.quantity_currently) as parts_number, avg(pis.cost)*sum(pis.quantity_currently) as value_of_parts
   from car_variant as cv, in_catalog as ic, parts_catalog as pc, car_model as cm, parts_in_stock as pis
      where cv.variant_id = ic.car_variant_id 
	     and ic.parts_catalog_id = pc.part_id
		 and cm.model_id = cv.model_id
		 and pis.part_id = pc.part_id
   group by cv.drive_type,cv.transmission
   having avg(pis.cost) >
   (
      select sum(cost)/sum(quantity_currently)
	     from parts_in_stock
		 where quantity_initially = quantity_currently
   )
   order by value_of_parts desc;

-- 8 CREATE VIEW : 
-- create view of all the customers and their cars and their total money spent 
create view [all customers] as
select c.name, p.pesel, car.model_name, car.vin, count(s.vin) as times_serviced, sum(r.cost) as money_spent
   from customer as c
      left join car
	     on car.customer_id = c.person_id
      left join people as p
	     on p.person_id = c.person_id
	  left join service as s
	     on s.vin = car.vin
      left join repair as r
	     on r.service_id = s.service_id
   group by c.name, p.pesel, car.model_name, car.vin;

select * from [all customers];