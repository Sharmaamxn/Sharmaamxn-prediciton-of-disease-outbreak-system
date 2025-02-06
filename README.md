# 🏥 Prediction of Disease Outbreak System  

This project is a **machine learning-based disease prediction system** that predicts the likelihood of **diabetes, heart disease, and Parkinson's disease** based on medical input data. It leverages **preprocessed datasets, optimized models, and a Streamlit-based frontend** for an interactive user experience.  

## 📌 Features  
✅ **Preprocessed datasets** for accurate and efficient predictions  
✅ **Optimized machine learning models** tailored for each disease  
✅ **Streamlit-based frontend** for easy interaction  
✅ **Trained models deployed using Pickle** for fast inference  
✅ **User-friendly interface** to input medical data and get real-time results  

## 📂 Project Structure  
```
📁 Prediction-of-Disease-Outbreak
│-- 📂 datasets/              # Preprocessed datasets
│   │-- diabetes.csv
│   │-- heart.csv
│   │-- parkinsons.csv
│-- 📂 training_models/       # Trained models saved as pickle files, ML training scripts and utilities
│   │-- diabetes.ipynb        # Data preprocessing & model training for Diabetes
│   │-- diabetes_model.sav    # Trained Diabetes model (Pickle format)
│   │-- heart.ipynb           # Data preprocessing & model training for Heart Disease
│   │-- heart_model.sav       # Trained Heart Disease model
│   │-- parkinsons.ipynb      # Data preprocessing & model training for Parkinson’s
│   │-- parkinsons_model.sav  # Trained Parkinson’s model
│-- web.py                    # Streamlit-based frontend (Main application)
│-- requirements.txt          # Dependencies
│-- README.md                 # Project documentation
```

## ⚙️ Models Used  
### 1️⃣ **Diabetes Prediction**  
- **Dataset Features:** Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, DiabetesPedigreeFunction, Age, Outcome  
- **Final Model:** **SVM (Support Vector Machine)** trained on **undersampled data** for better recall and precision.  

### 2️⃣ **Heart Disease Prediction**  
- **Dataset Features:** Age, Sex, CP, Trestbps, Chol, FBS, Restecg, Thalach, Exang, Oldpeak, Slope, CA, Thal, Target  
- **Final Model:** **SVM (Support Vector Machine)** trained on **oversampled data** for better recall and precision.    

### 3️⃣ **Parkinson’s Disease Prediction**  
- **Dataset Features:** Multiple vocal biomarkers like MDVP:Fo(Hz), MDVP:Jitter(%), Shimmer:APQ5, HNR, PPE, etc.  
- **Final Model:** **Random Forest** trained on **oversampled data** for better recall and precision.   

## 🎨 Frontend Implementation  
The **Streamlit-based frontend** allows users to:  
🔹 Input medical parameters for each disease category  
🔹 Load trained models from pickle files  
🔹 Get real-time disease predictions with an intuitive UI  

## 🚀 How to Run  
1️⃣ **Clone the Repository:**  
```bash
git clone https://github.com/your-username/Prediction-of-Disease-Outbreak.git
cd Prediction-of-Disease-Outbreak
```  

2️⃣ **Install Dependencies:**  
```bash
pip install -r requirements.txt
```  

3️⃣ **Run the Streamlit App:**  
```bash
streamlit run frontend/app.py
```  

## 📜 License  
This project is open-source and available under the **MIT License**.  

## 🤝 Contributing  
Contributions are welcome! Feel free to open an issue or submit a pull request.  

---

Let me know if you want any refinements! 🚀
