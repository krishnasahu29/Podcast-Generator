import os
from crewai import Agent, Task, Crew, LLM, Process
from crewai_tools import FirecrawlScrapeWebsiteTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
    api_key=os.environ.get("GOOGLE_API_KEY"),
    num_retries=3,          # Add automatic retries
    timeout=120,            # Add generous timeout
    fallbacks=["gemini/gemini-1.5-flash"]  # Add fallback model
)

# Define agents
blog_scraper = Agent(
    role='Web Content Scraper',
    goal="Extract complete and accurate information from a blog URLs",
    backstory="You are a web content scraper. You are given a blog URL and you need to extract the complete and accurate information from the blog.",
    llm=llm,
    tools=[ScrapeWebsiteTool()],
    verbose=True,
    allow_delegation=False,
)

blog_summarizer = Agent(
    role="Content Summarizer",
    goal="Summarize the blog content in a concise and informative manner",
    backstory="You are a blog summarizer. You are given a blog text and you need to summarize the blog content in a concise and informative manner.",
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

# Define tasks
def scrape_blog_task(url):
    return Task(
        description=f"""Scrape the blog content from the {url} using the FirecrawlScrapeWebsiteTool.
                    Extract the main content, including the title, subtitle, and other relevant information.
                    Filter out any irrelevant content, such as navigation links, ads, or other non-blog content.
                    Ensure that the output is a complete and accurate representation of the blog content.
                    Do not include any text which is not relevant to the blog content.
                    Remove all the symbols and special characters from the output.
                    The output should be in markdown format.
        """,
        expected_output="The complete and accurate information from the blog in markdown format",
        agent=blog_scraper,
    )

def summarize_blog_task(scraped_text):
    return Task(
        description=f"""Summarize the blog content in a concise and informative manner from {scraped_text}.
                    Do not include any text which is not relevant to the blog content.
                    Keep the output concise and to the point.
                    The output should be in markdown format.
        """,
        expected_output="""The summary of the blog content around 200-250 words in markdown format. 
        The summary will be used to generate a podcast script.
        """,
        agent=blog_summarizer,
    )

def create_podcast_script_task(url):
    scrape_task = scrape_blog_task(url)
    summarize_task = summarize_blog_task(scrape_task)
    
    # Define crew
    crew = Crew(
        agents=[blog_scraper, blog_summarizer],
        tasks=[scrape_task, summarize_task],
        verbose=True,
        process=Process.sequential,
    )

    return crew

def summarize_blog(url):
    crew = create_podcast_script_task(url)
    result = crew.kickoff()
    return result.raw

if __name__ == "__main__":
    url = "https://www.pluralsight.com/resources/blog/ai-and-data/what-is-claude-ai"
    result = summarize_blog(url)
    print(result)
