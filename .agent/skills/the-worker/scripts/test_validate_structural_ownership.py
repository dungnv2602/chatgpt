import tempfile
import unittest
from pathlib import Path
from validate_structural_ownership import validate

class Tests(unittest.TestCase):
 def make_root(self,root):
  (root/".agent/skills/the-worker/references").mkdir(parents=True)
  (root/".agent/skills/the-worker").mkdir(parents=True,exist_ok=True)
  (root/".agent").mkdir(exist_ok=True)
  (root/".agent/SESSION_START.md").write_text("# Session Start\nThe sole session-start cue is /start.\n[The Worker](skills/the-worker/SKILL.md)\n")
  (root/".agent/skills/the-worker/SKILL.md").write_text("# The Worker\n## Authority and scope\n## Activation\n")
  (root/".agent/skills/the-worker/references/conversation-mode.md").write_text("# Conversation Mode\n## Presentation settings\nThe selected mode controls presentation only.\n")
  (root/".agent/INITIALIZATION_POLICY.md").write_text("# Initialization Policy\nThe Worker is the sole operational authority.\n.agent/SESSION_START.md\n.agent/skills/the-worker/SKILL.md\n.agent/skills/the-worker/references/conversation-mode.md\n")
 def test_valid(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);self.make_root(r);self.assertEqual(validate(r),[])
 def test_extra_link(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);self.make_root(r);p=r/".agent/SESSION_START.md";p.write_text(p.read_text()+"[extra](other.md)\n")
   self.assertTrue(any("exactly one Worker pointer" in e for e in validate(r)))
 def test_missing_file(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);self.make_root(r);(r/".agent/skills/the-worker/SKILL.md").unlink()
   self.assertTrue(any("missing canonical path" in e for e in validate(r)))
 def test_mode_boundary(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);self.make_root(r);p=r/".agent/skills/the-worker/references/conversation-mode.md";p.write_text(p.read_text()+"\n## Execution\n")
   self.assertTrue(any("unexpected operational section marker" in e for e in validate(r)))
if __name__=="__main__": unittest.main()
