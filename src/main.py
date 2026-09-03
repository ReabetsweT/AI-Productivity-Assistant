"""
Main Application Entry Point
Demonstrates the AI Productivity Assistant functionality
"""

from email_generator import EmailGenerator
from meeting_summarizer import MeetingSummarizer
from task_planner import TaskPlanner
from research_assistant import ResearchAssistant
from chatbot import ProductivityChatbot


def main():
    """Main application flow"""
    
    print("=" * 60)
    print("AI-Powered Workplace Productivity Assistant")
    print("=" * 60)
    print()
    
    # Initialize all modules
    email_gen = EmailGenerator()
    meeting_summarizer = MeetingSummarizer()
    task_planner = TaskPlanner()
    research_assistant = ResearchAssistant()
    chatbot = ProductivityChatbot()
    
    # Demo: Email Generation
    print("1. EMAIL GENERATION DEMO")
    print("-" * 60)
    email = email_gen.create_email(
        recipient="John Doe",
        subject="Project Update",
        context="Completed Phase 1 of the AI project"
    )
    print(f"Generated Email: {email}")
    print()
    
    # Demo: Meeting Summarization
    print("2. MEETING SUMMARIZATION DEMO")
    print("-" * 60)
    sample_transcript = """
    Team Lead: Hello everyone, let's discuss the Q3 project progress.
    Developer 1: We completed the backend API development.
    Developer 2: Frontend is 80% complete, need another week.
    Team Lead: Good. Let's make sure we have the QA testing scheduled.
    QA Lead: We'll start testing next Monday.
    Team Lead: Perfect. Action items: Dev 1 - documentation, Dev 2 - complete frontend, QA - schedule testing.
    """
    summary = meeting_summarizer.summarize(sample_transcript)
    print(f"Meeting Summary: {summary}")
    print()
    
    # Demo: Task Planning
    print("3. TASK PLANNING DEMO")
    print("-" * 60)
    tasks = ["Research", "Design", "Development", "Testing", "Deployment"]
    plan = task_planner.create_plan(
        tasks=tasks,
        deadline="2026-09-30",
        priority="high"
    )
    print(f"Task Plan: {plan}")
    print()
    
    # Demo: Chatbot Interaction
    print("4. CHATBOT DEMO")
    print("-" * 60)
    response1 = chatbot.chat("Can you help me draft an email to my manager?")
    print(f"User: Can you help me draft an email to my manager?")
    print(f"Chatbot: {response1}")
    print()
    
    response2 = chatbot.chat("Make it about a project delay")
    print(f"User: Make it about a project delay")
    print(f"Chatbot: {response2}")
    print()
    
    print("=" * 60)
    print("Demo completed! All modules are operational.")
    print("=" * 60)


if __name__ == "__main__":
    main()
