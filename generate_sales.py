import pandas as pd
from datetime import datetime, timedelta
import random
from sqlalchemy import create_engine, text
from config import DB_URL

def generate_delhi_sales():
    categories = ['Beverages', 'Umbrellas', 'Ice Cream', 'Snacks']
    data = []
    
    for i in range(30):
        date = datetime.now().date() - timedelta(days=i)
        
        for category in categories:
            if category in ['Beverages', 'Ice Cream']:
                units = random.randint(80, 150)
            elif category == 'Umbrellas':
                units = random.randint(5, 30)
            else:
                units = random.randint(40, 90)
            
            prices = {'Beverages': 50, 'Umbrellas': 300, 'Ice Cream': 40, 'Snacks': 25}
            
            data.append({
                'sale_date': date,
                'product_category': category,
                'units_sold': units,
                'revenue': units * prices[category],
                'city': 'Delhi'
            })
    
    df = pd.DataFrame(data)
    df.to_csv('delhi_sales.csv', index=False)
    print(f"Made {len(df)} sales records")
    return df

def save_sales():
    df = pd.read_csv('delhi_sales.csv')
    engine = create_engine(DB_URL)
    
    with engine.connect() as conn:
        # Check if any sales exist for these dates
        check = text("SELECT COUNT(DISTINCT sale_date) FROM sales_raw")
        result = conn.execute(check)
        existing_dates = result.scalar()
        
        if existing_dates and existing_dates > 0:
            print(f"Sales data already exists ({existing_dates} dates). Skipping.")
            return
    
    df.to_sql('sales_raw', engine, if_exists='append', index=False)
    print(f"Saved {len(df)} sales records")

if __name__ == "__main__":
    generate_delhi_sales()
    save_sales()