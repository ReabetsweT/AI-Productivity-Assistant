"""
Email Generator Module
Handles automated email generation using AI
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

class EmailGenerator:
    """Generates professional emails using AI"""
    
    def __init__(self):
        self.api_key = os.getenv('openai_api_key')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        self.client = OpenAI(api_key=self.api_key)
    
    def create_email(self, recipient, subject, context, tone="professional"):
        """
        Generate an email based on recipient, subject, and context
        
        Args:
            recipient (str): Email recipient name
            subject (str): Email subject
            context (str): Email context/purpose
            tone (str): Tone of the email (professional, casual, formal)
        
        Returns:
            str: Generated email content
        """
        prompt = f"""You are a professional email writer. Generate a well-structured, concise email with the following details:
        
Recipient: {recipient}
Subject: {subject}
Context: {context}
Tone: {tone}

Please provide a complete email with greeting, body, and closing. Format it properly with line breaks."""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert email composer. Create professional, clear, and concise emails."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating email: {e}")
            return f"Error generating email for {recipient}. Please check your API key."
    
    def generate_quick_response(self, original_email, response_type="acknowledgment"):
        """
        Generate a quick response to an email
        
        Args:
            original_email (str): The email to respond to
            response_type (str): Type of response (acknowledgment, decision, clarification)
        
        Returns:
            str: Generated response
        """
        prompt = f"""Generate a {response_type} response to the following email. Keep it brief and professional.

Original Email:
{original_email}

Response Type: {response_type}"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert at writing quick email responses."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating response: {e}")
            return f"Error generating response. Please try again."
    
    def draft_template(self, email_type):
        """
        Generate an email template for a specific type
        
        Args:
            email_type (str): Type of email (meeting request, status update, etc.)
        
        Returns:
            str: Email template
        """
        prompt = f"Create an email template for: {email_type}. Include placeholders for customization."
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert at creating email templates."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=400
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating template: {e}")
            return f"Error generating template. Please try again."
