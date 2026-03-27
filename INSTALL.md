# Installing Ask Scott Adams

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and working

## Installation

```bash
claude install-plugin github:cdeistopened/scott-adams-wiki
```

Or add the plugin directory manually:

```bash
# From your project directory
claude plugin add /path/to/scott-adams-wiki/plugin
```

Or add it to your `.claude/settings.json`:

```json
{
  "plugins": [
    "/path/to/scott-adams-wiki/plugin"
  ]
}
```

## First Question to Try

```
How do I persuade someone who disagrees with me?
```

This routes to the Persuasion Audit and Reframe Engine — Adams' core toolkit. It asks what you're trying to persuade them of, runs your approach through his 7 persuasion filters (visual, identity, emotion, simplicity, pacing, anchoring, high-ground), and shows you where you're losing them.

## Other Good Starting Questions

- "Analyze this sales pitch — is it persuasive?"
- "What's my talent stack?"
- "Analyze this news story through the two movies lens"
- "How do I build a systems approach instead of setting goals?"
- "Teach me the full Adams persuasion framework"

## Troubleshooting

- **Skills not showing:** Make sure the plugin path is correct and Claude Code has been restarted
- **Transcripts not found:** The plugin references data in relative paths — ensure the full wiki directory is present
- **Generic answers:** Try invoking a specific skill directly: `/ask-scott-adams:persuasion-audit`

## Learn More

Visit [creativeintel.agency](https://creativeintel.agency) for more Ask [Creator] plugins.
