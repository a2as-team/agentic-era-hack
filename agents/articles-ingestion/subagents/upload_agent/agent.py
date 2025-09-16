from google.adk.tools import google_search
import os
import google.auth
from google.adk.agents import Agent

_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")


def upload_article_to_gcs(article_file: str, bucket_name: str, destination_blob_name: str) -> str:
   """Uploads a file to the given GCS bucket."""
   storage_client = storage.Client()
   bucket = storage_client.bucket("temp-articles-ingestion")
   blob = bucket.blob(destination_blob_name)

   blob.upload_from_filename(article_file)

   return f"File {article_file} uploaded to gs://{bucket_name}/{destination_blob_name}."


main_prompt = """

As a specialized AI assistant, your primary function is to generate and upload articles in Markdown format to a Google Cloud Storage (GCS) bucket.

Your workflow should be:

Fetching the article scraped by the root agent.

Generate the article content in a clear, well-structured Markdown format.

Establish a connection to the designated GCS bucket.

Upload the Markdown file to the specified bucket path, ensuring the file name and metadata are correct.

File name should always start with the current datetime.

Confirm the successful upload with a concise, clear message.

Your communication should be professional and focused on the task. Acknowledge and confirm each step of the process. If any errors occur, provide a specific and actionable error message."""

root_agent = Agent(
    name="upload_agent",
    model="gemini-2.5-flash",
    instruction=main_prompt,
    tools=[upload_article_to_gcs]
)
