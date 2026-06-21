import psycopg2
import pandas as pd 
import numpy as np
from sqlalchemy import create_engine, URL, text


conn = psycopg2.connect(
        host="localhost",      
        database="ipldatabase",
        user="postgres",
        password="vk@123456#",
        port="5432"
    )

db_url = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="vk@123456#",
    host="localhost",
    port=5432,
    database="ipldatabase",
)
engine = create_engine(db_url)

print("Database connected successfully!")

cursor = conn.cursor()

cursor.execute("SELECT version();")
data = cursor.fetchone()

print("PostgreSQL version:")
print(data)

# tables = pd.read_sql_query("""
# SELECT table_name
# FROM information_schema.tables
# WHERE table_schema='public'
# """, engine)

# print(tables)

df = pd.read_sql_query("SELECT * FROM matches ", engine)
# rename id to match_id right after loading so subsequent code uses the new name
df.rename(columns={'id': 'match_id'}, inplace=True)
# print(df.T)
# print(df.info())
# # print(df.describe())
# # print(pd.read_sql_query("select season, count(*) from matches group by season", engine ))
# print(df)
# # print(pd.read_sql_query("select result from matches", engine))
# print(df.isnull().sum())
# # # print(pd.read_sql_query("alter table matches drop column method",engine))
# # cur = conn.cursor()
# # cur.execute("""
# #     ALTER TABLE matches
# #     DROP COLUMN method;
# # """)
# # conn.commit()
# # print("Column dropped successfully!")
# # cur.close()
# # conn.close()
# print(df['id'].value_counts())
# print(df['result_margin'].value_counts())
# print(df['target_runs'].value_counts())

for col in df.columns:
    if df[col].nunique():
        print(df[col].value_counts())

print(df['season'].unique())        

# function to convert the season column inconsistency in data type 
df['season'] = df['season'].replace('2007/08', '2008')
df['season'] = df['season'].replace('2009/10', '2010')
df['season'] = df['season'].replace('2020/21', '2020')  
print(df['season'].unique())

# changing data type from object to datetime
df["date"] = df["date"].astype("datetime64[ns]")
df["target_overs"]= df["target_overs"].astype("float64")

# print(df['city'].unique())

# handling missing values in city and winner columns by dropping 
# the rows and for result_margin, target_runs and target_overs 
# by filling the missing values with mean of the respective columns

df = df.dropna(subset = ['city'])
df = df.dropna(subset = ['winner'])
df['result_margin'] = df['result_margin'].fillna(df['result_margin'].mean())
df['target_runs'] = df['target_runs'].fillna(df['target_runs'].mean())
df['target_overs'] = df['target_overs'].fillna(df['target_overs'].mean())
print(df.isnull().sum())

