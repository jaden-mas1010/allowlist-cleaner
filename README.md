# 🛡️ Allow List Cleaner (Cybersecurity Automation Script)

This project automates a common security task — updating and maintaining an *IP allow list*.  
It reads a file of allowed IP addresses, removes outdated or unauthorized ones, and rewrites the cleaned list safely.  
Built with Python, it demonstrates file handling, data validation, and simple automation logic for cybersecurity workflows.

---

## 🚀 Features
- Reads IP addresses from a text file (`allow_list.txt`)
- Removes any IPs specified in a "remove list"
- Rewrites the cleaned IPs back to the same file
- Displays the final allow list in the console
- Includes error handling for missing files and invalid operations

---

## 🧠 Skills Demonstrated
- Python File I/O (open, read, write)
- Lists and conditional logic
- Exception handling and clean code structure
- Security automation concepts (IP management)
- Reusable function design

---

## ⚙️ How It Works


### 1️⃣ Before cleaning  
Your file `allow_list.txt` might look like this:

192.168.25.60
192.168.140.81
192.168.203.198
192.168.1.100
192.168.1.101
192.168.1.102
192.168.1.103
10.0.0.5
10.0.0.8
10.1.1.10
172.16.0.25
172.16.0.26
172.16.10.30
192.168.50.12
192.168.50.13
192.168.60.99
192.168.70.45
192.168.80.200
10.10.5.5
10.10.5.6


### 2️⃣ Run the script  
```bash
python update_allow_list.py
✅ Successfully read 20 IP addresses from allow_list.txt
🚫 Removed 192.168.25.60 from allow list.
🚫 Removed 192.168.140.81 from allow list.
🚫 Removed 192.168.203.198 from allow list.
✅ Updated file saved successfully (17/20 IPs remain).

📄 Updated Allow List:
------------------------------
192.168.1.100
192.168.1.101
192.168.1.102
...
------------------------------
