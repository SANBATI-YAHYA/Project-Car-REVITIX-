# 🚗 Brake System Analysis - Revitex

## 🏢 About Revitex

**Revitex** (short for *Réseau de Visite Technique et d’Expertise*) is a Moroccan company created to modernize and structure the technical vehicle inspection sector.  
It was established through the **GOCTA** group (Groupement des Organismes de Contrôle Technique Automobile), in response to Law 52-05 and Article 314, allowing professionals to organize under a unified and efficient network.

---

## 🎯 Project Objective

The main goal of this project is to develop a clear and user-friendly **dashboard** to:
- Monitor and visualize the **brake system performance** of inspected vehicles.
- Compare **braking effectiveness** based on **vehicle brands and models**.
- Improve **data analysis** and **decision-making**.
- Make the dashboard **simple and accessible**, even to non-technical staff.

---
## 🧱 Project Structure

```bash
.
├── Automatisation/
│   └── automatisati.py           # Automation script
│
├── MODEL/
│   ├── Prediction model/
│   │   ├── Input/                # Raw/preprocessed data
│   │   ├── Output/               # Prediction results
│   │   └── data_final_modeling.csv
│   │
│   ├── model/
│   │   ├── PROJET 1.pbix         # Power BI report
│   │   ├── modelV1.ipynb         # First modeling version
│   │   ├── modelV2.IPYNB         # Second modeling version
│   │   ├── merged_data.csv       # Merged cleaned data
│   │   ├── datafinal.csv         # Final dataset
│   │   └── date_visite.png       # Image or dashboard screenshot
│
├── dash/
│   ├── assets/                   # Static assets (CSS, icons)
│   └── test.ipynb                # Test notebook for Dash app
│
└── README.md.  
```

## 🔍 Project Analysis

### 1. 📊 Global Analysis of Technical Inspections:
- Visualize the **overall number of vehicle inspections**.
- Identify **peak periods** (by month) of inspection activity.
- Analyze **vehicle registration dates**.
- Compare **brake system performance** by brand.
- Evaluate the **global efficiency** of the braking systems.

### 2. 🚘 Individual Vehicle Analysis:
- View specific data per vehicle (by **license plate or ID**).
- Compare **actual weight** of the vehicle during inspection with its **theoretical weight**.
- Detect **weight discrepancies** that may affect braking performance.
- Generate a **summary report** per vehicle with its specs, inspection history, and brake status.

---


## 🛠 Technologies Used

- 🐍 **Python** (`Pandas`, `Matplotlib`, `Plotly`, `Dash`)
- 📓 **Jupyter Notebook** for data modeling
- 📊 **Power BI** for KPI dashboards
- 📁 **CSV** files for raw and processed data
- ⚙️ **Custom automation scripts** in Python

---

## 📈 Key Results

- ✅ Interactive **Power BI dashboard** for brake system analysis
- ✅ Lightweight **Dash app** for real-time data exploration
- ✅ Auto-generated **vehicle summary reports**
- ✅ Detection of **anomalies and inconsistencies** in data

---

## 🧪 How to Run

1. ▶️ **Run the modeling notebooks:**

   ```bash
   MODEL/model/modelV1.ipynb
   MODEL/model/modelV2.IPYNB
xecute the automation script:


Automatisation/automatisati.py

### 📊 Open the Power BI dashboard:

MODEL/model/PROJET 1.pbix

### 🌐 Launch the Dash app:


dash/test.ipynb
