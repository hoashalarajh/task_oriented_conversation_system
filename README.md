# Task-Oriented Conversation System

This project implements a short-term, extended **task-oriented conversation system** designed to gather user feedback about a lecture in a user-centered manner. The system leverages hierarchical state transitions to guide the conversation effectively. 

### How this system is different and useful for you?
A key advantage of this system is its adaptability to specific requirements. The `pre-defined_survey_questions.py`  file contains the example configurations utilized in the original implementation, which can be entirely replaced with your own custom scripts.

### System Customization and Architecture
* **High Adaptability:** The system is designed to be easily customized for specific use cases. You can replace the example scripts provided in `pre-defined_survey_questions.py` with your own custom survey configurations.
* **State Management:** The architecture currently supports a maximum of four "superstates."
* **Survey Structuring:** It is recommended to partition your survey questions into up to four main thematic blocks corresponding to these superstates.
* **Scalability within Blocks:** While the number of superstates is capped at four, each block can handle an unlimited number of individual questions.


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
The dialogue system is instantiated from the `hstn` class and configured by assigning lecture-related text inputs to predefined attributes. Once configured, the system is executed using the `run_system_A()` method.

### Here is the example:

``` python
from hstn import hstn

# Create an instance of the dialogue system
dialogue_system = hstn()

# Assign lecture-related inputs
dialogue_system.about_lecture = text1
dialogue_system.task_organization = text2
dialogue_system.student_interaction = text3
dialogue_system.clarity = text4

# Run the dialogue system
# dialogue_system.run_system_A()
```


### Input Description

The following attributes must be set before running the system:

- `about_lecture`
General feedback or description of the lecture content.

- `task_organization`
Feedback related to how tasks or topics were structured.

- `student_interaction`
Observations about student engagement and interaction.

- `clarity`
Feedback regarding clarity of explanations and delivery.

Each attribute expects a text string.

### Execution Flow

1. An instance of the `hstn` class is created.

2. User-provided text inputs are assigned to the corresponding dialogue attributes.

3. Calling `run_system_A()` triggers the hierarchical state transition–based dialogue process.

4. The system processes the inputs and conducts the task-oriented conversation accordingly.

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
``` python
dialogue_system.run_system_A()
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









