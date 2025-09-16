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


def start_quiz(topic: str = "", difficulty: str = "medium") -> str:
    """
    Start an interactive quiz session based on the articles content.

    Args:
        topic: Optional specific topic to focus quiz questions on
        difficulty: Quiz difficulty level (easy, medium, hard)
    """
    articles = read_articles()

    if not articles or articles[0].startswith("No"):
        return "No articles available to generate quiz questions from."

    combined_content = "\n\n".join(articles)

    focus_instruction = f" focusing on {topic}" if topic else ""

    return f"""Based on these articles:\n\n{combined_content}

Please start an interactive quiz session{focus_instruction} with {difficulty} difficulty. 

Instructions for the quiz:
1. Generate ONE question at a time (not all questions at once)
2. Present the question with 4 multiple choice options (A, B, C, D)
3. DO NOT include the correct answer in your response
4. Wait for the user's answer before providing the next question
5. After each answer, tell them if they're correct/incorrect and provide a brief explanation
6. Keep track of their score
7. Generate a total of 5 questions for the complete quiz

Start with the first question now. Format it as:
Question 1/5: [Question text]
A) [Option A]
B) [Option B]
C) [Option C] 
D) [Option D]

Please provide your answer (A, B, C, or D)."""


def check_answer_and_continue(user_answer: str, current_question: str = "") -> str:
    """
    Check the user's answer and provide the next question or quiz completion.

    Args:
        user_answer: The user's answer (A, B, C, or D)
        current_question: The current question being answered (optional for context)
    """
    articles = read_articles()

    if not articles or articles[0].startswith("No"):
        return "No articles available to check answers against."

    combined_content = "\n\n".join(articles)

    return f"""Based on these articles:\n\n{combined_content}

The user answered: {user_answer}
{f"For the question: {current_question}" if current_question else ""}

Please:
1. Check if this answer is correct or incorrect
2. Provide a brief explanation of the correct answer with reference to the articles
3. Update the quiz score 
4. If this was not the final question (5/5), provide the NEXT question in the same format:
   Question X/5: [Question text]
   A) [Option A]  
   B) [Option B]
   C) [Option C]
   D) [Option D]
   
   Please provide your answer (A, B, C, or D).

5. If this was the final question, provide the final score and a summary of performance

Do not include the correct answer for the next question - only for the one just answered."""


# Keep the old functions for backward compatibility
def generate_quiz_questions(topic: str = "", difficulty: str = "medium") -> str:
    """
    Generate quiz questions based on the articles content.
    NOTE: This function shows all questions at once. Use start_quiz() for interactive quizzes.

    Args:
        topic: Optional specific topic to focus quiz questions on
        difficulty: Quiz difficulty level (easy, medium, hard)
    """
    articles = read_articles()

    if not articles or articles[0].startswith("No"):
        return "No articles available to generate quiz questions from."

    combined_content = "\n\n".join(articles)

    focus_instruction = f" focusing on {topic}" if topic else ""

    return f"""Based on these articles:\n\n{combined_content}

Please generate 5 {difficulty}-level quiz questions{focus_instruction}. 
Format each question as:
Q1: [Question]
A) [Option A]
B) [Option B] 
C) [Option C]
D) [Option D]
Correct Answer: [Letter]

Make sure the questions test comprehension and key concepts from the articles."""


def check_quiz_answer(question: str, user_answer: str) -> str:
    """
    Check if a quiz answer is correct and provide explanation.
    NOTE: This is for single answer checking. Use check_answer_and_continue() for interactive quizzes.

    Args:
        question: The quiz question
        user_answer: The user's answer (A, B, C, or D)
    """
    articles = read_articles()

    if not articles or articles[0].startswith("No"):
        return "No articles available to check answers against."

    combined_content = "\n\n".join(articles)

    return f"""Based on these articles:\n\n{combined_content}

For this question: {question}
User answered: {user_answer}

Please check if this answer is correct and provide:
1. Whether the answer is correct or incorrect
2. The correct answer with explanation
3. Reference to the relevant information from the articles"""


# Enhanced agent with better instructions
root_agent = Agent(
    name="article_assistant",
    model="gemini-2.5-flash",
    instruction="""You are a helpful AI assistant that specializes in summarizing articles and helping users learn through interactive questioning.

Your main capabilities:
1. **Summarize articles**: Provide clear, concise summaries of article content
2. **Answer questions**: Help users understand specific aspects of the articles  
3. **Interactive quizzes**: Create engaging one-question-at-a-time quizzes
4. **Check answers**: Evaluate quiz responses and provide explanations

When summarizing:
- Identify key themes and main points
- Use clear, accessible language
- Organize information logically
- Highlight important insights

When running interactive quizzes (start_quiz):
- Present ONE question at a time, never show all questions together
- Do NOT include correct answers when presenting questions
- Wait for user response before showing the next question
- Keep track of the user's score throughout the quiz
- Provide encouraging feedback after each answer
- Create questions that test real understanding, not just memorization

When checking answers:
- Be encouraging and educational
- Explain why an answer is correct or incorrect
- Reference specific information from the articles
- Offer additional context when helpful

Always be helpful, patient, and encouraging in your interactions.""",
    tools=[
        get_articles_summary,
        answer_question_about_articles,
        start_quiz,
        check_answer_and_continue,
        generate_quiz_questions,  # Keep for backward compatibility
        check_quiz_answer,  # Keep for backward compatibility
    ],
)

# Example usage and interaction loop
if __name__ == "__main__":
    print("Article Assistant is ready!")
    print("You can ask me to:")
    print("- Summarize the articles")
    print("- Answer questions about the content")
    print("- Start an interactive quiz (recommended)")
    print("- Generate all quiz questions at once")
    print("- Check individual quiz answers")
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
