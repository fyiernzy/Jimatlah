from sqlalchemy import create_engine, text
import pandas as pd

if __name__ == "__main__":
    engine = create_engine("sqlite:///mydevices.db")
    df = pd.read_csv('fake_data.csv')
    print(df)
    df.to_sql('Device', con=engine, if_exists='replace', index=False)
    with engine.connect() as conn:
        print(conn.execute(text("SELECT * FROM Device WHERE timestamp = 0")).fetchall())


    