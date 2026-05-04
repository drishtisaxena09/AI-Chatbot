# 🤖 Rule-Based AI Chatbot (Python)

## 📌 Description
This is a simple **rule-based AI chatbot** built using Python.  
It interacts with users through the command line, greets them based on the current time, and responds to basic questions using predefined responses.

This project is beginner-friendly and demonstrates how basic chatbot logic works without using any machine learning.

---

## ✨ Features
- 👋 Greets the user based on time (Morning / Afternoon / Evening)
- 🧑‍💻 Takes user name as input
- 💬 Responds to predefined questions using a dictionary
- 🤖 Handles unknown queries with a fallback response
- 🔁 Runs continuously until the user types `"bye"`

---

## 🛠️ Tech Stack
- **Language:** Python
- **Libraries Used:**
  - `datetime` (for time-based greeting)
  - `time` (basic usage)

---

## ⚙️ How It Works
1. The program asks for the user's name.
2. It checks the current time using the `datetime` module.
3. Based on the time, it greets the user (morning/afternoon/evening).
4. A dictionary stores predefined questions and answers.
5. The chatbot:
   - Converts user input to lowercase
   - Matches it with predefined responses
   - Returns the correct reply if found
   - Otherwise, shows a fallback message
6. The loop continues until the user types `"bye"`.

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rule-based-chatbot.git
