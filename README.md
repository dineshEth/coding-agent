# Python Agent

A command-line agent that uses Mistral AI API to perform file operations through natural language commands.

## Description

This project is a Python-based CLI agent that integrates with Mistral AI's API to provide intelligent file management capabilities. The agent can understand natural language commands and perform file operations such as reading, creating, appending, and deleting files.

## Features

- **File Operations**: Read, create, append, and delete files using natural language
- **Mistral AI Integration**: Uses the Mistral AI API (mistral-tiny model) for processing commands
- **Interactive CLI**: Real-time conversation interface with the AI assistant
- **Tool-based Architecture**: Implements tools that the AI can call to perform specific actions

## Available Tools

- `read_file` - Read the content of a file and return it as a string
- `create_file` - Create a new file with the given content
- `write_file_end` - Append content to the end of a file
- `delete_file` - Delete a file at the given path

## Installation

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/dinesh-prajapati/python-agent.git
   cd python-agent
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv agentvenv
   source agentvenv/bin/activate  # On Windows: agentvenv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Required packages:
   - `mistralai` - Mistral AI client library
   - `python-dotenv` - For environment variable management

## Configuration

1. Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

2. Edit the `.env` file and add your Mistral API key:
   ```
   MISTRAL_API_KEY=your_api_key_here
   ```

3. Obtain a Mistral API key from [Mistral AI Platform](https://mistral.ai/)

## Usage

Run the agent:
```bash
python main.py
```

### Example Commands

- "Read the file config.py"
- "Create a new file called test.txt with content 'Hello World'"
- "Append 'New line' to test.txt"
- "Delete the file test.txt"
- "What files are in this directory?"
- Type "exit" or "quit" to end the session

## Project Structure

```
python-agent/
├── main.py           # Main application logic
├── config.py         # Configuration and environment setup
├── .env.example      # Environment file template
├── .gitignore        # Git ignore patterns
├── README.md         # Project documentation
└── src/              # Additional source files
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Dinesh Prajapati**

## Acknowledgments

- [Mistral AI](https://mistral.ai/) - For providing the AI model and API
- Python Community - For the excellent libraries and tools
