#!/usr/bin/env python3
import json
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description="Evaluate a draft reply based on active listening principles.")
    parser.add_argument("--draft", required=True, help="The draft reply to evaluate.")
    args = parser.parse_args()

    draft = args.draft.lower()
    feedback = []

    if "you are wrong" in draft or "you're wrong" in draft:
        feedback.append("Feedback: Avoid adversarial language like 'you are wrong'. It immediately creates a confrontational dynamic. Suspend judgement.")

    if "read it more carefully" in draft or "you need to read" in draft:
        feedback.append("Feedback: Telling someone to 'read it more carefully' comes across as condescending and lacks non-judgemental listening. Try acknowledging their concern instead.")

    has_question = "?" in draft
    if not has_question:
        feedback.append("Feedback: Consider adding an open-ended question to invite further dialogue and demonstrate curiosity.")

    if not feedback:
        print(json.dumps({"status": "pass", "message": "Draft looks good and aligns with active listening principles."}))
        sys.exit(0)
    else:
        print(json.dumps({"status": "fail", "feedback": feedback}))
        sys.exit(1)

if __name__ == "__main__":
    main()
