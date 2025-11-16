import gradio as gr

def bmi_calculator(weight, height):
    # Check for zero height to avoid errors
    if height == 0:
        return "Height cannot be zero."
    
    # Calculate BMI: weight (kg) / height (m)^2
    bmi = weight / (height ** 2)
    
    # Determine category
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 25 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obesity"
        
    return f"Your BMI is {bmi:.2f} ({status})"

# Create the interface
interface = gr.Interface(
    fn=bmi_calculator,
    inputs=[
        gr.Number(label="Weight (kg)"),
        gr.Number(label="Height (meters)")
    ],
    outputs="text",
    title="Simple BMI Calculator",
    description="Enter your weight in kilograms and height in meters."
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
