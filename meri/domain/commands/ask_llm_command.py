from meri.domain.command_context import CommandContext


def ask_llm_command(context: CommandContext, user_prompt: str) -> str:
    return context.llm.ask(user_prompt)
