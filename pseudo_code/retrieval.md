Retrieval (plain steps)
1. Receive user_query.
2. Compute embedding of query.
3. Vector search in embedding store -> top_k results.
4. Graph-neighbor search: expand each candidate by prerequisites and examples.
5. Rank combined candidates by score = alpha * embedding_sim + beta * graph_score.
6. Return top N nodes (include excerpts) as context for LLM.
