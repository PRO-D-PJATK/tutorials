# Tutor2

Work in the same repository just change the name from tutor to tutor2 !!!

### Exercise: Data Cleaning and Standardization for Your Future Thesis Project

In this exercise, you will be tasked with selecting a database that is related to your future thesis project. You will clean, preprocess, and standardize this data in preparation for the type of analysis or modeling you plan to do in your diploma project. The exercise is split into two main tasks, each worth 20 points, focusing on database work, code quality, and Git usage.

### General Expectations:

Before diving into the tasks, here are five general expectations for this exercise:

1. **Database Selection**: Choose a dataset that aligns with the subject of your future diploma thesis. The data source should be large enough to require cleaning but manageable for the scope of this assignment.
2. **Data Cleaning**: Implement various data cleaning methods such as handling missing values, correcting data types, removing duplicates, and addressing outliers.
3. **Data Standardization**: Standardize and normalize the data where necessary. This might involve converting date formats, standardizing categorical variables, or scaling numerical data.
4. **Reproducibility**: The code you write should be reproducible on any local machine. Ensure that all paths and configurations are customizable through a config file, which is included in `.gitignore`.
5. **Version Control**: All changes should be well-documented in Git. Use meaningful commit messages, branching, and pull requests to organize your work.

### Task 1: Setting Up and Cleaning the Database (20 Points)

#### 1. Git Repository Setup (5 Points):
   - **Create a Git Repository**: Set up a new repository on GitHub with a clear and descriptive `README.md`.
   - **Branching**: Use Git branches effectively. Main work should be done in a feature branch, and pull requests should be created and merged into the `main` branch once each part of the task is complete.
   - **.gitignore**: Add a `.gitignore` file that excludes the database and any sensitive configuration files (e.g., `.env` or `config.json` for local paths, API keys, or credentials).
   - **Commits and Pull Requests**: Make sure to document your progress with meaningful commit messages and well-written pull requests, involving at least one peer from the class for a review.
   - **README Documentation**: The `README.md` should clearly describe the project’s goal, database source, and how to set up the environment locally.

#### 2. Database Usage (5 Points):
   - **Database Selection**: Choose a database (e.g., MySQL, PostgreSQL, MongoDB, SQLite, etc.) that fits your thesis topic.
   - **Connecting to the Database**: Write a script that connects to the database of your choice. The credentials for the database (username, password, database name, etc.) should be stored in a separate configuration file, which is excluded from Git via `.gitignore`.
   - **Initial Data Load**: Load the dataset from a local or remote source and import it into your database.

#### 3. Data Cleaning (10 Points):
   - **Missing Data**: Identify and handle missing data appropriately (e.g., imputation, removal, or using default values).
   - **Outliers and Duplicates**: Implement methods to detect and handle outliers and remove duplicate entries.
   - **Data Type Correction**: Ensure that all columns have the correct data types (e.g., numerical, categorical, datetime).
   - **Documentation**: Document each cleaning step in the script with comments explaining the rationale behind your choices.
