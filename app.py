import gradio as gr
import joblib
import numpy as np
import os
import json

# --- 1. Load the Pre-Trained Model ---
# This script assumes 'model.joblib' exists because you've run train.py
MODEL_PATH = "model.joblib"
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
    Takes all 24 number inputs as arguments, arranges them into the
    correct format, and returns the model's RUL prediction.
    """
    if model is None:
        return "Model not loaded. Please run 'python train.py' and restart the app."

    # Ensure all inputs are converted to float, handling None or empty strings
    processed_args = [float(arg) if arg is not None and arg != '' else 0.0 for arg in args]
    
    input_data = np.array(processed_args).reshape(1, -1)
    prediction = model.predict(input_data)
    final_prediction = prediction[0]
    
    return f"{round(final_prediction, 2)} cycles remaining"


# --- 4. Build the Gradio Interface ---
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# North Star 1.0")
    gr.Markdown(
        """
        Predictive maintenance machine learning system, forecasting faults and remaining useful life (RUL).

        Demo parameters trained on aircraft turbo fan engine dataset (NASA FD001 file). 

        Model automatically trains on dataset upon launch.

        """
    )

    
   # --- NEW: Video Display ---
# This component will display your video.
    gr.Gallery(
        value=["plane.jpg"],
        label="Customize easily for almost any machinery",
        columns=1, 
        object_fit="cover", 
        height="10"
    )
    
    gr.Markdown("### Enter Machine Parameters & Sensor Readings")
    
    # Create the user inputs in a grid
    inputs = []
    num_columns = 3
    for i in range(0, len(feature_names), num_columns):
        with gr.Row():
            for j in range(num_columns):
                if i + j < len(feature_names):
                    name = feature_names[i + j]
                    component = gr.Number(label=name, value=50.0)
                    inputs.append(component)
    
    # Place the prediction button below the inputs
    predict_btn = gr.Button("Predict RUL", variant="primary")

    gr.Markdown("### Prediction Result")
    # Create the output textbox below the button
    outputs = gr.Textbox(label="Predicted Remaining Useful Life (RUL)")
    
    # Connect the button's "click" event to our prediction function
    predict_btn.click(
        fn=predict_rul,
        inputs=inputs,
        outputs=outputs
    )

# --- 5. Launch the App ---
if __name__ == "__main__":
    demo.launch()