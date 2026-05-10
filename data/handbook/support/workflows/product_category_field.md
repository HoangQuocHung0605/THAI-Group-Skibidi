---
title: Product Category Field
description: "How to use the Product Category field and ZenDuo prompt to categorize support tickets"
category: Closing tickets
---

## Overview

This document provides information about the custom Zendesk field "Product Category", and how to populate it.  This is an expected part of the Closing phase of ticket handling.

## What is the Product Category field?

The Product Category field is a multi-select field in Zendesk that helps us identify which GitLab product areas are at the heart of each support ticket. This field is not yet required to be populated before setting any ticket to **Solved** status, however it is a highly beneficial field for providing customer insights to our product and development teams.

The data collected through this field enables:

- Analytics on which GitLab features generate the most support volume
- Trend identification for product team feedback
- Improved knowledge management and documentation prioritization

The options in the field have been populated from the [categories.yaml](https://gitlab.com/gitlab-com/www-gitlab-com/blob/master/data/categories.yml) file.

## Using the Product Category field

### When to populate the field

The Product Category field needs to be populated as part of the ticket closure process, though it can be updated at any time prior to the ticket closing. Setting the ticket to "Solved" will often be the most appropriate time to set this, as we tend to gain information during the course of solving a ticket that helps us better understand what was the primary cause of the problem the customer experienced.

### How to populate the field

You can populate the Product Category field in two ways:

1. **Manual selection**: If you clearly know which category applies to the ticket, select the appropriate options directly from the multi-select field. More than one category can apply to a single ticket.

2. **ZenDuo assistance**: Use the "Product Category" [ZenDuo prompt](#using-the-zenduo-product-category-prompt) to help identify the most relevant categories based on the ticket content.

3. **Engineering Directory tool assistance**: If you know the feature/s the ticket is related to, you can use the [Engineering Directory](https://gitlab-com.gitlab.io/support/toolbox/engineering-directory/) to identify which category that feature belongs to.

## Using the ZenDuo "Product Category" prompt

### What is the ZenDuo Product Category prompt?

The ZenDuo "Product Category" prompt is a specialized prompt designed to analyze ticket content and suggest appropriate Product Category selections. This prompt was developed through extensive iteration to provide consistent and helpful categorization suggestions. As an LLM tool, it won't always get it right, but generally it gets us close enough to be helpful.

### How to use the ZenDuo prompt

**NOTE**: The prompt takes some time to process - it will send at least 4 chunks of data to Duo Chat, and depending on the ticket complexity, it could be significantly more. It is recommended to set it running while you work on other tickets in different tabs.

To use the ZenDuo Product Category prompt:

1. Navigate to the ticket you want to categorize
2. Open ZenDuo App
3. Select the "Product Category" prompt and wait for the suggested categories.
4. Use the suggestions to populate the Product Category field. (This is a manual step for now.)

The suggestions are expected to be reported by ZenDuo in the following format, where the %age is an indicator of confidence in the category being relevant to the cause of the ticket.  It will not return any suggestions that are below 76% confidence.

```markdown
Pipeline Composition | 92% | Pipeline failed during merge request
Compliance Management | 78% | Branch protection rules not enforced
```

### Expected behavior and limitations

- The prompt analyzes the entire ticket conversation to identify relevant product areas
- Results are generally consistent, but may occasionally provide unhelpful suggestions
- Processing time varies based on ticket length and complexity
- Manual review of suggestions is always recommended before field completion

### When the prompt doesn't work well

If you find the ZenDuo prompt consistently providing unhelpful results for certain types of tickets, please provide feedback through the [feedback issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/7020). This helps improve the prompt's effectiveness over time.

## Troubleshooting

### Common issues

- **"I'm sorry, you have not selected a default GitLab Duo namespace"**: Navigate to [User Preferences](https://gitlab.com/-/profile/preferences) and select a **Default GitLab Duo namespace**. If you're unsure which to choose, select `GitLab.com`.
- **ZenDuo prompt takes too long**: This is expected behavior for complex tickets. Consider starting the prompt early in your ticket work or while handling other tasks.
- **Prompt suggests irrelevant categories**: Manual review and selection is always recommended. Use your judgment to select the most appropriate categories. Provide feedback in the feedback issue as the prompt may need tweaking. You can also use the Chat feature of ZenDuo and add a follow up prompt of "those categories are not in the filtered-categories.yml file"

### Getting help

If you encounter issues with the Product Category field or ZenDuo prompt:

- Provide feedback ([feedback issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/7020)) on prompt effectiveness to help improve future iterations

### References

- [Roadmap issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/6859) where this was introduced
