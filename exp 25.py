import openai_secret_manager

assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

import openai
openai.api_key = secrets["api_key"]
model_engine = "text-davinci-002"
prompt = "Once upon a time"
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)
text = response.choices[0].text
print(text)
