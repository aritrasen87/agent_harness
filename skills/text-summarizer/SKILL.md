---
name: text-summarizer
description: Use this skill to condense large text files into bulleted summaries. Do NOT use this for code review or debugging.
---

# Text Summarizer Skill

## Instructions
When you load this skill to summarize a document, follow these exact steps:
1. Use your filesystem tools to read the target file.
2. Extract the three most important themes from the text.
3. Format the output as a Markdown list.
4. Save the result in the `./workspace/` directory with a `_summary.md` suffix.

## Example Output Format
* **Theme 1:** [Brief description]
* **Theme 2:** [Brief description]
* **Theme 3:** [Brief description]