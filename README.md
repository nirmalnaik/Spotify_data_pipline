# Spotify ETL Pipeline

## Project Overview
This repository contains the code and documentation for an ETL pipeline that extracts data from the Spotify API, transforms it, and loads it into AWS services for storage and analysis. The pipeline utilizes AWS Lambda, S3, Glue, and Athena to handle data efficiently and scalably.

The pipeline is structured as follows:
- **Extract**: Data is pulled from the Spotify API using AWS Lambda functions.
- **Transform**: Data is transformed into a structured format suitable for analysis.
- **Load**: The transformed data is loaded into AWS Glue and made queryable via Amazon Athena.

## Prerequisites
- AWS Account
- Access to Spotify API
- Python 3.8 or later
- AWS CLI configured

## Setup
### AWS Resources
1. **Lambda Functions**: Create Lambda functions for data extraction and transformation.
   - `AWS_extract_lambda.py`: Manages the extraction of data from Spotify.
   - `AWS_transform_lambda.py`: Handles data transformation.
2. **S3 Bucket**: Store raw, transformed, and processed data.
3. **AWS Glue**: Setup Glue Crawlers to organize data schema.
4. **Amazon Athena**: Prepare Athena for running SQL queries on the processed data.

### Environment Setup
Ensure your local environment is set up with the AWS CLI and configured correctly to interact with the AWS resources.

## Deployment
Deploy the Lambda functions using the AWS Management Console or AWS CLI. Set up triggers in Amazon CloudWatch to automate the extraction process based on your preferred schedule.


