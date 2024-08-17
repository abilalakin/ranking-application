from sentence_transformers import SentenceTransformer, util


def calculate_similarity(query_embedding, text_embedding):
    """
    Calculate the cosine similarity between two embeddings.
    :param query_embedding: The embedding of the query.
    :param text_embedding: The embedding of the text.
    :return: Cosine similarity score.
    """
    return util.pytorch_cos_sim(query_embedding, text_embedding).item()


class Ranker:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def encode_text(self, text):
        """
        Encode the given text into an embedding.
        :param text: The text to encode.
        :return: A tensor representing the embedding of the text.
        """
        return self.model.encode(text, convert_to_tensor=True)
