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
- Walking: 5.09 miles
- Cycling: 5.09 miles
Volume by Exercise:
- Dumbbell Bench Press: 480.00 lbs*reps
- Dumbbell Romanian Deadlift: 600.00 lbs*reps
- Dumbbell Bicep Curl: 300.00 lbs*reps
- Dumbbell Squat: 420.00 lbs*reps
Total Duration: 2h 30m 7s
Total Distance: 10.18 miles
Total Reps: 374
Total Volume: 1800.00 lbs*reps
Distance Change from Previous Week: -34.58%
Volume Change from Previous Week: 3114.29%
```

## Dependencies

- Python 3.x
- `pytz` library for handling time zones

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

