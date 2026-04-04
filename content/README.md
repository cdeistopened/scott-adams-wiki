# Scott Adams Wiki

An interconnected knowledge graph built using the **Personal OS.wiki** methodology.

## Current State

| Category | Files | Status |
|----------|-------|--------|
| Domains | 4 | Complete overviews |
| Frameworks | 37 | 5 full articles, 32 scaffolds |
| Cases | 7 | 1 full article, 6 scaffolds |
| People | 46 | All scaffolds |
| **Total** | **95** | |

### Full Content (Evergreen/Budding)

These articles have been fully written with Quality Loop validation:

**Frameworks:**
- `two-movies-on-one-screen.md` - Evergreen (canonical example)
- `cognitive-dissonance.md` - Budding
- `word-salad.md` - Budding
- `reframing.md` - Budding
- `systems-vs-goals.md` - Budding

**Cases:**
- `fine-people-hoax.md` - Full case study

### Scaffolds (Seedling)

All other files contain:
- Frontmatter with metadata (type, mentions, episodes, related)
- Section templates to be filled
- Wikilink placeholders

## Architecture

```
scott-adams-wiki/
├── index.md              # Home page with navigation
├── README.md             # This file
├── domains/              # 4 broad categories
│   ├── perception.md
│   ├── persuasion.md
│   ├── prediction.md
│   └── lifestyle.md
├── frameworks/           # 37 named concepts
│   ├── two-movies-on-one-screen.md
│   ├── reframing.md
│   └── ...
├── cases/                # 7 example events (written once, linked everywhere)
│   ├── fine-people-hoax.md
│   ├── covid-response.md
│   └── ...
├── people/               # 46 recurring figures
│   ├── joe-biden.md
│   ├── elon-musk.md
│   └── ...
└── episodes/             # To be populated from transcripts
```

## Key Design Principles

1. **Cases are written once** - Examples like Charlottesville live in `/cases/` and are linked from multiple frameworks. No repeating stories.

2. **Wikilinks create the graph** - `[[two-movies-on-one-screen]]` creates bidirectional connections.

3. **Maturity levels** - Each file has a `maturity` field: seedling → budding → evergreen

4. **Source stats** - Each framework shows mention count and episode count from entity extraction.

## Next Steps

### Immediate
1. Fill remaining framework scaffolds with content from source chunks
2. Link frameworks to specific episodes
3. Populate `/episodes/` folder from transcript data

### Publishing
- Configure Quartz 4 for static site generation
- Enable graph view for relationship visualization
- Deploy to scottadams.wiki domain

## Source Data

Built from:
- ~1,200 episodes of "Coffee with Scott Adams"
- ~1,145 transcribed episodes
- ~5,600 embedded chunks (Qdrant)
- ~740 entity-extracted episodes

## Methodology

See `/wiki-architecture/` for:
- `SCHEMA.md` - Full schema design
- `PROCESS.md` - Replicable 10-phase pipeline

This methodology is designed to be replicable for any thinker's corpus (Ray Peat, Naval, etc.).
