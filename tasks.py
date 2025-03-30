from crewai import Task
from agents import input_agent, translation_agent, explanation_agent, summary_agent, json_formatter_agent

input_task = Task(
    description="Receive the Shloka as input and verify Shloka {topic} format or chapter:verse.",
    expected_output="Cleaned and verified Shloka.",
    agent=input_agent
)

translation_task = Task(
    description="Translate the Shloka {topic} from Sanskrit into both Hindi and English.",
    expected_output=(
        "JSON format with translations:\n"
        "{\n"
        "  \"translation\": {\n"
        "    \"en\": \"English text\",\n"
        "    \"hi\": \"Hindi text\"\n"
        "  }\n"
        "}"
    ),
    agent=translation_agent
)

explanation_task = Task(
    description="Explain the Shloka {topic} in Hindi and English.",
    expected_output=(
        "JSON format with explanations:\n"
        "{\n"
        "  \"explanation\": {\n"
        "    \"en\": \"English explanation\",\n"
        "    \"hi\": \"Hindi explanation\"\n"
        "  }\n"
        "}"
    ),
    agent=explanation_agent
)

summary_task = Task(
    description="Summarize the Shloka {topic} in Hindi and English.",
    expected_output=(
        "JSON format with summaries:\n"
        "{\n"
        "  \"summary\": {\n"
        "    \"en\": \"English summary\",\n"
        "    \"hi\": \"Hindi summary\"\n"
        "  }\n"
        "}"
    ),
    agent=summary_agent
)

# Add new formatting task
format_task = Task(
    description="Combine all outputs into final JSON structure",
    expected_output=(
        "Complete JSON structure:\n"
        "{\n"
        "  \"translation\": {\"en\": \"...\", \"hi\": \"...\"},\n"
        "  \"explanation\": {\"en\": \"...\", \"hi\": \"...\"},\n"
        "  \"summary\": {\"en\": \"...\", \"hi\": \"...\"}\n"
        "}"
    ),
    agent=json_formatter_agent,
    context=[translation_task, explanation_task, summary_task]
)
