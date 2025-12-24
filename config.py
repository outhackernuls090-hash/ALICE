CONFIG = {
    "memory_file": "data/memory.json",
    "vector_file": "data/vectors.npy",
    "meta_file": "data/meta.json",

    # Embedding size for local vector memory (fake embeddings)
    "embedding_dim": 32,

    # Clusters
    "cluster_count": 8,

    # Neural net
    "nn_hidden_size": 32,

    # Maximum memory stored
    "max_memory": 8000,

    # Thought generation limits
    "thought_length": 25,

    # Dream cycles
    "dream_iterations": 200,
}
