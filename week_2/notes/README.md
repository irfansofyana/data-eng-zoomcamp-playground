# Week 2 - Notes

## Data Lake

- [video souce](https://www.youtube.com/watch?v=W3Zm6rjOq70&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=16)

- [slide](https://docs.google.com/presentation/d/1RkH-YhBz2apIjYZAxUz2Uks4Pt51-fVWVN9CcH9ckyY/edit?usp=sharing)

### Wbat is Data lake?

Data lake is a central repository that allows us to store all structured and unstructured data at any scales. 

The main goal behind a Data Lake is being able to ingest data as quickly as possible and making it available to the other team members.

A Data Lake should be:
- Secure
- Scalable
- Able to run on inexpensive hardware

### Data Lake vs Data Warehouse

- Data:
    - Data Lake: Raw (contains structured, semi-structured, structured data with minimal processing)
    - Data Warehouse: Refined (Highly structured data that is cleaned, pre-processed, and refined)
- Size:
    - Data Lake: Large (petabytes since the data can be in any forms of size)
    - Data Warehouse: Smaller (since the data has been processed and cleaned, the size should be smaller)
- Use cases:
    - Data Lake: wide variety (machine learning, streaming analytics, AI)
    - Data Warehouse: Relational (BI reporting)

### ETL vs ELT
- Extract Transform and Load vs Extract Load and Transform
- ETL is mainly used for a small amount of data whereas ELT is used for large amounts of data
- ELT provides data lake support (Schema on read)

### Gotcha of Data Lake
Data Lakes are only useful if data can be easily processed from it. Techniques such as versioning and metadata are very helpful in helping manage a Data Lake. A Data Lake risks degenerating into a **Data Swamp** if no such measures are taken, which can lead to:

- No versioning of the data
- Incompatible schemas for same data
- No metadata associated
- Joins between the data is not possible

### Example cloud provider
- GCP - Cloud Storage
- AWS - S3
- Azure - Azure Blob

## Apache Airflow
TBA

### Provision Apache Airflow with Docker
TBA

### Creating DAG
TBA

## Homework
TBA