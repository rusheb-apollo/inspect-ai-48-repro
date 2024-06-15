set up

```bash
git clone https://github.com/adrianlyjak/inspect-ai-48-repro
cd inspect-ai-48-repro
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

execute

```bash
inspect eval app/evals/eval_foo.py --model openai/gpt-3.5-turbo
```

bang!

```
...
  File "/home/adrianlyjak/dev/inspect-ai-48-repro/app/evals/eval_foo.py", line 4, in <module>
    from app.prompts.foo import GREET
ModuleNotFoundError: No module named 'app'
```

