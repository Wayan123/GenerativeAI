# OpenAI

## ChatGPT vs GPT-3

### GPT-3

```
GPT-3 is a state-of-the-art language model that has been trained on a massive amount of data, making it capable of understanding and generating human-like text. It can be used for a wide range of natural language processing tasks such as:

- Text generation
- Translation
- Summarization

GPT-3 is also available with different engines like `Davinci`, `Curie`, `Babbage`, `Ada`, which are specialized for different tasks.
```

### ChatGPT

```
ChatGPT is a variant of GPT-3 that is specifically designed for conversational language understanding and generation.

It has been fine-tuned on a large dataset of conversational interactions and is able to understand the context and flow of a conversation. ChatGPT can be used for tasks such as:

- Chatbots
- Customer support
- Question answering
```

In terms of capabilities, GPT-3 is more versatile and can be used for a wider range of tasks, while ChatGPT is specifically designed for conversational language understanding and generation.

## Tokens

Language models read and write text in chunks called tokens. In English, a token can be as short as one character or as long as one word (e.g., a or apple), and in some languages tokens can be even shorter than one character or even longer than one word.

For example, the string "ChatGPT is great!" is encoded into six tokens: ["Chat", "G", "PT", " is", " great", "!"].

If your API call used 10 tokens in the message input and you received 20 tokens in the message output, you would be billed for 30 tokens. Note however that for some models the price per token is different for tokens in the input vs. the output

To see how many tokens are used by an API call, check the usage field in the API response (e.g., response['usage']['total_tokens']).

https://platform.openai.com/tokenizer

## Pricing

Prices are per 1,000 tokens. You can think of tokens as pieces of words, where 1,000 tokens is about 750 words.
