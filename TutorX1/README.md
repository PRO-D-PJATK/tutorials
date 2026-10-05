# TutorX1

This is extra work.
https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

### Airflow Task – Total of 20 Points  
**Project Description**  
Create two task flows (DAGs) in Airflow to perform data processing tasks. The first DAG is responsible for downloading and splitting data, while the second DAG processes the data to prepare it for further analysis.  

---

### Prerequisites  
- **Apache Airflow** installed on the local environment.  
- Python data-processing libraries such as `pandas`, `scikit-learn`.  
- Google Cloud account to save the split datasets in Google Sheets or another cloud location.  

---

### **DAG 1: Data Download and Splitting**  
*(Maximum 10 Points)*  

**Objective:** Create a DAG that:  
1. Downloads a dataset (e.g., from a link or local file path).  
2. Saves datasets to separate Google Sheets or cloud locations (e.g., "Training Dataset" and "Fine-Tuning Dataset").  

#### Steps to Complete  

1. **Data Download Operator (2 points)**  
   - Create a task to download data from a specified source (public source). 

2. **Data Upload to Google Sheets Operator (4 points)**  
   - Upload both datasets (training and fine-tuning) to separate Google Sheets.  
   - Set up OAuth 2.0 authentication or use a service account to save data in Google Sheets.  
   - **Tip**: You can use the `gspread` library or another Python library that works conveniently with Google Sheets.  

---

### **DAG 2: Data Processing**  
*(Maximum 10 Points)*  

**Objective:** Create a second DAG to process data from Google Sheets. Processing steps include:  
1. Cleaning data—handling missing values or processing them appropriately.  
2. Standardizing and normalizing data.  

#### Steps to Complete  

1. **Data Download Operator (2 points)**  
   - Create a task to retrieve the training dataset stored in Google Sheets in DAG 1.  

2. **Data Cleaning Operator (2 points)**  
   - Identify and handle missing values (either remove or process them).  
   - Additionally, check for and remove duplicates if necessary.  

3. **Data Standardization and Normalization Operator (4 points)**  
   - **Standardization**: Scale feature values.  
   - **Normalization**: Rescale feature values to numerical ranges.  
   - **Tip**: Use `StandardScaler` and `MinMaxScaler` from the `scikit-learn` library.  

4. **Data Upload Operator (2 points)**  
   - Save the cleaned and processed dataset back to the cloud or Google Sheets.  

---

### **Additional Information**  

#### Documentation  
- Ensure each DAG is described with comments, and the workflow steps are documented to allow reviewers to understand the approach.  

#### Testing  
- Verify that both DAGs are correctly configured and execute without errors in Airflow.  

---

### **Deliverables**  
- Provide a link to your DAGs.  
- Include screenshots demonstrating the successful execution of both DAGs.  

**Good Luck!**
