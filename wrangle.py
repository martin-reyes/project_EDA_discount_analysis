import pandas as pd




def acquire_store_data():

    filename = 'data/store_data_raw'
    
    # if file doesn't exist, acquire and cache
    if not os.path.isfile(filename):
    
        db = 'superstore_db'
        
        categories_query = "SELECT * FROM categories;"
        customers_query  = "SELECT * FROM customers;"
        orders_query     = "SELECT * FROM orders;"
        products_query   = "SELECT * FROM products;"
        regions_query    = "SELECT * FROM regions;"

        
        categories = pd.read_sql(categories_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        customers  = pd.read_sql(customers_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        orders     = pd.read_sql(orders_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        products   = pd.read_sql(products_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        regions    = pd.read_sql(regions_query, 
                                 f'mysql+pymysql://{env.user}:{env.pwd}@{env.host}/{db}')
        
        # join tables
        df = orders.merge(customers, on='Customer ID', how='left')
        df = df.merge(categories, on='Category ID', how='left')
        df = df.merge(regions, on='Region ID', how='left')
        df = df.merge(products, on='Product ID', how='left')
        df

        df.to_csv(filename, index=False)
        
        return df
    
    return pd.read_csv(filename)