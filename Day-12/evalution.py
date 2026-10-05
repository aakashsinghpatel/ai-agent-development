def evaluate_retrieval(
    results,
    expected_chunk_id
):
    """ Mrthod to evalutio  the retriver reponse by checking the chunkid in respose availabe or not that
     it should have
      like for an fixed query we know that chunk 4 should be there to get good response
       hance fot rhat query we check that the retriver has that chuck in the respons eof not
        after seach """
    retrieved_ids = [
        result["chunk_id"]
        for result in results
    ]

    return (
        expected_chunk_id
        in retrieved_ids
    )

