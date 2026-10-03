"""Finite regression fixtures for guide's judgment/prediction case studies.

These tests check the stated model instances, not empirical forecast quality.
Run: python -m unittest discover -s tests -p "test_judgment_cases.py" -v
"""

from itertools import combinations
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
DOCS = (
    "framework/judgment-validation.md",
    "framework/judgment-validation.zh-CN.md",
    "framework/examples/judgment-prediction-cases.md",
    "framework/examples/judgment-prediction-cases.zh-CN.md",
)


def nash_profiles(actions, payoffs):
    result = []
    for a in actions:
        for b in actions:
            p = payoffs[a, b]
            if all(p[0] >= payoffs[alt, b][0] for alt in actions) and all(
                p[1] >= payoffs[a, alt][1] for alt in actions
            ):
                result.append((a, b))
    return result


def deferred_accept(proposing, receiving, order):
    free = list(order)
    next_proposal = {p: 0 for p in proposing}
    held = {}
    while free:
        p = free.pop(0)
        preferences = proposing[p]
        if next_proposal[p] >= len(preferences):
            continue
        target = preferences[next_proposal[p]]
        next_proposal[p] += 1
        current = held.get(target)
        if current is None:
            held[target] = p
        elif receiving[target].index(p) < receiving[target].index(current):
            held[target] = p
            free.append(current)
        else:
            free.append(p)
    return held


