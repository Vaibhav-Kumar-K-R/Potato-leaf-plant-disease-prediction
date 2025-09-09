# 🍃 Potato Leaf Plant Disease Prediction

A deep learning–powered web app for detecting diseases in potato leaves.

---

## 📌 Overview

This project provides an end-to-end solution for identifying potato leaf diseases using image classification.  
It includes:
- A **Jupyter Notebook** for training and evaluating the model
- A **Streamlit app** for serving predictions
- A pre-trained model (`model.h5`)
- Example datasets and images for testing

---

## 📂 Project Structure

├── dataset2/ # Training/testing dataset <br>
├── image/ # Sample images for demo <br>
├── app.py # Flask web app for prediction <br>
├── model.h5 # Trained CNN model <br>
├── potato_disease_classification.ipynb # Training & evaluation notebook <br>
├── requirements.txt # Python dependencies <br>
└── .gitignore # Ignored files <br>


---

## 🚀 Getting Started

### ✅ Prerequisites
- Python 3.10 or higher
- `pip` package manager

### ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vaibhav-Kumar-K-R/Potato-leaf-plant-disease-prediction.git
   cd Potato-leaf-plant-disease-prediction
   
2.Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3.Run the Streamlit app:
   ```
   python app.py
   ```

4.Navigate to the browser
   ```
   Open the browser and navigate to http://localhost:8501
   ```
🧠 How It Works:

1.Model Training (potato_disease_classification.ipynb)<br>
2.Preprocesses dataset (dataset2/) <br>
3.Builds a CNN for classifying potato diseases <br>
4.Trains & evaluates performance <br>
5.Exports model as model.h5 <br>

🔹 Prediction Steps (app.py)

1.Loads the trained model<br>
2.Accepts uploaded images <br>
3.Outputs disease class & confidence score <br>
4.Get AI-based suggestions based on the disease class identified that aims to cure the disease class reported. <br>

##Results

1. <img width="615" height="800" alt="image" src="https://github.com/user-attachments/assets/cda5e6d2-768a-42a9-84ed-12a207edc08b" />

2. <img width="615" height="800" alt="image" src="https://github.com/user-attachments/assets/22f03f2c-fd93-4e84-97c4-ebf3344cfe94" />

3. <img width="615" height="800" alt="image" src="https://github.com/user-attachments/assets/306b5400-2a94-44d8-91cd-5476b13c76d3" />




🖼️ Usage
1.Train Model
```
jupyter notebook potato_disease_classification.ipynb 

```

2.Run Prediction 
```
python app.py
```

Upload an image and get instant predictions!

🤝 Contributing

Contributions are welcome!
Ideas for improvements:
Add more plant diseases
Improve the Streamlit UI
Integrate cloud deployment (Docker, Heroku, Render, etc.)

Datasets - PlantVillage for training data



