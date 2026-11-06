# Self Insight · 自观

A conversational skill for understanding personal difficulties and clarifying relationships and responsibilities. It chooses one primary module and consults supporting modules when needed.

[中文](README.md)

**9 modules · 13,521 searchable knowledge records · Cases & concept relationships**

![Self Insight: nine modules, seven-step self-awareness and 13,521 knowledge records](assets/module-map.png?v=20261106-13521)

| Module | Purpose |
|---|---|
| Self-awareness | Explore recurring feelings, self-judgments and relationship patterns |
| Boundaries | Clarify responsibilities, communicate limits and respond to violations |
| Understanding Emotions | Understand emotional interactions between children and caregivers |
| Rules & Actions | Explore parenting expectations, behavior and relationships |
| Dependency & Loss of Control | Understand children's dependency problems and support options |
| Stages & Roles | Adapt expectations to developmental stages |
| Inner Capacities | Explore conditions for autonomy, self-control and empathy |
| Personal Practice | Support caregivers through self-care, learning and communication |
| Focus | Distinguish environmental distractions, development and children's attention difficulties |

Display names do not broaden the original scope. Parenting material is not automatically applied to adults. Self-awareness may consult other modules without presuming a family cause.

## Contents and use

One entry point and nine modules, with 600 runtime files and 13,521 searchable knowledge records. This total combines the original 477 atoms with 13,044 expanded structured records, extracted and checked against 242 supplied texts. The original 54 knowledge and case files and dialogue methods are preserved. Search covers both layers and follows conditional links between them.

Records include concepts, procedures, cases, applicability conditions and limits. Record counts are not counts of unique concepts. Original transcripts, private notes, identity mappings and internal audit material are neither distributed nor required to use the skill.

Install all ten skills:

```sh
npx -y skills add Ptothez/self-insight-skill --skill '*'
```

The installer guides you through supported agents and installation scope. Keep all ten directories together with their original names. Installation requires Node.js / npx; use requires an agent that supports skills. Local knowledge search uses the Python 3 standard library, with no API, account or additional Python packages. Without Python, the agent can follow the included Markdown module indexes and read the knowledge files.

For example: "Use Self Insight to explore why I feel guilty after saying no." You may also specify a module. It follows facts and responses rather than a fixed number of questions. Cases are recorded only on explicit request.

It answers using the included knowledge and what you share. It asks for missing facts when they matter. Original documents are needed only when you request a check against a specific source. Missing information is not invented; unanswered questions remain explicit.

For example, a conversation may start with why a child's performance feels like a judgment of your worth, then move to practical responsibilities. The entry point keeps the known facts and consults Boundaries or another relevant module without restarting the story or assuming that every personal difficulty has a family cause.

## Limits

This supports reflection and conversation, not professional diagnosis or treatment. Acute safety risks take priority. Examples are not evidence that a user must have had a particular experience.

Documentation is bilingual. Core methods and knowledge remain in Chinese, without abridged translations replacing them. Other-language conversation quality depends on the model and has not been separately tested.
