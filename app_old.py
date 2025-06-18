import gradio as gr
import joblib
import numpy as np
import os
from PIL import Image 

# --- 1. Load the Pre-Trained Model ---
# This script assumes 'model.joblib' exists because you've run train.py
MODEL_PATH = "model.joblib"
IMAGE_PATH = "engine.jpg"
model = None

try:
    model = joblib.load(MODEL_PATH)
    print("Model 'model.joblib' loaded successfully.")
except FileNotFoundError:
    print(f"ERROR: Model file not found at '{MODEL_PATH}'.")
    print("Please run 'python train.py' in your terminal first to create the model file.")

# --- 2. Define Feature Names ---
# This list must be in the exact same order as the data your model was trained on.
feature_names = [
    'time_in_cycles', 'setting_1', 'setting_2', 's_1', 's_2', 's_3', 's_4', 's_5', 
    's_6', 's_7', 's_8', 's_9', 's_10', 's_11', 's_12', 's_13', 's_14', 's_15', 
    's_16', 's_17', 's_18', 's_19', 's_20', 's_21'
]

# --- 3. Create the Prediction Function ---
def predict_rul(*args):
    """
    Takes all 24 slider/number inputs as arguments, arranges them into the
    correct format, and returns the model's RUL prediction.
    """
    # First, check if the model was loaded successfully.
    if model is None:
        return "Model not loaded. Please run 'python train.py' and restart the app."

    # Convert the input arguments into a NumPy array for the model
    input_data = np.array(args).reshape(1, -1)
    
    # Make the prediction
    prediction = model.predict(input_data)
    
    # The model returns an array, so we get the first (and only) element
    final_prediction = prediction[0]
    
    return f"{round(final_prediction, 2)} cycles remaining"

# --- 4. Build the Gradio Interface ---
# We use a Gradio "Blocks" layout for more control over the UI.
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# Turbofan Engine Predictive Maintenance")
    gr.Markdown("Enter the engine's current sensor readings to predict its Remaining Useful Life (RUL). This demo uses a trained Linear Regression model.")
    
    with gr.Row():
        # Column for Inputs
        with gr.Column(scale=1):
            gr.Markdown("### Engine Parameters & Sensor Readings")
            # Create a list to hold all our input components
            inputs = []
            for name in feature_names:
                # Use a slider for each input for easy interaction
                inputs.append(gr.Slider(minimum=0, maximum=1000, label=name, value=50))
        
        # Column for Image and Output
        with gr.Column(scale=1):
            # Using a reliable placeholder image link.
            gr.Image(
                "engine.jpg", 
                label="Turbofan Engine"
            )
            
            gr.Markdown("### Prediction Result")
            # Create the output textbox
            outputs = gr.Textbox(label="Predicted Remaining Useful Life (RUL)")

    # Create the button to trigger the prediction
    predict_btn = gr.Button("Predict RUL", variant="primary")
    
    # Connect the button's "click" event to our prediction function
    predict_btn.click(
        fn=predict_rul,
        inputs=inputs,
        outputs=outputs
    )

# --- 5. Launch the App ---
if __name__ == "__main__":
    demo.launch()
