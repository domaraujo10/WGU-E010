#prompts the user to enter server uptime in days
#converts uptime to hours
#prompts the user to enter the current number of active users
#adds 1 to represent a new user log-in
#prompts the user to enter total disk space (GB) and used disk space (GB)
#calculates available disk space
#prints a clear status report with results

server_uptime = int(input("Enter server uptime in days:"))
server_uptime_hours = server_uptime * 24
active_users = int(input("Current number of active users: ")) + 1
total_disk = int(input("Enter total disk space (GB): "))
used_disk = int(input("Enter used disk space (GB): "))
available_disk = total_disk - used_disk
print("Server Status Report:")
print(f"Days of uptime: {server_uptime}")
print(f"Hours of uptime: {server_uptime_hours}")
print(f"Current number of active users: {active_users}")
print(f"Total disk space: {total_disk} GB")
print(f"Used disk space: {used_disk} GB")
print(f"Available disk space: {available_disk} GB")

