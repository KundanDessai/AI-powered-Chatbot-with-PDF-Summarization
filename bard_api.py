import google.generativeai as genai

# Use your Bard API key
genai.configure(api_key=" ")

def ask_bard(prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-pro")  # Correct API model
        response = model.generate_content(prompt)
        return response.text  # Get chatbot response
    except Exception as e:
        return f"Error: {str(e)}"
