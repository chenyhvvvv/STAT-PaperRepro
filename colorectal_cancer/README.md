# Colorectal Cancer — STAT Conversational Analysis

End-to-end demos of STAT analyzing a colorectal cancer spatial
transcriptomics dataset through multi-turn natural-language chat.
Each demo captures everything STAT produced: the generated Jupyter
notebook, the per-turn LLM prompt/response/code-execution logs, and
(for demo 1) UI screenshots of each turn.

<p align="center">
  <img src="demo_chat_turn.jpg" alt="Example STAT chat turn" width="650" />
</p>

The figure above shows one representative chat turn: user query →
STAT pipeline (query planning → skill selection → code generation) →
executed output and biological interpretation.

## Contents

| Demo | Date | LLM backbone | Turns |
| --- | --- | --- | --- |
| `CRC_analysis_demo_1/` | 2026-05-12 | GPT-5.5 (OpenAI) | 8 |
| `CRC_analysis_demo_2/` | 2026-04-17 | Claude-Sonnet-4.6 (Poe) | 7 |

Each demo folder contains:

- `analysis.ipynb` — the Jupyter notebook STAT produced during the session
- `turn_NNN_*.md` — full LLM prompt / response / code-execution log per turn
- `chat_screen_shot/` (demo 1 only) — UI screenshots of each turn

## Notes

API keys and absolute paths have been redacted from cell 0 of each
notebook. To re-run, replace `YOUR_API_KEY_HERE` with your own key
and point `session.load_dataset(...)` at the local CRC dataset.
