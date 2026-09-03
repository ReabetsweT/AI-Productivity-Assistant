"""
Chatbot Module
Handles conversational AI and multi-turn interactions
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from email_generator import EmailGenerator
from meeting_summarizer import MeetingSummarizer
from task_planner import TaskPlanner
from research_assistant import ResearchAssistant

load_dotenv()

class ProductivityChatbot:
    """AI-powered chatbot for workplace productivity assistance"""
    
    def __init__(self):
        self.api_key = os.getenv('openai_api_key')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        self.client = OpenAI(api_key=self.api_key)
        self.conversation_history = []
        
        # Initialize modules
        try:
            self.email_gen = EmailGenerator()
            self.meeting_summarizer = MeetingSummarizer()
            self.task_planner = TaskPlanner()
            self.research_assistant = ResearchAssistant()
        except ValueError as e:
            print(f"Warning: Some modules not initialized: {e}")
    
    def chat(self, user_message, context=None):
        """
        Handle user messages and generate responses
        
        Args:
            user_message (str): User's message
            context (str): Optional context for better responses
        
        Returns:
            str: Chatbot response
        """
        # Store message in conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Prepare system message with context
        system_message = """You are an AI Workplace Productivity Assistant. Help users with:
- Email drafting and communication
- Meeting summarization
- Task planning and management
- Research and information gathering
- General productivity advice

Be professional, concise, and actionable. Offer to use specific tools when appropriate."""
        
        # Build messages for API
        messages = [{"role": "system", "content": system_message}]
        messages.extend(self.conversation_history[-10:])  # Keep last 10 messages for context
        
        if context:
            messages.insert(1, {"role": "system", "content": f"Additional context: {context}"})
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            
            assistant_response = response.choices[0].message.content
            
            # Store response in history
            self.conversation_history.append({
                "role": "assistant",
                "content": assistant_response
            })
            
            return assistant_response
        except Exception as e:
            print(f"Error in chat: {e}")
            error_response = f"I encountered an error: {str(e)}. Please check your API keys and try again."
            self.conversation_history.append({
                "role": "assistant",
                "content": error_response
            })
            return error_response
    
    def get_conversation_history(self):
        """
        Retrieve the conversation history
        
        Returns:
            list: List of conversation messages
        """
        return self.conversation_history
    
    def reset_conversation(self):
        """Clear conversation history"""
        self.conversation_history = []
    
    def suggest_assistance(self, current_task):
        """
        Suggest relevant assistance based on current task
        
        Args:
            current_task (str): Description of current task
        
        Returns:
            list: List of suggested assistances
        """
        prompt = f"""Based on this task: {current_task}
        
Suggest 3-5 specific ways I can help. Return as a simple numbered list."""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a productivity assistant. Provide concise, actionable suggestions."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            return response.choices[0].message.content.split('\n')
        except Exception as e:
            print(f"Error suggesting assistance: {e}")
            return ["Error generating suggestions"]
    
    def draft_email(self, recipient, subject, context, tone="professional"):
        """
        Draft an email using the email generator
        
        Args:
            recipient (str): Email recipient
            subject (str): Email subject
            context (str): Email context
            tone (str): Email tone
        
        Returns:
            str: Generated email
        """
        try:
            return self.email_gen.create_email(recipient, subject, context, tone)
        except Exception as e:
            return f"Error drafting email: {str(e)}"
    
    def summarize_meeting(self, transcript):
        """
        Summarize a meeting transcript
        
        Args:
            transcript (str): Meeting transcript
        
        Returns:
            dict: Meeting summary
        """
        try:
            return self.meeting_summarizer.summarize(transcript)
        except Exception as e:
            return {"error": str(e)}
    
    def create_task_plan(self, tasks, deadline=None, priority="medium"):
        """
        Create a task plan
        
        Args:
            tasks (list): List of tasks
            deadline (str): Deadline
            priority (str): Priority level
        
        Returns:
            dict: Task plan
        """
        try:
            return self.task_planner.create_plan(tasks, deadline, priority)
        except Exception as e:
            return {"error": str(e)}
    
    def research_topic(self, query):
        """
        Research a topic
        
        Args:
            query (str): Research query
        
        Returns:
            str: Research findings
        """
        try:
            return self.research_assistant.research_query(query)
        except Exception as e:
            return f"Error researching topic: {str(e)}"
