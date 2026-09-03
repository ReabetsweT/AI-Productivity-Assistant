# Usage Guide

## Quick Start

### 1. Email Generation

Generate professional emails quickly:

```python
from src.email_generator import EmailGenerator

# Initialize the generator
generator = EmailGenerator()

# Create an email
email = generator.create_email(
    recipient="colleague@company.com",
    subject="Project Status Update",
    context="We've completed the initial phase and are ready for review",
    tone="professional"
)

print(email)
```

### 2. Meeting Summarization

Automatically summarize meetings:

```python
from src.meeting_summarizer import MeetingSummarizer

# Initialize the summarizer
summarizer = MeetingSummarizer()

# Transcribe your meeting (or paste transcript)
meeting_transcript = """
Team: Discussed Q3 goals, budget allocation, and timeline.
Manager: We need to focus on customer retention.
Developer: Backend infrastructure needs upgrade.
"""

# Get summary
summary = summarizer.summarize(meeting_transcript)

print("Summary:", summary['summary'])
print("Key Points:", summary['key_points'])
print("Action Items:", summary['action_items'])
```

### 3. Task Planning

Create intelligent task plans:

```python
from src.task_planner import TaskPlanner

# Initialize the planner
planner = TaskPlanner()

# Define your tasks
tasks = [
    "Research market trends",
    "Create presentation",
    "Present to stakeholders",
    "Incorporate feedback"
]

# Create plan
plan = planner.create_plan(
    tasks=tasks,
    deadline="2026-09-15",
    priority="high"
)

print("Optimized Plan:", plan)
```

### 4. Research Assistance

Analyze documents and synthesize information:

```python
from src.research_assistant import ResearchAssistant

# Initialize the assistant
assistant = ResearchAssistant()

# Documents to analyze
documents = [
    "Document 1 content here...",
    "Document 2 content here...",
    "Document 3 content here..."
]

# Analyze
analysis = assistant.analyze_documents(
    documents=documents,
    query="What are the key trends in AI adoption?"
)

print("Findings:", analysis['findings'])
print("Evidence:", analysis['evidence'])
```

### 5. Chatbot Interaction

Have multi-turn conversations:

```python
from src.chatbot import ProductivityChatbot

# Initialize chatbot
chatbot = ProductivityChatbot()

# First message
response1 = chatbot.chat("Can you help me organize my week?")
print("Chatbot:", response1)

# Follow-up (maintains context)
response2 = chatbot.chat("I have 5 major projects to complete")
print("Chatbot:", response2)

# Get conversation history
history = chatbot.get_conversation_history()
print("Conversation:", history)
```

## Advanced Usage

### Custom Prompts

Modify prompts for specific use cases:

```python
# Example: Custom email tone
email = generator.create_email(
    recipient="CEO@company.com",
    subject="Annual Results",
    context="Present 2026 financial results",
    tone="formal"
)
```

### Batch Processing

Process multiple items efficiently:

```python
emails_to_draft = [
    {"recipient": "person1@company.com", "subject": "Meeting Request"},
    {"recipient": "person2@company.com", "subject": "Follow-up"},
    {"recipient": "person3@company.com", "subject": "Feedback"}
]

for email_data in emails_to_draft:
    email = generator.create_email(
        recipient=email_data["recipient"],
        subject=email_data["subject"],
        context="General correspondence"
    )
    # Save or send email
```

## Tips & Best Practices

### 1. Be Specific
Provide detailed context for better AI outputs:
```python
# Good
context = "Project delayed by 2 weeks, need to reschedule client meeting for Q4"

# Less specific
context = "Project delayed"
```

### 2. Use Conversation Context
Provide context in chatbot for better responses:
```python
response = chatbot.chat(
    "Summarize my priorities",
    context="I'm a product manager working on a mobile app launch"
)
```

### 3. Review AI Outputs
Always review generated content before sending:
```python
email = generator.create_email(...)
# Review and edit if needed
# Then send/use the email
```

### 4. Iterative Refinement
Use follow-up prompts to refine outputs:
```python
# First attempt
plan = planner.create_plan(tasks, deadline="2026-09-15")

# Refine if needed
refined_plan = planner.create_plan(tasks, deadline="2026-09-20")
```

## Integration Examples

### With Flask Web Framework

```python
from flask import Flask, request, jsonify
from src.email_generator import EmailGenerator

app = Flask(__name__)
generator = EmailGenerator()

@app.route('/generate-email', methods=['POST'])
def generate_email():
    data = request.json
    email = generator.create_email(
        recipient=data['recipient'],
        subject=data['subject'],
        context=data['context']
    )
    return jsonify({'email': email})

if __name__ == '__main__':
    app.run(debug=True)
```

## Troubleshooting

### Issue: Low quality outputs
- **Solution**: Provide more specific context and examples
- Use clearer, more detailed prompts

### Issue: Slow responses
- **Solution**: Check API rate limits
- Implement caching for similar requests

### Issue: Inconsistent results
- **Solution**: Adjust temperature/creativity parameters
- Use more specific role definitions in prompts

## Next Steps

- Explore advanced prompt engineering techniques
- Integrate with your existing workflow
- Customize modules for your specific needs
- Contribute improvements to the project
