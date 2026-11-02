# Count the total errors and warnings
total = 0

print("ERROR REPORT")
print("-" * 40)

with open("application.log", 'r') as file:
    content = file.read()

# Iterate through each log entry
for line in content.split("\n"):
    timestamp = line[:19]
    
    if not line.strip():
        continue

    toks = line.split("|")

    # Clean and standardize severity
    status = toks[1].strip()
    status = status.replace("error", "ERROR")
    status = status.replace("warning", "WARNING")

    # Check for errors and warnings
    if "WARNING" in status or status.find("ERROR") != -1:
        log_message = " - ".join([timestamp, status, toks[2].strip()])

        total += 1
        print(log_message)

# Total errors and warnings
print()
print(f"Total errors and warnings: {total}")