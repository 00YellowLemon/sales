import subprocess
import json
import os

def test_evaluate_draft_fail():
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/evaluate_draft.py')
    result = subprocess.run(
        ['python3', script_path, '--draft', 'You are wrong. You need to read it more carefully.'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 1
    output = json.loads(result.stdout)
    assert output['status'] == 'fail'
    assert len(output['feedback']) == 3

def test_evaluate_draft_pass():
    script_path = os.path.join(os.path.dirname(__file__), '../scripts/evaluate_draft.py')
    result = subprocess.run(
        ['python3', script_path, '--draft', 'I hear your concerns about the constraints. Could you look at page 4 and let me know your thoughts?'],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    output = json.loads(result.stdout)
    assert output['status'] == 'pass'
