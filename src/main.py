"""
Main Application Entry Point
Demonstrates the AI Productivity Assistant functionality
"""

import sys
import os
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from email_generator import EmailGenerator
from meeting_summarizer import MeetingSummarizer
from task_planner import TaskPlanner
from research_assistant import ResearchAssistant
from chatbot import ProductivityChatbot


def print_section(title):
    """Print a formatted section header"""
    print("\n" + "="*70)
    print(f"  {title}")
    print("="*70)


def demo_email_generation():
    """Demonstrate email generation"""
    print_section("1. EMAIL GENERATION DEMO")
    try:
        email_gen = EmailGenerator()
        email = email_gen.create_email(
            recipient="John Smith",
            subject="Q3 Project Status Update",
            context="Completed Phase 1 development, ready for review by stakeholders",
            tone="professional"
        )
        print("\nGenerated Email:")
        print("-" * 70)
        print(email)
        print("-" * 70)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def demo_meeting_summarization():
    """Demonstrate meeting summarization"""
    print_section("2. MEETING SUMMARIZATION DEMO")
    try:
        meeting_summarizer = MeetingSummarizer()
        sample_transcript = """Manager: Good morning everyone. Let's start with the Q3 review.
        Developer 1: We completed the backend API development and it's ready for testing.
        Developer 2: The frontend is 85% complete. We should finish by end of week.
        Manager: Great progress. When can we start QA testing?
        QA Lead: We can begin testing next Monday with the backend API.
        Manager: Perfect. Action items: Dev 1 - prepare API documentation, Dev 2 - complete remaining features, QA Lead - schedule testing.
        """
        
        summary = meeting_summarizer.summarize(sample_transcript)
        print("\nMeeting Summary:")
        print("-" * 70)
        for key, value in summary.items():
            print(f"\n{key.upper()}:")
            if isinstance(value, list):
                for item in value:
                    print(f"  • {item}")
            else:
                print(f"  {value}")
        print("-" * 70)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def demo_task_planning():
    """Demonstrate task planning"""
    print_section("3. TASK PLANNING DEMO")
    try:
        task_planner = TaskPlanner()
        tasks = [
            "Market research and competitor analysis",
            "Design UI/UX mockups",
            "Backend API development",
            "Frontend implementation",
            "QA testing",
            "Deployment preparation"
        ]
        
        plan = task_planner.create_plan(
            tasks=tasks,
            deadline="2026-10-15",
            priority="high"
        )
        
        print("\nTask Plan:")
        print("-" * 70)
        import json
        print(json.dumps(plan, indent=2))
        print("-" * 70)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def demo_research_assistance():
    """Demonstrate research assistance"""
    print_section("4. RESEARCH ASSISTANCE DEMO")
    try:
        research_assistant = ResearchAssistant()
        research_result = research_assistant.research_query(
            "What are the latest trends in AI and machine learning for workplace productivity?"
        )
        
        print("\nResearch Findings:")
        print("-" * 70)
        print(research_result[:800] + "..." if len(research_result) > 800 else research_result)
        print("-" * 70)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def demo_chatbot():
    """Demonstrate chatbot interaction"""
    print_section("5. CHATBOT DEMO")
    try:
        chatbot = ProductivityChatbot()
        
        print("\nUser: Can you help me manage my workload this week?")
        response1 = chatbot.chat("Can you help me manage my workload this week?")
        print(f"\nAssistant: {response1}")
        
        print("\n" + "-" * 70)
        print("\nUser: I have 5 projects and a presentation due Friday.")
        response2 = chatbot.chat("I have 5 projects and a presentation due Friday.")
        print(f"\nAssistant: {response2}")
        
        print("-" * 70)
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def interactive_mode():
    """Interactive chatbot mode"""
    print_section("INTERACTIVE MODE - AI PRODUCTIVITY ASSISTANT")
    print("\nType 'quit' to exit, 'help' for commands\n")
    
    try:
        chatbot = ProductivityChatbot()
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("\nThank you for using AI Productivity Assistant. Goodbye!")
                break
            
            if user_input.lower() == 'help':
                print("\nAvailable commands:")
                print("  email - Draft an email")
                print("  meeting - Summarize a meeting")
                print("  tasks - Create a task plan")
                print("  research - Research a topic")
                print("  quit - Exit")
                print("  Or just chat normally!\n")
                continue
            
            if not user_input:
                continue
            
            response = chatbot.chat(user_input)
            print(f"\nAssistant: {response}\n")
    
    except KeyboardInterrupt:
        print("\n\nExiting...")
    except Exception as e:
        print(f"❌ Error: {e}")


def main():
    """Main application"""
    print("\n" + "*" * 70)
    print("*" + " " * 68 + "*")
    print("*" + "  AI-POWERED WORKPLACE PRODUCTIVITY ASSISTANT".center(68) + "*")
    print("*" + " " * 68 + "*")
    print("*" * 70)
    
    print("\nSelect an option:")
    print("  1. Run all demos")
    print("  2. Email generation demo")
    print("  3. Meeting summarization demo")
    print("  4. Task planning demo")
    print("  5. Research assistance demo")
    print("  6. Chatbot demo")
    print("  7. Interactive mode (chat with AI)")
    print("  8. Exit")
    
    choice = input("\nEnter your choice (1-8): ").strip()
    
    results = {
        "Email": False,
        "Meeting": False,
        "Tasks": False,
        "Research": False,
        "Chatbot": False
    }
    
    if choice == "1":
        results["Email"] = demo_email_generation()
        results["Meeting"] = demo_meeting_summarization()
        results["Tasks"] = demo_task_planning()
        results["Research"] = demo_research_assistance()
        results["Chatbot"] = demo_chatbot()
    elif choice == "2":
        demo_email_generation()
    elif choice == "3":
        demo_meeting_summarization()
    elif choice == "4":
        demo_task_planning()
    elif choice == "5":
        demo_research_assistance()
    elif choice == "6":
        demo_chatbot()
    elif choice == "7":
        interactive_mode()
    elif choice == "8":
        print("\nGoodbye!")
        return
    else:
        print("\n❌ Invalid choice. Exiting.")
        return
    
    # Print summary if all demos were run
    if choice == "1":
        print_section("DEMO SUMMARY")
        for feature, success in results.items():
            status = "✓ Passed" if success else "✗ Failed"
            print(f"  {feature}: {status}")
    
    print("\n" + "*" * 70)
    print("\nThank you for using AI Productivity Assistant!\n")


if __name__ == "__main__":
    main()
