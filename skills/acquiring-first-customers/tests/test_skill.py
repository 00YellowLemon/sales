import pytest
import os
from unittest.mock import patch, mock_open
from scripts.validate_skill import validate_skill

def test_validate_skill_success():
    valid_content = """---
name: valid-skill-name
description: A valid description.
---
# Skill Title
Do this step.
"""
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=valid_content)):
            errors = validate_skill("dummy.md")
            assert len(errors) == 0

def test_validate_skill_too_long():
    long_content = "---\nname: valid-skill\ndescription: desc\n---\n" + ("line\n" * 501)
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=long_content)):
            errors = validate_skill("dummy.md")
            assert any("exceeds 500 lines" in e for e in errors)

def test_validate_skill_has_xml():
    xml_content = """---
name: valid-skill
description: desc
---
Here is an <xml>tag</xml>.
"""
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=xml_content)):
            errors = validate_skill("dummy.md")
            assert any("contains XML/HTML tags" in e for e in errors)

def test_validate_skill_bad_name():
    bad_name_content = """---
name: Invalid_Name
description: desc
---
"""
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=bad_name_content)):
            errors = validate_skill("dummy.md")
            assert any("not lowercase-hyphenated" in e for e in errors)

def test_validate_skill_missing_frontmatter():
    missing_content = "# Just some markdown\nNo frontmatter here."
    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", mock_open(read_data=missing_content)):
            errors = validate_skill("dummy.md")
            assert any("Missing YAML frontmatter" in e for e in errors)

def test_file_not_found():
    with patch("os.path.exists", return_value=False):
        errors = validate_skill("dummy.md")
        assert len(errors) == 1
        assert "File not found" in errors[0]
