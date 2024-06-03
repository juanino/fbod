# Workout Data Summary

This Python program reads workout data from a CSV file, summarizes the training by weeks, and outputs the summary. It calculates total duration, distance, reps, and volume lifted (in lbs*reps) for each week. Additionally, it breaks down the distance and volume by exercise type.

## Features

- Reads workout data from a CSV file.
- Summarizes training by weeks.
- Calculates total duration, distance, reps, and volume lifted.
- Breaks down distance and volume by exercise type.
- Converts total duration to a human-readable format (hours, minutes, seconds).
- Converts distance from meters to miles.
- Converts weight from kilograms to pounds.
- Outputs the summary to the console.

## How to Use

1. Clone the repository:

   ```
   git clone https://github.com/your_username/your_repository.git
   ```

2. Navigate to the directory:

   ```
   cd your_repository
   ```

3. Ensure you have Python installed.

4. Run the script:

   ```
   python workout_summary.py
   ```

5. View the summary printed in the console.

## Sample Output

```
Week: 2024-05-27 to 2024-06-02
Distance by Exercise:
- Plank: 0.00 miles
- Dumbbell Bench Press: 0.00 miles
- Dumbbell Romanian Deadlift: 0.00 miles
- Push Up on Knees: 0.00 miles
- Dumbbell Bicep Curl: 0.00 miles
- Dumbbell Squat: 0.00 miles
- Dead Bug: 0.00 miles
- Walking: 1.78 miles
- Cycling: 2.55 miles
Volume by Exercise:
- Dumbbell Bench Press: 61.26 lbs*reps
- Dumbbell Romanian Deadlift: 45.95 lbs*reps
- Push Up on Knees: 62.40 lbs*reps
- Dumbbell Bicep Curl: 31.74 lbs*reps
- Dumbbell Squat: 45.95 lbs*reps
- Dead Bug: 83.43 lbs*reps
Total Duration: 9h 7m 36s
Total Distance: 4.33 miles
Total Reps: 127
Total Volume: 330.77 lbs*reps
```

## Dependencies

- Python 3.x
- `pytz` library for handling time zones

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

