# **Data Cleaning and Deduplication using Hash Tables**

This project automates the **cleaning and deduplication of CSV data** using a **custom Hash Table implementation** in Python. The cleaned data is then **stored in a PostgreSQL database**.

## 🚀 **Features**

✔ Cleans messy data by **removing extra spaces** and **fixing capitalization**  
✔ Detects and **removes duplicate records** using a **hash table**  
✔ **Validates and standardizes emails**  
✔ Converts **NULL values to None** for proper database storage  
✔ Saves **cleaned data** as a new CSV file  
✔ Inserts **unique records** into a PostgreSQL database  

---

## 📌 **Steps to Run the Code**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/your-repo.git
cd your-repo
```

### **2️⃣ Install Dependencies**
Make sure you have **Python** and **PostgreSQL** installed. Then install required packages:
```bash
pip install psycopg2
```

### **3️⃣ Prepare the Input Data**
- Place your raw CSV file in the project directory as **`file.csv`**  
- Ensure it has the following columns:  
  ```
  id, name, email, city, purchase_amount, date
  ```

### **4️⃣ Run the Script**
```bash
python clean_data.py
```

### **5️⃣ Check the Cleaned Data**
- The script creates a **cleaned_file.csv** with the cleaned records.  
- It also inserts unique data into a **PostgreSQL database**.

---

## 🗄 **Database Table Structure**
The script creates a `data` table in PostgreSQL with the following schema:
```sql
CREATE TABLE IF NOT EXISTS data (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50),
    purchase_amount DECIMAL(10,2)
);
```

---

## ⚠ **Notes**
- Ensure your **PostgreSQL server is running** before executing the script.  
- Update the database credentials in the script:
  ```python
  psycopg2.connect(dbname='postgres', user='postgres', password='123', host="localhost", port="5432")
  ```
- Modify the script to **fix invalid emails** (e.g., `blackwidow@@shield.com` → `blackwidow@shield.com`).  

---

## 🛠 **Customization**
- **Adjust Email Validation:** Add regex to detect and fix incorrect emails.  
- **Modify Hash Table Size:** Increase or decrease based on expected dataset size.  
- **Change Database Table Name:** Update `data` to any custom name.  

---

## 📜 **License**
This project is open-source and available under the **MIT License**.
