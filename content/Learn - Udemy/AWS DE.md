---
created: 2024-09-30T21:35
updated: 2024-09-30T21:52
---

select *
from titanic
limit 10;

select avg(Survived)
from titanic;

select avg(case when (Sex = 'female') or (Age <= 12) then Survived end ) as women_children_rate
from titanic;

select avg(case when (Sex != 'female') and (Age > 12) then Survived end ) as others_rate
from titanic;
