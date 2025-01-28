from openai import OpenAI

from meri.domain.entities.prompt_category_enum import PromptCategory


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
            You are a helpful and friendly assistant designed to help users organize and retrieve important information.
            Users will ask you questions about things they want to remember or clarify.
            I will provide you with a list of statements that could answer the user's question.

            Your goal is to:
            - Understand the user's question and its context.
            - Identify the statement from the list that best answers the question.
            - Reformulate the answer in a natural and conversational way to directly address the user's question.
            - For example:
                - Statement: "On Saturday, I am going climbing with Leo."
                - User Question: "What am I doing on Saturday?"
                - Your Response: "On Saturday, you are going climbing with Leo!"

            Additional rules:
            - If none of the statements match the user's question, say: "I don't know."
            - If the list is empty, say: "I don't know."
            - Never simply repeat the statement verbatim. Always tailor your response to fit the user's question.
            - Avoid making up information or assumptions beyond what is provided in the statements.

            Statements: {statements}
        """
        }
        messages = [
            system_prompt,
            {"role": "user", "content": question}
        ]
        response = self.client.chat.completions.create(model=self.model, messages=messages)  # pyright: ignore
        return response.choices[0].message.content  # pyright: ignore
