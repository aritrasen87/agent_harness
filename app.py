from deepagents import create_deep_agent
from deepagents.backends.filesystem import FilesystemBackend
from langchain_openai import ChatOpenAI

# 1. Initialize your language model
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# 2. Give the agent a pluggable filesystem backend so it can read/write files
# This grants the agent tools like read_file, write_file, and ls.
backend = FilesystemBackend(root_dir=".")

# 3. Create the Deep Agent harness
agent = create_deep_agent(
    model=llm,
    system_prompt="You are a helpful and autonomous task orchestrator.",
    backend=backend,
    
    # Loads project-level conventions into the system prompt
    memory=["./AGENTS.md"], 
    
    # Scans the folder, parses YAML frontmatter, and makes skills available to the agent
    skills=["./skills"] 
)

# 4. Invoke the agent
if __name__ == "__main__":
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": "I have a long article in workspace/article.txt. Please summarize it for me."}
        ]
    })
    
    print("\n--- Agent Execution Complete ---")
    print(response["messages"][-1]["content"])