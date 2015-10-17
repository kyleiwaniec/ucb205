from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import *
from pyspark.sql import functions as F
#from pyspark import SparkContext, HiveContext
#sc = SparkContext()
#sqlContext = HiveContext(sc)

####################################################################################################################################
# Data and shenanigans
####################################################################################################################################

ec = sqlContext.sql("SELECT * FROM  effective_clean")
rc = sqlContext.sql("SELECT * FROM  readmissions_clean")
hospitals = sqlContext.sql("SELECT * FROM hospitals_clean")
surveys = sqlContext.sql("SELECT * FROM survey_responses_clean")


ec_max = ec.agg(F.max("score").alias("max_score")).first()
name = 'score'
udf = UserDefinedFunction(lambda x: x/ec_max.max_score, StringType())
normalized_ec = ec.select(*[udf(column).alias(name) if column == name else column for column in ec.columns])

rc_max = rc.agg(F.max("score").alias("max_score")).first()
name = 'score'
udf = UserDefinedFunction(lambda x: 1-(x/rc_max.max_score), StringType())
normalized_rc = rc.select(*[udf(column).alias(name) if column == name else column for column in rc.columns])
normalized_rc.show(10)

union_procedures = normalized_ec.unionAll(normalized_rc)
union_procedures_avg = union_procedures.groupBy("provider_id").agg(F.avg("score").alias("avg_score"))
joined_procedures = union_procedures_avg.join(hospitals, hospitals.provider_id == union_procedures_avg.provider_id, "inner").orderBy(union_procedures_avg.avg_score.desc())
union_procedures_avg_byState = union_procedures.groupBy("state").agg(F.avg("score").alias("avg_score"))
joined_procedures_byState = union_procedures_avg_byState.orderBy(union_procedures_avg_byState.avg_score.desc())

####################################################################################################################################
# What hospitals are models of high-quality care? What states are models of high-quality care?
####################################################################################################################################

# top 10 hospitals
hospitals_avg_scores = sqlContext.sql("SELECT provider_number, AVG(tot_score) AS aveScore FROM total_perf_scores_clean GROUP BY provider_number  ORDER BY aveScore DESC")
top_ten_hospitals_list = hospitals_avg_scores.join(hospitals, hospitals.provider_id == hospitals_avg_scores.provider_number, "inner").orderBy(hospitals_avg_scores.aveScore.desc())
top_ten_hospitals_list.show(10)


# top 10 states
states_avg_scores = sqlContext.sql("SELECT state, AVG(tot_score) AS aveScore FROM total_perf_scores_clean GROUP BY state  ORDER BY aveScore DESC")
states_avg_scores.show(10)

####################################################################################################################################
# Which procedures have the greatest variability between hospitals?
####################################################################################################################################

union_procedures.registerTempTable('union_procedures_tbl')
union_procedures_tbl = sqlContext.sql("SELECT * FROM union_procedures_tbl")

union_procedures_tbl_variance = sqlContext.sql("SELECT measure_name, measure_id, variance(score) AS variance FROM union_procedures_tbl GROUP BY measure_name, measure_id  ORDER BY variance DESC")
union_procedures_tbl_variance.show(10)

####################################################################################################################################
# Are average scores for hospital quality or procedural variability correlated with patient survey responses?
####################################################################################################################################

joined_scores = hospitals_avg_scores.join(surveys, surveys.provider_number == hospitals_avg_scores.provider_number, "inner")
joined_scores.stat.corr('aveScore', 'survey_score')





