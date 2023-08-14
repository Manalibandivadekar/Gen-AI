import os
import openai
from config import apikey

openai.api_key = apikey

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Write a resignation email to my boss ?"
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

'''
{
  "id": "chatcmpl-7lrHcdbO5dv09pxzvC0d8b2eyCziL",
  "object": "chat.completion",
  "created": 1691640592,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Subject: Resignation Letter\n\nDear [Boss's Name],\n\nI hope this email finds you well. I am writing to formally resign from my position at [Company Name], effective [last working day, typically two weeks from the date of the email].\n\nI have thoroughly enjoyed my time working at [Company Name], and I want to express my gratitude for the opportunities and experiences that I have gained during my tenure here. The knowledge and skills I have acquired have been invaluable to my professional growth.\n\nAfter careful consideration and reflection, I have decided to move on to pursue new challenges and opportunities that align more closely with my long-term career goals. While this was not an easy decision to make, I believe it is the right one for my personal and professional development.\n\nI am committed to ensuring a smooth transition in my departure. Over the next two weeks, I will do everything within my capacity to complete any pending tasks or projects and provide necessary handover documentation to my successor. However, please do not hesitate to let me know if there is anything specific you would like me to prioritize during this transition period.\n\nI would like to extend my sincere gratitude to you for your guidance, support, and mentorship throughout my time at [Company Name]. Working under your leadership has been an incredible experience"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 19,
    "completion_tokens": 256,
    "total_tokens": 275
  }
}
'''.