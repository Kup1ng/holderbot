# HolderBot  

<div align="center"><a href="https://github.com/Kup1ng/holderbot">
  <img src="https://github.com/user-attachments/assets/b660f9cb-0541-4c03-9660-2b5f2cb9e6e2" width="200" alt="Image Description">
</a>
</div>

---

## **Supported Panels**  
- [x] **Marzneshin**  

---

## **Setup**  

### **Server and Docker Setup**  

<details>
<summary>Show Server Commands</summary>

#### Install Docker  
```bash
curl -fsSL https://get.docker.com | sh
```
</details>

---

### **Install & Run the Bot**  

<details>
<summary>Show Run Commands</summary>

#### 1. Create Directory and Download Files  
```bash
mkdir -p /opt/holderbot/data
curl -o /opt/holderbot/docker-compose.yml https://raw.githubusercontent.com/Kup1ng/holderbot/master/docker-compose.yml
cd /opt/holderbot
curl -o .env https://raw.githubusercontent.com/Kup1ng/holderbot/master/.env.example
nano .env
```

#### 2. Pull Docker Image  
```bash
docker compose pull
```

#### 3. Start the Bot  
```bash
docker compose up -d
```

After a few moments, the bot will start running.

</details>

---

### **Update the Bot**  

<details>
<summary>Show Update Commands</summary>

Make sure you're in the **HolderBot** directory:  
```bash
cd /opt/holderbot
```

Then update the bot:  
```bash
docker compose pull && docker compose up -d
```

</details>

---

### **Manage the Bot**  

<details>
<summary>Show Manage Commands</summary>

Make sure you're in the **HolderBot** directory:  
```bash
cd /opt/holderbot
```

- **Restart the Bot:**  
  ```bash
  docker compose restart
  ```

- **Stop the Bot:**  
  ```bash
  docker compose down
  ```

- **View Logs:**  
  ```bash
  docker compose logs -f
  ```

</details>

---

### **Switch to DEV Mode (preview mode)**  

<details>
<summary>Show DEV Commands</summary>

Make sure you're in the **HolderBot** directory:  
```bash
cd /opt/holderbot
```

- **Open the Docker Compose File:**  
  ```bash
  nano docker-compose.yml
  ```

- **Change the Image Tag:**  
  
  **From:**  
  ```yaml
  Kup1ng/holderbot:latest
  ```
  **To:**  
  ```yaml
  Kup1ng/holderbot:dev
  ```

- **Pull the Docker Image:**  
  ```bash
  docker compose pull
  ```

- **Start the Bot:**  
  ```bash
  docker compose up -d
  ```
</details>

