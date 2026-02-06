# Task-Oriented Conversation System

This project implements a short-term, extended **task-oriented conversation system** designed to gather user feedback about a lecture in a user-centered manner. The system leverages hierarchical state transitions to guide the conversation effectively.  

![HSTNs](https://github.com/user-attachments/assets/0a606e6b-8563-486f-9e5d-078dbd21d844)

---

Note to practitioners: The original system was tested on the kaggle platform. In order to run this on your local machine please follow the guidelines below:

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Running Locally](#running-locally)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Overview

The system models task-oriented conversations for lecture feedback collection. It is designed to:  

- Adaptively handle short-term and extended interactions.  
- Follow a hierarchical state transition structure for decision-making.  
- Ensure a user-centered feedback process.  

The core principle is demonstrated in the Hierarchical State Transition Diagram above.  

---

## Features

- **Hierarchical State Transitions**: Guides conversation dynamically based on user responses.  
- **Customizable Models**: Supports different AI conversation models.  
- **Flexible Deployment**: Can be run on Kaggle or local machines with minimal configuration.  
- **Data-Driven Feedback**: Collects and stores feedback efficiently.  

---

## Installation

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/Task_oriented_conversation_system.git
cd Task_oriented_conversation_system
```

2. Create and activate a Python virtual environment:
```bash
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
---

## Usage
1. Import and initialize the system:
```python
from conversation_system import ConversationSystem

system = ConversationSystem()
model, contents = system.define_model()
```

2. Start the conversation and provide user feedback:
``` python
response = system.run_conversation(user_input="I found the lecture informative.")
print(response)
```
---
## Configuration
The system requires a valid API key for model access. By default, on Kaggle, it uses `UserSecretsClient()`. For local use, replace it with an environment variable:

### Update `define_model` for local use
```python
import os
import json
import base64
import genai  # Your AI library

def define_model(self):
    # Retrieve API key from local environment variable
    GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
    if not GOOGLE_API_KEY:
        raise ValueError("Please set your GOOGLE_API_KEY environment variable before running.")

    # Configure the client library
    genai.configure(api_key=GOOGLE_API_KEY)

    model = 'gemini-1.0-pro'
    contents_b64 = '...'  # unchanged
    generation_config_b64 = '...'  # unchanged
    safety_settings_b64 = '...'  # unchanged
    user_input_b64 = ''

    contents = json.loads(base64.b64decode(contents_b64))
    generation_config = json.loads(base64.b64decode(generation_config_b64))
    safety_settings = json.loads(base64.b64decode(safety_settings_b64))
    user_input = base64.b64decode(user_input_b64).decode()

    generation_config['temperature'] = 1.0
    return (model, contents)
```
---

## Setting API Key Locally

- Linux/macOS:
```bash
export GOOGLE_API_KEY="your_api_key_here"
```
- Windows Command Prompt:
```bash
set GOOGLE_API_KEY="your_api_key_here"
```
- Windows PowerShell:
```bash
$env:GOOGLE_API_KEY="your_api_key_here"
```
---

## Running locally:

### After configuring the API key:
```bash
python main.py
```
The system will run locally using the specified model and collect user feedback interactively.


---

## Contributing:

### Contributions are welcome!

- Fork the repository

- Create a new branch:

```bash
git checkout -b feature/your-feature

```

- Commit your changes:
```bash
git commit -m "Add feature"
```

- Push and open a Pull Request.

---

## License:

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.


---









