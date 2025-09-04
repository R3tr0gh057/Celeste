import ollama

def get_ai_response(prompt, model="dolphin-mistral"):
    print(f"sending prompt to {model}: {prompt}")
    try:
        response = ollama.chat(
            model=model,
            messages=[{'role':'user', 'content':prompt}]
        )
        return response['message']['content'].strip()
    
    except Exception as e:
        error_message = f"Error connecting to {model}: {e}"
        print (error_message)
        return error_message