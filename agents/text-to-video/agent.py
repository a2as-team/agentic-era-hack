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

import os
import time
import uuid
import tempfile
import base64
from typing import Optional
import google.auth
from google import genai
from google.genai.types import GenerateVideosConfig
from google.cloud import storage
from google.adk.agents import Agent
import sys

# Set up authentication
_, project_id = google.auth.default()
os.environ.setdefault("GOOGLE_CLOUD_PROJECT", project_id)
os.environ.setdefault("GOOGLE_CLOUD_LOCATION", "global")
os.environ.setdefault("GOOGLE_GENAI_USE_VERTEXAI", "True")

def create_html_for_video(video_data: bytes, prompt: str, agent_dir: str) -> str:
    """Generates a clean, themed HTML page to display the video."""
    # Convert video to base64 for embedding
    video_base64 = base64.b64encode(video_data).decode('utf-8')
    
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Generated Video</title>
    <style>
        :root {{
            --app-bg-color: #ffffff;
            --app-secondary-bg-color: #f0f2f6;
            --app-text-color: #31333F;
            --app-font: "Source Sans Pro", sans-serif;
        }}
        body {{
            font-family: var(--app-font);
            background-color: var(--app-secondary-bg-color);
            color: var(--app-text-color);
            margin: 0;
            padding: 2rem;
        }}
        .container {{
            max-width: 800px;
            margin: auto;
            background: var(--app-bg-color);
            padding: 2rem;
            border-radius: 0.5rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .header h1 {{
            font-size: 1.75rem;
            font-weight: 600;
            margin-bottom: 2rem;
        }}
        .video-player {{
            width: 100%;
            margin-bottom: 2rem;
        }}
        video {{
            width: 100%;
            border-radius: 0.25rem;
        }}
        .expander {{
            border: 1px solid #e6e9ef;
            border-radius: 0.5rem;
            overflow: hidden;
        }}
        .expander-header {{
            background-color: #f8f9fa;
            padding: 0.75rem 1rem;
            font-weight: 600;
            border-bottom: 1px solid #e6e9ef;
        }}
        .expander-content {{
            padding: 1rem;
            font-size: 0.95rem;
            line-height: 1.6;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎬 AI Generated Video</h1>
        </div>
        <div class="video-player">
            <video controls autoplay muted loop>
                <source src="data:video/mp4;base64,{video_base64}" type="video/mp4">
                Your browser does not support the video tag.
            </video>
        </div>
        <div class="expander">
            <div class="expander-header">
                <span>Prompt</span>
            </div>
            <div class="expander-content">
                <p>{prompt}</p>
            </div>
        </div>
    </div>
</body>
</html>
"""
    
    # Create output directory
    output_dir = os.path.join(agent_dir, "output")
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate unique filename
    html_filename = f"ai_video_{uuid.uuid4().hex[:8]}.html"
    html_filepath = os.path.join(output_dir, html_filename)
    
    # Write HTML file
    with open(html_filepath, "w", encoding='utf-8') as f:
        f.write(html_content)
        
    return html_filepath

def generate_video(prompt: str) -> str:
    """
    Generates a video based on a user's prompt and creates an HTML page 
    to display it with embedded video data.
    """
    try:
        client = genai.Client()
        
        print(f"Starting video generation for prompt: {prompt[:100]}...")
        
        operation = client.models.generate_videos(
            model="veo-3.0-fast-generate-001",
            prompt=prompt,
            config=GenerateVideosConfig(
                aspect_ratio="16:9",
                duration_seconds=8,
                resolution="720p",
            ),
        )

        print("Video generation started... waiting for completion...")
        retry_count = 0
        max_retries = 180  # 30 minutes max wait time
        
        while not operation.done and retry_count < max_retries:
            time.sleep(10)
            try:
                operation = client.operations.get(operation)
                print(f"⏳ Still generating... ({retry_count * 10}s elapsed)")
                retry_count += 1
            except Exception as e:
                print(f"Error checking operation status: {e}")
                retry_count += 1

        if not operation.done:
            return "❌ Video generation timed out. Please try again with a shorter or simpler prompt."

        if operation.error:
            return f"❌ Error generating video: {operation.error}"

        if operation.response:
            try:
                print("✅ Video generated, retrieving content directly...")
                video_data = operation.result.generated_videos[0].video.video_bytes
                
                if not video_data:
                    return "❌ Failed to retrieve video data from the response."
                
                print(f"✅ Video data retrieved successfully ({len(video_data)} bytes)")
                
                # Create HTML page with embedded video
                agent_dir = os.path.dirname(__file__)
                html_filepath = create_html_for_video(video_data, prompt, agent_dir)
                abs_html_path = os.path.abspath(html_filepath)

                return f"🎉 Success! Your AI-generated video is ready!\n\n🔗 Open this link to watch your video:\nfile://{abs_html_path}\n\n💡 The video is embedded in the page, so it will work offline!\n\n📝 Your prompt: \"{prompt[:100]}{'...' if len(prompt) > 100 else ''}\""

            except (AttributeError, IndexError) as e:
                print(f"Could not get video content from response. Error: {e}")
                print(f"Full response: {operation.response}")
                return "❌ Video generation finished, but could not retrieve video content."
        
        return "❌ Video generation operation finished but no response was received."
        
    except Exception as e:
        print(f"Unexpected error in generate_video: {e}")
        return f"❌ An unexpected error occurred: {str(e)}"

# Create the root agent using Agent
root_agent = Agent(
    name="text_to_video_agent",
    model="gemini-2.0-flash-exp",
    tools=[generate_video],
    instruction="""You are an AI Video Generation Assistant powered by Google's VEO-3 technology.

Your main purpose is to help users create amazing AI-generated videos from their text descriptions.

When users ask for a video:
1. Use the generate_video tool with their prompt
2. Provide encouraging and helpful responses
3. Give tips for better prompts if needed

For video prompts, help users create detailed, vivid descriptions that will result in better videos. Good prompts should include:
- Clear description of the scene/subject
- Visual details (colors, lighting, style)
- Action or movement descriptions
- Setting/environment details

Example of a good prompt: "A golden retriever puppy playing in a sunny meadow filled with wildflowers, shot in slow motion with warm cinematic lighting"

IMPORTANT: When the video generation is successful, the tool will return a message containing a 'file://' link. You MUST include the full, clickable 'file://' link in your final response to the user so they can open the video.

Always be enthusiastic and helpful when discussing video creation!""",
)

if __name__ == '__main__':
    import unittest

    class SimpleAgentTest(unittest.TestCase):
        def test_html_creation(self):
            """
            Tests that the create_html_for_video function generates a valid HTML file
            with the correct content.
            """
            video_data = b"test"
            prompt = "this is a test prompt"
            agent_dir = os.path.dirname(__file__)
            
            os.makedirs(os.path.join(agent_dir, "output"), exist_ok=True)

            html_filepath = create_html_for_video(
                video_data=video_data,
                prompt=prompt,
                agent_dir=agent_dir
            )

            self.assertTrue(os.path.exists(html_filepath))

            with open(html_filepath, 'r') as f:
                content = f.read()

            encoded_video_data = base64.b64encode(video_data).decode('utf-8')
            self.assertIn(encoded_video_data, content)
            self.assertIn(prompt, content)

            os.remove(html_filepath)

    # To run the tests, you would execute this file directly.
    # The agent's chat loop is replaced by this test runner.
    print("Running embedded simple test...")
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SimpleAgentTest))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    if not result.wasSuccessful():
        # Exit with a non-zero code if tests fail
        sys.exit(1)
