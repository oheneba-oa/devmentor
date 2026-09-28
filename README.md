## Prompt Engineering Experiment

### 1. Which prompt was most useful, and why?

Prompt C was the most useful overall because it produced clear and focused answers without becoming unnecessarily long.

### 2. What differences did you observe?

Prompt A produced long and detailed responses.
Prompt B was more conversational and learner-focused.
Prompt C was more concise and followed the response rules more closely.

### 3. Did more instructions always help?

No. More instructions improved consistency, but too many broad instructions could still lead to long responses.

### 4. Which rules changed behaviour the most?

The rules about keeping introductions short, explaining before showing code, using practical examples, and avoiding unnecessary detail had the clearest effect.

### 5. What happened when a rule was vague?

Vague instructions produced less predictable responses. When asked "Show me an example," the three prompts interpreted the request differently.


## Memory Investigation

The memory experiment showed that DevMentor does not permanently remember previous information by itself.

When the message "My favorite programming language is Python" was still stored in the conversation history, DevMentor correctly answered that my favorite language was Python.

After I removed that earlier message from the `messages` list and asked the same question again, DevMentor said it did not know my favorite programming language.

This shows that the apparent memory comes from the application state. The Python program stores the conversation in the `messages` list and sends that message history back to the model as context on each request. If the relevant message is removed from the history, the model no longer has access to that information.