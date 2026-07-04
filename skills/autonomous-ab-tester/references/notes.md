# Notes: How to Build a Self-Improving Company with AI

## Rethinking Company Organization
- Outlines the traditional concept of companies structured like Roman legions, with nested hierarchies, spans of control, and human beings as conduits for passing orders down and sending information back up.
- Argues that assuming hierarchically organized companies are the optimal economic units of value is a broken mental model in the age of AI.
- Criticizes the approach of merely adding AI to existing workflows to make employees (like engineers) 20% more productive.
- Proposes reimagining companies by extracting domain knowledge, defining it as context or a set of skills, and using AI agents to autonomously execute workflows.

## The Self-Improving Loop
- Describes the ultimate goal of implementing AI: a self-improving, recursive loop.
- Example: An AI agent accesses sales documentation. When it answers a query poorly and a human corrects it, the agent evaluates the human correction, summarizes it, extracts the specific skill or domain knowledge, and adds it back to its own repository (e.g., in a markdown file).
- The next time the agent is asked the same query, it succeeds autonomously based on this self-improved skill set.
- Recommends identifying parts of the company that can function with this loop, placing humans in a monitoring or supervisory capacity, and leveraging compute ("throwing tokens at the problem") to continuously improve the company.

## Autonomous A/B Testing
- Gives the example of product analytics: an agent reviews product analytics to identify high friction parts of the sales funnel.
- The agent researches best practices, develops a solution, implements an A/B test, runs it autonomously for a week, evaluates the metrics, selects the winning variant, and deploys it.
- This creates a self-optimizing product loop running continuously without human intervention.

## Ephemeral Software and On-Demand Workflows
- Discusses making the entire organization legible to AI by recording absolutely everything: emails, Slack messages, DMs, office hours, and even verbal conversations.
- Notes the necessity of diarizing and synthesizing this massive data down into breadcrumbs to fit within AI context windows.
- Suggests every function in a company can generate its own software or dashboards on demand.
- Advocates for treating data and business context as precious, but treating the software layer as completely ephemeral.
- As models improve, the company should discard the previously generated software, provide the original set of instructions, and regenerate new, superior software.

## The New Role of Humans and Organizational Structure
- Asserts that middle management is effectively obsolete, arguing that AI should handle the coordination problem.
- Recommends building a company entirely of individual contributors (ICs), builders, and operators, with directly responsible, named individuals (not committees) in charge of execution.
- Emphasizes tracking token usage per employee as a proxy for engagement with AI, suggesting those maximizing token usage are exploring the boundaries of possibility.
- Envisions the AI system holding the company’s "brain" (data, skills, know-how) while humans sit at the edge, interfacing with reality in areas where models cannot go, such as high-stakes, high-emotion situations, ethical considerations, and real-world sales conversations.
