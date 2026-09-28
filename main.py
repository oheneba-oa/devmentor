import ollama

from config import APP_NAME, MODEL
from prompts import SYSTEM_PROMPT


# Store the system prompt and conversation history.
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]


def ask_llm(question):
    """Send the conversation to Ollama and return the assistant response."""

    messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    try:
        response = ollama.chat(
            model=MODEL,
            messages=messages
        )

        answer = response["message"]["content"]

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer

    except Exception as error:
        # Remove the unanswered user message if the request fails.
        messages.pop()

        return f"Unable to get a response from Ollama. Error: {error}"


def reset_conversation():
    """Clear the conversation while keeping the system prompt."""

    global messages

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("Conversation reset.")


def display_history():
    """Display user and assistant messages without the system prompt."""

    conversation = messages[1:]

    if not conversation:
        print("No conversation history.")
        return

    for number, message in enumerate(conversation, start=1):
        role = message["role"].upper()
        content = message["content"]

        print(f"{number}. {role}: {content}\n")


def main():
    """Run the DevMentor command-line application."""

    print("=" * 50)
    print(f"{APP_NAME} AI Assistant")
    print("=" * 50)
    print("Commands: /history | /reset | /exit\n")

    while True:
        question = input("You: ").strip()

        if not question:
            print("Please enter a question.")
            continue

        if question.lower() in ["/exit", "exit", "/quit", "quit"]:
            print("Goodbye!")
            break

        elif question == "/reset":
            reset_conversation()
            continue

        elif question == "/history":
            display_history()
            continue

        answer = ask_llm(question)

        print(f"\n{APP_NAME}:")
        print(answer)
        print()


if __name__ == "__main__":
    main()