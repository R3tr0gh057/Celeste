import ollama

def get_ai_response(prompt, model="dolphin-mistral"):
    # Ensure prompt is conversational and not point-based
    if "Respond in a natural, conversational way" not in prompt:
        prompt = (
            "You are Celeste, a friendly and helpful AI assistant. Respond in a natural, conversational way, avoid bullet points or numbered lists, and keep the tone engaging and human-like, it should be very short and concise as well, spanning no more than a few short sentences. Here is the user's message: " + prompt
        )
    print(f"sending prompt to {model}: {prompt}")
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role':'user', 'content':prompt}]
        )
        return response['message']['content'].strip()
    except Exception as e:
        error_message = f"Error connecting to {model}: {e}"
        print(error_message)
        return error_message
