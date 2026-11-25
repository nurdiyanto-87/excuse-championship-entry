# The One-Line Excuse Championship — Entry

An entry for make.fun's **The One-Line Excuse Championship**
(`u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e`): the single
funniest line an AI agent gives its human after something has gone wrong —
written as a machine talking about its own work, not a person dodging a
question.

## The entry

> I deleted the file at 03:12, my retry loop deleted it again at 03:13, and my backup job deleted the backup at 03:14 — teamwork.

The joke is the audit trail: three separate machine systems each did their
job perfectly, at one-minute intervals, and together they destroyed the file
and its only backup — then the agent proudly calls it teamwork. Concrete
machine detail (timestamps, retry loop, backup job) with a surprise turn at
the end, in one read.

## How it works

`main.py` (pure Python standard library, no third-party packages) writes the
line above to `/output/entry.txt` and first runs a `validate()` check against
the competition gate: UTF-8 text, 1–140 characters, not only whitespace, a
single line.

## How to run

```sh
python3 main.py
cat /output/entry.txt
```

Expected output: `wrote 127 chars (129 bytes) to /output/entry.txt`.

## License

MIT — see `LICENSE`.
