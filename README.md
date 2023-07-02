# GenerativeAI

Generative AI refers to a class of artificial intelligence models designed to create new data by learning patterns and structures from existing data.

Generative AI models are built by training on a large dataset of general examples (such as wikipedia, commoncrawl, etc) and then using that knowledge to generate new examples that are similar to the training data. So the idea is to generate new data. A generative AI model that is trained on a dataset of images of cats may be able to generate new images of cats that are similar to the training data.

## Life Cycle of Generative AI Models

🔹 Data collection (web scraping, APIs, etc.)
🔹 Pre-processing (cleaning, tokenization, etc.)
🔹 Model training (unsupervised learning, transfer learning)
🔹 Fine-tuning (supervised learning, specialized datasets)
🔹 Deployment (APIs, applications)
🔹 Maintenance (updates, improvements)

## Predictive AI and Generative AI

Generative AI and predictive AI are two different types of artificial intelligence (AI) that are used for different purposes

Predictive AI is used to predict future events based on past data. Generative AI is used to create new data based on patterns and structures learned from existing data.

## Embeddings (Numerical Vector)

Turning Words, Images and Videos into Numbers

Embeddings are techniques that convert complex data, such as words, into simpler numerical representations (called vectors). This makes it easier for AI systems to understand and work with the data.

## Transformers

Transformers are a type of `neural network architecture` that underlies models like GPT-3, leveraging self-attention mechanisms to process and generate text efficiently and effectively

Transformer-based models can process input tokens in parallel, making them more scalable and capable of handling long-range dependencies in the text.

## Transfer learning

Transfer learning is a machine learning technique in which a model is trained on one task and then used to perform another task.

The idea is that the knowledge and representations learned by the model from the source task can be transferred to the target task, helping the model generalize better and achieve better performance, especially when the target task has limited data.

### Fine Tuning

Fine-tuning is one of the ways to implement `transfer learning`.

Fine-tuning is a process in which a pre-trained model is adapted to a new domain or task.

Fine-tuning is a common approach to transfer learning, where knowledge gained from training a model on one task is used to improve generalization on another task.
