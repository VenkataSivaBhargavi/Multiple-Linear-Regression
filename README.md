# Multiple-Linear-Regression
📌 Project Overview
This project uses Multiple Linear Regression, a supervised Machine Learning algorithm, to predict a startup's profit based on its research and development spending, administration spending, marketing spending, and state.

The project is implemented in Python using Pandas, NumPy, Matplotlib, and Scikit-learn. The trained model is also saved and reloaded using Pickle.

🎯 Objectives
- Load and explore the startup dataset.
- Prepare the input features and target variable.
- Convert the categorical State column into numeric values.
- Split the data into training and testing sets.
- Train a Multiple Linear Regression model.
- Evaluate model performance using R² score and Root Mean Squared Error (RMSE).
- Save the trained model as a Pickle file.

📊 Dataset Description
The notebook loads 50_Startups.csv, a dataset containing information about startup spending and profit.
Column	Description
R&D Spend	Amount spent on research and development
Administration	Amount spent on administration
Marketing Spend	Amount spent on marketing
State	State associated with the startup
Profit	Target variable to predict


Feature Preparation
The notebook converts the categorical State values into numeric values:
- New York → 0
- California → 1
- Florida → 2
The independent variables (X) are all columns except Profit. The dependent variable (y) is Profit.
Note: This numeric mapping treats the states as numbers. For a more robust categorical-data approach, consider one-hot encoding the State column.


🧠 Machine Learning Algorithm
Multiple Linear Regression
Multiple Linear Regression is a supervised learning algorithm used to predict a continuous target variable using two or more input features.

In this project, the model predicts startup profit using:
- R&D Spend
- Administration
- Marketing Spend
- Encoded State
Regression Equation
The general equation is:
\[
Y = b_0 + b_1X_1 + b_2X_2 + b_3X_3 + b_4X_4
\]
Where:
- Y = Predicted profit
- b₀ = Intercept
- b₁, b₂, b₃, b₄ = Learned coefficients
- X₁ = R&D Spend
- X₂ = Administration
- X₃ = Marketing Spend
- X₄ = Encoded State
The model learns the coefficients and intercept from the training data.
⚙️ Model Training
The notebook uses Scikit-learn's LinearRegression model and splits the dataset into training and testing sets using test_size=0.2 and random_state=42.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

reg = LinearRegression()
reg.fit(X_train, y_train)


📈 Model Performance
The notebook reports the following results:
Metric	Result
Training R² Score	0.9537 (approximately 95.37%)
Testing R² Score	0.8990 (approximately 89.90%)
Training RMSE	8,930.03
Testing RMSE	9,043.31


These values are the outputs recorded in the notebook. Actual results may vary if the dataset, preprocessing, or train-test split changes.
R² Score
The R² score indicates how much variation in the target variable is explained by the model. A score closer to 1.0 generally indicates a better fit on the evaluated data.
Root Mean Squared Error (RMSE)
RMSE measures the typical scale of prediction errors in the target variable's units. Lower values generally indicate smaller prediction errors.


💾 Saving the Trained Model
The notebook saves the trained regression model to MLR_MODEL.pkl using Pickle:
import pickle

with open("MLR_MODEL.pkl", "wb") as file:
    pickle.dump(reg, file)
It then reloads the saved model:
with open("MLR_MODEL.pkl", "rb") as file:
    model = pickle.load(file)
Only load Pickle files from trusted sources.

🛠️ Technologies Used
- Python — programming language
- NumPy — numerical operations
- Pandas — dataset loading and manipulation
- Matplotlib — plotting library imported in the notebook
- Scikit-learn — data splitting, Linear Regression, and evaluation metrics
- Pickle — model serialization


📂 Project Structure
An example GitHub repository structure is:
Multiple-Linear-Regression/
├── README.md
├── MLR.ipynb
├── 50_Startups.csv
└── MLR_MODEL.pkl
Include the dataset and model file only if you are permitted to share them. The notebook currently reads the dataset from /content/50_Startups.csv, which is a common Google Colab path. If running locally, update the path to match where the CSV is stored.


🚀 How to Run
1. Clone or download the repository.
2. Install the required libraries:
   pip install numpy pandas matplotlib scikit-learn
3. Place 50_Startups.csv in the appropriate location and update the path in MLR.ipynb if needed.
4. Open MLR.ipynb in Jupyter Notebook, JupyterLab, or Google Colab.
5. Run the notebook cells in order to train and evaluate the model.
6. The notebook saves the trained model as MLR_MODEL.pkl.


🔮 Future Improvements
- Use one-hot encoding for the categorical State feature.
- Perform exploratory data analysis and visualize feature relationships.
- Compare model performance with other regression algorithms.
- Add cross-validation and residual analysis.
- Build a web application for interactive profit prediction.
- Add automated tests and a reproducible environment file.

  
⭐ Conclusion
This project demonstrates how Multiple Linear Regression can estimate startup profit from spending-related features and state information. It covers data preparation, model training, evaluation using R² and RMSE, and saving the trained model for later use.
