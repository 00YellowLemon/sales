---
name: autonomous-ab-tester
description: Sets up autonomous A/B testing loops to optimize internal metrics. Use when tasked with improving a funnel, optimizing a UI component, or running data-driven product experiments without human intervention.
---

# Autonomous A/B Tester

This skill implements an autonomous loop for continuous product optimization. It enables an AI agent to act like a Chief Product Officer: analyzing metrics, hypothesizing improvements, deploying tests, evaluating results, and shipping the winner.

## Core Principles

1.  **Throw Tokens at the Problem**: Leverage compute to continuously run optimization cycles in the background.
2.  **End-to-End Autonomy**: The agent must be capable of traversing the entire loop: analysis -> hypothesis -> code generation -> deployment -> evaluation.
3.  **Measurable Impact**: Every change must be tied to a clear, quantitative metric (e.g., conversion rate, click-through rate, API latency).

## Workflow

To establish an autonomous A/B testing loop, implement the following phases:

### Phase 1: Analysis and Hypothesis
1.  Ingest product analytics or telemetry data.
2.  Identify the area with the highest friction or lowest performance.
3.  Research best practices and formulate a testable hypothesis (e.g., "Changing the CTA from 'Submit' to 'Get Started' will increase conversion").

### Phase 2: Implementation
1.  Generate the code for the new variant (Variant B).
2.  Implement a routing mechanism to split traffic (e.g., 50/50) between the control (Variant A) and Variant B.
3.  Ensure telemetry is accurately tracking the target metric for both variants.

### Phase 3: Deployment and Evaluation
1.  Deploy the test and allow it to run for a statistically significant period (e.g., one week, or until N events occur).
2.  Evaluate the results. If Variant B outperforms Variant A with statistical significance, promote Variant B to 100% of traffic.
3.  If Variant B fails, discard it, retain the learning, and generate a new hypothesis.

## Infrastructure Requirements

To succeed, the system needs:
*   **Analytics Access**: Read access to a database or analytics API (e.g., PostHog, Mixpanel).
*   **Deployment Access**: The ability to modify code, commit to a branch, and ideally trigger a deployment (via CI/CD or direct server modification for internal tools).
*   **Feature Flagging**: A simple mechanism to toggle features on and off for specific user sessions.

## Best Practices
*   **Start Small:** Begin by optimizing internal tools or non-critical funnels before unleashing the agent on the primary revenue-generating checkout flow.
*   **Guardrails:** Implement safety checks to ensure the generated code does not break the build or introduce syntax errors before routing traffic to it.
