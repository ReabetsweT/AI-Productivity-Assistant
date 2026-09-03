"""
Task Planner Module
Handles intelligent task planning and prioritization
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
import json
from datetime import datetime, timedelta

load_dotenv()

class TaskPlanner:
    """Plans and prioritizes tasks using AI"""
    
    def __init__(self):
        self.api_key = os.getenv('openai_api_key')
        if not self.api_key:
            raise ValueError("OpenAI API key not found in environment variables")
        self.client = OpenAI(api_key=self.api_key)
    
    def create_plan(self, tasks, deadline=None, priority="medium"):
        """
        Create an intelligent task plan
        
        Args:
            tasks (list): List of tasks to plan
            deadline (str): Project deadline (YYYY-MM-DD format)
            priority (str): Overall priority level (low, medium, high)
        
        Returns:
            dict: Structured task plan with timeline
        """
        tasks_str = "\n".join([f"- {task}" for task in tasks])
        
        prompt = f"""Create an optimized task plan for the following:

Tasks:
{tasks_str}

Deadline: {deadline if deadline else 'Not specified'}
Priority: {priority}

Provide a JSON response with:
1. task_sequence: ordered list of tasks
2. estimated_hours: dict mapping tasks to hours
3. dependencies: tasks that depend on other tasks
4. risks: potential risks and mitigation strategies
5. daily_schedule: breakdown of tasks by day

Return valid JSON only."""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert project manager. Return valid JSON responses."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            try:
                plan = json.loads(response.choices[0].message.content)
                return plan
            except json.JSONDecodeError:
                return {
                    "tasks": tasks,
                    "sequencing": tasks,
                    "timeline": {},
                    "dependencies": {},
                    "risks": ["Could not parse full plan"],
                    "message": response.choices[0].message.content
                }
        except Exception as e:
            print(f"Error creating plan: {e}")
            return {
                "tasks": tasks,
                "sequencing": tasks,
                "timeline": {},
                "dependencies": {},
                "risks": [f"Error: {str(e)}"]
            }
    
    def prioritize_tasks(self, tasks, criteria=None):
        """
        Prioritize tasks based on various criteria
        
        Args:
            tasks (list): List of tasks to prioritize
            criteria (list): Prioritization criteria (urgency, importance, effort, etc.)
        
        Returns:
            list: Prioritized task list
        """
        tasks_str = "\n".join([f"- {task}" for task in tasks])
        criteria_str = ", ".join(criteria) if criteria else "urgency, importance, dependencies"
        
        prompt = f"""Prioritize these tasks based on: {criteria_str}

Tasks:
{tasks_str}

Return a JSON list with 'task' and 'priority_score' (1-10) for each task, ordered by priority."""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert at task prioritization. Return valid JSON lists."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=600
            )
            
            try:
                prioritized = json.loads(response.choices[0].message.content)
                # Sort by priority score
                if isinstance(prioritized, list):
                    return sorted(prioritized, key=lambda x: x.get('priority_score', 5), reverse=True)
                return prioritized
            except json.JSONDecodeError:
                return tasks
        except Exception as e:
            print(f"Error prioritizing tasks: {e}")
            return tasks
    
    def estimate_effort(self, task_description):
        """
        Estimate effort required for a task
        
        Args:
            task_description (str): Description of the task
        
        Returns:
            dict: Effort estimation with hours and complexity
        """
        prompt = f"""Estimate the effort required for this task:

{task_description}

Provide a JSON response with: estimated_hours, complexity (easy/medium/hard), risks, and recommendations."""
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert at effort estimation. Return valid JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.6,
                max_tokens=400
            )
            
            try:
                return json.loads(response.choices[0].message.content)
            except json.JSONDecodeError:
                return {
                    "estimated_hours": "Unable to parse",
                    "complexity": "Unknown",
                    "response": response.choices[0].message.content
                }
        except Exception as e:
            print(f"Error estimating effort: {e}")
            return {"error": str(e)}
