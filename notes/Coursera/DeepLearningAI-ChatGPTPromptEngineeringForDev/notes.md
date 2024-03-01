# ChatGPT Prompt Engineering for Developers

## Introduction
- **Objective:** Utilize Large Language Models (LLMs) to rapidly develop innovative applications with the OpenAI API.
- **Key Learning Areas:**
  1. Fundamentals of LLM operation.
  2. Best practices in prompt engineering.
  3. Using LLM APIs for various tasks (summarizing, inferring, transforming, expanding content).
- **Foundational Principles:** Introduction to two essential principles for effective prompt engineering.
- **Hands-On Practice:** Includes exercises in Jupyter notebooks and building a custom chatbot.
- **LLM Types:**
  - **Base LLM:** Focuses on predicting the next word based on training data.
  - **Instruction-Tuned LLM:** Aimed at following instructions with enhancements for being helpful, honest, and harmless through fine-tuning and RLHF (Reinforcement Learning with Human Feedback).

## Guidelines for Prompting
### 1. First Principle: Clear and Specific Instructions
- **Tactics:**
  1. Delimiters to separate input parts and prevent prompt injections.
  2. Structured outputs with detailed parameters.
  3. Conditional logic (if-else) checks.
  4. Few-shot prompting with example outcomes.
### 2. Second Principle: Allow Adequate Processing Time
- **Tactics:**
  1. Define task steps and formats.
  2. Encourage solution development before conclusion.
### 3. Model Limitations Awareness
- Recognizing:
  1. Knowledge boundaries.
  2. Hallucination risks.
  3. Importance of basing responses on relevant information.

## Iterative Prompt Building
- **Process Overview:**
  1. Idea Generation
  2. Implementation (Prompt Creation)
  3. Experimental Testing
  4. Error Analysis
  5. Refinement
- **Tips:** Adjust prompt length and refine with a batch of examples for optimal results.

## Summarizing Techniques
- **Types of Summarization Prompts:**
  1. Generic summarization for broad application.
  2. Purpose-specific summarization focusing on relevant information extraction.

## Inferring Insights
- **Process:**
  1. From Input to Analysis
- **Examples:**
  1. Label identification.
  2. Sentiment analysis.
  3. Topic detection.
- **Strategies:** Use prompts like "What is the sentiment of..." or "Identify a list of emotions..."

## Transforming Content
- **Conversion Examples:**
  1. Language translation.
  2. Spelling and grammar correction.
  3. HTML to JSON conversion.
  4. Informal to formal tone adjustment.
  5. Style and tone modifications.

## Expanding Ideas
- **Use Case:** Generating responses to customer reviews.
- **Temperature Control:**
  - Low temperature for predictability.
  - High temperature for creativity.

## Building a Chatbot
- **Approach:**
  1. Input: Series of messages.
  2. Output: Model-generated response.
- **Roles:**
  1. System: Sets assistant behavior and conversation frame.
  2. User: Provides message input.
  3. Assistant: Delivers GPT-generated response.
- **Context Management:** Use message JSONs with role and content for setup.

## Conclusion
- Highlight on responsible and ethical use of LLMs in development.
