set up

```bash
git clone https://github.com/adrianlyjak/inspect-ai-48-repro
cd inspect-ai-48-repro
git checkout rs-spike-01
```

execute

```bash
python app/evals/eval_foo.py
```

bang!

```
...
  File "/home/adrianlyjak/dev/inspect-ai-48-repro/app/evals/eval_foo.py", line 4, in <module>
    from app.prompts.foo import GREET
ModuleNotFoundError: No module named 'app'
```
