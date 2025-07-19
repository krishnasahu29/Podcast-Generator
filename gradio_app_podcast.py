import gradio as gr
import os
import tempfile
from gtts import gTTS
import io
import base64
from datetime import datetime

# Import the functions from your existing CrewAI code
# Make sure your existing code is saved as 'podcast_generator.py'
from podcast_generator import summarize_blog

def generate_podcast(url):
    """
    Main function that processes URL and generates podcast content
    """
    if not url or not url.strip():
        return "Please enter a valid URL", None, "❌ Error: No URL provided"

    try:
        # Update status
        status = "🔄 Processing URL with CrewAI agents..."
        yield "Processing...", None, status

        # Call the existing summarize_blog function from your code
        summary = summarize_blog(url)

        # Update status
        status = "🎙️ Generating audio from summary..."
        yield summary, None, status

        # Generate audio from summary
        audio_file = generate_audio(summary)

        # Final status
        status = "✅ Podcast generation completed successfully!"
        yield summary, audio_file, status

    except Exception as e:
        error_msg = f"❌ Error: {str(e)}"
        yield f"Error processing URL: {str(e)}", None, error_msg

def generate_audio(text):
    """
    Generate audio from text using Google Text-to-Speech
    """
    try:
        # Remove markdown formatting for better audio
        clean_text = text.replace('#', '').replace('*', '').replace('_', '')

        # Generate speech
        tts = gTTS(text=clean_text, lang='en', slow=False)

        # Create temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            tts.save(tmp_file.name)
            return tmp_file.name

    except Exception as e:
        print(f"Error generating audio: {e}")
        return None

def copy_to_clipboard(text):
    """
    Helper function to copy text to clipboard
    """
    return f"Summary copied to clipboard!\n\n{text}"

# Custom CSS for styling
custom_css = """
<style>
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    .section-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
        font-weight: bold;
    }
    .status-box {
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
        font-weight: bold;
    }
    .url-input {
        font-size: 16px;
        padding: 10px;
    }
</style>
"""

# Create the Gradio interface
def create_podcast_interface():
    """
    Create the main Gradio interface with 3 sections
    """

    with gr.Blocks(css=custom_css, title="AI Podcast Generator") as interface:

        # Header
        gr.HTML("""
        <div class="main-container">
            <h1 style="text-align: center; color: #667eea; margin-bottom: 30px;">
                🎙️ AI Podcast Generator
            </h1>
            <p style="text-align: center; color: #666; margin-bottom: 40px;">
                Transform blog URLs into podcast-ready content with AI-powered summarization and audio generation
            </p>
        </div>
        """)

        # Section 1: URL Input
        with gr.Row():
            with gr.Column():
                gr.HTML('<div class="section-header">📝 Section 1: URL Input</div>')

                url_input = gr.Textbox(
                    label="Blog URL",
                    placeholder="Enter blog URL here (e.g., https://www.example.com/blog-post)",
                    elem_classes=["url-input"],
                    scale=3
                )

                with gr.Row():
                    process_btn = gr.Button("🚀 Generate Podcast", variant="primary", scale=2)
                    clear_btn = gr.Button("🗑️ Clear", variant="secondary", scale=1)

                # Example URLs
                # gr.HTML("""
                # <details style="margin-top: 15px;">
                #     <summary style="cursor: pointer; color: #667eea;"><strong>📋 Example URLs (Click to expand)</strong></summary>
                #     <div style="margin-top: 10px; padding: 10px; background: #f5f5f5; border-radius: 5px;">
                #         <p><strong>AI/Tech:</strong> https://www.pluralsight.com/resources/blog/ai-and-data/what-is-claude-ai</p>
                #         <p><strong>Business:</strong> https://hbr.org/2024/01/how-to-build-a-successful-ai-strategy</p>
                #         <p><strong>Science:</strong> https://www.nature.com/articles/d41586-024-00001-1</p>
                #     </div>
                # </details>
                # """)

        # Section 2: Blog Summary
        with gr.Row():
            with gr.Column():
                gr.HTML('<div class="section-header">📄 Section 2: Blog Summary</div>')

                summary_output = gr.Textbox(
                    label="AI-Generated Summary",
                    placeholder="Your blog summary will appear here...",
                    lines=10,
                    max_lines=15,
                    show_copy_button=True,
                    interactive=False
                )

                # Copy button
                copy_btn = gr.Button("📋 Copy Summary", variant="secondary")

        # Section 3: Audio Output
        with gr.Row():
            with gr.Column():
                gr.HTML('<div class="section-header">🎧 Section 3: Audio Output</div>')

                audio_output = gr.Audio(
                    label="Generated Podcast Audio",
                    type="filepath",
                    interactive=False
                )

                # Download instructions
                gr.HTML("""
                <p style="color: #666; font-style: italic; margin-top: 10px;">
                    💡 Tip: Use the download button (⬇️) in the audio player to save the MP3 file
                </p>
                """)

        # Status section
        with gr.Row():
            status_output = gr.Textbox(
                label="Status",
                value="🟢 Ready to process URL",
                interactive=False,
                show_label=True
            )

        # Event handlers
        process_btn.click(
            fn=generate_podcast,
            inputs=[url_input],
            outputs=[summary_output, audio_output, status_output],
            # show_progress=True
        )

        clear_btn.click(
            fn=lambda: ("", "", None, "🟢 Ready to process URL"),
            outputs=[url_input, summary_output, audio_output, status_output]
        )

        copy_btn.click(
            fn=copy_to_clipboard,
            inputs=[summary_output],
            outputs=[gr.Textbox(visible=False)]
        )

        # Footer
        gr.HTML("""
        <div style="text-align: center; margin-top: 40px; padding: 20px; color: #666;">
            <p>🤖 Powered by CrewAI, Google Gemini, and Gradio</p>
            <p>Built for: Build & Deploy End-to-End AI Agents</p>
        </div>
        """)

    return interface

# Launch the application
if __name__ == "__main__":
    # Create and launch the interface
    app = create_podcast_interface()

    # Launch with configuration
    app.launch(
        # server_name="0.0.0.0",  # Makes it accessible from outside localhost
        server_port=7860,
        share=False,  # Set to True if you want a public link
        show_error=True,
        # show_tips=True,
        # enable_queue=True
    )
