"""Regression checks for guide's single active conceptual taxonomy."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
ACTIVE_DOCS = [*ROOT.glob("README*.md"), *ROOT.glob("framework/**/*.md"), *ROOT.glob("applications/**/*.md")]
RETIRED = (
    "原六工作视角", "与六维和充分性的关系", "旧框架的", "旧的自指推导",
    "former six lenses", "six working lenses", "六个工作视角", "all six dimensions:", "former self-reference-first",
    "the prior interpretive labels", "Other working lenses remain",
    "关系维度", "因果维度", "它不是维度", "It is not a dimension.",
)

class ConceptTaxonomyTest(unittest.TestCase):
    def test_no_parallel_taxonomy(self):
        for path in ACTIVE_DOCS:
            with self.subTest(path=str(path.relative_to(ROOT))):
                content = path.read_text(encoding="utf-8")
                for term in RETIRED:
                    self.assertNotIn(term, content, f"retired taxonomy: {term}")

    def test_foundations_and_conditional_scope(self):
        zh = (ROOT / "framework/README.zh-CN.md").read_text(encoding="utf-8")
        en = (ROOT / "framework/README.md").read_text(encoding="utf-8")
        for term in ("九组关键区分", "六个系统观察维度", "五个专题", "四种方法"):
            self.assertIn(term, zh)
        for term in ("nine distinctions", "six system perspectives", "five topics", "four methods"):
            self.assertIn(term, en)
        zh_explore = (ROOT / "framework/methods/exploration.zh-CN.md").read_text(encoding="utf-8")
        en_explore = (ROOT / "framework/methods/exploration.md").read_text(encoding="utf-8")
        zh_decide = (ROOT / "framework/methods/decision.zh-CN.md").read_text(encoding="utf-8")
        en_decide = (ROOT / "framework/methods/decision.md").read_text(encoding="utf-8")
        self.assertIn("开放式探究无需预设下一行动转换", zh_explore)
        self.assertIn("Open-ended inquiry needs no planned action transition", en_explore)
        self.assertIn("不要求事先运行统一的充分性三态分类", zh_decide)
        self.assertIn("not a prior universal three-state sufficiency classification", en_decide)

if __name__ == "__main__":
    unittest.main()
