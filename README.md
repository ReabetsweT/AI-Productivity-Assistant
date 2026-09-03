# AI-Powered Workplace Productivity Assistant

## Project Overview

This project is an AI-powered assistant designed to automate and streamline workplace productivity tasks. The assistant leverages cutting-edge AI technologies to help professionals save time and increase efficiency across various work activities.

## Key Features

### 1. **Email Generation**
- Automated drafting of professional emails
- Template-based customization
- Tone and style adjustments
- Quick response suggestions

### 2. **Meeting Summarization**
- Automatic transcription summarization
- Key points extraction
- Action items identification
- Meeting minutes generation

### 3. **Task Planning**
- Intelligent task prioritization
- Deadline management
- Workload distribution
- Progress tracking

### 4. **Research Assistance**
- Document analysis and synthesis
- Information gathering
- Citation management
- Research report generation

### 5. **Chatbot Interaction**
- Natural language processing
- Context-aware responses
- Multi-turn conversations
- Knowledge base integration

## Technology Stack

- **AI Platforms**: ChatGPT, Gemini, Notion AI
- **Programming Languages**: Python, JavaScript
- **Framework**: Flask/FastAPI (Backend)
- **Database**: (To be determined)
- **Tools & Libraries**: LangChain, OpenAI API, Google Generative AI

## Project Structure

```
AI-Productivity-Assistant/
├── README.md
├── requirements.txt
├── config/
│   └── api_keys.example.env
├── src/
│   ├── main.py
│   ├── email_generator.py
│   ├── meeting_summarizer.py
│   ├── task_planner.py
│   ├── research_assistant.py
│   └── chatbot.py
├── tests/
│   └── test_*.py
└── docs/
    ├── SETUP.md
    ├── USAGE.md
    └── ARCHITECTURE.md
```

## Getting Started

### Prerequisites
- Python 3.8 or higher
- API keys for OpenAI (ChatGPT) and/or Google (Gemini)
- Virtual environment (venv or conda)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/ReabetsweT/AI-Productivity-Assistant.git
cd AI-Productivity-Assistant
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up API keys:
```bash
cp config/api_keys.example.env config/api_keys.env
# Edit api_keys.env with your API keys
```

5. Run the application:
```bash
python src/main.py
```

## Usage Examples

### Email Generation
```python
from src.email_generator import EmailGenerator

generator = EmailGenerator()
email = generator.create_email(
    recipient="colleague@company.com",
    subject="Project Update",
    context="Completed Phase 1 deliverables"
)
print(email)
```

### Meeting Summarization
```python
from src.meeting_summarizer import MeetingSummarizer

summarizer = MeetingSummarizer()
summary = summarizer.summarize(meeting_transcript)
print(summary.key_points)
print(summary.action_items)
```

### Task Planning
```python
from src.task_planner import TaskPlanner

planner = TaskPlanner()
plan = planner.create_plan(
    tasks=["Research", "Writing", "Review"],
    deadline="2026-09-10",
    priority="high"
)
```

## Prompt Engineering Approach

This project demonstrates best practices in prompt engineering:

- **Clear Instructions**: Specific, detailed prompts with context
- **Role Definition**: Assigning roles to AI models (e.g., "You are a professional email writer")
- **Examples**: Providing input/output examples for better results
- **Constraints**: Setting boundaries and requirements
- **Iterative Refinement**: Testing and improving prompts based on outputs

## Ethical Considerations

- **Responsible AI Use**: Ensuring all generated content is accurate and appropriate
- **Data Privacy**: Protecting sensitive workplace information
- **Bias Awareness**: Monitoring AI outputs for potential biases
- **Transparency**: Being clear about AI-generated content
- **Human Oversight**: Maintaining human review of all generated materials

## Features in Development

- [ ] Advanced NLP for better context understanding
- [ ] Integration with calendar systems
- [ ] Real-time collaboration features
- [ ] Multi-language support
- [ ] Custom model fine-tuning

## Testing

Run the test suite:
```bash
pytest tests/
```

## Documentation

- [Setup Guide](docs/SETUP.md)
- [Usage Guide](docs/USAGE.md)
- [Architecture Guide](docs/ARCHITECTURE.md)

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Reabetswe T**  
AI Skills Acceleration Program (ASA 17)  
Johannesburg, Week 17

## Contact & Support

For questions or feedback, please create an issue in this repository or reach out through the ASA 17 program channels.

---

**Last Updated**: September 3, 2026  
**Status**: In Development  
**Deadline**: September 3, 2026
