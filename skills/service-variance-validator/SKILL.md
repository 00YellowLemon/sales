---
name: service-variance-validator
description: Implements quality control checks to detect non-uniform outputs in AI-native service workflows. Use when building a service pipeline, validating outputs, or setting up automated QA for generative tasks.
---

# Service Variance Validator

This skill focuses on mitigating "variance" (non-uniform or inconsistent outputs) in AI-driven services. In AI-native service companies, inconsistency destroys trust and causes churn faster than slow speeds or high prices. This skill provides a framework for tracking and eliminating variance.

## Core Principles

1.  **Variance is an Existential Threat**: Customers pay for outcomes, not effort. The outcome must be highly predictable.
2.  **Process is the Product**: The internal workflow and Standard Operating Procedures (SOPs) are the actual product. They must be rigid enough to guarantee consistency.
3.  **Human-in-the-Loop for Judgment, Not Patching**: Use humans only where genuine domain judgment is required, not to paper over brittle AI logic.

## Workflow

When designing a workflow or reviewing an existing pipeline, implement the following variance reduction strategies:

### 1. Define the SOP (Standard Operating Procedure)
Force the AI agent to explicitly write out its step-by-step SOP before executing a task. This creates an audit trail and ensures the model isn't "freestyling."

### 2. Implement Step-Wise Validation
Break monolithic tasks into smaller, discrete steps. After each step, implement an automated verification check against predefined constraints.
*   *Example:* If extracting financial data, Step 1 extracts. Step 2 asserts that `Total Assets = Total Liabilities + Equity`. If it fails, halt and retry, or escalate to a human.

### 3. Establish Golden Responses
Maintain a repository of "golden" (perfect) inputs and outputs. Periodically run the system against these golden sets to detect drift or regression in quality.

### 4. Track Throughput and Cycle Times
Instrument the code to log how long each step takes and the overall cycle time. Treat these as primary product metrics. Look for high variance in cycle times as an indicator of a struggling or confused agent.

## Implementation Pattern

```python
# Conceptual implementation of step-wise validation
def process_claim(claim_data):
    # Step 1: Extraction
    extracted_entities = agent.extract(claim_data)

    # Step 2: Variance Validation
    if not validate_schema(extracted_entities, expected_schema):
         raise VarianceError("Output does not match expected schema")

    if not logical_consistency_check(extracted_entities):
         # Escalate to human-in-the-loop
         return route_to_human(claim_data, "Logical inconsistency detected")

    # Step 3: Final Generation
    return agent.generate_report(extracted_entities)
```

## Best Practices
*   **Fail Fast:** If the AI is uncertain or output format degrades, fail immediately rather than returning a hallucinated or malformed result to the customer.
*   **Cap Early Pilots:** When building a new workflow, artificially limit the number of inputs to prevent volume from masking variance issues.
