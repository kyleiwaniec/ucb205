#!/bin/bash


hdfs dfs -mkdir /user/w205/hospital_transformed

hdfs dfs -mkdir /user/w205/hospital_transformed/hospitals
hdfs dfs -put hospitals.csv /user/w205/hospital_transformed/hospitals

hdfs dfs -mkdir /user/w205/hospital_transformed/effective_care
hdfs dfs -put effective_care.csv /user/w205/hospital_transformed/effective_care

hdfs dfs -mkdir /user/w205/hospital_transformed/readmissions
hdfs dfs -put readmissions.csv /user/w205/hospital_transformed/readmissions

hdfs dfs -mkdir /user/w205/hospital_transformed/survey_responses
hdfs dfs -put survey_responses.csv /user/w205/hospital_transformed/survey_responses

echo "hadoop dirs made"
return 1