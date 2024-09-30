---
created: 2024-09-30T21:35
updated: 2024-09-30T21:53
---

Few things about building pipelines for ml purposes. 

1. look into mlflow for orchestration
2. need to look into how to reuse custom artifact like dynamic data definition files during the mlflow call. 
3. imblearn' `pipeline` right now seems most compatible with sklearn and feature engine.
4. joblib can be use to to distribute sklearn's module execution on frameworks like dask, ray, pyspark. (hence one need to check whether imblearn pipeline supports it)
5. take advantage of sklearn feature union and column transformer to parallelize different feature extractor and encoder. 