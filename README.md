DOCKERHUB: https://hub.docker.com/u/bigdatateam/




Para las practicas de WEEK 3 usar: 

bigdatateam/yarn-notebook  .  https://hub.docker.com/r/bigdatateam/yarn-notebook/




WEEK 4 


I install pyspark with python,
after install I get this error:

asusn56@nautilus:~$ pyspark
Could not find valid SPARK_HOME while searching ['/home', '/usr/local/bin']
/usr/local/bin/pyspark: línea 24: /bin/load-spark-env.sh: No existe el archivo o el directorio
/usr/local/bin/pyspark: línea 77: /bin/spark-submit: No existe el archivo o el directorio

for solution use this command:


asusn56@nautilus:~$ PYSPARK_PYTHON=python3 SPARK_HOME=/usr/local/lib/python3.6/dist-packages/pyspark pyspark

where

SPARK_HOME is the location where you have install pyspark. For get this path, you typing:

pip show pypspark  and read te info about the path

after that use this path in the command line. :)

Other solution is you set enviroment variable SPARK_HOME permanent en your system .. 


WEEK 5 -

TLC Trip Record Data
FULL DATASET: https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page

WEEK 6

TELCO dataset: https://dandelion.eu/datagems/SpazioDati/telecom-sms-call-internet-mi/description/


