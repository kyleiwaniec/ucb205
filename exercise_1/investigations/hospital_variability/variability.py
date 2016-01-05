####################################################################################################################################
# Which procedures have the greatest variability between hospitals?
####################################################################################################################################

union_procedures.registerTempTable('union_procedures_tbl')

procedures_variance = sqlContext.sql("SELECT measure_name, measure_id, variance(zscore) AS variance FROM union_procedures_tbl GROUP BY measure_name, measure_id  ORDER BY variance DESC")
procedures_variance.show(10)

####################################################################################################################################
# Which hospitals have the greatest variability between procedures?
####################################################################################################################################

hospitals_variance = sqlContext.sql("SELECT provider_id, variance(zscore) AS variance FROM union_procedures_tbl GROUP BY provider_id  ORDER BY variance DESC")
hospitals_variance.show(10)