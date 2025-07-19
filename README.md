# 🎙️ AI Podcast Generator

Transform blog URLs into podcast-ready content with AI-powered summarization and audio generation. This project uses multi-agent LLM pipelines to automate content extraction, summarization, and audio generation for instant podcast episodes.

---

## Features & Techniques

- **Gradio Blocks UI**  
  The frontend leverages [Gradio Blocks](https://www.gradio.app/docs/blocks/), allowing a modular, multi-section web layout.  
- **Async UI Status and Streaming**  
  Utilizes [Gradio generator functions](https://www.gradio.app/guides/streaming_generator/) for live status updates and progressive summary/audio generation.  
- **Markdown Content Handling**  
  Summary output is formatted in Markdown ([MDN: Markdown basics](https://developer.mozilla.org/en-US/docs/MDN/Structures/Markdown)), with markdown-to-audio conversion by stripping formatting for better voice experience.
- **Temporary File Handling**  
  Uses [`tempfile.NamedTemporaryFile`](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile) for MP3 audio file management, preventing clutter and supporting Gradio’s downloadable outputs.
- **gTTS Audio Pipeline**  
  Converts summaries to speech in one step using [gTTS](https://pypi.org/project/gTTS/).
- **Multi-Agent Orchestration**  
  Implements coordinated scraping and summarization via [CrewAI](https://docs.crewai.com/). Agents use delegated roles for scraping and summarization.
- **Fallback, Retry, and Timeout Config for LLMs**  
  The [LLM module](podcast_generator.py) is configured with retry logic, fallbacks, and timeouts for production stability.

## Notable Technologies & Libraries

- [Gradio](https://www.gradio.app/): UI for Python web apps and ML demos.
- [gTTS](https://pypi.org/project/gTTS/): Google’s Text-to-Speech for Python.
- [CrewAI](https://docs.crewai.com/): Orchestrated multi-agent framework.
- [Google Gemini](https://ai.google.dev/): Large language model powering all stages via API.
- [python-dotenv](https://pypi.org/project/python-dotenv/): Loads environment variables for secure credential management.

> **Fonts:** Uses default Gradio/system fonts. No custom fonts are specified in the UI.

## Project Structure


- **gradio_app_podcast.py**  
  Main Gradio UI and event handlers; wires together text/audio generation and streaming updates.
- **podcast_generator.py**  
  Defines LLM agents, scraping/summarization logic, model configuration (with retries/fallbacks), and exports the high-level summarization pipeline.

## Advanced Features

- [Gradio’s generator → streaming event updates](https://www.gradio.app/guides/streaming_generator/) enable step-by-step reporting to the UI while processing each phase.
- **Agent-based processing:** Scraping and summarization are split into specialized LLM agents with role/task abstraction, using [CrewAI patterns](https://docs.crewai.com/).
- **Markdown-to-Audio pipeline:** The generated markdown summary is sanitized for voice generation in [gTTS](https://pypi.org/project/gTTS/).
- **Environment-based configuration:** LLM and API setups use [python-dotenv](https://pypi.org/project/python-dotenv/) for clean secret handling.

---

📞 Support If you have any questions or need support, please reach out on: GitHub: @krishnasahu29 LinkedIn: www.linkedin.com/in/krishnasahu29 Email: krishna.sahu.work222@gmail.com