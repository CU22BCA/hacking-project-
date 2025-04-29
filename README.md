# hacking-project- 🔐 Info Disclosure CTF Lab
This is a small vulnerable lab built to simulate an information disclosure vulnerability as part of a CTF (Capture The Flag) challenge. The main goal is to find the hidden flag within the application using your hacking skills.

🧪 Project Description
This project is designed around the concept of Security Misconfigurations and Information Disclosure. Sensitive information has been hidden somewhere in the application — your job is to discover it using techniques like:

Checking HTML comments

Reviewing JavaScript files

Inspecting server logs

Exploring hidden or unprotected endpoints

🛠 Tech Stack
Language: Python (Flask)

Editor: VS Code

Front-End: HTML, CSS, JavaScript

📁 Project Structure
php
Copy
Edit
INFO_DISCLOSURE_APP/
├── logs/
│   └── server.log             # Server log file with suspicious activity
│   └── flag.txt               # The hidden flag (find it!)
├── templates/
│   ├── admin.html             # Admin login UI
│   ├── admindash.html         # Admin dashboard with hidden secrets
│   ├── index.html             # Main homepage
│   ├── info.html              # Lab introduction and tips
├── static/
│   └── obfuscated_script.js   # Obfuscated JS with possible leaks
│   └── script.js              # Regular JS logic
│   └── sw.js                  # Service worker (used in CTF challenge)
├── app.py                     # Flask application backend
🎯 Objective
Find the flag hidden in this web application. It may be inside logs, source code, or embedded in the frontend.

💡 Hint: Inspect elements, view-source, and monitor network requests to discover hidden clues.
