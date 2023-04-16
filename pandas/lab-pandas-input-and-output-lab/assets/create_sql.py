import sqlite3
conn = sqlite3.connect('sales_data.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE sales (
    product VARCHAR(50),
    region VARCHAR(50),
    sales INT,
    revenue INT
);
          ''')

c.execute('''
          INSERT INTO sales VALUES
    ('Product A', 'Region 1', 10, 100),
    ('Product A', 'Region 2', 20, 200),
    ('Product A', 'Region 3', 30, 300),
    ('Product B', 'Region 1', 40, 400),
    ('Product B', 'Region 2', 50, 500),
    ('Product B', 'Region 3', 60, 600),
    ('Product C', 'Region 1', 70, 700),
    ('Product C', 'Region 2', 80, 800),
    ('Product C', 'Region 3', 90, 900);
          ''')

conn.commit()
