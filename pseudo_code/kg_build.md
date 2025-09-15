KG build (plain steps)
1. Split book text into paragraphs.
2. Extract named entities / concept phrases from paragraphs.
3. For each concept create a node {id, label, excerpt, source}.
4. For sentences mentioning two concepts, add an edge (relation type inferred).
5. Save KG as JSON or load into Neo4j for production.
