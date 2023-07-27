# Vector Stores

LLM's knowledge is restricted to its training set. Suppose the model was trained on data up to 2021 and is asked about a company founded in 2023. In that case, it may generate a plausible but entirely fabricated description - a phenomenon known as **hallucination**. Managing hallucinations is tricky, especially in applications where accuracy and reliability are paramount, such as customer-service chatbots, knowledge-base assistants, or AI tutors.

One promising strategy to mitigate hallucination is the use of **retrievers** in tandem with LLMs. A retriever fetches relevant information from a trusted knowledge base (like a search engine), and the LLM is then specifically prompted to rearrange the information without inventing additional details.

Efficient retrievers are built using **embedding** models that map texts to vectors. These vectors are then stored in specialized databases called vector stores.

## Embeddings

Embedding is just a vector, a list of numbers with a semantic meaning only understandable by the machine.

Turning Words, Images and Videos into Numbers.

Embeddings are techniques that convert complex data, such as words, into simpler numerical representations (called vectors). This makes it easier for AI systems to understand and work with the data.

To store documents as vectors, a vector database requires a process called `embedding` to convert each word into a vector of hundreds or thousands of `different dimensions`. For example, OpenAI `Ada` embedding results in over 1500 dimensions.

Think of `embeddings` as a way to turn words into points on a `map`. Each word gets its own spot on the map, and similar words are close to each other, while different words are far apart. This “map” is like a grid. Each word is a point on the grid, and each dimension is a different axis. The word “cat” might be at (1, 2, 3) and the word “dog” might be at (1, 2, 4). The words “cat” and “dog” are similar, so they are close together on the map. But the word “cat” is different from the word “dog”, so they are not at the same point on the map.

The `directions` on this map are called `dimensions`. Each dimension is like a different characteristic or feature of a word. For example, one dimension might represent how “happy” a word is, while another might represent whether it’s an animal or not. The more dimensions we have, the more characteristics we can capture about each word.

`Vector embeddings` are numerical representations of objects such as words, images, or other data points in a high-dimensional space.

A `high-dimensional` space is a mathematical concept that represents a space with many dimensions, where each dimension is a separate axis or feature of the data. In practical terms, a high-dimensional space is simply a way to describe data that has many features or attributes.

**Language models** can only inspect a few thousand words at a time. So if we have really large documents, how can we get the language model to answer questions about everything that's in there?

This is where **embeddings** and vector stores come into play.

**Embeddings** create numerical representations for pieces of text.

This numerical representation captures the **semantic meaning** of the piece of text that it's been run over.Pieces of text with **similar content** will have **similar vectors**.

In the example below, we can see that we have three sentences. The first two are about pets, while the third is about a car.If we look at the representation in the numeric space, we can see that when we compare the two vectors on the pieces of text corresponding to the sentences about pets, they're very similar.

While if we compare it to the one that talks about a car, they're not similar at all. This will let us easily figure out which pieces of text are like each other, which will be very useful as
we think about which pieces of text we want to include when passing to the language model to answer a question.

![Embeddings](images/Embeddings.png)

## Vector Databases

Vector databases, also known as `similarity search` databases or `nearest neighbor search` databases, are specialized databases designed to store and query vector embeddings efficiently. They enable you to perform operations like finding the most similar items to a given vector or searching for items that meet specific similarity criteria.

Traditional databases aren’t optimized for these tasks, which is why vector databases have become increasingly popular.

Vector databases store data such as text, video or images that are converted into vector `embeddings` for AI models to access them quickly. Vector databases are used in machine learning (ML) applications such as recommendation systems, search engines, and natural language processing (NLP).

Vector databases are different from traditional databases in that they store data in the form of vectors. Traditional databases store data in the form of table rows and columns. The vector database stores data in the form of vectors, which are lists of numbers represented as a sequence of numbers or as a single value in a row and a single value in the column section.

Although SQL and NoSQL databases might work for some ML use cases, vector databases are better suited for use cases involving text, search, recommendation, audio, and NLP. Vector databases are also better suited for use cases involving similarity search, which is a search technique that finds similar items based on their features.

![Alt Text](images/VectorDB2.png)

![Alt Text](images/VectorDB1.png)

A **vector database** is a way to store vector representations. The way that we create this vector database is we populate it with chunks of text coming from incoming documents. When we get a big incoming document, we're first going to break it up into smaller chunks. This helps create pieces of text that are smaller than the original document, which is useful because we may not be able to pass the whole document to the language model. So we want to create these small chunks
so we can only pass the most relevant ones to the language model. We then create an embedding for each of these chunks, and then we store those in a vector database.

