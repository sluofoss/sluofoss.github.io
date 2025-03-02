---
title: DAX vs MDX
created: 2025-03-02
updated: 2025-03-02T21:42
---

# Tldr:
	Mdx not required,
	We are not dealing with cube (MOLAP) in Power BI

# Investigate
	1. is power bi semantic model stored tabular or a cube? 
		a. TABULAR 
	2. in AnalysisService.Database AnalysisServices.Database - PowerQuery M | Microsoft Learn, it says that the query should be MDX, but obviously we're using DAX instead and it works. 
		a. DAX for multidimensional models in SQL Server Analysis Services | Microsoft Learn
		b. Because semantic model is tabular, this is a rabbit hole not worth diving to.
	3. MDX is suppose to be for cube data but it also works on tabular? 
		a. DAX vs MDX — Is there any difference? | by Muhammad Asif | Medium
	4. does whether it been tabular or cube affect how we can most efficiently query the semantic model in SSAS?
		a. DAX for multidimensional models in SQL Server Analysis Services | Microsoft Learn
		b. Not necessary.


Cube rant about business 
https://www.reddit.com/r/dataengineering/comments/172x3p9/comment/k40mg8j/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

Some believe cube to be moot because hadoop removed performance bottle neck
https://www.reddit.com/r/dataengineering/comments/172x3p9/comment/k3zaaqz/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button