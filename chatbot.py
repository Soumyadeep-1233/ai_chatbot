# chatbot.py
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace or use dotenv

def get_bot_response(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content.strip()
