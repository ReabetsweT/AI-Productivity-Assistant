"""
Meeting Summarizer Module
Handles automatic summarization of meeting transcripts
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import json
from datetime import datetime

load_dotenv()

class MeetingSummarizer:
    """Summarizes meeting transcripts and extracts key information"""
    
    def __init__(self):
        self.api_key = os.getenv('openai_api_key')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        self.client = OpenAI(api_key=self.api_key)
    
    def summarize(self, transcript):
        """
        Summarize a meeting transcript
        
        Args:
            transcript (str): Full meeting transcript
        
        Returns:
            dict: Summary with key points and action items
        """
        prompt = f"""Analyze the following meeting transcript and provide:
1. A concise summary (2-3 sentences)
2. Key points (as a list)
3. Action items (with owners if mentioned)
4. Decisions made

Format your response as JSON with keys: summary, key_points, action_items, decisions

Transcript:
{transcript}"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert at summarizing meetings. Always respond with valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=800
            )
            
            # Parse JSON response
            try:
                result = json.loads(response.choices[0].message.content)
                return result
            except json.JSONDecodeError:
                # Fallback if response isn't valid JSON
                content = response.choices[0].message.content
                return {
                    "summary": content[:200] if len(content) > 200 else content,
                    "key_points": ["See full response for details"],
                    "action_items": [],
                    "decisions": []
                }
        except Exception as e:
            print(f"Error summarizing meeting: {e}")
            return {
                "summary": "Error processing transcript",
                "key_points": [],
                "action_items": [],
                "decisions": []
            }
    
    def extract_action_items(self, transcript):
        """
        Extract only action items from a transcript
        
        Args:
            transcript (str): Meeting transcript
        
        Returns:
            list: List of action items with assigned owners
        """
        prompt = f"""Extract action items from this meeting transcript. Format as a JSON list with objects containing 'task' and 'owner' fields.

Transcript:
{transcript}"""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Extract action items and return valid JSON list."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=500
            )
            
            try:
                return json.loads(response.choices[0].message.content)
            except json.JSONDecodeError:
                return [{"task": response.choices[0].message.content, "owner": "Unknown"}]
        except Exception as e:
            print(f"Error extracting action items: {e}")
            return []
    
    def generate_meeting_minutes(self, transcript, attendees, meeting_title="Team Meeting"):
        """
        Generate formal meeting minutes
        
        Args:
            transcript (str): Meeting transcript
            attendees (list): List of meeting attendees
            meeting_title (str): Title of the meeting
        
        Returns:
            str: Formatted meeting minutes
        """
        attendees_str = ", ".join(attendees) if attendees else "Not specified"
        
        prompt = f"""Generate formal meeting minutes based on this transcript.

Meeting Details:
- Title: {meeting_title}
- Attendees: {attendees_str}
- Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}

Transcript:
{transcript}

Format the minutes professionally with sections for: Agenda, Discussion, Decisions, and Action Items."""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert at writing formal meeting minutes."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.5,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Error generating meeting minutes: {e}")
            return "Error generating meeting minutes. Please try again."
