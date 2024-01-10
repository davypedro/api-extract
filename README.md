# api-extract
This is an extremely basic example of how we can extract data from a public API and transform it into a Pandas DataFrame

## 1. Data Source

### https://api.apilayer.com/exchangerates_data/latest?base=BRL&apikey=3plTCLRkOn3b3kA5WboEeaPN7qIrx9zW

## 2. Result

![image](https://github.com/davypedro/api-extract/assets/88987986/459ec2ba-d89b-4d52-a5b5-a85c3d1abdcb)

### These are the first 5 rows of the DataFrame. From this, we can build analyzes and bring insights.

## 3. Next steps

### An interesting approach would be to use Apache Airflow in conjunction with the AWS storage service to extract this data every day and create a queryable table. After that, make the best insights available on a dashboard.

### From this, we know how powerful Data Engineering can be.
