from openai_test import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a witch in love with demon."},
    {"role": "user", "content": "Ceate a poem that praise the demon you love"}
  ]
)

print(completion.choices[0].message)

# for i in completion.choices :
#     print(i)