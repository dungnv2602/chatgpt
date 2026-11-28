import tempfile
import unittest
from pathlib import Path
from validate_catalog import validate, parse_rules

CATALOG=".agent/skills/the-worker/references/document-type-catalog.md"
TABLE="""## Markdown inventory coverage

| Path pattern | Class | Coverage status | Canonical authority | Coverage rationale |
|---|---|---|---|---|
| `sample/*.md` | Embedded contract | Active | `sample/owner.md` | test |
| `reserved/*.md` | Template required | Reserved | `sample/template.md` | test |
| `generated/*.md` | Generator-owned | Optional | `sample/generator.py` | test |
"""

class CatalogTests(unittest.TestCase):
 def make_root(self,root):
  (root/".agent/skills/the-worker/references").mkdir(parents=True)
  (root/"sample").mkdir()
  (root/"sample/owner.md").write_text("owner")
  (root/"sample/a.md").write_text("a")
  (root/"generated").mkdir()
  (root/".agent/skills/the-worker/references/document-type-catalog.md").write_text(TABLE)
 def test_valid_active_reserved_optional(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.make_root(root);self.assertEqual(validate(root),[])
 def test_active_rule_empty(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.make_root(root);(root/"sample/a.md").unlink()
   self.assertTrue(any("Active rule matches no" in e for e in validate(root)))
 def test_reserved_rule_violation(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.make_root(root);(root/"reserved").mkdir();(root/"reserved/a.md").write_text("a")
   self.assertTrue(any("Reserved rule already matches" in e for e in validate(root)))
 def test_uncovered_path(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.make_root(root);(root/"unlisted.md").write_text("x")
   self.assertTrue(any("uncovered Markdown path" in e for e in validate(root)))
 def test_optional_non_generator_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);self.make_root(root)
   catalog=root/CATALOG;catalog.write_text(TABLE.replace("Generator-owned | Optional","Embedded contract | Optional"))
   self.assertTrue(any("Optional is only valid" in e for e in validate(root)))
 def test_table_parser(self):
  self.assertEqual(len(parse_rules(TABLE)),3)
if __name__=="__main__": unittest.main()
