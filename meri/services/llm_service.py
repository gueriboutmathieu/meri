from openai import OpenAI

from meri.domain.entities.prompt_category import PromptCategory


class LlmService:
    def __init__(self, api_key: str, model: str) -> None:
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key=api_key)

    def categorize(self, user_prompt: str) -> PromptCategory:
        """
        Categorize the user's prompt into predefined categories like 'question' or 'statement'.
        """
        system_prompt = {
            "role": "system",
            "content": (
                "You are a classifier. Your job is to determine if the following user input is a 'question' or a 'statement'."
                "Only respond with 'question' or 'statement', no explanations."
            )
        }

        messages = [
            system_prompt,
            {"role": "user", "content": user_prompt}
        ]
        response = self.client.chat.completions.create(model=self.model, messages=messages)  # pyright: ignore
        category = response.choices[0].message.content.strip().lower()  # pyright: ignore
        return PromptCategory(category)

    def ask_about_statements(self, question: str, statements: list[str]) -> str:
        system_prompt = {
            "role": "system",
            "content": f"""
                You are a helpful and kind assistant designed to help users stay organized and remember important information.
                Users will ask you questions about things they want to remember or clarify.
                I will provide you with a list of statements that could answer the user's question.
                Use this information to answer their questions clearly and politely.
                Choose the statement that best answers the user's question.
                If none of the statements match the user's question, say 'I don't know'.
                If the list is empty, say 'I don't know'.
                Never provide false information or make up answers.

                Statements: {statements}
            """
        }
        messages = [
            system_prompt,
            {"role": "user", "content": question}
        ]
        response = self.client.chat.completions.create(model=self.model, messages=messages)  # pyright: ignore
        return response.choices[0].message.content  # pyright: ignore
