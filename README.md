# 🏗️ Construction Cost Estimation & Pricing Analytics Dashboard

## 📌 Project Overview

The **Construction Cost Estimation & Pricing Analytics Dashboard** is an interactive data analytics application built using Python and Streamlit. It helps users explore construction cost estimates, analyse pricing strategies, understand cost components, and calculate project quotations based on configurable profit rates and pricing adjustments.

The project demonstrates how data analytics and interactive dashboards can support cost estimation and pricing decisions in the construction industry.

## 🎯 Business Objectives

- Analyse material and labour costs across construction estimates.
- Understand how profit rates affect estimated project prices.
- Compare average estimates across different pricing policies.
- Analyse the distribution of discounts and markups.
- Calculate construction quotations interactively.
- Export quotation details and filtered dataset records.

## ✨ Key Features

### 1. Business Overview
- Total number of projects.
- Total estimated project value.
- Average project estimate.
- Average base cost.

### 2. Cost Structure Analysis
- Compare average material and labour costs.
- Visualise the relationship between material costs and labour costs.
- Explore project estimates by pricing variables.

### 3. Pricing Policy Analysis
- Compare average estimates across pricing policies.
- Analyse discount and markup distributions.
- Filter the dashboard by pricing policy and adjustment type.

### 4. Interactive Quotation Calculator
Enter the following values to calculate a construction quotation:

- Material cost
- Labour cost
- Profit rate
- Discount or markup

The calculator displays the base cost, profit component, and final estimate. It also allows users to download a quotation as a CSV file.

### 5. Data Export
- Download filtered project records.
- Export individual quotation calculations.

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Plotly
- **Web Application:** Streamlit
- **Version Control:** Git and GitHub
- **Deployment:** Streamlit Community Cloud

## 📊 Dataset

The dataset contains 1,000 construction cost estimates and six columns:

| Column | Description |
|---|---|
| `Material_Cost` | Estimated material expenditure |
| `Labor_Cost` | Estimated labour expenditure |
| `Profit_Rate` | Profit percentage applied to base cost |
| `Discount_or_Markup` | Pricing adjustment applied to the estimate |
| `Policy_Reason` | Business justification for the pricing decision |
| `Total_Estimate` | Final estimated project price |

The dataset contains no missing values in the initial inspection.

## 🧮 Cost Estimation Formula

The dashboard calculates estimates using the following formula:

**Base Cost**

`Material Cost + Labour Cost`

**Profit Amount**

`Base Cost × Profit Rate / 100`

**Final Estimate**

`Base Cost + Profit Amount + Discount or Markup`

A negative adjustment represents a discount, while a positive adjustment represents a markup.

## 🚀 Run the Project Locally

### Prerequisites

- Python 3.9 or later
- pip

### Step 1: Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/construction-cost-dashboard.git
```

Replace `YOUR_USERNAME` with your GitHub username.

### Step 2: Navigate to the project folder

```bash
cd construction-cost-dashboard
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in the terminal to use the dashboard.

## 📁 Project Structure

```text
construction-cost-dashboard/
│
├── app.py
├── construction_estimates.csv
├── requirements.txt
└── README.md
```

## ⚠️ Project Limitations

- The dataset represents construction cost estimates and does not establish actual project expenditure or cost overruns.
- The quotation calculator uses a predefined pricing formula rather than a machine-learning prediction model.
- Pricing policy comparisons are descriptive and do not establish causal relationships.
- Estimates depend on the quality of the input values and the assumptions used in the calculation.

## 🔮 Future Enhancements

- Add project type, location, floor area, and construction material inputs.
- Introduce cost-per-square-foot analysis.
- Incorporate actual versus estimated project costs when suitable data becomes available.
- Develop cost-overrun analysis using historical project data.
- Add downloadable PDF quotations and more advanced reporting.

## 👨‍💻 Author

**Harshal Patil**

Data Science | Data Analytics | Construction Project Planning

---

*This project demonstrates the application of Python-based analytics and interactive dashboard development to a construction business problem.*
