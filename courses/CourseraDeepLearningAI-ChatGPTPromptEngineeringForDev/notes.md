# ChatGPT Prompt Engineering for development Notes

## 1.1 Introduction
- Use LLM to quickly build new and powerful apps
- Build quickly using OpenAI API
- Course describes how LLMs work, best practices for prompt engineering
- Using LLM APIs for summarizing, inferring, transforming, expanding
- 2 key principles for prompt
- Build a custom chatbot
- Practice on Jupyter notebook
- 2 types of LLM
  - base LLM: predicts next word, based on text training data
  - instruction tuned llm: tries to follow instructions. fine-tine on instructions and RLHF: Reinforcement Learning with Human Feedback. Can be trained to be helpful, honest and harmless. More useful.

## 1.2 Guidelines for Prompting
- First Principle: Clear and specific instructions
  - Tactic 1: Use delimiters to clearly indicate distinct parts of the input. Using delimiters prohibits prompt injections
  - Tactic 2: Ask for a structured output. With detail of structure parameters.
  - Tactic 3: Ask the model to check whether some conditions are satisfied (if-else)
  - Tactic 4: Few shot prompting: give few successful examples
- Second Principle: Give the model time to think
  - Tactic 1: Specify the steps required to complete a task. Define clear format.
  - Tactic 2: Instruct the model to work out its own solution before rushing to a conclusion.
- Model Limitations
  - Doesn't know boundaries of its knowledge well
  - Hallucinations: Makes statement which sounds plausible but not true
  - Ask model to first find relevant information, and answer based on that