# Introduction to Google Colab + Linear Regression

This educational project shows how to start working in **Google Colab** and complete a simple **linear regression** task in Python — one of the basic machine learning models.

Contents:

- a complete Colab notebook (`colab_regresja.ipynb`),
- a sample dataset (`mieszkania.csv`),
- step-by-step instructions for running the project and publishing it on GitHub.

---

## 1. What is Google Colab?

**Google Colaboratory (Colab)** is a free online environment for writing and running Python code.  
Nothing needs to be installed locally — it runs in the browser and saves automatically to **Google Drive**.

Colab lets you:

- write and run **Python** (e.g. machine learning, data analysis, plots),
- store projects in the cloud (Google Drive),
- share notebooks with others,
- use Google compute (CPU / GPU / TPU).

---

## 2. How to open Google Colab

### Step 1: Open Colab from Gmail

1. While signed into Gmail, click the **9-dot Google apps menu** in the top-right corner.  
2. Find **Colab** (or “Colaboratory”).  
3. If it is missing, click **“More from Google”** or open:  
   [https://colab.research.google.com](https://colab.research.google.com)

### Step 2: Open this project’s notebook

#### Option A — upload the notebook locally

1. Unzip the downloaded project folder.  
2. In Colab choose: **File → Upload notebook**.  
3. Select `colab_regresja.ipynb`.  
4. You can now run the cells.

#### Option B — save a copy to Google Drive

In Colab click: **File → Save a copy in Drive**.  
Your changes will then sync to the cloud automatically.

---

## 3. Project contents

| File | Description |
|------|-------------|
| `colab_regresja.ipynb` | Main notebook with code, guidance, and exercises |
| `mieszkania.csv` | Sample data: apartment area (m²) vs price (thousands of PLN) |
| `requirements.txt` | Dependencies (if you run locally) |
| `.gitignore` | Ignores temporary files |
| `README.md` | This document |

---

## 4. Assignment: Linear regression

### Goal

Predict **apartment price (thousands of PLN)** from **floor area (m²)**.

Model:

\[
y = a \cdot x + b
\]

where:

- \( y \) — predicted price,  
- \( x \) — floor area,  
- \( a \) — slope (how fast price grows with area),  
- \( b \) — intercept (baseline price when area = 0).

### Data (`mieszkania.csv`)

| metraz_m2 | cena_tys |
|------------|-----------|
| 35 | 310 |
| 50 | 395 |
| 65 | 470 |
| 80 | 560 |
| 100 | 670 |
| 120 | 770 |

This sample shows that **price increases with floor area**.

### Steps in the notebook

In `colab_regresja.ipynb` you will:

1. **Import** the CSV with pandas.  
2. **Split** features (`X = area`) and target (`y = price`).  
3. **Train** a linear regression model (`LinearRegression` from `scikit-learn`).  
4. **Visualize** results on a plot.  
5. **Predict** for new values (e.g. 40, 60, 80 m²).

### Independent exercises

1. Add a `cena_za_m2` column and inspect how it changes with area.  
2. Plot area (x) vs price per m² (y).  
3. Compute model errors: MAE and/or MSE.  
4. Add a second feature such as `metraz_m2 ** 2` and check whether a polynomial model fits better.  
5. Save a plot to PNG (`plt.savefig("regresja.png")`).

---

## 5. Suggested project layout

```
colab_regresja_projekt/
├── colab_regresja.ipynb
├── mieszkania.csv
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 6. How to publish on GitHub

### Option 1 — browser (simplest)

1. Sign in at [https://github.com](https://github.com).  
2. Click **New Repository**.  
3. Name it, e.g. `colab-regresja`.  
4. Drag and drop project files (`.ipynb`, `.csv`, `README.md`, etc.).  
5. Click **Commit changes**.

### Option 2 — directly from Colab

1. In Colab choose: **File → Save a copy in GitHub**.  
2. Select your repository.  
3. Add a short commit message (e.g. “First version of the linear regression project”).  
4. Confirm.

---

## 7. Key takeaways

- **Colab** is a free in-browser Python environment.  
- **Linear regression** predicts continuous values (prices, temperatures, etc.).  
- In `scikit-learn`, create the model with `LinearRegression()`.  
- Visualizing data helps interpret results.  
- **GitHub** is useful for sharing code and building a portfolio.

---

## 8. What next?

- Load **your own dataset** (e.g. car prices, height vs weight).  
- Try `PolynomialFeatures` and compare the fit.  
- Create a new Colab notebook and experiment.

---

## 9. Submission

- Create a repository in the **PROJ-D-2024** organization named `Colabolatory_<student-number>`.  
- Submit the repository link in the Teams assignment.
