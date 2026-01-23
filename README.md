# 🫃🏻 Obesity Detector 🔍

A **Streamlit web app** that predicts the obesity level of a person using a trained **Deep Learning model**.  
This project leverages personal health metrics (age, gender, height, weight, BMI, and physical activity level) to estimate whether an individual is **Normal Weight, Underweight, Overweight, or Obese**, providing clear results and visual feedback.

---

## ✨ Features
- 📊 Interactive UI built with **Streamlit**
- 🧠 Deep Learning model trained on **obesity dataset**
- 🔍 Prediction outputs:
  - **Normal Weight / Underweight / Overweight / Obese**
  - **Visual emoji feedback**
  - **Confidence from model prediction**
- 📈 TensorFlow/Keras-based classification
- 🧾 Input summary for transparency
- 🛡️ Educational tool (not a substitute for medical advice)

---

## 🛠️ Tech Stack
- **Python 3.8+**
- **Streamlit** – UI framework
- **TensorFlow / Keras** – Deep Learning model
- **Pandas / NumPy** – Data handling
- **CSV Dataset** – Obesity data (age, gender, height, weight, BMI, activity level)

---

## 📂 Project Structure
```
obesity-detector/
│── model/
│   └── model.keras                      # Trained DL model
│── dataset/
│   └── obesity_data.csv                # Dataset with features
│── images/
│   └── logo.png                         # App logo
│── app.py                               # Streamlit app
│── requirements.txt                     # Dependencies
│── README.md                            # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
```bash
git clone https://github.com/your-username/obesity-detector.git
cd obesity-detector
```

2. **Create a virtual environment**
```
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. **Install dependencies**
```
pip install -r requirements.txt
```

4. **Run the app**
```
streamlit run app.py
```

---

## 📊 Usage
- Launch the app in your browser (default: http://localhost:8501).
- Enter personal details:
```
- Age, Gender, Height, Weight, BMI, Physical Activity Level
```
- Click Predict Obesity Level.
- View:
```
- Prediction result (Normal / Underweight / Overweight / Obese)
- Emoji + message feedback
- Input summary
```
---

## 🧠 Model Information
- Algorithm: Deep Learning (TensorFlow/Keras)
- Training Dataset: Obesity dataset (CSV)
- Features: Age, Gender, Height, Weight, BMI, Physical Activity Level
- Accuracy: Depends on dataset and training configuration

---

## ⚠️ Disclaimer
- This project is for educational purposes only.
- It is not a substitute for professional medical advice, diagnosis, or treatment.
- Always consult a qualified healthcare provider for medical concerns.

---

## 🤝 Contributing
- Contributions are welcome!
- Fork the repo
- Create a feature branch (feature/new-ui)
- Commit changes
- Open a Pull Request

---

## 📜 License
- This project is licensed under the MIT License – feel free to use and modify.








