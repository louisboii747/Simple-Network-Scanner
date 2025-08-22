# 🔍 Fast Network Scanner (Python)

A simple multithreaded Python script that scans your local network, pings each device, and shows whether it's online — complete with hostname lookup.

Perfect for beginners learning networking, ethical hacking, or how to use Python for system tools.

## ⚙️ Features

- 🔄 Multithreaded scanning for fast performance  
- 🌐 Detects your local IP and scans the `/24` subnet  
- 🖥️ Hostname resolution for each live device  
- 🧠 Works on both **Windows** and **Linux (Debian and RHEL systems)**

## 🚀 How to Run

1. Make sure you have Python 3 installed:
   ```bash
   python --version
   ```

2. Download the script:
   - Click the green **Code** button > **Download ZIP**, or  
   - Clone it:
     ```bash
     git clone https://github.com/yourusername/network-scanner.git
     ```

3. Run the script:
   ```bash
   python network_scanner.py
   ```

You’ll see output like:
```
[+] 192.168.1.1 is online (router.local)
[+] 192.168.1.12 is online (DESKTOP-B91K3T2)
[-] 192.168.1.22 is offline
```

## 🛠️ To-Do / Ideas

- Add colored terminal output
- Export results to a file
- Add GUI version with Tkinter
- Allow custom subnet input

## 📚 Learn More

This tool is a great stepping stone toward learning:
- Ethical hacking 🧑‍💻  
- Networking fundamentals 🌐  
- Python scripting 💻  
- System automation ⚡

---

Made with 💙 by Louis Hinchliffe
