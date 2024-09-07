set up

```bash
git clone https://github.com/adrianlyjak/inspect-ai-48-repro
cd inspect-ai-48-repro
python3.11 -m venv .venv
source .venv/bin/activate
pip install -e .
```

execute

```bash
inspect eval app/evals/eval_foo.py --model openai/gpt-3.5-turbo
```

Success!
