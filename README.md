# Story AI Generator 🧠📖
### A ChatGPT-Based Tool for User Story Generation

![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-Django-green)
![LLM](https://img.shields.io/badge/LLM-GPT--5-orange)

Story AI Generator is an AI-driven tool developed to support the **Requirements Specification process** through the automated generation of **User Stories**.

Built using **GPT-5** and based on the **US-Prompt approach**, the tool enables contextualized and quality-driven generation of user stories without requiring prior knowledge of prompt engineering.

The tool encapsulates prompt engineering strategies and automatically transforms user inputs into structured prompts capable of generating well-formed user stories aligned with quality criteria.

🌐 Website  
https://storyaigenerator.com.br

📦 Repository  
https://github.com/rms-icomp/story-ai-generator

---

# 🚀 Motivation

Writing high-quality user stories is an important and often time-consuming activity in Requirements Engineering.

Story AI Generator was created to simplify and operationalize this process by integrating prompt engineering techniques and LLM capabilities into a guided and accessible interface.

Users only provide basic information about the system and the tool automatically generates structured user stories.

---

# ✨ Main Features

Story AI Generator provides:

- 🧠 Automated generation of user stories;
- 📋 Structured collection of requirement information;
- 📝 Guided interface for story specification;
- ⚙️ Customizable inputs according to project context;
- 📚 Story generation guided by QUS quality criteria;
- 📤 Export generated stories to **Excel (.xlsx)**.

---

# 👥 Target Users

Story AI Generator was designed for:

- Requirements Engineers
- Product Owners
- Systems Analysts
- Requirements Analysts
- Product Managers
- Software Teams

The tool also supports:

- Researchers
- Students
- Educational scenarios

---

# 🧠 Prompt Engineering Techniques

Story AI Generator incorporates prompt engineering approaches designed to improve generation quality.

## Meta-Prompting

Structured instructions composed of:

- Explicit instructions
- Examples
- Quality constraints
- Guided reasoning

## Few-Shot Prompting

Supports generation through examples.

## US-Prompt

Core mechanism responsible for user story generation.

The prompt strategy was introduced and validated in previous studies and encapsulated inside the application.

Generated stories follow recommendations from the **QUS Framework**.

---

# 🏗️ Architecture

Story AI Generator was fully developed using **Python** and **Django**.

## Backend

Responsible for:

- Request processing
- Prompt construction
- Integration with OpenAI API
- Story generation

## Frontend

Built using:

- Django Templates
- HTML5
- CSS3
- JavaScript

## Infrastructure

Deployment:

- Amazon Web Services (AWS)

Version Control:

- Git
- GitHub
---

# 📸 Screenshots

## Input Interface

![Input Interface](docs/images/input-form.png)

---

## Generated Stories

![Generated Stories](docs/images/output-interface.png)

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/rms-icomp/story-ai-generator.git
cd story-ai-generator
```

## Create Environment

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create:

```text
.env
```

Example:

```env
OPENAI_API_KEY=your_api_key
```

Run:

```bash
python manage.py runserver
```

Access:

```text
http://127.0.0.1:8000
```

---

# 📦 Artifact Availability

[TO FILL]

Artifacts include:

- Generated User Stories
- Supporting Material
- Prompt Resources
- Experimental Data

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 📝 Paper Reference

Santos, R., Tomás, H., Gadelha, B., Conte, T., & Oran, A.

**Story AI Generator: A ChatGPT-Based Tool for User Story Generation.**

Proceedings of the Brazilian Symposium on Software Engineering (SBES 2026).

---

# 👥 Authors

### Reine Santos
Institute of Computing  
Federal University of Amazonas  
Manaus, Amazonas, Brazil  
📧 rms@icomp.ufam.edu.br

### Hamiê Tomás
Federal Institute of Education, Science and Technology of Amazonas  
Manaus, Amazonas, Brazil  
📧 hamie.tomas@ifam.edu.br

### Bruno Gadelha
Institute of Computing  
Federal University of Amazonas  
Manaus, Amazonas, Brazil  
📧 bruno@icomp.ufam.edu.br

### Tayana Conte
Institute of Computing  
Federal University of Amazonas  
Manaus, Amazonas, Brazil  
📧 tayana@icomp.ufam.edu.br

### Ana Carolina Oran
Institute of Computing  
Federal University of Amazonas  
Manaus, Amazonas, Brazil  
📧 ana.oran@icomp.ufam.edu.br

---

# 🏛️ Institutions

- Institute of Computing — Federal University of Amazonas (UFAM)  
https://icomp.ufam.edu.br/

- Federal Institute of Education, Science and Technology of Amazonas (IFAM)  
https://www.ifam.edu.br/

