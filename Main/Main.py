import pandas as pd
import matplotlib
import numpy

df = pd.read_csv(
    r'C:\Users\tomas\New folder\Data Preprocessing\globalmart_dirty_orders_2000.csv', 
    keep_default_na=False,
    na_values=['-', '#N/A', 'N/A', 'NULL', '?', 'unknown', 'NONE', 'na', ''], # catch all null values before parsing
    index_col= 'record_id'
)   

columns = [
    'source_system', 'customer_id', 'customer_name', 
    'customer_email', 'phone_raw', 'age_raw', 'gender_raw', 
    'signup_date_raw', 'order_id', 'order_date_raw', 'ship_date_raw', 
    'delivery_date_raw', 'customer_timezone', 'country_raw', 'city_raw', 
    'postal_code_raw', 'product_category_raw', 'product_name_raw', 
    'sku_raw', 'quantity_raw', 'unit_price_raw', 'currency_raw', 
    'discount_raw', 'shipping_cost_raw', 'item_weight_raw', 
    'payment_method_raw', 'order_status_raw', 'returned_flag_raw', 
    'return_reason_raw', 'satisfaction_score_raw', 'loyalty_points_raw', 
    'site_visits_last30_raw', 'support_tickets_90d_raw', 
    'distance_to_warehouse_km_raw', 'campaign_source_raw', 
    'customer_segment_raw', 'support_ticket_date_raw', 
    'complaint_text_raw', 'ingestion_batch', 'data_source_note'
]

def returnRows(df):
    return f"Total row count: {len(df)}"

def returnDatatype(df):
    return df.dtypes

def checkMissingValues(df, columns):
    null_rows = df[columns].isnull().sum()
    missing_values = null_rows[null_rows > 0]
    total_rows = len(df)
    
    percentages = (missing_values / total_rows) * 100
    print("--------------------Missing Rows--------------------")
    summary_df = pd.DataFrame({
        'Missing Count': missing_values,
        'Percentage (%)': percentages.round(2)  
    })

    return summary_df

## specifies which columns and row has null values
def specifyWhere(df, columns):
    missing_locations = {}
    for col in columns:
        null_indeces = df[df[col].isnull()].index.tolist()

        if null_indeces:
            missing_locations[col] = null_indeces

    return missing_locations

def checkSpecificColumnDuplicates(df, column_name):
    duplicate_mask = df.duplicated(subset=[f"{column_name}"])
    duplicate = duplicate_mask[duplicate_mask > 0]
    
    duplicate_list = pd.DataFrame({
        'record_id': duplicate,
   })

    return duplicate_list

## all commands functions run here are pre-normalization
checkSpecificColumnDuplicates(df, 'order_id')
   
