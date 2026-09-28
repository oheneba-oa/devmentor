# DevMentor

## Description

DevMentor is a local conversational AI assistant built with Python and Ollama.

It is designed to help junior developers understand programming concepts using clear explanations, practical examples, and simple language.

The application runs locally using `gemma4:latest` through Ollama. Conversation history is stored inside the Python application and is sent back to the model on each request to maintain context.

## Features

- Runs locally through Ollama
- Uses `gemma4:latest`
- Accepts dynamic user input
- Uses a custom system prompt
- Maintains multi-turn conversation history
- Supports `/history`
- Supports `/reset`
- Supports `/exit`
- Handles empty input
- Handles Ollama and invalid-model errors without crashing
- Uses separate configuration and prompt files
- Keeps conversation state inside the Python application

## Architecture

DevMentor follows this flow:

```text
User
  ↓
Python Application
  ↓
Conversation History
  ↓
Ollama API
  ↓
Local Gemma Model
  ↓
Response
  ↓
Python Application
  ↓
User
```

The Python application manages the interaction between the user and the local language model.

The local Gemma model runs through Ollama on the user's machine.

Conversation state is stored inside the Python application using the `messages` list.

The Ollama API acts as the communication layer between the Python application and the local model.

On each request, the system prompt, relevant conversation history, and latest user message are sent to the model.

After the model responds, the assistant's response is added to the `messages` list so it becomes part of the context for the next request.

## Project Structure

```text
devmentor/
├── main.py
├── config.py
├── prompts.py
├── requirements.txt
├── README.md
└── main.ipynb
```

`main.py` contains the main application logic, conversation controls, Ollama calls, error handling, and interactive chat loop.

`config.py` contains application settings such as the application name and selected model.

`prompts.py` contains the DevMentor system prompt.

`requirements.txt` contains the Python packages required to run the project.

`main.ipynb` contains the step-by-step development process and experiments carried out while building the application.

## Installation

Create a Conda environment:

```bash
conda create -n devmentor_env python=3.11
```

Activate the environment:

```bash
conda activate devmentor_env
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Make sure Ollama is installed and running.

Check the locally installed models:

```bash
ollama list
```

The model used for this project is:

```text
gemma4:latest
```

## Running the Application

Run the application from the project directory:

```bash
python main.py
```

The application will start and wait for user input.

Available commands:

```text
/history
/reset
/exit
```

`/history` displays the current conversation between the user and DevMentor.

`/reset` clears the conversation history while keeping the system prompt.

`/exit` ends the application cleanly.

## System Prompt Design

DevMentor uses a system prompt to define its role and behaviour.

The assistant is designed as a programming tutor for junior developers.

The system prompt instructs DevMentor to:

- Use simple and direct language
- Introduce technical terms clearly
- Give a short explanation before adding detail
- Use practical examples or analogies when useful
- Show code only when it helps understanding
- Avoid unnecessary complexity
- Keep most answers concise
- Admit when it is unsure instead of guessing
- Remain focused on programming and software development

## Prompt Engineering Experiment

Three different system prompts were tested using the same questions:

- Prompt A: Minimal
- Prompt B: Detailed
- Prompt C: Constrained

The same questions were used for all three prompts:

- Explain REST APIs.
- Explain recursion.
- What is dependency injection?
- Show me an example.

### 1. Which prompt was most useful, and why?

Prompt C was the most useful overall because it produced clear and focused answers without becoming unnecessarily long.

### 2. What differences did you observe?

Prompt A produced long and detailed responses.

Prompt B was more conversational and learner-focused.

Prompt C was more concise and followed the response rules more closely.

### 3. Did more instructions always help?

No. More instructions improved consistency, but too many broad instructions could still lead to long responses.

Prompt C performed better because its instructions were more specific and constrained.

### 4. Which rules changed behaviour the most?

The rules about keeping introductions short, explaining before showing code, using practical examples, and avoiding unnecessary detail had the clearest effect.

### 5. What happened when a rule was vague?

Vague instructions produced less predictable responses.

When asked:

```text
Show me an example.
```

the three prompts interpreted the request differently.

Prompt A gave several unrelated examples.

Prompt B recognised that the request was unclear and asked for more information.

Prompt C selected a simple programming topic and gave an example.

This showed that vague instructions can lead to different model behaviours.

## Memory Investigation

The memory experiment showed that DevMentor does not permanently remember previous information by itself.

When the message:

```text
My favorite programming language is Python.
```

was still stored in the conversation history, DevMentor correctly answered that my favorite programming language was Python.

After I removed that earlier message from the `messages` list and asked the same question again, DevMentor said it did not know my favorite programming language.

This shows that the apparent memory comes from the application state.

The Python program stores the conversation in the `messages` list and sends that message history back to the model as context on each request.

If the relevant message is removed from the history, the model no longer has access to that information.

## Challenge Questions

### 1. Why does the app send previous messages to the LLM?

The app sends previous messages so the model has the context needed to understand follow-up questions.

Without the earlier messages, each request would be treated as a new conversation.

### 2. What is the difference between system, user, and assistant messages?

The `system` message defines the assistant's role, behaviour, and instructions.

The `user` message contains what the user says or asks.

The `assistant` message contains the response generated by the model.

### 3. If you close Python and restart, why does the assistant forget?

The conversation history is stored in the running Python application.

When the program closes, that application state is lost because the messages are not permanently saved.

### 4. Is memory stored inside the LLM or inside the application?

The conversation memory is stored inside the application.

The Python program stores previous messages in the `messages` list and sends them to the model again when a new request is made.

### 5. What happens when the conversation becomes extremely long?

A very long conversation can exceed the model's context window.

The context window is the amount of information the model can process in a single request.

As the conversation grows, more tokens are used and the application may eventually need to manage the history.

Possible approaches include removing older messages or summarising older parts of the conversation while keeping the most relevant context.

### 6. Why is "You are helpful." a weak system prompt? How would you improve it?

It is weak because it does not clearly define the assistant's role, audience, explanation style, expected behaviour, or what it should do when it is unsure.

A stronger system prompt should clearly state who the assistant is, who it is helping, how it should explain concepts, how examples should be used, and how it should respond when it does not know something.

### 7. After the LLM replies, what should happen to messages before the next user turn, and why?

The assistant's response should be added to the conversation history.

This ensures that both the user's message and the assistant's response are available as context when the next user message is sent.

Without storing the assistant response, the model would not have the complete conversation needed to understand later follow-up questions.

## Conclusion

DevMentor demonstrates the main components of a conversational AI application without using high-level AI frameworks.

The project combines a system prompt, message history, application state, the Ollama API, and a local language model.

The prompt engineering experiment showed that system prompt design affects the style, length, and consistency of model responses.

The memory investigation also showed that conversation memory is controlled by the Python application rather than being permanently stored inside the language model.