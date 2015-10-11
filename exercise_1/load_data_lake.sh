mkdir hospitals
cd hospitals/

# get data
wget -O hosptals.zip https://data.medicare.gov/views/bg9k-emty/files/Nqcy71p9Ss2RSBWDmP77H1DQXcyacr2khotGbDHHW_s?content_type=application%2Fzip%3B%20charset%3Dbinary&filename=Hospital_Revised_Flatfiles.zip


# unzip raw data
mkdir raw_data
chmod -R 777 raw_data
mv hosptals.zip raw_data/
(cd raw_data/; unzip hosptals.zip)


# rename files and put a level up
tail -n +2 raw_data/'Hospital General Information.csv' > hospitals.csv
tail -n +2 raw_data/'Timely and Effective Care - Hospital.csv' > effective_care.csv
tail -n +2 raw_data/'Readmissions and Deaths - Hospital.csv' > readmissions.csv
tail -n +2 raw_data/'hvbp_hcahps_05_28_2015.csv' > survey_responses.csv

echo 'files renamed'
ls

# make hadoop dirs
echo "making hadoop dirs"
hdfs dfs -mkdir /user/w205/hospital_compare

hdfs dfs -mkdir /user/w205/hospital_compare/hospitals
hdfs dfs -put hospitals.csv /user/w205/hospital_compare/hospitals

hdfs dfs -mkdir /user/w205/hospital_compare/effective_care
hdfs dfs -put effective_care.csv /user/w205/hospital_compare/effective_care

hdfs dfs -mkdir /user/w205/hospital_compare/readmissions
hdfs dfs -put readmissions.csv /user/w205/hospital_compare/readmissions

hdfs dfs -mkdir /user/w205/hospital_compare/survey_responses
hdfs dfs -put survey_responses.csv /user/w205/hospital_compare/survey_responses

echo "hadoop dirs made"
return 1