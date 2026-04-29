from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# 1. Initialize your language model
llm = ChatOpenAI(model="gpt-5-2025-08-07")

from pathlib import Path
BASE_DIR = Path.cwd()
print(BASE_DIR)

# 2. Give the agent a pluggable filesystem backend so it can read/write files
# This grants the agent tools like read_file, write_file, and ls.
backend = FilesystemBackend(root_dir=str(BASE_DIR))

# 3. Create the Deep Agent harness
agent = create_deep_agent(
    model=llm,
    system_prompt="You are a helpful and autonomous task orchestrator.",
    backend=backend,
    
    # Loads project-level conventions into the system prompt
    memory=[str(BASE_DIR / "AGENTS.md")],
    
    # Scans the folder, parses YAML frontmatter, and makes skills available to the agent
    skills=[str(BASE_DIR / "skills")] 
)

# 4. Invoke the agent
if __name__ == "__main__":
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": "I have a long article in /workspace/article.txt. Please summarize it for me."}
        ]
    })
    print("\n--- Agent Execution Complete ---")
    
    print(response['messages'][-1].content)