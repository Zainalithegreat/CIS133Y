import numpy as np
import pymssql
import pandas as pd
import matplotlib.pyplot as plt

connection = pymssql.connect(server='cisdbss.pcc.edu', user='275student', password='275student', database='NAMES')

sql_query = """
    SELECT Year, Gender, SUM(NameCount) AS TotalCount
    FROM all_data
    GROUP BY Year, Gender
    ORDER BY Year;
"""

df = pd.read_sql(sql_query, connection)

male_data = df[df['Gender'] == 'M']
female_data = df[df['Gender'] == 'F']

plt.plot(male_data['Year'], male_data['TotalCount'], label='Male')
plt.plot(female_data['Year'], female_data['TotalCount'], label='Female')

plt.xlabel("Year")
plt.ylabel("Total Name Count")
plt.title("Total Name Count by Year and Gender")
plt.legend()

plt.show()






