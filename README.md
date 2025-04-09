# 🤖 Code Explainer Micro-Agent

A minimal yet powerful AI-powered micro-agent that **explains code in plain English** and **suggests improvements**. Paste any code snippet, and let the agent break it down like your personal tutor 🧠✨

![Code Explainer Screenshot](https://user-images.githubusercontent.com/your-image-link.png) <!-- optional: add screenshot -->

---

## 🚀 Features

- 📘 **Code Explanation**: Understand what the code does in simple language
- 🛠️ **Suggestions**: Clean code tips, performance enhancements, and naming improvements
- 🌐 Built with **Streamlit** + **Ollama LLMs**
- 🧠 Works with **python programming language**

---

## 🧪 Demo

Paste your code into the text box and get:
- A concise, human-readable explanation
- Actionable suggestions to refactor or optimize

Try it locally 👇

---

## 🧰 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/)
- Python 3.8+
- dotenv for API key management

---

## 📦 Installation

1. **Clone the repo**
```bash
git clone https://github.com/siddhiipatell/code-explainer-microagent.git
cd code-explainer-microagent
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set your Ollama base URL and model name**
Ollama runs on localhost:11434 by default:
Create a .env file:
```bash
# .env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3 # You can use llama2, mistral, or any model you've pulled
```

5. **Run the app**
```bash
streamlit run app.py
```

## 🖼️ Project Structure
```bash
code-explainer-microagent/
├── app.py                    # Streamlit UI
├── llm_utils
│   ├── __init__.py
│   └── ollama_api.py
├── utils/
│   ├── explainer.py          # Code explanation logic
│   └── refactorer.py         # Suggest improvements
├── .env                      # (not tracked) your base url and model
└── requirements.txt          # Dependencies
```

## 💡 Examples

🧾 Input:

```python
def add(x, y):
    return x + y
```

## 📘 Output:
```bash
This function takes two arguments, x and y, and returns their sum. It's a simple addition function.
```

## 🛠 Suggestion:
```bash
Add a docstring for better documentation

Add type hints: def add(x: int, y: int) -> int:
```

## 🛠 Improvements (Coming Soon)
- 🔍 Code language detection
- 🧪 Linting or syntax validation
- 💾 Export as PDF or Markdown
- 💬 "Chat with your code" feature using LangChain


## 🤝 Contributing
Pull requests are welcome! Got an idea for a feature? Open an issue or fork away.

## 📜 License
MIT License © Siddhi Patel

## ⭐ Show Some Love
If this helped you or you learned something, leave a ⭐ on the repo
