from pyspark import SparkContext, HiveContext
sc = SparkContext()
sqlCtx = HiveContext(sc)

df = sqlCtx.sql("SELECT provider_id, hospital_name, state FROM hospitals")
sc.parallelize(df).saveAsTextFile("/user/w205/hospital_transformed/hospitals/hospitals.txt")
