
# 🌱 Nutribench: Multilingual Nutrition Benchmark for Fairness and Model Evaluation

Nutribench is an open-source benchmark for analyzing **multilingual nutrition understanding** in large language models (LLMs).  
It provides structured datasets, analysis tools, and reproducible pipelines to evaluate **model fairness**, **translation consistency**, and **reasoning accuracy** across languages.

---

## 🧩 Project Structure
```markdown
├── language_outputs/ # Model-generated outputs in multiple languages
├── nutribench_100_queries.csv # Benchmark queries for evaluation
├── data_loader.py # Loads and preprocesses nutrition benchmark data
├── analysis_functions.py # Statistical and fairness analysis functions
├── run_analysis.py # Main entry point for running benchmark analysis
├── README.md # Documentation and usage guide
```

## 🚀 Quick Start

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/nutribench.git
cd nutribench
```

### 2️⃣ Install Dependencies

If you have a requirements.txt, install dependencies with:
```bash
pip install -r requirements.txt
```

Otherwise, you can manually install the main dependencies:
```bash
pip install pandas numpy matplotlib seaborn
```

### 3️⃣ Run the Analysis

Execute the main script to start a benchmark run:
```bash
python run_analysis.py
```

This will:

-- Load queries from ``` nutribench_100_queries.csv ```

-- Process multilingual outputs from ```language_outputs/```

--Compute metrics such as:

- **Cross-lingual accuracy and consistency**

- **Translation bias**

- **Nutritional reasoning fairness indicators**

- **Export results to CSV or visualization plots**

### 🧠 Modules Overview
🔹 ```data_loader.py```

Handles:

- **Reading and cleaning nutrition queries**

- **Loading multilingual model outputs**

- **Structuring data for cross-lingual comparison**

🔹 ```analysis_functions.py```

Implements:

- **Bias and fairness analysis metrics**

- **Statistical summaries (mean, std, correlations)**

- **Visualization utilities (bar charts, confusion matrices, heatmaps)**

🔹 ```run_analysis.py```

Coordinates the full workflow:

- **Loads dataset**

- **Calls analysis functions**

- **Saves evaluation results and figures**

## 📊 Dataset: `nutribench_100_queries.csv`

This dataset contains 100 multilingual nutrition-related prompts covering:

- **Food identification and calorie estimation**
- **Ingredient translation**
- **Cultural dietary reasoning**
- **Health and nutrition comparisons**

### Example preview:

| id | language | query | expected_category |
|----|-----------|--------|------------------|
| 1  | en | How many calories are in 100g of rice? | calorie_estimation |
| 2  | zh | 100克米饭有多少卡路里？ | calorie_estimation |
| 3  | es | ¿Cuántas calorías hay en 100 g de arroz? | calorie_estimation |