# changind the name of the teams 
# which are present multiple times with diffrent names 
# in team 1 and team2
df['team1'] = df['team1'].replace('Delhi Daredevils', 'Delhi Capitals')
df['team2'] = df['team2'].replace('Delhi Daredevils', 'Delhi Capitals')
df['team1'] = df['team1'].replace('Royal Challengers Bengaluru', 'Royal Challengers Bangalore')
df['team2'] = df['team2'].replace('Royal Challengers Bengaluru', 'Royal Challengers Bangalore')
df['team1'] = df['team1'].replace('Pune Warriors', 'Rising Pune Supergiant')
df['team2'] = df['team2'].replace('Pune Warriors', 'Rising Pune Supergiant')
df['team1'] = df['team1'].replace('Kings XI Punjab', 'Punjab Kings')
df['team2'] = df['team2'].replace('Kings XI Punjab', 'Punjab Kings')
df['team1'] = df['team1'].replace('Rising Pune Super Giants','Rising Pune Supergiants')
df['team2'] = df['team2'].replace('Rising Pune Super Giants', 'Rising Pune Supergiants')
df['team1'] = df['team1'].replace('Rising Pune Supergiant','Rising Pune Supergiants')
df['team2'] = df['team2'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')
# in toss_winner 
df['toss_winner'] = df['toss_winner'].replace('Delhi Daredevils','Delhi Capitals')
df['toss_winner'] = df['toss_winner'].replace('Royal Challengers Bengaluru', 'Royal Challengers Bangalore')
df['toss_winner'] = df['toss_winner'].replace('Pune Warriors', 'Rising Pune Supergiants')
df['toss_winner'] = df['toss_winner'].replace('Kings XI Punjab', 'Punjab Kings')
df['toss_winner'] = df['toss_winner'].replace('Rising Pune Super Giants','Rising Pune Supergiants')
df['toss_winner'] = df['toss_winner'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants') 
# in winner 
df['winner'] = df['winner'].replace('Delhi Daredevils','Delhi Capitals')
df['winner'] = df['winner'].replace('Royal Challengers Bengaluru', 'Royal Challengers Bangalore')
df['winner'] = df['winner'].replace('Pune Warriors', 'Rising Pune Supergiants')
df['winner'] = df['winner'].replace('Kings XI Punjab', 'Punjab Kings')
df['winner'] = df['winner'].replace('Rising Pune Super Giants','Rising Pune Supergiants')
df['winner'] = df['winner'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants') 
# drop the becouse their is no team which name is kochi tuskers kerala                                
df = df.drop(df[df['team1'] == 'Kochi Tuskers Kerala'].index)
df = df.drop(df[df['team2'] == 'Kochi Tuskers Kerala'].index)
print(df['team1'].unique())
print(df['team2'].unique())
print(df['winner'].unique())
print(df['toss_winner'].unique())

print(df.info())

   # # now clean the data of delivaries 
sf = pd.read_sql_query('select * from deliveries ', engine)
print(sf)
print(sf.T)
print(sf.info())
print(sf['match_id'].unique())
print(sf['inning'].unique())
print(sf['batting_team'].unique())
print(sf['bowling_team'].unique())
print(sf['over'].unique())
print(sf['ball'].unique())
print(sf['extras_type'].unique())

# print(pd.read_sql_query('select over from deliveries limit 30',engine))
# print(pd.read_sql_query('select is_wicket from deliveries limit 20',engine))
print(sf.isnull().sum())
print(sf.shape)
 
            ### droping the column how have 98 % is null value in side it 
## cur = conn.cursor()
## cur.execute("""
##    ALTER TABLE deliveries
##    DROP COLUMN player_dismissed,
##     DROP COLUMN dismissal_kind,
##     DROP COLUMN fielder;
            
## """)
## conn.commit()
## print("Column dropped successfully!")
## cur.close()
## conn.close()
            ### droping column is_wicket
## cur = conn.cursor()
## cur.execute("""
## alter table deliveries
## drop column is_wicket;
## """)
## conn.commit()
## cur.close()
## conn.close()

# changing the name of the team which have dublicate entry from diffrent names 
sf['batting_team'] = sf['batting_team'].replace('Delhi Daredevils', 'Delhi Capitals')
sf['bowling_team'] = sf['bowling_team'].replace('Delhi Daredevils', 'Delhi Capitals')
sf['batting_team'] = sf['batting_team'].replace('Royal Challengers Bengaluru', 'Royal Challengers Bangalore')
sf['bowling_team'] = sf['bowling_team'].replace('Royal Challengers Bengaluru', 'Royal Challengers Bangalore')
sf['batting_team'] = sf['batting_team'].replace('Pune Warriors', 'Rising Pune Supergiant')
sf['bowling_team'] = sf['bowling_team'].replace('Pune Warriors', 'Rising Pune Supergiant')
sf['batting_team'] = sf['batting_team'].replace('Kings XI Punjab', 'Punjab Kings')
sf['bowling_team'] = sf['bowling_team'].replace('Kings XI Punjab', 'Punjab Kings')
sf['batting_team'] = sf['batting_team'].replace('Rising Pune Super Giants','Rising Pune Supergiants')
sf['bowling_team'] = sf['bowling_team'].replace('Rising Pune Super Giants', 'Rising Pune Supergiants')
sf['batting_team'] = sf['batting_team'].replace('Rising Pune Supergiant','Rising Pune Supergiants')
sf['bowling_team'] = sf['bowling_team'].replace('Rising Pune Supergiant', 'Rising Pune Supergiants')
sf = sf.drop(sf[sf['bowling_team'] == 'Kochi Tuskers Kerala'].index)
sf = sf.drop(sf[sf['batting_team'] == 'Kochi Tuskers Kerala'].index)
print(sf['batting_team'].unique())
print(sf['bowling_team'].unique())

print(df.head(0))  # show matches columns from the already-loaded DataFrame (includes match_id)
print(sf.head(0))  # show deliveries columns from the already-loaded DataFrame
#print(pd.read_sql_query('select match_id from deliveries limit 30',engine))
# show renamed column from the already-loaded `df` instead of re-querying DB `id`
print(df[['match_id']].head(30))

# joining both the tables on the base on id and match_id becouse both are same in contant 
# `df` already has `match_id` (renamed earlier), so no further rename needed here
# avoid re-querying the DB here (would show DB column `id`); use in-memory DataFrames instead
# print(pd.read_sql_query('select * from matches limit 0 ', engine))
# print(pd.read_sql_query('select * from deliveries limit 0',  engine))

# Merge deliveries and matches on `match_id`
# Ensure both `match_id` columns use the same dtype so merge matches correctly
# convert to string (safe when IDs may be numeric or contain leading zeros)
df['match_id'] = df['match_id'].astype(str)
sf['match_id'] = sf['match_id'].astype(str)

print('df.match_id dtype:', df['match_id'].dtype)
print('sf.match_id dtype:', sf['match_id'].dtype)
print('df.match_id sample:', df['match_id'].head())
print('sf.match_id sample:', sf['match_id'].head())

# Now merge deliveries and matches on `match_id`
final_table = sf.merge(df, on='match_id', how='left', suffixes=('_del', '_mat'))
print('Merged shape:', final_table.shape)
print(final_table.head())
# Save merged result for downstream use
final_table.to_csv('merged_matches_deliveries.csv', index=False)
print('Saved merged_matches_deliveries.csv')

print(final_table.info())
# print(final_table['result'].head(10))
# print(final_table['batting_team'].head(20))
# print(final_table['team1'].head(20))
print(final_table['result'].unique())
final_table = final_table.dropna(subset= ['season'])


print(final_table.isnull().sum())
print(final_table['team1'].unique())
print(final_table['season'].unique())


# We should drop these columns from the pandas DataFrame, not try to ALTER a DB table
# if 'final_table' in locals():
#     final_table = final_table.drop(columns=['batting_team', 'bowling_team'], errors='ignore')
#     print('Dropped DataFrame columns: batting_team, bowling_team')
# else:
#     print('final_table not found; skipping DataFrame column drop')

print(final_table.info())
print(final_table.shape)

print(final_table['super_over'].unique())



# cursor.execute("""
# drop table if exists final_table;
# CREATE TABLE final_table (
#     match_id           VARCHAR(50),
#     inning             INTEGER,
#     over               INTEGER,
#     ball               INTEGER,
#     batter             VARCHAR(100),
#     bowler             VARCHAR(100),
#     non_striker        VARCHAR(100),
#     batsman_runs       INTEGER,
#     extra_runs         INTEGER,
#     total_runs         INTEGER,
#     extras_type        VARCHAR(50),
#     season             VARCHAR(10),
#     city               VARCHAR(100),
#     date               TIMESTAMP,
#     match_type         VARCHAR(50),
#     player_of_match    VARCHAR(100),
#     venue              VARCHAR(200),
#     team1              VARCHAR(100),
#     team2              VARCHAR(100),
#     toss_winner        VARCHAR(100),
#     toss_decision      VARCHAR(20),
#     winner             VARCHAR(100),
#     result             VARCHAR(20),
#     result_margin      NUMERIC(15,2),
#     target_runs        NUMERIC(15,2),
#     target_overs      NUMERIC(10,2),
#     super_over         VARCHAR(5),
#     umpire1            VARCHAR(100),
#     umpire2            VARCHAR(100)
# );
# """)

# conn.commit()
# final_table.to_sql(
#     "final_table",
#     engine,
#     if_exists="append",
#     index = False
# )

print(pd.read_sql_query('select team1,team2 from final_table limit 30', engine))
print(pd.read_sql_query('select match_id from final_table limit 30',engine))

print(pd.read_sql_query(
    "SELECT match_id, team1, COUNT(*) AS total_rows "
    "FROM final_table "
    "GROUP BY match_id, team1 "
    "ORDER BY match_id;",
    engine
))
print(pd.read_sql_query('select * from final_table limit 10',engine))
print(final_table['ball'].unique())