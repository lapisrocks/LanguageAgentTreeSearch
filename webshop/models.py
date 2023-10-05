import os
import openai
import backoff 
from transformers import GPT2Tokenizer

completion_tokens = prompt_tokens = 0
MAX_TOKENS = 15000
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-medium')

api_key = os.getenv("OPENAI_API_KEY", "")
if api_key != "":
    openai.api_key = api_key
else:
    print("Warning: OPENAI_API_KEY is not set")
    
api_base = os.getenv("OPENAI_API_BASE", "")
if api_base != "":
    print("Warning: OPENAI_API_BASE is set to {}".format(api_base))
    openai.api_base = api_base

@backoff.on_exception(backoff.expo, openai.error.OpenAIError)
def completions_with_backoff(**kwargs):
    return openai.ChatCompletion.create(**kwargs)

def gpt3(prompt, model="text-davinci-002", temperature=1.0, max_tokens=100, n=1, stop=None) -> list:
    outputs = []
    for _ in range(n):
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=stop
        )
        outputs.append(response.choices[0].text.strip())
    return outputs

def gpt(prompt, model="gpt-3.5-turbo-16k", temperature=1.0, max_tokens=100, n=1, stop=None) -> list:
    if model == "test-davinci-002":
        return gpt3(prompt, model, temperature, max_tokens, n, stop)
    else:
        messages = [{"role": "user", "content": prompt}]
        return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)

def gpt4(prompt, model="gpt-4", temperature=0.2, max_tokens=100, n=1, stop=None) -> list:
    if model == "test-davinci-002":
        return gpt3(prompt, model, temperature, max_tokens, n, stop)
    else:
        messages = [{"role": "user", "content": prompt}]
        return chatgpt(messages, model=model, temperature=temperature, max_tokens=max_tokens, n=n, stop=stop)
    
def chatgpt(messages, model="gpt-3.5-turbo-16k", temperature=1.0, max_tokens=100, n=1, stop=None) -> list:
    global completion_tokens, prompt_tokens
    outputs = []
    while n > 0:
        cnt = min(n, 20)
        n -= cnt
        res = completions_with_backoff(model=model, messages=messages, temperature=temperature, max_tokens=max_tokens, n=cnt, stop=stop)
        outputs.extend([choice["message"]["content"] for choice in res["choices"]])
        # log completion tokens
        completion_tokens += res["usage"]["completion_tokens"]
        prompt_tokens += res["usage"]["prompt_tokens"]
    return outputs
    
def gpt_usage(backend="gpt-4"):
    global completion_tokens, prompt_tokens
    if backend == "gpt-4":
        cost = completion_tokens / 1000 * 0.06 + prompt_tokens / 1000 * 0.03
    elif backend == "gpt-3.5-turbo":
        cost = completion_tokens / 1000 * 0.002 + prompt_tokens / 1000 * 0.0015
    elif backend == "gpt-3.5-turbo-16k":
        cost = completion_tokens / 1000 * 0.004 + prompt_tokens / 1000 * 0.003
    return {"completion_tokens": completion_tokens, "prompt_tokens": prompt_tokens, "cost": cost}
