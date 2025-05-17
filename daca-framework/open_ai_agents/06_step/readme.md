# 🛡️ Guardials Agent Framework

**Guardials** is a Python library designed to run in parallel with LLM-based agents, providing **input/output validation**, **feedback mechanisms**, and **streamlined agent control**. It acts as a trusted co-pilot for your AI agent by ensuring every interaction remains safe, reliable, and actionable.

This framework is built with **FastAPI** to expose a high-performance API interface, enabling real-time interaction and control. It is highly modular and designed to scale with your agent workflows.

---

## 🚀 Features

- 🔄 **Agent Loop Control**: Auto-manages conversation rounds with `MAX_TURN_VALUE`.
- ✅ **Validation**: Ensures safe and expected input/output for agents.
- 🧠 **Feedback System**: Injects Guardials' validation into agent response cycles.
- ⚡ **FastAPI Integration**: Quick and scalable API out of the box.
- 🧱 **Composable Architecture**: Plug-and-play components like `Runner`, `Training_block`, and more.
- 🧵 **Streaming & Syncing**: Real-time data handling with `Runner.stream` and `Runner.sync`.

---

## 📦 Installation

```bash
pip install guardials fastapi uvicorn
🧭 Project Structure
plaintext
Copy
Edit
guardials_agent/
├── main.py                  # FastAPI server entry point
├── guardials/               # Guardials integration
│   ├── validator.py         # Input/Output validation logic
│   ├── feedback.py          # Feedback mechanisms
│   └── ...
├── agent/                   # Agent loop and logic
│   ├── runner.py            # Runner with .agent, .stream, .sync
│   ├── training_block.py    # Training or pre-processing logic
│   └── config.py            # MAX_TURN_VALUE and settings
└── README.md                # Project documentation
🔁 Agent Loop
The main agent loop is governed by a turn-based interaction model:

MAX_TURN_VALUE = 10  # Limit the conversation to a maximum of 10 turns
The Runner handles agent orchestration:

Runner.agent()   # Run the core agent logic
Runner.stream()  # Enable streaming responses
Runner.sync()    # Synchronous execution path
🧪 Validation with Guardials
Guardials ensures that every interaction is safe, by running in parallel with your agent:

python
Copy
Edit
from guardials import Validator

def validate_io(input_data, output_data):
    validator = Validator()
    return validator.validate(input_data, output_data)
Feedback from validation can be used to update or correct agent behavior dynamically.

🌐 API with FastAPI
FastAPI is used to expose the agent capabilities via HTTP endpoints:

from fastapi import FastAPI
from agent.runner import Runner

app = FastAPI()

@app.post("/interact/")
async def interact(user_input: str):
    return Runner.sync(user_input)
Run the server with:

uvicorn main:app --reload
📚 Usage Example

from agent.runner import Runner

user_input = "What's the weather like today?"
response = Runner.sync(user_input)

print("Agent:", response)
🤝 Contributing
Contributions are welcome! Please open issues or pull requests to suggest improvements or report bugs.

📄 License
This project is licensed under the MIT License.

✨ Acknowledgments
Built with ❤️ using FastAPI

Inspired by the need for safer, smarter, and scalable LLM agent management.
