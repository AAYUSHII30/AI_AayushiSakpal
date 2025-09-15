# AI_AayushiSakpal
AI-Powered Knowledge Graph to Manim Animation Automation
## Short description
A pipeline that accepts a student query (concept), retrieves structured knowledge from a small knowledge graph, uses an LLM to generate a short slide deck + narration (grounded to sources), and automatically converts the slides to a Manim animation.

(Problem statement referenced from Statements.pdf provided via mail) 

## What I submit
- `README.md` (this file)
- `diagrams/architecture.png` (pipeline diagram)
- `pseudo_code/` (kg_build.md, retrieval.md, manim_generation.md)
- `samples/small_kg.json` (tiny knowledge graph)
- `samples/sample_prompts.txt` (LLM prompt templates)
- `manim_templates/base_slide_template.py` and `samples/demo_scene.py` (small runnable Manim demo)
- `references.md` (tools & notes)

## Quick pipeline (one line)
Query → Hybrid retrieval from KG + embeddings → LLM (RAG) generates structured slides with `sources` → Template → Manim → Video

## How to run the small demo locally
1. Install Manim Community Edition (see manim docs).  
2. From repository root: `cd samples`  
3. `manim -pql demo_scene.py SlideScene`  
4. Video opens in the player.

## Key design points (short)
- **Hybrid retrieval (graph + embeddings)**: combines exact concept relations with semantic search.  
- **Grounded LLM output**: LLM is given node excerpts as context and must return slide bullets + a `sources` field mapping each bullet to KG node ids — this reduces hallucinations.  
- **Manim template automation**: structured JSON → code template → rendered scene.

## Standout features (what makes this strong)
- Citation mapping for every slide bullet (traceability).  
- Automatic worked example generation (model instructed to create one short worked example when possible).  
- “Domain adapter” note: pipeline is easily adapted to Space Tech (custom visualization templates), matching AIQ Space Ventures’ focus. :contentReference[oaicite:6]{index=6}

## Evaluation criteria (for reviewer)
- Traceability: bullets map to KG node ids.  
- Pedagogical clarity: slides are concise + include one worked example.  
- Automation: Manim code auto-generated (templates).  
- Reproducibility: demo can be run locally.

(See other files in the repo for pseudocode, prompts, and demo files.)
