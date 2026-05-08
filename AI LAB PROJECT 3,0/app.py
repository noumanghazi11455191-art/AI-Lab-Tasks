from flask import Flask, render_template, request
import pickle
import numpy as np
import os
import pandas as pd

app = Flask(__name__)

# Force absolute path for stability
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. LOAD DATA & CLEAN SYMPTOMS
training_data = pd.read_csv(os.path.join(BASE_DIR, 'Training.csv'))

# This line ensures we ONLY take the 132 symptoms. 
# We remove 'prognosis' and any 'Unnamed' columns created by extra commas in the CSV.
symptoms_list = [col for col in training_data.columns if col != 'prognosis' and 'Unnamed' not in col]

# 2. LOAD MODEL
model_path = os.path.join(BASE_DIR, 'final_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

# 3. KNOWLEDGE BASE (Ensure keys match prediction strings)
prescriptions = {
    "Fungal infection": "Use Clotrimazole Cream and keep the infected area dry.",
    "Allergy": "Take Cetirizine and avoid dust or pollen.",
    "Diabetes": "Maintain low sugar diet and consult an endocrinologist.",
    "Hypertension": "Reduce salt intake and monitor blood pressure regularly.",
    "Acne": "Wash face twice daily with a mild cleanser.",
    "Psoriasis": "Apply moisturizing creams and consult a dermatologist."
}

specialists = {
    "Fungal infection": {"type": "Dermatologist", "hospital": "Hameed Latif Hospital"},
    "Allergy": {"type": "Immunologist", "hospital": "Doctors Hospital"},
    "Diabetes": {"type": "Endocrinologist", "hospital": "Shaukat Khanum Hospital"},
    "Hypertension": {"type": "Cardiologist", "hospital": "Punjab Institute of Cardiology"},
    "Acne": {"type": "Dermatologist", "hospital": "Jinnah Hospital"},
    "Psoriasis": {"type": "Dermatologist", "hospital": "Services Hospital"}
}

@app.route('/')
def home():
    return render_template('index.html', symptoms=symptoms_list)

@app.route('/location')
def location():
    return render_template('location.html')

@app.route('/predict', methods=['POST'])
def predict():
    selected_symptoms = request.form.getlist('symptoms')
    
    # Initialize vector with the exact length the model expects (132)
    input_vector = np.zeros(len(symptoms_list))

    for symptom in selected_symptoms:
        if symptom in symptoms_list:
            index = symptoms_list.index(symptom)
            input_vector[index] = 1

    # Reshape for a single prediction
    prediction = model.predict([input_vector])[0]
    
    # Clean string
    clean_prediction = prediction.strip()

    prescription = prescriptions.get(clean_prediction, "Please consult a medical specialist.")
    doctor_info = specialists.get(clean_prediction, {
        "type": "General Physician",
        "hospital": "City Hospital"
    })

    return render_template(
        'result.html',
        prediction=clean_prediction,
        prescription=prescription,
        doctor=doctor_info
    )

if __name__ == '__main__':
    app.run(debug=True)