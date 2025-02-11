# ReqLogX - Advanced HTTP Request Logger

ReqLogX is a lightweight and flexible HTTP request logging server designed to capture and log all incoming HTTP requests. It supports multiple logging formats and can log requests to both console and file.

## 🚀 Features

- 📡 **Listens on a configurable port** (via CLI argument or config file)
- 📜 **Logs all incoming HTTP requests** (GET, POST, PUT, DELETE, etc.)
- 📂 **Supports multiple logging formats**:
  - ✅ Human-friendly (default)
  - ✅ Raw HTTP format
  - ✅ cURL format
- 📃 **Logs to file and console** simultaneously
- 🔧 **Easily configurable** through `server_config.ini`
- 🏗 **Follows best practices** for modularity, separation of concerns, and logging

---

## 📦 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/ReqLogX.git
cd ReqLogX
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt  # No dependencies needed for now
```

### 3️⃣ Run the Server

```bash
python server.py
```

By default, it runs on port **8080**.

### 4️⃣ (Optional) Run on a Custom Port and log format

```bash
python server.py --port 9090 --log-format http
```

---

## ⚙️ Configuration

Modify the `server_config.ini` file to change settings:

```ini
[server]
port = 8080
log_format = human
log_file = requests.log
log_to_file = true
```

- `port`: The port number to listen on
- `log_format`: Logging format:
  - `human` (easy-to-read format)
  - `http` (raw HTTP format)
  - `curl` (cURL command format)
- `log_file`: Path to log file.
- `log_to_file`: Enable or disable logging to file.

---

## 📜 Logging Formats

### **1️⃣ Human-Friendly (Default)**

```plaintext
📌 Request from 127.0.0.1:5656
📝 Method: POST
🔗 Path: /api/test
📜 Headers:
{
    "Content-Type": "application/json"
}
📦 Body: {"message": "hello"}
--------------------------------------------------
```

### **2️⃣ Raw HTTP Format**

```http
POST /api/test HTTP/1.1
Host: localhost:8080
Content-Type: application/json

{"message": "hello"}
```

### **3️⃣ cURL Command Format**

```bash
curl -X POST -H 'Content-Type: application/json' --data '{"message": "hello"}' 'http://localhost:8080/api/test'
```

---

## 📡 Sending a Request

Test the logger using `cURL`:

```bash
curl -X POST http://localhost:8080/test -H "Content-Type: application/json" -d '{"name": "test"}'
```

---

## 🏗 Project Structure

```bash
ReqLogX/
│── server.py          # Main HTTP server
│── logger.py          # Logging logic
│── server_config.ini  # Configuration file
│── Makefile           # Makefile for automating tasks
│── README.md          # Documentation
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

1. Fork the repository 🍴
2. Create a new branch (`git checkout -b feature-new-logging-format`)
3. Commit your changes (`git commit -m "Added new logging format"`)
4. Push to the branch (`git push origin feature-new-logging-format`)
5. Create a pull request 🚀
