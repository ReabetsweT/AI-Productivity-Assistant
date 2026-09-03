# Setup Guide

## Installation Steps

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment support (built-in with Python 3.3+)

### 2. Clone the Repository
```bash
git clone https://github.com/ReabetsweT/AI-Productivity-Assistant.git
cd AI-Productivity-Assistant
```

### 3. Create Virtual Environment
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure API Keys
```bash
# Copy the example configuration
cp config/api_keys.example.env config/api_keys.env

# Edit api_keys.env with your actual API keys
nano config/api_keys.env
# or use your preferred text editor
```

### 6. Verify Installation
```bash
python src/main.py
```

## Getting API Keys

### OpenAI API Key (for ChatGPT)
1. Go to https://platform.openai.com/api-keys
2. Sign up or log in to your OpenAI account
3. Create a new API key
4. Add it to your `api_keys.env` file as `openai_api_key`

### Google API Key (for Gemini)
1. Go to https://aistudio.google.com/app/apikey
2. Click "Create API key"
3. Add it to your `api_keys.env` file as `google_api_key`

### Notion API Key
1. Go to https://www.notion.so/my-integrations
2. Create a new integration
3. Copy the internal integration token
4. Add it to your `api_keys.env` file as `notion_api_key`

## Project Structure
- `src/` - Main application modules
- `config/` - Configuration files
- `tests/` - Test suite
- `docs/` - Documentation
- `requirements.txt` - Project dependencies
- `README.md` - Project overview

## Running the Application
```bash
python src/main.py
```

## Running Tests
```bash
pytest tests/
```

## Troubleshooting

### Issue: ModuleNotFoundError
**Solution**: Make sure your virtual environment is activated and dependencies are installed
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: API Key errors
**Solution**: Verify your API keys are correctly added to `config/api_keys.env`

### Issue: Python version compatibility
**Solution**: Ensure you're using Python 3.8 or higher
```bash
python --version
```
