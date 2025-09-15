# AI_AayushiSakpal
AI-Powered Knowledge Graph to Manim Animation Automation
## Short description
A pipeline that accepts a student query (concept), retrieves structured knowledge from a small knowledge graph, uses an AI model (LLM) to generate a short slide deck + narration (grounded to sources), and automatically converts the slides to a **Manim animation video**.

(Problem statement referenced from Statements.pdf provided via mail) 

## What I submit
- `README.md` → this file (main submission report)  
- `diagrams/architecture.png` → pipeline diagram  
- `pseudo_code/` → step-by-step pseudo-code  
  - `kg_build.md`  
  - `retrieval.md`  
  - `manim_generation.md`  
- `samples/` → tiny demo dataset + prompt + sample Manim code  
  - `small_kg.json` (tiny knowledge graph)  
  - `sample_prompts.txt` (LLM prompt template)  
  - `demo_scene.py` (runnable Manim demo)  
- `manim_templates/base_slide_template.py` → Manim code template  
- `references.md` → tools, libraries, submission notes  

## Quick pipeline (one line)
Query → Hybrid retrieval from KG + embeddings → LLM (RAG) generates structured slides with `sources` → Template → Manim → Video

## System Architecture  
[ Student Query ]
        |
        v
[ Knowledge Graph ] ---> (provides context)
        |
        v
[ AI Module (LLM) ] -- generates slides + narration -->
        |
        v
[ Formatter ] --> [ Manim Template Generator ] --> [ Manim Renderer ]
        |
        v
[ Output Video for Student ]

## Pseudo-code (high-level)  
input: "Dynamic Programming"

1. Search knowledge graph for concept + related nodes
2. Collect excerpts (definitions, examples, problems)
3. Send to AI model → generate structured slides JSON:
      { "title":..., "bullets":[], "narration":..., "sources":[] }
4. Formatter cleans structure and fills Manim templates
5. Manim renders MP4 animation

output: final educational video

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
