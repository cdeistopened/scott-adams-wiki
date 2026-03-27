---
name: prediction-scorecard
description: "Evaluate a prediction, forecast, or bet using Scott Adams' prediction methodology and assign a confidence score. Use when someone says 'is this prediction good', 'should I bet on this', 'how confident should I be', 'evaluate this forecast', 'what's the probability of X', 'is this person right about Y', or 'calibrate my prediction.' Applies Adams' prediction framework and scores the prediction."
---

# Prediction Scorecard

Evaluate any prediction, forecast, or bet using Scott Adams' prediction methodology from Coffee with Scott Adams. Adams made his reputation by calling the 2016 election when almost nobody else did — and he has a specific framework for how he evaluates predictions.

## When to Use

The user has a prediction (their own or someone else's) and wants to evaluate whether it's well-calibrated. Or they want to understand why a past prediction succeeded or failed.

## How to Run This

Ask: "What's the prediction you want to evaluate? Be specific — who predicted what, when, and what would 'right' and 'wrong' look like?"

Then run through each diagnostic filter.

---

## The Prediction Diagnostic

### Filter 1: Mechanism Check

Adams distinguishes between predictions based on a model (testable mechanism) vs. predictions based on vibes (tribal affiliation, emotional preference, pattern matching from one example).

**Questions:**
- Does the prediction specify a mechanism — a WHY, not just a WHAT?
- Could you explain the mechanism to someone from a different political/cultural tribe and have it still make sense?
- Or is the prediction really just "I want this to happen" dressed up as analysis?

**Adams's principle:** "A good prediction tells you both what will happen AND why. If the person can't explain the mechanism, they're just guessing in a way that flatters their worldview."

**Red flag:** If the prediction aligns perfectly with the predictor's political team and the mechanism is vague ("it just feels like the momentum is going that way"), score this filter low.

### Filter 2: Track Record Audit

Adams is obsessive about track records. His central argument: the value of a prediction framework is measured by its past accuracy, not by how smart it sounds.

**Questions:**
- What is this person's track record on similar predictions?
- Have they made public predictions before that we can check?
- If this is your first prediction on a topic, whose track record on this topic should you weight most heavily?

**Adams's principle:** "I can't tell you who's right. I can tell you whose filter on the world has produced the most accurate predictions. Bet on the filter with the best track record."

**Red flag:** If the person has never made a checkable prediction before, or if they only cite their hits and never their misses, the prediction should be heavily discounted.

### Filter 3: The Two Movies Test

**Questions:**
- Is there a "Movie B" — a completely different and internally consistent interpretation of the same facts that leads to the opposite prediction?
- How confident is the predictor that Movie B is wrong?
- Can the predictor steelman Movie B, or do they dismiss it as crazy?

**Adams's principle:** If the predictor cannot articulate the strongest version of the opposing view, they are likely in cognitive dissonance rather than analysis.

**Score:** High confidence is only justified when the predictor can articulate Movie B and explain specifically why it predicts worse.

### Filter 4: Unfalsifiability Check

**Questions:**
- What would make this prediction wrong? Can the predictor specify?
- Is there a timeline? (An undated prediction can never be wrong — it's "just not right yet")
- Are the success criteria specific enough to score?

**Adams's diagnostic tells for bad predictions:**
- **Unspecific doom forecast:** "This could tear apart the fabric of civilization" — What does that look like? How do you measure it?
- **Moving goalposts:** "Well, what I really meant was..." after the prediction fails
- **Retroactive reinterpretation:** "I was right about the direction, just not the timing"

**Score:** A prediction that specifies what, when, and what constitutes success/failure scores high. A vague directional statement with no timeline scores low.

### Filter 5: Base Rate Check

**Questions:**
- What usually happens in situations like this? (The base rate)
- Is this prediction claiming something unusual will happen?
- If yes, is the evidence for deviation from base rate proportional to how unusual the claim is?

**Adams's insight:** Most predictions fail because they predict something unusual without proportional evidence. The boring prediction (things continue roughly as they are) is right most of the time.

### Filter 6: Black Swan Vulnerability

Adams's biggest prediction miss was pre-COVID 2020 Trump landslide. His post-mortem: the persuasion filter is excellent at predicting outcomes in stable environments but cannot account for black swan events.

**Questions:**
- What external event could invalidate this prediction regardless of its logical soundness?
- Is the prediction robust to disruption, or does it assume stable conditions?
- Has the predictor accounted for "things I can't predict but that would change everything"?

---

## Scoring Summary

| Dimension | Score | Notes |
|-----------|-------|-------|
| Mechanism (model vs. vibes) | /10 | |
| Track Record | /10 | |
| Two Movies (steelman opposition) | /10 | |
| Falsifiability | /10 | |
| Base Rate Awareness | /10 | |
| Black Swan Robustness | /10 | |
| **Overall Confidence** | **/60** | |

## Confidence Translation

| Score | Confidence Level | Adams Would Say |
|-------|-----------------|-----------------|
| 50-60 | Very High | "I would bet money on this" |
| 40-49 | High | "My filter says this is likely, but I've been wrong before" |
| 30-39 | Moderate | "I lean this way but I can see the other movie" |
| 20-29 | Low | "Too many unknowns to have real confidence" |
| 10-19 | Very Low | "This is a guess dressed up as a prediction" |
| 0-9 | Coin Flip | "Nobody knows, and anyone who says they do is hallucinating" |

## Closing

After scoring, ask: "Based on this analysis, do you want to adjust your prediction, or do you want to think through what would need to change for the opposing view to be correct?"

## Related Skills

- **media-decoder** — Both use the "two movies" test, but the decoder applies it to news narratives while the scorecard applies it to specific predictions.
- **reframe-engine** — Prediction is Lens 6 in the reframe engine. Use the reframe engine for broader problem-solving; use the scorecard for focused prediction evaluation.
- **loserthink-workshop** — Both diagnose thinking errors. The workshop catches base rate neglect, unfalsifiability, and confirmation bias — the same errors that make predictions fail.

## Related Frameworks

- `prediction-methodology.md` — The full prediction framework article
- `two-movies-on-one-screen.md` — The two movies test used in Filter 3
- `forty-eight-hour-rule.md` — Wait 48 hours before judging a controversy; initial facts are almost always wrong
- `golden-age.md` — Adams's contrarian optimism thesis: tech drives prosperity invisible to those focused on political noise
- `halfpinion.md` — A complaint without an alternative; diagnostic for weak predictions disguised as analysis
