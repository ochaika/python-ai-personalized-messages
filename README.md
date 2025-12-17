# Python AI Personalized Messages

This project demonstrates how to generate personalized text messages from CSV data using Python.
It is designed as a portfolio-ready example with a clean structure and AI-ready architecture.

## 🚀 Features

- Load structured data from CSV files
- Analyze and process user information
- Generate personalized messages
- AI-ready design with environment variables (`.env`)
- Safe fallback logic when no AI API key is provided
- Clear project structure suitable for real-world applications

## 📂 Project Structure

python-ai-personalized-messages/
│
├── data/
│ ├── people.csv
│ └── sample.csv
│
├── src/
│ ├── load_data.py
│ ├── analyze.py
│ ├── generate_text.py
│ └── prompts.py
│
├── outputs/
│ └── messages.txt
│
├── run.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md


## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/ochaika/python-ai-personalized-messages.git
cd python-ai-personalized-messages

1.(Optional) Create and activate a virtual environment

2.Install dependencies:
pip install -r requirements.txt

3.pip install -r requirements.txt

4.Run the project:
python run.py

5.Check the generated output:
outputs/messages.txt

AI Integration

The project is prepared for AI integration using an environment variable:
AI_API_KEY=your_api_key_here

If no API key is provided, the project automatically uses a fallback text generation logic.
This allows the project to run safely without external services.

Notes

API keys are not stored in the repository

.env.example is provided for configuration reference

The project is suitable for extension with real AI APIs in the future

This project was created as a learning and portfolio example.







