# E-Commerce Product Recommendation Engine  
A scalable recommendation system built to enhance customer satisfaction by leveraging machine learning and distributed computing frameworks.

---

## Project Overview  
This project develops an **E-Commerce Product Recommendation Engine** capable of handling large-scale datasets to provide personalized recommendations. Using **PySpark** for distributed computing and comparing it with non-distributed implementations, the system demonstrates efficiency and accuracy for real-world e-commerce platforms.  

---

## Key Features  
- **Scalable Framework:** Handles large datasets with 7M+ user-product interactions.  
- **Advanced Machine Learning Models:** Implements collaborative filtering (KNN, SVD, SVD++, NMF) and linear regression.  
- **Comprehensive Comparisons:** Evaluates performance with and without PySpark, analyzing key metrics like precision, recall, F1 score, and execution time.  
- **Distributed Processing:** Utilizes **MapReduce** (mapper and reducer scripts) for data preprocessing.  

---

## Files Included  
### Reports  
- **IEEE Report:** [IEEE Format Report (PDF)](https://github.com/Jaffer74/E-Commerce-Product-Recommendation-Engine-Enhancing-Customer-Online-Shopping-Experience/blob/main/Reports/E%20Commerce%20Product%20Recommendation%20Engine_Report(IEEE).pdf)  
- **Overall Report:** [Detailed Project Report (PDF)](reports/ProjectReport_overall.pdf)  

### Codebase  
1. **PySpark Implementation:**  
   - `pyspark_model.ipynb`: Jupyter notebook with PySpark implementation for distributed processing.  
2. **Non-PySpark Implementation:**  
   - `non_pyspark_model.ipynb`: Jupyter notebook for the non-distributed approach.  
3. **MapReduce Scripts:**  
   - `mapper.py`: Mapper script for distributed processing.  
   - `reducer.py`: Reducer script for aggregating results.

### Dataset  
- `rating_electronics.csv`: Dataset containing 7M+ rows with user-product interactions (User ID, Product ID, Ratings, and Timestamps).  

---

## Project Structure  
```plaintext
├── data/               # Dataset and preprocessed files  
├── notebooks/          # Jupyter Notebooks (PySpark and non-PySpark implementations)  
├── mapreduce/          # Mapper and Reducer scripts for data processing  
├── reports/            # Project reports (IEEE and detailed report)  
├── results/            # Outputs, visualizations, and metrics comparisons  
├── README.md           # Project documentation  
```
## Dataset Description  
- **Source:** [Amazon Product Reviews Dataset](https://www.kaggle.com/datasets)  
- **Features:**
  - **User ID:** Unique identifier for each user.  
  - **Product ID:** Unique identifier for each product.  
  - **Ratings:** Numerical values (1-5) representing user preferences.  
  - **Timestamp:** Indicates when a rating was given.  

---

## Implementation Details  
1. **Data Preprocessing:**  
   - Cleaned missing values, removed duplicates, and encoded categorical variables.  
   - Normalized data to handle sparsity and ensure model compatibility.  

2. **Collaborative Filtering Models:**  
   - **Memory-Based:** KNN and KNN with Pearson Coefficient.  
   - **Model-Based:** SVD, SVD++, NMF, and Linear Regression.  

3. **Distributed Computing:**  
   - Utilized **PySpark** for scalable training and prediction.  
   - Integrated **MapReduce** (Mapper and Reducer) for efficient data processing.

---

## Results and Comparisons  
- **Key Metrics:** Precision, Recall, F1 Score, Accuracy, Execution Time.  
- **Comparison Results:** PySpark significantly reduced computation time while maintaining high prediction accuracy.  

### Access Full Reports  
- **IEEE Report:** [Download Here](reports/E_Commerce_Product_Recommendation_Engine_Report.pdf)  
- **Overall Report:** [Download Here](reports/ProjectReport_overall.pdf)  

### Access Code and Results  
- PySpark Implementation: [`pyspark_model.ipynb`](notebooks/pyspark_model.ipynb)  
- Non-PySpark Implementation: [`non_pyspark_model.ipynb`](notebooks/non_pyspark_model.ipynb)  
- Mapper and Reducer Scripts: [`mapper.py`](mapreduce/mapper.py), [`reducer.py`](mapreduce/reducer.py)  
- Dataset: [`rating_electronics.csv`](data/rating_electronics.csv)  

---

## Technologies Used  
- **Programming Language:** Python (v3.8+)  
- **Frameworks:** PySpark, Hadoop  
- **Libraries:** NumPy, Pandas, Scikit-learn  
- **Tools:** Jupyter Notebooks, Google Colab  

---

## How to Run  
1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/yourusername/ecommerce-recommendation-engine.git
   cd ecommerce-recommendation-engine
    ```
   
2. **Run MapReduce Scripts:**
    ```bash
    hadoop jar /path/to/hadoop-streaming.jar \
    -mapper mapreduce/mapper.py \
    -reducer mapreduce/reducer.py \
    -input data/rating_electronics.csv \
    -output data/output_results
    ```
3. **Run PySpark Model:**
   Open and run notebooks/pyspark_model.ipynb.

4. **Run Non-PySpark Model:**
   Open and run notebooks/non_pyspark_model.ipynb.

    
