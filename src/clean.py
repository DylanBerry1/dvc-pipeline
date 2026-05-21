import pandas as pd
from dateutil import parser

print('Beginning data cleaning')
df = pd.read_csv('data/raw/events.csv')

df = df.dropna()

df = df[(df['event_type'] == 'click') | (df['event_type'] == 'login')\
		| (df['event_type'] == 'scroll') | (df['event_type'] == 'purchase') |\
		(df['event_type'] == 'view')]

df = df[df['duration_seconds'] >= 0]

def norm_timestamp(timestamp):
	time = parser.parse(timestamp)
	return time.strftime("%Y-%m-%dT%H:%M:%S")
	
df['timestamp'] = df['timestamp'].apply(norm_timestamp)
	

df.to_csv("data/clean/events.csv")