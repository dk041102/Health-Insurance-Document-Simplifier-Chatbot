def query_db(vectordb, query, k=3):
    results = vectordb.similarity_search(query, k=k)
    for i, r in enumerate(results, start=1):
        print(f"\n🔸 Result {i}:\n{r.page_content}\n")