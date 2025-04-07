
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

    # open the file for reading
    with open("logs.log", "r") as log_file:
        for line in log_file:
            # print(line)
            timestamp, process, status, pid = parse_info(line)
            # print(timestamp, process, status, pid)
            
            process_type = identify_process(process)
            print(process_type)

if __name__ == '__main__':
    main()