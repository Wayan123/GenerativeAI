# LangChain

LangChain is a `framework` for developing applications powered by language models.

It connects a language model to other sources of data

Imagine

- You want to build an application on top of ChatGPT or any other powerful language model.
- You want to connect it to other sources of data (like a database, PDF, Email),
- You also want to construct Prompts based on plain user inputs,
- You also want to store coverssational history,
- You also want to combine the model with other models
- Give access to Google Search or Wikipedia to make it even more powerful

LangChain makes all of this a whole lot easier. It allows building applications with LLMs through composability.

![Alt Text](images/LangChain1.png)

LangChain just composes large amounts of data that can easily be referenced by a LLM with as little computation power as possible. It works by taking a big source of data, take for example a 50-page PDF, and breaking it down into "chunks" which are then embedded into a Vector Store.

![Alt Text](images/LangChain2.png)

Now that we have vectorized representations of the large document, we can use this in conjunction with the LLM to retrieve only the information we need to be referenced when creating a prompt-completion pair.

When we insert a prompt into our new chatbot, LangChain will query the Vector Store for relevant information. Think of it as a mini-Google for your document. Once the relevant information is retrieved, we use that in conjunction with the prompt to feed to the LLM to generate our answer.

![Alt Text](images/LangChain3.png)

## Key Components / Modules

### Models / Model I/O (LLM Wrappers)

Generaic Interface for LLMs

You can access models form OpenAI, Cohere, HuggingFace and many more providers.

[Models, Prompt and Parsers Note Book](langchain_llm_application_development/L1_Model_prompt_parser.ipynb)

### Prompts

PromptTemplates that allow you to dynamically change the prompts with user input, similar to how regex are used

```python

# Import prompt and define PromptTemplate

from langchain import PromptTemplate

template = """
You are an expert data scientist with an expertise in building deep learning models.
Explain the concept of {concept} in a couple of lines
"""

prompt = PromptTemplate(
    input_variables=["concept"],
    template=template,
)


# Run LLM with PromptTemplate

llm(prompt.format(concept="autoencoder"))
llm(prompt.format(concept="regularization"))

```

### Chains

Chain is an end-to-end wrapper around multiple individual components, providing a way to accomplish a common use case by combining these components in a specific sequence. The most commonly used type of chain is the LLMChain, which consists of a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser.

Many a time, to solve tasks, a single API call to an LLM is not enough. This module allows other tools to be integrated. For example, you may need to get data from a specific URL, summarize the returned text, and answer questions using the generated summary. This module allows multiple tools to be concatenated in order to solve complex tasks.

Chains go beyond one LLM call and sequences of calls. For example you can chain together a prompt template and a LLM call.

#### Sequential Chain

Sequential Chain allows you to chain multiple calls to LLMs together.

[Chains NoteBook](langchain_llm_application_development/L3_Chains.ipynb)

https://python.langchain.com/docs/modules/chains/foundational/sequential_chains

![Sequential Chains](images/LangChain-SequentialChains.png)

![Sequential Chain](images/LangChain-SequentialChain.png)

#### Router Chain

Router Chain allows you to route the input to different chains based on the input.

[Chains NoteBook](langchain_llm_application_development/L3_Chains.ipynb)

https://python.langchain.com/docs/modules/chains/foundational/router

![Router Chain](images/LangChain-RouterChain.png)

### Memory (Embeddings and Vector Stores)

When you interact with models, naturally they don't remember what you say before or any of
the previous conversation, which is an issue when you're building some applications like Chatbot and you want to have a conversation with them.

https://python.langchain.com/docs/modules/memory/

[Memory Note Book](langchain_llm_application_development/L2_Memory.ipynb)

Provides a Standard Interface for memory and memory implementations

You can easily store a message history of a Chatbot.

The idea behind embeddings and Vector Stores is to break large data into chunks and store those to be queried when relevant.

### Indexes

Utility functions to load your own text data and create indexes for it.
You can combine your own data with the data from the LLMs.
It provides Document Loaders for PDFs, Emails, and many more.

It also provides Vector store interfaces to store and query vectors.

We want to use **language models** and combine it with a lot of our documents.

But there's a key issue. **Language models** can only inspect a few thousand
words at a time. So if we have really large documents, how can we get
the language model to answer questions about everything
that's in there?

This is where **embeddings** and vector stores come into play.
First, let's talk about embeddings.

**Embeddings** create numerical representations for pieces of text.

This numerical representation captures the **semantic meaning** of the piece of text that it's been run over.Pieces of text with **similar content** will have **similar vectors**.

In the example below, we can see that we have three sentences. The first two are about pets, while the third is about a car.If we look at the representation in the numeric space, we can see that when we compare the two vectors on the pieces of text corresponding to the sentences about pets, they're very similar.

While if we compare it to the one that talks about a car, they're not similar at all. This will let us easily figure out which pieces of text are like each other, which will be very useful as
we think about which pieces of text we want to include when passing to the language model to answer a question.

![Embeddings](images/LangChain-Embeddings.png)

A **vector database** is a way to store these vector representations. The way that we create this vector database is we populate it with chunks of text coming from incoming documents. When we get a big incoming document, we're first going to break it up into smaller chunks. This helps create pieces of text that are smaller than the original document, which is useful because we may not be able to pass the whole document to the language model. So we want to create these small chunks
so we can only pass the most relevant ones to the language model. We then create an embedding for each of these chunks, and then we store those in a vector database.

![Vector Databases](images/LangChain-VectorDatabases.png)

### Agents and Tools

Setup agents that can use tools like Google Search, Wikipedia, and many more.

```python

from langchain.agents import GoogleSearchAgent

agent = GoogleSearchAgent()

agent.search("Hello World")

```
