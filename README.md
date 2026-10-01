# LangChain Groq Chatbot Project

A Python project exploring conversational AI chatbots using **LangChain** and **Groq** LLMs.

## 🚀 Features

- **Interactive Chatbot**: Command-line chatbot interacting with Groq-hosted models.
- **Conversation History**: Retains chat context across multiple user inputs (`HumanMessage` and `AIMessage`).
- **Custom System Messages**: Custom persona and behavior control (e.g., funny AI assistant persona).

## 📁 Project Structure

- `System_Message.py`: Chatbot implementation using `SystemMessage` for custom personality and full message history.
- `chatbot_with_history.py`: Interactive CLI chatbot tracking human and AI conversation history.
- `temp.py` & `test.py`: Simple test scripts for Groq model invocations.
- `requirements.txt`: Python package dependencies.
- `.env.example`: Example environment configuration.

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/varunpatil1706-spec/first_project.git
cd first_project
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv myenv
myenv\Scripts\activate

# Linux / macOS
python3 -m venv myenv
source myenv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables
Create a `.env` file in the root directory (or copy from `.env.example`):
```bash
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the chatbot
```bash
python chatbot_with_history.py
```
or
```bash
python System_Message.py
```
Type `exit` to end the conversation.
