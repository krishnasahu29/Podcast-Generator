<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# 🎙️ AI Podcast Generator

Transform blog URLs into podcast-ready content using AI-powered summarization and audio generation. This project combines advanced language models, multi-agent task orchestration, and speech synthesis in a modular Gradio web application. The target workflow: input a blog URL, receive a concise summary, and obtain an MP3 podcast via text-to-speech.

## Interesting Techniques

- **LLM Delegation \& Task Design**: Uses composable [CrewAI agents](https://github.com/Shopify/crewai) to split scraping and summarization into separate roles—enabling modular, testable pipelines.
- **Dynamic Web Scraping**: Employs [FirecrawlScrapeWebsiteTool](https://github.com/Firecrawl/Firecrawl) and [ScrapeWebsiteTool](https://github.com/Shopify/crewai-tools) to extract main content from blogs, filtering out navigation, ads, and irrelevant data. See [MDN: Web Scraping](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Using_the_W3C_DOM_API) for more on the DOM.
- **Markdown to Audio Pipeline**: Converts extracted and summarized [Markdown](https://developer.mozilla.org/en-US/docs/Web/Markdown) text directly into MP3 using [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/).
- **Interactive UI**: Built with [Gradio](https://www.gradio.app/), enabling instant interface prototyping, event-driven updates, and custom layout blocks.
- **Progressive Status Updates**: Generator yields incremental status and feedback to the UI as each process completes.
- **Environment and Secret Management**: Secure API keys and configurations loaded with [python-dotenv](https://pypi.org/project/python-dotenv/).


## Notable Technologies \& Libraries

- **[CrewAI](https://github.com/Shopify/crewai)** for agent/task orchestration.
- **[gTTS](https://pypi.org/project/gTTS/)** (Google Text-to-Speech) for MP3 audio generation.
- **[Gradio](https://www.gradio.app/)** for web UIs.
- **[python-dotenv](https://pypi.org/project/python-dotenv/)** for `.env` config management.
- **[FirecrawlScrapeWebsiteTool](https://github.com/Firecrawl/Firecrawl)** for robust, scriptable web scraping.


## Fonts

- The UI uses **Inter** and **Montserrat** for modern, readable typography.
    - [Inter (Google Fonts)](https://fonts.google.com/specimen/Inter)
    - [Montserrat (Google Fonts)](https://fonts.google.com/specimen/Montserrat)


## Project Structure

```
.
├── gradio_app_podcast.py
├── podcast_generator.py
├── .env
# (add other files as relevant)
```

- **`gradio_app_podcast.py`** – Entry point. Contains Gradio interface, event handling, user interaction, and text/audio output logic.
- **`podcast_generator.py`** – Handles all AI processing: defines CrewAI agent classes, scraping/summarization tasks, and the LLM setup.
- **`.env`** – Environment variables, including API keys for LLMs and scraping tools. *Not checked in; use sample for deployment.*


### Other Possible Folders (expand as your project grows):

- **`/assets/`** – Images or static resources for the Gradio interface (not included, add if custom branding is used).
- **`/styles/`** – CSS or theme overrides for custom Gradio layouts or typography.

----

Let me know if you'd like modifications or want me to create this README.md file for you.

<div style="text-align: center">⁂</div>

[^1]: Screenshot-2025-07-19-104039.jpg

[^2]: gradio_app_podcast.py

[^3]: podcast_generator.py