![Vector Databases](images/VectorDatabases.png)

### Distance vs. Similarity

While there isn’t a single preferred approach to measuring the similarity or distance between vectors created by OpenAI, `cosine` similarity is a common and widely used method for comparing embeddings generated by language models like GPT-4.

Cosine similarity focuses on the angle between two vectors rather than their magnitudes, making it less sensitive to the magnitude of the embeddings. This property is particularly useful when comparing embeddings from language models, as it captures the relative orientation of the vectors in the high-dimensional space, which often represents the semantic relationship between words or text samples.

However, the choice of similarity or distance measure ultimately depends on the specific task and requirements. In some cases, other similarity measures, like Euclidean distance or correlation-based measures, might be more appropriate. It’s essential to experiment with different measures and evaluate their performance on the given problem to select the most suitable approach.

[Which distance function should I use?](https://platform.openai.com/docs/guides/embeddings/which-distance-function-should-i-use)

### Vector DBs

[activeloop Deep Lake](https://docs.activeloop.ai/)

https://www.pinecone.io/

https://github.com/chroma-core/chroma

https://github.com/weaviate/weaviate

https://weaviate.io/

https://github.com/activeloopai/deeplake

https://github.com/qdrant/qdrant

### Chroma vs Pinecone

| Parameters               | Chroma                                                                                                                                                                                                                                                                                                                  | Pinecone                                                                                                                                                                                                                                                                                                                  |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Open Source              | Yes                                                                                                                                                                                                                                                                                                                     | Pinecone offers a free tier for up to 1 million vectors. Beyond that, you can choose from a variety of paid plans based on your usage.                                                                                                                                                                                    |
| Self-hosted              | Yes                                                                                                                                                                                                                                                                                                                     | No                                                                                                                                                                                                                                                                                                                        |
| Storage Location         | Chroma provides a local ephemeral storage option, which means that the vector data is stored on your local machine or the machine running your application. It doesn’t require any external service or database to store the data. As Chroma has been open-sourced, you also have the option to host your own instance. | Pinecone is a managed database persistence service, which means that the vector data is stored in a remote, cloud-based database managed by Pinecone. Your application interacts with the Pinecone service through APIs to store and retrieve the vector data.                                                            |
| Data Persistence         | With Chroma’s ephemeral option, the data stored in Chroma is temporary and exists only during the runtime of the application. Once the application stops or the machine is restarted, the data is lost. This option makes Chroma suitable for testing and experimentation purposes or for temporary storage.            | Pinecone provides data persistence, which means that the vector data stored in the Pinecone database will be retained even after the application stops or the machine is restarted. This makes Pinecone (and Chroma’s self-host option) suitable for long-term storage and production use cases.                          |
| Scalability Alternatives | Chroma’s local storage is limited by the resources (e.g. memory and storage) of the local machine. As your data grows, you may need to scale your machine’s resources to handle the increased data.                                                                                                                     | Being a managed service, Pinecone handles the scalability aspect for you. As your data grows, Pinecone will scale the underlying infrastructure to accommodate the increased data. Pinecone is designed to handle large-scale vector data storage and retrieval efficiently, making it suitable for production use cases. |

### Vector Database Benchmarks

https://qdrant.tech/benchmarks/

### Usecases

1. Long term memory for LLM (Language Model)

2. Semantic Search : Search based on meaning or context rather than on exact word matches.

3. Similarity Search for text, images, videos, audio, etc.

4. Recommendation (Ranking) Engines : Suggest the most relevant items to users based on their past purchases or preferences. Identifying the nearest neighbors of a given item in a vector database can help with this.

5. Anomaly Detection : Identify unusual patterns in data that do not conform to expected behavior.

## When do use Vector DBs

GPT is an incredibly powerful tool for natural language processing tasks. However, when it comes to customized tasks, its capacity can be limited by the input token size.

For example, GPT has a limited input size (4,096 for GPT3.5), but you have a very long text (e.g. a book) that you want to ask questions about. While fine-tuning GPT with your private data is a potential solution, it can be a complex and expensive process, requiring high computational power and expertise in machine learning.

Fortunately, there is an alternative solution that can enhance GPT’s performance without requiring any changes to the model itself: using an external vector database to store your data and letting GPT retrieve relevant data to answer your prompting questions.
