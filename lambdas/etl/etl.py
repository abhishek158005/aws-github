import sys
import logging
import pandas as pd


def lambda_handler(event, context):

    print('=============================')
    print(event)

    # bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
    # s3_file_name = event["Records"][0]["s3"]["object"]["key"]

    # print(bucket_name, s3_file_name)
    
    # df = pd.read_csv(f's3://{bucket_name}/{s3_file_name}', sep=',')
    # print (df.head())

    # DATA = pd.read_csv(f's3://{bucket_name}/{s3_file_name}', names = FIELDNAMES)
    # print(DATA)

    # conn, cursor = get_db_connection()

    # LOGGER.info('Creating tables in database if tables not exists!')
    # tables = table_script.db_create_tables(conn, cursor)

    # LOGGER.info('Creating and Fetching Data from DataFrames!')
    
    # products_df, customer_df, store_df = csv_to_df(DATA)

    # basket_df = load_basket.create_basket_df(conn, cursor, DATA)

    # LOGGER.info('Inserting Data into Database..')
    # load_basket.execute_values(conn, basket_df, 'basket_df')
    # load_db.execute_values(conn, customer_df, 'customer_df')
    # load_db.execute_values(conn, products_df, 'products_df')
    # load_db.execute_values(conn, store_df, 'store_df')

    context = {
        'status' : 200,
        'message' : 'Success',
    }
    return context


# handler('' , '')

