# 📊 Business Sales & Profitability Performance Analytics

## 🎯 Executive Summary
This project delivers a comprehensive sales performance and profitability analysis using transaction data from the **Superstore Dataset** (9,994 sales transactions). The primary goal is to evaluate revenue drivers, regional trends, product category profitability, and discounting strategies to provide executive-level recommendations.

---

## 📈 Key Metrics at a Glance
| Metric | Value |
| :--- | :--- |
| **Total Revenue** | **$2,297,200.86** |
| **Total Net Profit** | **$286,397.02** |
| **Overall Profit Margin** | **12.47%** |
| **Total Transactions** | **9,994** |

---

## 🔍 Major Business Findings

### 1. Technology Leads Revenue & Profit
- **Technology**: **$836,154.03** Revenue | **$145,454.95** Profit (Margin: **17.40%**)
- **Office Supplies**: **$719,047.03** Revenue | **$122,490.81** Profit (Margin: **17.04%**)
- **Furniture**: **$741,999.80** Revenue | **$18,451.27** Profit (Margin: **2.49%**)

> ⚠️ **Key Risk:** Furniture sales generate high volume but minimal profit due to major losses in **Tables** (-$17,725.48) and **Bookcases** (-$3,472.56).

### 2. Discount Strategy Destroys Profit Margins
- Discounts up to **20%** maintain positive margins (11.8% to 29.5%).
- Discounts **≥ 30%** result in severe profit losses (e.g., 30% discount yields -10.05% margin; 70% discount yields -98.66% margin).

### 3. Regional Performance Breakdown
| Region | Sales | Profit | Margin % |
| :--- | :--- | :--- | :--- |
| **West** | $725,457.82 | $108,418.45 | **14.94%** |
| **East** | $678,781.24 | $91,522.78 | **13.48%** |
| **South** | $391,721.91 | $46,749.43 | **11.93%** |
| **Central** | $501,239.89 | $39,706.36 | **7.92%** |

---

## 💡 Strategic Recommendations
1. **Cap Maximum Discounts at 20%**: Immediately end discounting above 20% to eliminate recurring revenue leaks.
2. **Restructure Furniture Pricing**: Re-evaluate supplier agreements and pricing models for Tables and Bookcases.
3. **Double Down on West & East Expansion**: Allocate marketing resources toward the West and East regions where profit margins exceed 13.5%.
4. **Promote High-Margin Sub-Categories**: Focus promotion on **Copiers** (37.2% margin) and **Paper** (43.4% margin).

---

## 🛠️ Tools Used
- **Python** (Pandas, Plotly, Streamlit)
- **Data Analytics**: Data Cleaning, KPI Calculation, Trend Analysis

---
cd superstore-sales-analytics
pip install -r requirements.txt
streamlit run app.py
