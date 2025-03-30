import os
from dotenv import load_dotenv
load_dotenv()

# ✅ Force LiteLLM to read the correct API key (important!)
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

from crewai import Agent
from langchain_community.chat_models import ChatLiteLLM

# ✅ Set up Gemini via LiteLLM
llm = ChatLiteLLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.5,
    verbose=True,
    api_key="AIzaSyCJkcCpvggxQj9SD5Wx50mKVRSel4uW5Rs"  # 🔐 directly provide your API key here
)

# Define agents
input_agent = Agent(
    role="Input Handler",
    goal="Accept and prepare the {topic} for translation and explanation",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in Sanskrit text formats and Bhagavad Gita structure."
        "Have good English and Hindi "
    ),
    llm=llm
)

translation_agent = Agent(
    role="Translation Scholar",
    goal= "Translate the given {topic} into Hindi and English",
    verbose=True,
    memory=True,
    backstory="A linguistic expert fluent in Sanskrit, Hindi, and English with deep spiritual knowledge.",
    llm=llm
)

explanation_agent = Agent(
    role="Gita Commentator",
    goal="Provide detailed spiritual explanations in both Hindi and English",
    verbose=True,
    memory=True,
    backstory="Experienced in interpreting the Gita from both traditional and modern perspectives.",
    llm=llm
)

summary_agent = Agent(
    role="Spiritual Summary Writer",
    goal="Create short and simple summaries of the Shloka in Hindi and English",
    verbose=True,
    memory=True,
    backstory="Great at simplifying deep spiritual ideas for everyone to understand.",
    llm=llm
)

json_formatter_agent = Agent(
    role="JSON Formatter",
    goal="Combine all outputs into structured JSON format",
    verbose=True,
    memory=True,
    backstory="Expert in data formatting and JSON structure organization.",
    llm=llm
)

