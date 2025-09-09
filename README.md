# 🍃 Potato Leaf Plant Disease Prediction

A deep learning–powered web app for detecting diseases in potato leaves.

---

## 📌 Overview

This project provides an end-to-end solution for identifying potato leaf diseases using image classification.  
It includes:
- A **Jupyter Notebook** for training and evaluating the model
- A **Flask app** for serving predictions
- A pre-trained model (`model.h5`)
- Example datasets and images for testing

---

## 📂 Project Structure

├── dataset2/ # Training/testing dataset
├── image/ # Sample images for demo
├── app.py # Flask web app for prediction
├── model.h5 # Trained CNN model
├── potato_disease_classification.ipynb # Training & evaluation notebook
├── requirements.txt # Python dependencies
└── .gitignore # Ignored files


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
pip install -r requirements.txt


3.Run the Streamlit app:
python app.py

4.Navigate to http://localhost:8501

🧠 How It Works:

1.Model Training (potato_disease_classification.ipynb)
2.Preprocesses dataset (dataset2/)
3.Builds a CNN for classifying potato diseases
4.Trains & evaluates performance
5.Exports model as model.h5

🔹 Prediction (app.py)

1.Loads the trained model
2.Accepts uploaded images
3.Outputs disease class & confidence score
4.Get AI-based suggestions based on the disease class identified that aims to cure the disease class reported.

🖼️ Usage
Train Model
jupyter notebook potato_disease_classification.ipynb

Run Prediction
python app.py


Upload an image and get instant predictions!

🤝 Contributing

Contributions are welcome!
Ideas for improvements:
Add more plant diseases
Improve the Streamlit UI
Integrate cloud deployment (Docker, Heroku, Render, etc.)
Enhance model accuracy with transfer learning

📜 License
This project currently has no license. Consider adding an open-source license (e.g., MIT, Apache 2.0).

🙏 Acknowledgements
TensorFlow/Keras for deep learning
Streamlit for web deployment

Datasets like PlantVillage for training data

