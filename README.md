# Official Repo of Language Agent Tree Search (LATS)

<p>
    <a href="https://www.python.org/">
        <img alt="Build" src="https://img.shields.io/badge/Python-3.7+-1f425f.svg?color=purple">
    </a>
    <a href="https://copyright.illinois.edu/">
        <img alt="License" src="https://img.shields.io/badge/License-MIT-blue">
    </a>
</p>

![teaser](pics/teaser.png)

Official implementation for paper [Language Agent Tree Search Unifies Reasoning Acting and Planing in Language Models]() with code, prompts, model outputs. More can be found at https://andyz245.github.io/LanguageAgentTreeSearch/


### Reasoning + Acting (HotPotQA)

#### Setup

To get started:

1. Clone this repo and move to the HotPotQA directory:
```bash
git clone https://github.com/andyz245/LanguageAgentTreeSearch && cd hotpot
```

2. Install the module dependencies into your environment:
```bash
pip install -r requirements.txt
```

3. Set `OPENAI_API_KEY` environment variable to your OpenAI API key:
```bash
export OPENAI_API_KEY=<your key>
```

4. Set the scripts and run paper experiments
```bash
sh lats.sh
```

- ``--n_generate_sample``: number of times to prompt during expansion/sampling
- ``--n_evaluate_sample``: number of times to prompt for state evaluation
- ``--iterations``: maximum number of trajectories to sample

### Reasoning (Programming)

#### Setup

To get started:

1. Clone this repo and move to the HotPotQA directory:
```bash
git clone https://github.com/andyz245/LanguageAgentTreeSearch && cd programming
```

2. Install the module dependencies into your environment:
```bash
pip install -r requirements.txt
```

3. Set `OPENAI_API_KEY` environment variable to your OpenAI API key:
```bash
export OPENAI_API_KEY=<your key>
```

4. Set the scripts and run paper experiments
```bash
sh run_mcts.sh
```

``root/`` contains all the trajectories from the paper's experiments

Code adapted from https://github.com/noahshinn024/reflexion/tree/main

### Decision-making (WebShop)

#### Setup

To get started:

1. Clone this repo and move to the HotPotQA directory:
```bash
git clone https://github.com/andyz245/LanguageAgentTreeSearch && cd webshop
```

2. Install the module dependencies into your environment:
```bash
pip install -r requirements.txt
```

3. Set `OPENAI_API_KEY` environment variable to your OpenAI API key:
```bash
export OPENAI_API_KEY=<your key>
```

4. Set the scripts and run paper experiments
```bash
sh lats.sh
```

- ``--n_generate_sample``: number of times to prompt during expansion/sampling
- ``--n_evaluate_sample``: number of times to prompt for state evaluation
- ``--iterations``: maximum number of trajectories to sample

## Citations
Please cite the paper and star this repo if you use LATS and find it interesting/useful, thanks! Feel free to contact andyz3@illinois.edu or open an issue if you have any questions.

```bibtex

```
