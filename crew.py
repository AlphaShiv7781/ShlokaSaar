from crewai import Crew, Process
from agents import input_agent, translation_agent, explanation_agent, summary_agent, json_formatter_agent
from tasks import input_task, translation_task, explanation_task, summary_task, format_task

crew = Crew(
    agents=[
        input_agent,
        translation_agent,
        explanation_agent,
        summary_agent,
        json_formatter_agent  # Add this
    ],
    tasks=[
        input_task,
        translation_task,
        explanation_task,
        summary_task,
        format_task  # Add this
    ],
    process=Process.sequential
)
