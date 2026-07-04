---
name: ephemeral-dashboard-generator
description: Generates temporary, single-use internal dashboards or software tools on demand. Use when a user asks to build an internal tool, generate a quick dashboard for an event, or replace outdated internal software.
---

# Ephemeral Dashboard Generator

This skill enables Claude to rapidly generate temporary internal software, dashboards, and workflows based on high-level business context. It embodies the engineering practice of treating internal software as ephemeral while preserving the underlying business logic and data.

## Core Principles

1.  **Software is Ephemeral; Data is Precious**: Do not over-engineer internal tools. Treat them as disposable. The true value lies in the data and the embedded business context, not the code itself.
2.  **On-Demand Generation**: Create dashboards and tools only when needed for specific events, functions, or temporary processes.
3.  **One-Shot Regeneration**: Instead of maintaining and refactoring old internal codebases, discard the existing software when models or requirements improve and completely regenerate it from the original set of instructions.

## Workflow

When asked to create an internal tool or dashboard, follow this process:

### 1. Extract Business Context
Identify the specific function the software will serve (e.g., event management, product analytics tracking). Ensure you understand the desired inputs, required data layers, and expected outputs.

### 2. Isolate State and Data
Design the architecture so that the frontend and logic layers are completely stateless and decoupled from the data storage. All data (logs, emails, markdown records) must be stored in a persistent, precious data layer that outlives the application.

### 3. Generate the Ephemeral Application
Use the fastest available frameworks (e.g., lightweight Python/Flask, simple React, or single-file HTML/JS) to one-shot the application. Focus on immediate functionality rather than long-term maintainability.

### 4. Provide Regeneration Instructions
Provide the user with the exact prompt or set of instructions used to generate this tool. Instruct the user to save this prompt, so they can discard the tool and regenerate an improved version in a month or two when models advance.

## Best Practices

*   **Avoid Database Migrations:** For ephemeral tools, prefer simple, flexible storage (like JSON or Markdown files in a dedicated directory) if a formal database isn't strictly necessary.
*   **No CI/CD Overhead:** Do not set up complex deployment pipelines for these tools. They should be runnable locally with a single script or command.
*   **Document the "Why"**: The only documentation needed is the business context that explains *why* the tool was generated, to facilitate future regeneration.
