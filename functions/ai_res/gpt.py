import openai
openai.api_key = "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"

def gpt_res(prompt):
    response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 4000,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    return response["choices"][0]["text"]