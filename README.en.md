# Family Mentor: Think Through Relationships and Emotions With AI

[简体中文](README.md) | [English](README.en.md)

When family conflict or a recurring emotion leaves you stuck, this skill guides your AI to understand what happened before offering advice. It uses questions to help you separate facts, feelings, and interpretations. You can challenge its interpretation, ask for practical suggestions, or stop at any time.

The public package includes a main entry skill and one self-awareness module. It can help explore recurring anxiety, self-evaluation, and familiar reactions in relationships. Other family modules are not included. It cannot know what an absent family member thinks and does not provide psychotherapy.

## Install and Use

Use an AI client that supports Agent Skills. No additional API key is required; the skill uses your client's existing model configuration.

```bash
npx -y skills add Ptothez/family-mentor-skill -g --all
```

For example, ask:

> Use Family Mentor to help me understand why even a small criticism makes me angry. I am not sure what I am afraid of.

The AI should first establish what help you want, then work from a concrete experience. It should not prolong a conversation just to complete a questionnaire.

## How It Helps

- Check what happened before discussing possible explanations.
- Use exceptions and different situations to examine claims such as "I always do this."
- Change direction or stop when questions stop producing useful information.
- Avoid treating one family history as a universal explanation.

Method files are in each skill's `references` directory. Install both `family-mentor` and `family-mentor-self-awareness`: the entry skill selects the module, and the module guides the conversation.

## Privacy and Limits

This repository contains no author's private conversations, forms, family cases, private knowledge base, or account configuration. The skill does not upload files by itself. Whether your conversation reaches a cloud service and how it is stored depend on your AI client and model provider. Installation does not make sensitive conversations local-only.

These are AI conversation guidelines, not a clinically validated treatment. They do not replace mental health or medical services. Immediate danger calls for appropriate local emergency assistance and professional support.

Validation covers public files, references, and installation integrity. Simulated dialogue does not establish real counseling effectiveness.

## License

MIT; see [LICENSE](LICENSE).
