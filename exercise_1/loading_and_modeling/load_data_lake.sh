#!/bin/bash

echo -n "YO DAWG!! are you logged in as w205? 'cause you need to be' [y/n]: "
read answer



if [[ "$answer" == "n" ]]; then
	echo "login as w205 - we're depending on you"
	return 1
fi




cd /data/w205
mkdir hospitals
chmod -R 777 hospitals
cd hospitals/

# get data
wget -O  hospitals.zip "https://data.medicare.gov/views/bg9k-emty/files/Nqcy71p9Ss2RSBWDmP77H1DQXcyacr2khotGbDHHW_s?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip"

# unzip raw data
mkdir raw_data
chmod -R 777 raw_data
mv hospitals.zip raw_data/
cd raw_data/
unzip hospitals.zip


# rename files and put a level up
cd ../
tail -n +2 raw_data/'Hospital General Information.csv' > hospitals.csv
tail -n +2 raw_data/'Timely and Effective Care - Hospital.csv' > effective_care.csv
tail -n +2 raw_data/'Timely and Effective Care - National.csv' > effective_care_national.csv
tail -n +2 raw_data/'Readmissions and Deaths - Hospital.csv' > readmissions.csv
tail -n +2 raw_data/'Readmissions and Deaths - National.csv' > readmissions_national.csv
tail -n +2 raw_data/'hvbp_hcahps_05_28_2015.csv' > survey_responses.csv
tail -n +2 raw_data/'hvbp_tps_05_28_2015.csv' > total_perf_scores.csv

echo 'files renamed'
ls -al

# make hadoop dirs

echo "making hadoop dirs... please be patient"

hdfs dfs -mkdir /user/w205/hospital_compare

hdfs dfs -mkdir /user/w205/hospital_compare/hospitals
hdfs dfs -put hospitals.csv /user/w205/hospital_compare/hospitals

hdfs dfs -mkdir /user/w205/hospital_compare/effective_care
hdfs dfs -put effective_care.csv /user/w205/hospital_compare/effective_care

hdfs dfs -mkdir /user/w205/hospital_compare/effective_care_national
hdfs dfs -put effective_care_national.csv /user/w205/hospital_compare/effective_care_national

hdfs dfs -mkdir /user/w205/hospital_compare/readmissions
hdfs dfs -put readmissions.csv /user/w205/hospital_compare/readmissions

hdfs dfs -mkdir /user/w205/hospital_compare/readmissions_national
hdfs dfs -put readmissions_national.csv /user/w205/hospital_compare/readmissions_national

hdfs dfs -mkdir /user/w205/hospital_compare/survey_responses
hdfs dfs -put survey_responses.csv /user/w205/hospital_compare/survey_responses

hdfs dfs -mkdir /user/w205/hospital_compare/total_perf_scores
hdfs dfs -put total_perf_scores.csv /user/w205/hospital_compare/total_perf_scores

echo "hadoop dirs made"
return 1