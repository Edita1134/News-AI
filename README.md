

# 🚀 **Innovative Tech Research and Blogging System** ✨

Welcome to the **Innovative Tech Research and Blogging System**! This project is designed to uncover groundbreaking technologies and narrate compelling tech stories. Our system features two powerful agents equipped to handle all your research and writing needs. Let's dive into the details! 🌟

## 🌐 **Overview**

Our system integrates advanced AI models to facilitate both tech research and writing. Leveraging the latest in AI technology, we aim to explore emerging trends and create engaging content about technological advancements.

## 🧑‍🔬 **Senior Researcher Agent** 🧠

### 🎯 **Role: Senior Researcher**

- **Objective**: Uncover groundbreaking technologies in `{topic}`.
- **Backstory**: Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world. 🌍
- **Features**:
  - **Verbose Mode**: Detailed output for thorough research.
  - **Memory**: Retains information for context-aware research.
  - **Tools**: Equipped with essential tools for deep analysis.
  - **Delegation**: Allows delegation for enhanced productivity.

### ⚙️ **Configuration**:
```python
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

news_researcher=Agent(
    role="Senior Researcher",
    goal='Uncover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)
```

## ✍️ **Writer Agent** 📖

### 🎯 **Role: Writer**

- **Objective**: Narrate compelling tech stories about `{topic}`.
- **Backstory**: With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner. ✨
- **Features**:
  - **Verbose Mode**: Provides detailed explanations and insights.
  - **Memory**: Retains context for consistent storytelling.
  - **Tools**: Utilizes custom tools for effective writing.
  - **Delegation**: Delegation is not allowed to ensure direct control.

### ⚙️ **Configuration**:
```python
news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
```

## 🔧 **Setup and Configuration**

1. **Install Dependencies**:
   - Make sure to install the required packages using `pip`:
     ```bash
     pip install crewai tools dotenv langchain_google_genai
     ```

2. **Environment Variables**:
   - Ensure you have your Google API key set up in a `.env` file:
     ```plaintext
     GOOGLE_API_KEY=your_google_api_key_here
     ```

3. **Run the Script**:
   - Execute your Python script to initialize the agents and start exploring and writing about the latest tech trends.

## 📚 **Getting Started**

- Explore the power of our Senior Researcher agent to dive deep into emerging technologies.
- Use our Writer agent to transform complex tech insights into engaging narratives.

## 🚀 **Contribute**

We welcome contributions to enhance this system! Feel free to fork the repository and submit pull requests.

## 📜 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy exploring and writing! 🚀💡

