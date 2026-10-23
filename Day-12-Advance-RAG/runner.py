from pathlib import Path

from advance_rag import (build_rag,retrieve)

from generator import (generate_answer)


DOCUMENT_PATH = (Path("documents")/ "python.txt")


def main():

    # Red text from document
    text = DOCUMENT_PATH.read_text(encoding="utf-8")

    print("Building RAG knowledge base...")

    # Store document into ChromaDB (Chunks)
    # Only first time arg willbe created rest all time it get update o re run the program as used
    # collection.upsert based on it
    
    build_rag(text,DOCUMENT_PATH.name)

    print("\nAdvanced RAG is ready.")

    while True:
        query = input("\nYou : ").strip()

        if query.lower() in {"exit","quit"}:
            break

        # Retieve the candidated based on top k then rerank it an dget top_k_2 results
        results = retrieve(query,top_k=5)

        print("\nRetrieved Sources Ranking:")

        for result in results:
            print(f"- "
                f"{result['source']} "
                f"(chunk "
                f"{result['chunk_id']})"
            )

        answer = generate_answer(query,results)

        print("\nRAG :")

        print(answer)


if __name__ == "__main__":
    main()


