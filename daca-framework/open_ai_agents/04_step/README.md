# 🧠 Class 04: Agentic AI Tools & SDK Integration

This class focuses on understanding the architecture of agents, schema design, OpenAPI tools, and integrating computer tools using the OpenAI Agent SDK.

---

## 📘 Key Concepts

### 🧰 Tool Cells → Function Cells
- **Tool Cell**: A modular function/component used by agents.
- **Function Cell**: The implementation of a specific tool.
- Tools are defined by **schemas** (structure + function detail).

### 📊 OpenAPI + FastAPI
- We can define our **own schemas** for functions using FastAPI/OpenAPI.
- OpenAI Agent SDK supports OpenAPI statement schemas.

### 🤖 Everything is an Agent
- Tools like:
  - Web Search Tool
  - File Search Tool
  - Browser Tool
  - Computer Tool
- These are all accessible and programmable via Agent SDK.

### 🧠 OpenAI Agent SDK
- Last trained on **June 1, 2024**
- Will continue to **improve and advance**
- Supports cloud-native agents and external tools.

---

## 🧪 Useful Tools

- **Web Search Tool**: Enables the agent to browse the web.
- **File Search Tool**: Lets the agent interact with local/remote files.
- **Computer Tool**: Provides access to system-level tasks (like preview, browser automation).
- **Playwright**: For browser automation (can be run locally).

---

## 🧾 Terminology

- **Truncate**: To remove or shorten content (e.g., `truncate text` = `cut text`).
- **Schema**: Structure of a function/tool that an agent can understand and use.

---

## 🧑‍💻 Code Example (Google Colab Setup)

```python
import nest_asyncio
nest_asyncio.apply()

from google.colab import userdata
import os

# Load secret keys
os.environ["openapikey"] = userdata.get('openapikey')

# Access other secrets
secret_key = userdata.get("secret key")
