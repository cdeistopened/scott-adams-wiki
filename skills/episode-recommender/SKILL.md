---
name: episode-recommender
description: "Find the right Coffee with Scott Adams episode to listen to based on a topic, framework, or question. Use when someone says 'what episode should I listen to', 'find me an episode about', 'which episode covers', 'recommend an episode', or 'where does Adams talk about X.' Searches transcripts and recommends specific episodes with timestamps and key quotes."
---

# Episode Recommender

Search 1,151 episodes of Coffee with Scott Adams and recommend the best episodes for a given topic, framework, or question.

## How to Run This

Ask: "What topic, framework, or question are you interested in?"

Then search the transcript archive and recommend 3-5 episodes, ranked by relevance and quality.

## Search Strategy

1. **First:** Check `references/frameworks/` for a relevant framework article — these already cite the best episodes
2. **Second:** Check `references/indexes/by-framework.md` and `references/indexes/by-domain.md` for episode lists
3. **Third:** Search polished transcripts (389 files) at `data/coffee-with-scott-adams/polished/` — these are cleaner
4. **Fourth:** Search all episodes (1,151 files) at `data/coffee-with-scott-adams/episodes/` for broader coverage

## Recommendation Format

For each recommended episode:

```
### [Episode Title]
**Date:** YYYY-MM-DD | **Duration:** XX:XX | **File:** [filename]

**Why this one:** [1-2 sentences on what makes this episode particularly good for the topic]

**Key quote:** "[A representative quote from the episode]" [timestamp if available]

**Also covers:** [Other topics discussed in this episode]
```

## Topic-to-Episode Quick Map

Use this for common queries before searching transcripts:

| Topic | Start With |
|-------|-----------|
| Cognitive dissonance tells | Episode 81 (2018-06-14, "How to Spot Cognitive Dissonance") — the definitive episode |
| Kill shots | Win Bigly discussion episodes, Trump nickname analysis episodes |
| Talent stack | Episodes referencing *How to Fail at Almost Everything* |
| Persuasion filter | Early 2016 episodes where he laid out the thesis |
| Two movies on one screen | Any episode after Nov 2016 — he uses this framework daily |
| Affirmations | Episodes discussing *How to Fail*, personal development episodes |
| Loserthink | 2019 book promotion episodes, episodes diagnosing thinking errors |
| Trump Master Persuader | September 2015 through November 2016 episodes |
| Moist robot | Hypnosis background episodes, persuasion technique deep-dives |

## Listening Tips

Share with the user:
- Episodes start with the "simultaneous sip" ritual — it's a pacing technique, not just a gimmick
- Adams's best teaching happens when he goes to the whiteboard (video episodes)
- The show is solo — no guests, no editing, just Adams thinking out loud
- Political content is heavy — if the user wants frameworks without politics, recommend the book-focused episodes and the whiteboard teaching episodes

## Related Skills

- **ask-scott-adams** — The concierge router helps identify the right skill before searching episodes. If the user needs a framework applied rather than an episode to listen to, route them there first.
