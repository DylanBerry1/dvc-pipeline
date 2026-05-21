import pandas as pd
from dateutil import parser
import os

weekday_translator = {
	0:'Monday',
	1:'Tuesday',
	2:'Wednesday',
	3:'Thursday',
	4:'Friday',
	5:'Saturday',
	6:'Sunday'
}

print('Beginning data feature extraction')
os.makedirs("data/features", exist_ok=True)

df = pd.read_csv('data/transformed/events.csv')

def sec_to_min(seconds):
	return seconds / 60

def to_weekday(date):
	return weekday_translator[parser.parse(date).weekday()]
	
df['duration_minutes'] = df['duration_seconds'].apply(sec_to_min)
df['weekday'] = df['date'].apply(to_weekday)

df.to_csv('data/features/events.csv', index=False)