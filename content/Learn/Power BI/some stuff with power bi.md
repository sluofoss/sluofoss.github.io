---
created: 2024-10-03T20:59
updated: 2024-10-17T00:53
tags:
  - analytics
---
# pbip
it is possible to create custom DAX and power query import tables by editing the text file model.bim

however it doesnt work for power query direct query mode for teradata for some reason.

# bypass the 1 million row limit from power bi premium

1. import mode/ splitting direct query table using rank filte 
2. use 
	1. var c1 = calculate(table, relatedtable(hugetable))
	2. var c2 = calculate(table, relatedtable(hugetable))
	3. var c3 = calculate(table, relatedtable(hugetable))
	4. return union(c1, c2, c3)

you can query cube (ssas) using dax nested within  m query, in m query you can have loop, thus it should be able to get around that. but have been hitting alot of server side error.