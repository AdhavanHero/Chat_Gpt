# -*- coding: utf-8 -*-
"""chat Gpt Movie Recommendation.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dRa_x_DvaVFh-Ry9jXlG0l_-uKBMZE_2
"""





import openai
# Set up the OpenAI API client
openai.api_key = "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"


# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = input("Which genre movies can i recommend in list?\n")+"movies"

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    top_p=1,
    stop=None,
    temperature=0.9,
)

response = completion.choices[0].text
print(response)