class FormalCases(unittest.TestCase):
    def test_c01_one_shot_prisoners_dilemma(self):
        pay = {
            ("C", "C"): (3, 3),
            ("C", "D"): (-1, 5),
            ("D", "C"): (5, -1),
            ("D", "D"): (1, 1),
        }
        self.assertEqual(nash_profiles(("C", "D"), pay), [("D", "D")])
        for other in ("C", "D"):
            self.assertGreater(pay["D", other][0], pay["C", other][0])
            self.assertGreater(pay[other, "D"][1], pay[other, "C"][1])
        self.assertEqual(sum(pay["C", "C"]), 6)
        self.assertEqual(sum(pay["D", "D"]), 2)

    def test_c02_repeated_prisoners_dilemma(self):
        # Last-round dominance is the induction step for a known finite horizon.
        pay = {
            ("C", "C"): (3, 3),
            ("C", "D"): (-1, 5),
            ("D", "C"): (5, -1),
            ("D", "D"): (1, 1),
        }
        for remaining_rounds in range(200):
            # When later rounds are fixed at (D,D), their constant payoff
            # does not alter the current strictly dominant choice.
            continuation = remaining_rounds * pay["D", "D"][0]
            for opponent in ("C", "D"):
                self.assertGreater(
                    pay["D", opponent][0] + continuation,
                    pay["C", opponent][0] + continuation,
                )
        def cooperative_incentive(delta):
            return 3 / (1 - delta) - (5 + delta / (1 - delta))
        self.assertLess(cooperative_incentive(0.4), 0)
        self.assertAlmostEqual(cooperative_incentive(0.5), 0)
        self.assertGreater(cooperative_incentive(0.6), 0)

    def test_c03_gale_shapley(self):
        men = {"A": ("X", "Y"), "B": ("Y", "X")}
        women = {"X": ("B", "A"), "Y": ("A", "B")}
        men_first = deferred_accept(men, women, ("A", "B"))
        self.assertEqual(men_first, {"X": "A", "Y": "B"})
        self.assertEqual(deferred_accept(men, women, ("B", "A")), men_first)
        women_first = deferred_accept(women, men, ("X", "Y"))
        self.assertEqual(women_first, {"B": "X", "A": "Y"})

        for allocation in (
            {man: woman for woman, man in men_first.items()},
            women_first,
        ):
            for man, woman in allocation.items():
                for alternative in men[man]:
                    if men[man].index(alternative) >= men[man].index(woman):
                        continue
                    partner = next(m for m, w in allocation.items() if w == alternative)
                    self.assertFalse(
                        women[alternative].index(man)
                        < women[alternative].index(partner)
                    )

    def test_c04_stable_roommates_no_solution(self):
        pref = {
            "A": ("B", "C", "D"),
            "B": ("C", "A", "D"),
            "C": ("A", "B", "D"),
            "D": ("A", "B", "C"),
        }
        perfect = [
            (("A", "B"), ("C", "D")),
            (("A", "C"), ("B", "D")),
            (("A", "D"), ("B", "C")),
        ]
        blocking = []
        for pairs in perfect:
            partner = {a: b for a, b in pairs}
            partner.update({b: a for a, b in pairs})
            blockers = [
                (a, b)
                for a, b in combinations(pref, 2)
                if partner[a] != b
                and pref[a].index(b) < pref[a].index(partner[a])
                and pref[b].index(a) < pref[b].index(partner[b])
            ]
            self.assertTrue(blockers)
            blocking.append(blockers)
        self.assertIn(("B", "C"), blocking[0])
        self.assertIn(("A", "B"), blocking[1])
        self.assertIn(("A", "C"), blocking[2])

    def test_c05_stag_hunt(self):
        pay = {
            ("S", "S"): (4, 4),
            ("S", "H"): (0, 3),
            ("H", "S"): (3, 0),
            ("H", "H"): (3, 3),
        }
        self.assertEqual(
            set(nash_profiles(("S", "H"), pay)),
            {("S", "S"), ("H", "H")},
        )
        self.assertAlmostEqual(4 * 0.75, 3)
        self.assertLess(4 * 0.5, 3)
        self.assertGreater(4 * 0.8, 3)

    def test_c06_public_goods(self):
        for other_contributors in range(4):
            keep = 1 + 2 * other_contributors / 4
            contribute = 2 * (other_contributors + 1) / 4
            self.assertGreater(keep, contribute)
        self.assertEqual(2 * 4, 8)
        self.assertEqual(1 * 4, 4)

    def test_c07_second_price_auction(self):
        valuations = {"A": 10, "B": 8, "C": 5}
        bids = valuations.copy()
        winner = max(bids, key=bids.get)
        price = max(v for bidder, v in bids.items() if bidder != winner)
        self.assertEqual((winner, price, valuations[winner] - price), ("A", 8, 2))
        # Other bids fixed; no alternative A-bid yields utility above 2.
        for alternative in range(21):
            if alternative > 8:
                utility = 10 - 8
            elif alternative < 8:
                utility = 0
            else:  # A tie may win at price 8 or lose.
                utility = 2
            self.assertLessEqual(utility, 2)

    def test_c08_congestion(self):
        def delay(profile, index):
            return profile.count("A") if profile[index] == "A" else 2.5
        profiles = (("A", "A"), ("A", "B"), ("B", "A"), ("B", "B"))
        costs = {p: sum(delay(p, i) for i in range(2)) for p in profiles}
        self.assertEqual(costs[("A", "A")], 4)
        self.assertEqual(min(costs.values()), 3.5)
        for index in (0, 1):
            other = list(("A", "A"))
            other[index] = "B"
            self.assertGreater(delay(tuple(other), index), 2)

    def test_c09_nash_bargaining(self):
        # Maximize (x - 1) * (7 - x) on [1,7].
        def product(x):
            return (x - 1) * (7 - x)
        candidates = [1 + i / 100 for i in range(601)]
        optimum = max(candidates, key=product)
        self.assertAlmostEqual(optimum, 4)
        self.assertAlmostEqual(10 - optimum, 6)

    def test_c10_cooperative_core(self):
        # Sum of three pair constraints: 2 * grand_value >= 3 * 100.
        self.assertLess(2 * 120, 3 * 100)
        self.assertEqual(2 * 150, 3 * 100)
        allocation = (50, 50, 50)
        self.assertEqual(sum(allocation), 150)
        for pair in combinations(range(3), 2):
            self.assertGreaterEqual(sum(allocation[i] for i in pair), 100)

    def test_markdown_fences_and_local_links(self):
        fence = chr(96) * 3
        link = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
        for relative in DOCS:
            with self.subTest(document=relative):
                path = ROOT / relative
                self.assertTrue(path.is_file(), f"Missing file: {relative}")
                text = path.read_text(encoding="utf-8")
                self.assertTrue(text.endswith("\n"), f"No final newline: {relative}")
                opened = False
                for line_number, line in enumerate(text.splitlines(), 1):
                    if not line.startswith(fence):
                        continue
                    if not opened:
                        self.assertRegex(
                            line,
                            r"^" + re.escape(fence) + r"[A-Za-z0-9_-]+$",
                            f"Invalid opening fence {relative}:{line_number}",
                        )
                    else:
                        self.assertEqual(
                            line, fence,
                            f"Invalid closing fence {relative}:{line_number}",
                        )
                    opened = not opened
                self.assertFalse(opened, f"Unclosed fenced block: {relative}")
                for target in link.findall(text):
                    if target.startswith(("http://", "https://", "#", "mailto:")):
                        continue
                    file_part = target.split("#", 1)[0]
                    if not file_part:
                        continue
                    self.assertTrue(
                        (path.parent / file_part).is_file(),
                        f"Broken link in {relative}: {target}",
                    )


if __name__ == "__main__":
    unittest.main()
