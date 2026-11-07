failed = 0
attempts = {}
file_log_data = open('sample.log','r').read()
for line in file_log_data.splitlines():
	if "LOGIN_FAILED" in line:
		failed = failed + 1
		ip = file_log_data.split()[-1]
		if ip in attempts:
			attempts[ip] += 1
		else:
			attempts[ip] = 1

print("The number of failed login are: ",failed)
for ip, count in attempts.items():
	if count >= 2:
		print("[WARNING]", ip, "has", count, "failed attempts!")
	else:
		print("[NORMAL]", ip, "has", count, "failed attempt.")
with open("security_report.txt", "w") as report:

    report.write("===== SECURITY REPORT =====\n")

    for ip, count in attempts.items():

        if count >= 2:
            message = f"[WARNING] {ip}: {count} failed attempts\n"
        else:
            message = f"[NORMAL] {ip}: {count} failed attempt\n"

        report.write(message)

print("\nSecurity report generated successfully!")