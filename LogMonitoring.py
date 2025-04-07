from datetime import datetime

# parse the current log line to obtain the necessary info
def parse_info(line):
    
    # split the line by "," into seperate fields (timestamp, process, status, pid)
    timestamp, process, status, pid = line.split(",")

    # print(timestamp, process, status, pid)

    # remove whitespace from the left side of the process and status
    process = process.lstrip()
    status = status.lstrip()

    # print(process)
    # print(status)

    # remove the newline from the pid
    pid = pid.strip('\n')

    # print(pid)

    return timestamp, process, status, pid

# identify if the process is a job or task
def identify_process(process):
    # if the keyword "job" is in the process description then it's a job
    if "job" in process:
        process_type = "job"
    elif "task" in process: #if the keyword "task" is in the process description then it's a task
        process_type = "task"
    return process_type

# calculate the duration between start and end timestamps
def calculate_duration(start_time, end_time):
    # print(type(start_time))
    # convert start and time into datetime objects
    start = datetime.strptime(start_time, "%H:%M:%S")
    end = datetime.strptime(end_time, "%H:%M:%S")

    # print(end, start)
    # print(type(start))
    # print(type(end))

    # calculate the duration in second and convert it to minutes
    duration = (end-start).total_seconds() / 60  

    return duration

# log message if the processing time exceeds certain thresholds
def log_messages(process_type, pid, duration):
    message = ""
    # if the duration is greater then 10 minutes => log an error message
    if duration > 10:
        message = f'Error: {process_type} with id: {pid} and duration: {duration:.2f} minutes has exceeded the time limit of 10 minutes\n'
    elif duration > 5: # if the duration is greater then 5 minuts -> log a warning message
        message = f'Warning: {process_type} with id: {pid} and duration: {duration:2f} minutes has exceeded the time limit of 5 minutes\n'

    # write to file if it's an error or a warning messsage
    if message !="":
        with open("output.txt", "a") as g:
            g.write(message)

def main():
    # intialize a dictionary to store every job/task with the two allocated times: start and end ('job_pid':['start_time', 'end_time'])
    jobs = dict()
    # open the file for reading
    with open("logs.log", "r") as log_file:
        for line in log_file:
            # print(line)
            timestamp, process, status, pid = parse_info(line)
            # print(timestamp, process, status, pid)
            
            process_type = identify_process(process)
            # print(process_type)

            # if status is "START" then store the start time for the job
            if status == "START":
                jobs[pid] = [timestamp]
            elif pid in jobs.keys() and status == "END": #if status is "END" then store the end time for the job
                jobs[pid].append(timestamp)

                duration = calculate_duration(jobs[pid][0], jobs[pid][1])
                # print(duration, pid)
                
                # log the appropiate message when duration exceeds 5 or 10 minutes
                log_messages(process_type, pid, duration)
            # print(jobs[pid])

                
if __name__ == '__main__':
    main()