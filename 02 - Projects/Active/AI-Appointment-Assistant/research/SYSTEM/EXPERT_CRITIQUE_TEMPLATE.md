# EXPERT CRITIQUE LOG

This file tracks world-expert feedback for every project deliverable.
Format: [Date] | [Deliverable] | [Expert Role] | [Issue] | [Severity] | [Status]

---

## How to Use

1. Before marking any deliverable as "done," run it through all 5 expert roles
2. Log every issue found (even minor ones)
3. Fix critical/high severity issues before proceeding
4. Re-run experts after fixes to confirm resolution

## Expert Roles

### 1. SRE / Reliability Engineer
- "What happens when this component fails?"
- "Is there retry logic? Circuit breaker? Fallback?"
- "How do we know it failed? What alerts fire?"
- "What's the blast radius if this goes down?"

### 2. Security Engineer
- "What user inputs does this accept? Are they validated?"
- "Are any secrets or keys exposed in code or logs?"
- "Is rate limiting in place?"
- "What PII is collected, stored, or transmitted?"

### 3. UX Designer
- "Can a non-technical user complete the flow without help?"
- "How many steps/screens does it take?"
- "What happens when something goes wrong from the user's perspective?"
- "Is the language clear and jargon-free?"

### 4. Cost / FinOps Analyst
- "What's the token cost per conversation?"
- "What's the monthly cost at 100/1000/10000 users?"
- "Where are the cost surprises?"
- "Is there a token budget or spending cap?"

### 5. Domain Expert
- "Does this handle all real-world scenarios?"
- "What edge cases are missing?"
- "Are business rules complete and unambiguous?"
- "Does this comply with relevant regulations?"

---

## Critique Log

<!-- Add entries below this line -->
