from openai import OpenAI

import constants

client = OpenAI()
client.api_key = constants.api_key
def dalle(prompt):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    return image_url
def chatGPT(systemPrompt,prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": systemPrompt
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

def generateVisuals(prompt):
    return chatGPT(constants.PROMPT_VISUAL,prompt)

def generateSheet(prompt):
    return chatGPT(constants.PROMPT_SHEET,prompt)