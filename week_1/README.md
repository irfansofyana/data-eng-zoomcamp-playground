# README

In the first week, we learn about terraform and docker (especially docker for postgres and python).

## Notes

For detail and comprehensive notes, see [here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_1_basics_n_setup)

## Homework

There are two sections in this homework.

### Setup Terraform and GCP
I personally follow a good notes about setup terraform and GCP from this [note](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/1_intro.md).

I rewrite the terraform files and you can see in [dtc-de folder]("https://github.com/irfansofyana/data-eng-zoomcamp-playground/tree/main/dtc-de").

I got billing problem when setup the terraform. I received `Error updating Dataset "projects/dtc-de-339114/datasets/trips_data_all": googleapi: Error 403: Billing has not been enabled for this project. Enable billing at https://console.cloud.google.com/billing. The default table expiration time must be less than 60 days, billingNotEnabled`

To solve this problem, I tried to "restart" the billing for this project by disabled the billing and enabled it again a few moments later. I also tried to run `terraform destroy` and run the terraform files again and it worked! 

### Data Analysis on NY Taxi Data using Postgres

In this homework, we need to answer some questions. To solve the questions, basically we need to do:

0. Setup the infrastructure locally
    Provision postgreSQL server with pgadmin. We can use the docker-compose file and spin up the dockerfile by running `docker-compose` up command. After spin up the postgreSQL and pgadmin, I also run a web server locally so that my docker container can download the dataset faster. Read details in the next step.

1. Ingest NY Taxi Data

    Download the dataset: `wget https://s3.amazonaws.com/nyc-tlc/trip+data/yellow_tripdata_2021-01.csv`. To ingest data into PostgreSQL, you can use the Dockerfile. 
    
    - First: build the docker image by running command `docker build -t taxi_ingest:v001 .`
    - Run & ingest data: using following command:
    ```
        docker run -it \
        --network=2_docker_sql_default\
        taxi_ingest:v001 \
        --user=root \
        --password=root \
        --host=pgdatabase \
        --port=5432 \
        --db=ny_taxi \
        --table_name=yellow_taxi_trips \
        --url="http://172.30.67.236:8000/yellow_tripdata_2021-01.csv" 
    ```
    
    please note that `network` name is obtained from the network name of our docker-compose. This is required so that our ingestion script can talk to our postgreSQL database.

    the `user`, `password`, `host`, `port`, `db`, and `table_name` used here can be obtained from the docker-compose file in the previous step.

    meanwhile the `url` is obtained from my http server that I created in the previous step so that the ingestion script can download from there and it will be faster than downloading the data from S3.

2. Ingest dataset about zones

    Download the dataset: `wget https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv`

    To ingest dataset about zones, I created a new table called `taxi_zone` and insert all the data from the dataset into postgreSQL using PgAdmin. See the SQL script in [taxi_zone.sql file](https://github.com/irfansofyana/data-eng-zoomcamp-playground/tree/main/week_1/taxi_zone.sql)

    After we have the `taxi_zone` table and the `yellow_taxi_trips` table, we can find the answer of Homework question using PgAdmin query tool. The SQL query to find the answer will be inserted into this README after passing the deadline.

    **Update**: My HW solution can be seen [here](https://github.com/irfansofyana/data-eng-zoomcamp-playground/tree/main/week_1/homework/my_solution.txt)
