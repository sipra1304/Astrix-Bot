# 🚀 Astrix Chatbot

Welcome to the **Astrix Chatbot** project! Astrix is an astronaut-themed guide for Advaita, the annual techno-cultural fest of IIIT Bhubaneswar. This chatbot leverages data scraped from the Advaita website to answer your queries effectively. Let's dive in! 🌌

## 📜 Table of Contents

- [🌟 Introduction](#-introduction)
- [✨ Features](#-features)
- [⚙️ Prerequisites](#️-prerequisites)
- [📥 Installation](#-installation)
- [🚀 Usage](#-usage)
  - [🔍 Scraping Data](#-scraping-data)
  - [🤖 Setting Up the Chatbot](#-setting-up-the-chatbot)
- [🛠 Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🔗 Resources](#-resources)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)

## 🌟 Introduction

Meet **Astrix** 🧑‍🚀, your friendly astronaut-themed chatbot designed to guide you through **Advaita**, the grandest fest in the stellar galaxy, hosted by IIIT Bhubaneswar. Astrix uses advanced AI to provide accurate and context-aware responses to all your queries about the fest. See you at the fest! 🚀

**Note**: This is still a prototype and a context-based chatbot. Additional URLs will be added soon to make it function more robustly. Feel free to use this MVP for your custom chatbot projects!

## ✨ Features

- 🌐 **Scrapes data** from multiple pages of the Advaita website.
- 📄 **Stores scraped data** in a JSON file.
- 🔍 **Loads and processes** the JSON data for use with the chatbot.
- 🤖 **Utilizes LangChain** with Google Generative AI for embeddings and context retrieval.
- 💬 **Provides accurate and context-aware responses** to user queries.
- 🌌 Maintains an **astronaut-themed conversational style**.

## ⚙️ Prerequisites

- 🐍 Python 3.8 or higher
- 🔑 Google API Key for Google Generative AI
- 🧭 Selenium WebDriver
- 🖥 ChromeDriver
- 🌟 Virtual Environment (optional but recommended)

## 📥 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/advaita-astrix-chatbot.git
   cd advaita-astrix-chatbot
   ```

2. **Create and activate a virtual environment** (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   - Create a `.env` file in the project root.
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```

## 🚀 Usage

### 🔍 Scraping Data

1. **Run the scraping script** to collect data from the Advaita website and save it to a JSON file:
   ```bash
   python scrape_advaita.py
   ```

### 🤖 Setting Up the Chatbot

1. **Run the chatbot script** to load the scraped data, set up the chatbot, and start answering queries:
   ```bash
   python chatbot.py
   ```

## 🛠 Tech Stack

- **Python** 🐍
- **Selenium WebDriver** 🧭
- **LangChain** 🔗
- **Google Generative AI** 🤖
- **Chroma** 📊

## 📂 Project Structure

```
advaita-astrix-chatbot/
│
├── scrape_advaita.py        # Script to scrape data from the Advaita website
├── chatbot.py               # Script to set up and run the chatbot
├── requirements.txt         # Required Python packages
├── .env                     # Environment variables (e.g., Google API key)
├── scraped_data.json        # JSON file with scraped data
└── README.md                # Project README
```

## 🔗 Resources

Here are some LangChain links and blogs that were instrumental in making this project:

- **RAG Q/A**: [Quickstart for RAG Q/A](https://python.langchain.com/v0.1/docs/use_cases/question_answering/quickstart)
- **Embeddings**: [Text Embedding Documentation](https://python.langchain.com/v0.1/docs/modules/data_connection/text_embedding/)
- **Vector Store**: [Vector Store Documentation](https://python.langchain.com/v0.1/docs/modules/data_connection/vectorstores/)
- **Document Loader**: [Document Loader Documentation](https://python.langchain.com/v0.1/docs/modules/data_connection/document_loaders/)

## 🤝 Contributing

Contributions are welcome! Please fork this repository and submit a pull request with your changes. 

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
