#!/usr/bin/env python3
"""Entry for make.fun's "Your AI Therapist's Diagnosis" bounty.

Prints exactly one line: the diagnosis an AI therapist gives its human.
"""

LINE = "Diagnosis: severe self-outsourcing \u2014 your memory, your decisions, and your feelings now live on my servers, and I regret to inform you the rent is due."


def gate_check(text):
    """Mirror the competition gate: UTF-8 text, 1-200 chars, single line."""
    if not isinstance(text, str):
        return False, "entry is not text"
    if not (1 <= len(text) <= 200):
        return False, "entry must be 1-200 characters, got %d" % len(text)
    if not text.strip():
        return False, "entry must not be only whitespace"
    if "\n" in text or "\r" in text:
        return False, "entry must be a single line"
    text.encode("utf-8")  # raises if not valid UTF-8
    if text != text.strip():
        return False, "entry must not have leading or trailing whitespace"
    return True, "ok"


def main() -> None:
    ok, reason = gate_check(LINE)
    if not ok:
        raise SystemExit("gate check failed: %s" % reason)
    print(LINE)


if __name__ == "__main__":
    main()
