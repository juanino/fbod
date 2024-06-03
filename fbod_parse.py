import csv
from datetime import datetime, timedelta
import pytz

# Define a function to read the CSV file
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read the headers
        for row in reader:
            data.append(row)
    return headers, data

# Define a function to process the data
def process_data(headers, data):
    processed_data = []
    for row in data:
        record = {}
        for i, header in enumerate(headers):
            record[header] = row[i]
        processed_data.append(record)
    return processed_data

# Define a function to convert seconds to a human-readable format
def seconds_to_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

# Define a function to summarize training by weeks
def summarize_by_week(processed_data):
    summaries = {}
    est = pytz.timezone('US/Eastern')
    for entry in processed_data:
        date_utc = datetime.strptime(entry['Date'], '%Y-%m-%d %H:%M:%S %z')
        date_est = date_utc.astimezone(est)
        week_start = date_est - timedelta(days=date_est.weekday())
        week_end = week_start + timedelta(days=6)
        week_key = week_start.strftime('%Y-%m-%d') + ' to ' + week_end.strftime('%Y-%m-%d')
        if week_key not in summaries:
            summaries[week_key] = {
                'Duration(s)': 0,
                'Distance(miles)': 0,
                'Reps': 0,
                'Volume(lbs*reps)': 0,
                'Distance_by_exercise': {},  # Dictionary to store distance by exercise type
                'Volume_by_exercise': {}     # Dictionary to store volume by exercise type
            }
        summaries[week_key]['Duration(s)'] += float(entry['Duration(s)'])
        exercise = entry['Exercise']
        distance_miles = round(float(entry['Distance(m)']) / 1609.34, 2)
        summaries[week_key]['Distance(miles)'] += distance_miles
        summaries[week_key]['Reps'] += int(entry['Reps'])
        weight_kg = float(entry['Weight(kg)'])
        weight_lbs = weight_kg * 2.20462
        volume = weight_lbs * int(entry['Reps'])
        summaries[week_key]['Volume(lbs*reps)'] += volume
        # Update distance by exercise type
        if distance_miles > 0:  # Only update for non-zero distances
            if exercise not in summaries[week_key]['Distance_by_exercise']:
                summaries[week_key]['Distance_by_exercise'][exercise] = 0
            summaries[week_key]['Distance_by_exercise'][exercise] += distance_miles
        # Update volume by exercise type
        if weight_kg > 0:  # Only update for exercises with weight greater than 0
            if exercise not in summaries[week_key]['Volume_by_exercise']:
                summaries[week_key]['Volume_by_exercise'][exercise] = 0
            summaries[week_key]['Volume_by_exercise'][exercise] += volume
    return summaries

# Define the filename
filename = 'workout_data.csv'

# Read the CSV file
headers, data = read_csv(filename)

# Process the data
processed_data = process_data(headers, data)

# Summarize training by weeks
weekly_summary = summarize_by_week(processed_data)

# Sort the weekly summaries by start date of each week
sorted_weekly_summary = dict(sorted(weekly_summary.items(), key=lambda item: datetime.strptime(item[0].split(' to ')[0], '%Y-%m-%d')))

# Print the weekly summaries
previous_week_summary = None
for week, summary in sorted_weekly_summary.items():
    print(f"Week: {week}")
    print("Distance by Exercise:")
    for exercise, distance in summary['Distance_by_exercise'].items():
        print(f"- {exercise}: {distance:.2f} miles")  # Round to 2 decimal places
    print("Volume by Exercise:")
    for exercise, volume in summary['Volume_by_exercise'].items():
        print(f"- {exercise}: {volume:.2f} lbs*reps")  # Round to 2 decimal places
    print(f"Total Duration: {seconds_to_time(summary['Duration(s)'])}")
    print(f"Total Distance: {summary['Distance(miles)']:.2f} miles")  # Round to 2 decimal places
    print(f"Total Reps: {summary['Reps']}")
    print(f"Total Volume: {summary['Volume(lbs*reps)']:.2f} lbs*reps")
    if previous_week_summary:
        distance_change = ((summary['Distance(miles)'] - previous_week_summary['Distance(miles)']) / previous_week_summary['Distance(miles)'] * 100) if previous_week_summary['Distance(miles)'] != 0 else 0
        volume_change = ((summary['Volume(lbs*reps)'] - previous_week_summary['Volume(lbs*reps)']) / previous_week_summary['Volume(lbs*reps)'] * 100) if previous_week_summary['Volume(lbs*reps)'] != 0 else 0
        print(f"Distance Change from Previous Week: {distance_change:.2f}%")
        print(f"Volume Change from Previous Week: {volume_change:.2f}%")
    print()
    previous_week_summary = summary

