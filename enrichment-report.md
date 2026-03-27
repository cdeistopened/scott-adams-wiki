# Scott Adams Plugin Enrichment Report

**Date:** 2026-03-26
**Auditor:** Claude Code (Opus 4.6)

---

## Inventory Before Audit

| Category | Count |
|----------|-------|
| Skills | 12 (6 Decision, 4 Tutor, 1 Utility, 1 Router) |
| Framework articles | 36 |
| Decomposition reports | 5 (pipeline artifacts, not user-facing) |
| Index files | 2 (by-domain, by-framework) |

## Orphan Analysis

**10 framework articles** had zero references from any SKILL.md:

| Orphan Article | Domain | Resolution |
|----------------|--------|------------|
| `analogies-dont-persuade` | persuasion | Wired to persuasion-audit (Filter 1 negative case), persuasion-masterclass, loserthink-workshop |
| `audience-of-one` | persuasion | Wired to persuasion-audit, persuasion-masterclass, negotiation-strategist (new skill) |
| `authoring-others` | systems | Wired to reframe-engine, moist-robot-hypothesis, systems-designer, negotiation-strategist |
| `ego-as-tool` | persuasion | Wired to persuasion-audit, persuasion-masterclass, moist-robot-hypothesis, negotiation-strategist |
| `forty-eight-hour-rule` | prediction | Wired to prediction-scorecard, media-decoder |
| `golden-age` | prediction | Wired to prediction-scorecard, systems-designer |
| `halfpinion` | cognition | Wired to loserthink-workshop, prediction-scorecard, media-decoder |
| `progression-of-awareness` | cognition | Wired to loserthink-workshop, media-decoder |
| `removing-the-reason` | persuasion | Wired to persuasion-masterclass, reframe-engine, negotiation-strategist (new skill) |
| `shake-the-box` | persuasion | Wired to persuasion-masterclass, reframe-engine, negotiation-strategist (new skill) |

**5 decomposition reports** are unreferenced but correctly so. They are pipeline input artifacts (source material for the build process), not user-facing framework articles. No wiring needed.

**2 index files** (by-domain, by-framework) were already referenced by ask-scott-adams and episode-recommender. No action needed.

## New Skill Built

### negotiation-strategist (Decision Skill)

**Rationale:** Three rich orphan articles (removing-the-reason, shake-the-box, audience-of-one) form a natural cluster around negotiation and dealmaking. Adams analyzed Trump's negotiation playbook across hundreds of episodes. The existing plugin had no skill for applying these frameworks to real negotiations.

**Structure:** 5-tool diagnostic (Audience of One, Remove the Reason, Shake the Box, Pacing Before Leading, Anchoring) with structured strategy output template.

**References consumed:** `removing-the-reason.md`, `shake-the-box.md`, `audience-of-one.md`, `pacing-and-leading.md`, `anchoring.md`, `ego-as-tool.md`, `authoring-others.md`, `thinking-past-the-sale.md`

**Location:** `plugin/skills/negotiation-strategist/SKILL.md`

## Cross-Pollination Enrichment

### 1. Jab/Hook Persuasion Ratio (from GaryVee)

**Source:** `garyvee-wiki/plugin/references/frameworks/jab-jab-jab-right-hook-framework.md`

**Thesis:** GaryVee's 3:1 jab-to-hook ratio maps directly onto Adams's pacing-and-leading. Pacing IS jabbing (delivering value). Leading IS the right hook (making the ask). Most persuaders fail because they lead without pacing, the same way most content creators over-hook.

**Key contribution:** Turns pacing-and-leading from a qualitative concept ("pace before you lead") into a quantifiable discipline ("3-4 paces per lead"). Introduces the concept of "reframe jabs" -- delivering a useful reframe without an ask accumulates persuasion trust.

**Wired to:** persuasion-audit, persuasion-masterclass

**Location:** `plugin/references/frameworks/jab-hook-persuasion-ratio.md`

### 2. Data Hook Persuasion (from Hormozi)

**Source:** `hormozi-wiki/plugin/references/frameworks/content-as-lead-gen.md`

**Thesis:** Hormozi's "lead with a specific number" principle works because data hooks simultaneously activate three of Adams's strongest persuasion mechanisms: visual persuasion (numbers are "visible"), anti-analogy (numbers bypass the analogy-critique circuit), and anchoring (the first number on the table frames everything).

**Key contribution:** Introduces the concept of "data kill shots" -- specific numbers that are visual, sticky, and carry seeds of truth, but are harder to counter than label kill shots because data can only be disputed with better data.

**Wired to:** persuasion-audit, persuasion-masterclass

**Location:** `plugin/references/frameworks/data-hook-persuasion.md`

## Inventory After Audit

| Category | Before | After | Delta |
|----------|--------|-------|-------|
| Skills | 12 | 13 | +1 (negotiation-strategist) |
| Framework articles | 36 | 38 | +2 (cross-pollination) |
| Orphan frameworks | 10 | 0 | -10 (all wired) |
| Skills modified | 0 | 8 | persuasion-audit, persuasion-masterclass, reframe-engine, loserthink-workshop, prediction-scorecard, media-decoder, systems-designer, moist-robot-hypothesis |

## Skills Modified (Summary of Wiring)

| Skill | Frameworks Added |
|-------|-----------------|
| persuasion-audit | +analogies-dont-persuade, +audience-of-one, +ego-as-tool, +jab-hook-persuasion-ratio, +data-hook-persuasion |
| persuasion-masterclass | +analogies-dont-persuade, +audience-of-one, +ego-as-tool, +removing-the-reason, +shake-the-box, +jab-hook-persuasion-ratio, +data-hook-persuasion |
| reframe-engine | +removing-the-reason, +shake-the-box, +authoring-others |
| loserthink-workshop | +halfpinion, +progression-of-awareness, +analogies-dont-persuade |
| prediction-scorecard | +forty-eight-hour-rule, +golden-age, +halfpinion |
| media-decoder | +forty-eight-hour-rule, +halfpinion, +progression-of-awareness |
| systems-designer | +authoring-others, +golden-age |
| moist-robot-hypothesis | +authoring-others, +ego-as-tool |

## Remaining Gaps (Not Addressed)

1. **No plugin.json** in `.claude-plugin/` -- flagged in wiki-projects CLAUDE.md, not addressed here
2. **Decomposition reports not user-facing** -- correct as-is, but could be surfaced as "how this plugin was built" documentation
3. **CLAUDE.md router** needs update to include negotiation-strategist in skill listing
4. **22 framework articles need enrichment** per wiki-projects CLAUDE.md -- this audit wired orphans but did not enrich thin articles
