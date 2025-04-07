# Log Monitoring App
# Description
The application uses the logs.log file to read and process information about jobs and tasks, each having a start and end timestamp. Depending on the duration of each task, the application:
- Logs a warning if the task takes longer than 5 minutes
- Logs an error if the task takes longer than 10 minutes

# Implementation
To store the information, I used a dictionary where the key is the PID of the job/task, and value is a list containing the start and end times.
Example:
```
jobs = {"56100":["11:12:00", "11:15:00"}
```
The application's logic is organized into several functions:
- parse_info(line): Extracts the timestamp description, status and PID from each line
- identify_process(process): Verify from the process description if it's a job or task
- calculate_duration(start_time, end_time): Calculates the duration of the process
- log_messages(process_type, pid, duration): Writes a warning or error message into the output.txt file if the duration exceeds the limits

# Tests
I added a series of unit test using unittest, which verify the extracted log data, the correct type of the process(job/task), the calculation of duration, and the correct writing of error nessage into the file.

Possible Improvement: Add more unit tests, including edge cases (Ex: if the 'END' status is missing) 
   
