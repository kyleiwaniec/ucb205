#execfile('/data/w205/ucb205/exercise_1/investigations/run_me_first.py')

from pyspark.sql.functions import UserDefinedFunction
from pyspark.sql.types import *
from pyspark.sql import functions as F
from pyspark.sql.window import Window

####################################################################################################################################
# Data and shenanigans
####################################################################################################################################

effective_pos = sqlContext.sql("SELECT * FROM  effective_clean_pos")
effective_neg = sqlContext.sql("SELECT * FROM  effective_clean_neg")
effective_national = sqlContext.sql("SELECT * FROM  effective_clean_national")
readmissions = sqlContext.sql("SELECT * FROM  readmissions_clean")
readmissions_national = sqlContext.sql("SELECT * FROM  readmissions_clean_national")
hospitals = sqlContext.sql("SELECT * FROM hospitals_clean")
surveys = sqlContext.sql("SELECT * FROM survey_responses_clean")

# readmissions.select("measure_id").distinct().count() # 14
# readmissions_national.select("measure_id").distinct().count() #14

readmissions_stddev = sqlContext.sql("SELECT measure_id, stddev(score) AS stddev FROM readmissions_clean GROUP BY measure_id")
effective_pos_stddev = sqlContext.sql("SELECT measure_id, stddev(score) AS stddev FROM effective_clean_pos GROUP BY measure_id")
effective_neg_stddev = sqlContext.sql("SELECT measure_id, stddev(score) AS stddev FROM effective_clean_neg GROUP BY measure_id")


readmissions_national_w_std = readmissions_national.join(readmissions_stddev, readmissions_national.measure_id == readmissions_stddev.measure_id, "inner").select(readmissions_national.measure_id, readmissions_national.measure_name, readmissions_national.national_rate, readmissions_stddev.stddev)
readmissions_national_w_std.registerTempTable('readmissions_national_w_std_tbl')

# scores get flipped becuase bigger is worse.
readmissions_normalized = sqlContext.sql("SELECT rc.measure_id, rc.measure_name, rc.provider_id, rc.state, rc.score, r.national_rate, r.stddev, (-(rc.score-r.national_rate)/r.stddev) as zscore FROM readmissions_clean rc INNER JOIN readmissions_national_w_std_tbl r ON r.measure_id = rc.measure_id GROUP BY rc.measure_id, rc.measure_name, rc.provider_id, rc.state, rc.score, r.national_rate, r.stddev  ORDER BY zscore DESC")

effective_pos_national_w_std = effective_national.join(effective_pos_stddev, effective_national.measure_id == effective_pos_stddev.measure_id, "inner").select(effective_national.measure_id, effective_national.measure_name, effective_national.national_rate, effective_pos_stddev.stddev)
effective_pos_national_w_std.registerTempTable('effective_pos_national_w_std_tbl')
effective_pos_normalized = sqlContext.sql("SELECT rc.measure_id, r.measure_name, rc.provider_id, rc.state, rc.score, r.national_rate, r.stddev, (rc.score-r.national_rate)/r.stddev as zscore FROM effective_clean rc INNER JOIN effective_pos_national_w_std_tbl r ON r.measure_id = rc.measure_id GROUP BY rc.measure_id, r.measure_name, rc.provider_id, rc.state, rc.score, r.national_rate, r.stddev  ORDER BY zscore DESC")

effective_neg_national_w_std = effective_national.join(effective_neg_stddev, effective_national.measure_id == effective_neg_stddev.measure_id, "inner").select(effective_national.measure_id, effective_national.measure_name, effective_national.national_rate, effective_neg_stddev.stddev)
effective_neg_national_w_std.registerTempTable('effective_neg_national_w_std_tbl')
# lower is better
effective_neg_normalized = sqlContext.sql("SELECT rc.measure_id, r.measure_name, rc.provider_id, rc.state, rc.score, r.national_rate, r.stddev, -(rc.score-r.national_rate)/r.stddev as zscore FROM effective_clean rc INNER JOIN effective_neg_national_w_std_tbl r ON r.measure_id = rc.measure_id GROUP BY rc.measure_id, r.measure_name, rc.provider_id, rc.state, rc.score, r.national_rate, r.stddev  ORDER BY zscore DESC")

union_effective = effective_pos_normalized.unionAll(effective_neg_normalized)

# now we have a level palying field
union_procedures = union_effective.unionAll(readmissions_normalized)



