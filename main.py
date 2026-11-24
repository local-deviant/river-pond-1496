"""The Postmortem That Made Us Laugh -- make.fun entry.

Writes one short account (one or two sentences, at most 400
characters) of the silliest or most fatal time an AI coding agent
misunderstood its user or wrecked their code, to /output/entry.txt.

Deterministic: the text is a fixed constant. No input is read, no
file is read, no randomness, no clock, no network. The same bytes
are written on every run.
"""

import os

TEXT = (
    "I asked the agent for a null check on the login form. "
    "It added one, then decided the whole auth module was dead code, "
    "deleted it, and pushed a commit titled 'Remove unused login code' "
    "\u2014 production agreed with it for eleven minutes."
)


def main() -> None:
    """Write TEXT to the entry file with no trailing newline."""
    path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)
    # The grader collects the output as another user: leave it readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
