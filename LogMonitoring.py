
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
            print(process_type)

            # if status is "START" then store the start time for the job
            if status == "START":
                jobs[pid] == [timestamp]
            elif pid in jobs.keys() and status == "END": #if status is "END" then store the end time for the job
                jobs[pid].append(timestamp)

            print(jobs[pid])

if __name__ == '__main__':
    main()