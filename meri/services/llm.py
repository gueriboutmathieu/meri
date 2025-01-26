from openai import OpenAI


system_prompt = {
    "role": "system",
    "content": "You are a loyal companion who helps people to stay organized and remember what truly matters."
}


class Llm:
    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=api_key)

    def ask(self, user_prompt: str) -> str:
        messages = [
            system_prompt,
            {"role": "user", "content": user_prompt}
        ]
        response = self.client.chat.completions.create(model=self.model, messages=messages)  # pyright: ignore
        return response.choices[0].message.content  # pyright: ignore
