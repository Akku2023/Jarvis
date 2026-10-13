
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {
            "role": "system",
            "content": "You are Jarvis, a helpful virtual assistant. Keep your answers concise and friendly."
        },
        {
            "role": "user",
            "content": "What is coding?"
        }
    ]
)

print("Jarvis:", response["message"]["content"])
