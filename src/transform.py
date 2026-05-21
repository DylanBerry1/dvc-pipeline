import pandas as pd
from dateutil import parser

print('Beginning data transformation')
os.makedirs("data/transformed", exist_ok=True)
df = pd.read_csv('data/clean/events.csv')



def extract_timestamp(timestamp):
	time = parser.parse(timestamp)
	return time.strftime('%Y-%m-%d')

df['date'] = df['timestamp'].apply(extract_timestamp)


df.to_csv('data/transformed/events.csv', index=False)