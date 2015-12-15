
##Exercise 1 Postmortem##

####This branch contains *absolute minimum* effort to run exercise 1 successfully. It is not intended to an improvement on existing code.###

Where it all went horribly wrong:   
1. No instructions provided to run code   
2. Results listed in the accompanying txt file were out of date   
3. Advice to self: SLOW THE F* DOWN.   


###How to run code:###

1. run as w205.
2. ignore all warnings.

```
cd ucb205/exercise_1/
. loading_and_modeling/load_data_lake.sh
```
go back to root exercise dir:
```
cd ucb205/exercise_1/

hive -f loading_and_modeling/hive_base_ddl.sql

hive -f transforming/transforms.sql
```
/data/spark15/bin/pyspark
```
execfile("/data/ucb205/exercise_1/investigations/run_me_first.py")
```
without leaving pyspark:
```
execfile("/data/ucb205/exercise_1/investigations/best_hospitals/hospitals.py")
execfile("/data/ucb205/exercise_1/investigations/best_states/states.py")
execfile("/data/ucb205/exercise_1/investigations/hospital_variability/variability.py")
execfile("/data/ucb205/exercise_1/investigations/hospitals_and_patients/correlations.py")
hospital_quality_correlation
hospital_variance_correlation

```


