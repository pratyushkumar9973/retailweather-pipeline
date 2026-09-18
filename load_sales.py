import pandas as pd
from sqlalchemy import create_engine
from config import DATABASE_URL

def load_sales_csv():
    
    try:
        print("Reading sales CSV...")
        df = pd.read_csv('delhi_sales.csv')
        
        print(f"Found {len(df)} sales records")
        
        
        engine = create_engine(DATABASE_URL)
        
        df.to_sql('sales_raw', engine, if_exists='append', index=False)
        
        print(f"Loaded {len(df)} sales records to database")
        return True
        
    except Exception as e:
        print(f"Error loading sales: {e}")
        return False
        


if __name__ == "__main__":
    load_sales_csv()
