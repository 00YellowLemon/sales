---
name: continuous-knowledge-synthesizer
description: Processes human corrections, extracts domain knowledge, and updates internal knowledge bases. Use when a user provides feedback, corrects an AI response, or asks to update the system guidelines based on a conversation.
---

# Continuous Knowledge Synthesizer

This skill implements a self-improving, recursive loop. It allows an AI agent to learn from human corrections, extract the underlying domain knowledge, and persist it back into its own knowledge base (e.g., Markdown files) so the mistake is never repeated.

## Core Principles

1.  **Legibility**: All interactions, corrections, and feedback must be captured and made legible to the AI. If it isn't recorded, it didn't happen.
2.  **Autonomous Updating**: The AI should not wait for a human to update the documentation. It must summarize the correction and update the relevant files itself.
3.  **Diarization and Synthesis**: Raw interactions (like transcripts or long chat logs) are too noisy. They must be synthesized, categorized, and distilled into actionable "breadcrumbs" or rules.

## Workflow

When provided with a human correction or feedback on a previous output, execute the following steps:

### 1. Evaluate the Correction
Analyze the human's input. Identify exactly what the AI did wrong and what the correct behavior or fact is.

### 2. Extract the Skill/Knowledge
Formulate a generalized rule, skill, or piece of domain knowledge based on the correction. Separate the specific context of the current conversation from the underlying principle.

### 3. Locate the Target Repository
Identify the appropriate Markdown file or database where this knowledge belongs (e.g., a user manual, a style guide, or a specific domain knowledge file).

### 4. Synthesize and Inject
Update the target file. Do not simply append the raw conversation. Instead, weave the new rule organically into the existing structure. If the file is becoming too large, categorize the knowledge logically (e.g., "Fundraising", "Engineering Best Practices").

## Implementation Example (Conceptual)

If a user says: *"Don't format SQL keywords in lowercase, we strictly use uppercase."*

1.  **Evaluate:** AI used lowercase SQL; user requires uppercase.
2.  **Extract:** Rule: "All SQL keywords must be capitalized."
3.  **Locate:** Find `docs/coding_standards.md`.
4.  **Inject:** Add the rule under the "Database/SQL" section of the document.

## Best Practices
*   **Version Control:** Ensure updates are committed to version control so changes can be tracked and rolled back if necessary.
*   **Avoid Duplication:** Before adding a new rule, scan the document to ensure it doesn't conflict with or redundantly state an existing rule.
