# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import logging
import os
from pathlib import Path
from typing import List
from zoneinfo import ZoneInfo

import google.auth
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

BASE_PATH = Path(__file__).resolve().parent


def read_articles() -> List[str]:
    """Read all articles from the articles directory."""
    articles = []
    articles_path = BASE_PATH / Path("articles/")

    logging.info(f"Reading articles from {articles_path}")

    if not articles_path.exists():
        logging.warning(f"Articles directory not found: {articles_path}")
        return [
            "No articles directory found. Please create an 'articles' folder with text files."
        ]

    # Look for common text file extensions
    for pattern in ["*.txt", "*.md"]:
        logging.info(f"Searching for files with pattern: {pattern}")
        logging.info(f"Articles path: {articles_path}")
        logging.info(f"Glob pattern: {articles_path.glob(f'**/{pattern}')}")

        for file in articles_path.glob(f"**/{pattern}"):
            logging.info(f"Reading file: {file}")
            try:
                with open(file, "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if content:  # Only add non-empty files
                        articles.append(f"=== {file.name} ===\n{content}")
            except Exception as e:
                articles.append(f"Error reading {file.name}: {str(e)}")

    if not articles:
        articles.append("No readable articles found in the articles directory.")

    return articles


def get_articles_summary(query: str = "") -> str:
    """
    Get a summary of all articles, optionally filtered by a query.

    Args:
        query: Optional query to focus the summary on specific topics
    """
    articles = read_articles()

    if not articles or articles[0].startswith("No"):
        return articles[0] if articles else "No articles available."

    combined_content = "\n\n".join(articles)

    if query:
        return f"Here are the articles with focus on '{query}':\n\n{combined_content}\n\nPlease provide a summary focusing on: {query}"
    else:
        return f"Here are all the articles:\n\n{combined_content}\n\nPlease provide a comprehensive summary of these articles."


def answer_question_about_articles(question: str) -> str:
    """
    Answer specific questions about the articles content.

    Args:
        question: The user's question about the articles
    """
    articles = read_articles()
    print(articles)

    if not articles or articles[0].startswith("No"):
        return "No articles available to answer questions about."

    combined_content = "\n\n".join(articles)

    return f"Based on these articles:\n\n{combined_content}\n\nPlease answer this question: {question}"


# Enhanced agent with better instructions
root_agent = Agent(
    name="article_chat",
    model="gemini-2.5-flash",
    instruction="""You are a helpful AI assistant that specializes in summarizing articles and answer user questions.

Your main capabilities:
1. **Summarize articles**: Provide clear, concise summaries of article content
2. **Answer questions**: Help users understand specific aspects of the articles  

When summarizing:
- Identify key themes and main points
- Use clear, accessible language
- Organize information logically
- Highlight important insights

Always be helpful, patient, and encouraging in your interactions.""",
    tools=[
        get_articles_summary,
        answer_question_about_articles,
    ],
)

if __name__ == "__main__":
    print("Article Assistant is ready!")
    print("You can ask me to:")
    print("- Summarize the articles")
    print("- Answer questions about the content")
    print("\nType 'quit' to exit\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        if user_input:
            response = root_agent.say(user_input)
            print(f"Assistant: {response}\n")
        else:
            print("Please enter a question or request.\n")
