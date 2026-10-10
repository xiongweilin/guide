"""Finite countermodels for action-first guide propositions.

These are exhaustive checks of finite mathematical special cases, not human
judgment studies, production authorization or Lean kernel proofs.
"""
from itertools import combinations, product
import unittest


def common_safe_action(possible, actions, allowed):
    return next(
        (action for action in actions
         if all((world, action) in allowed for world in possible)),
        None,
    )


def contingent_observation_policy(possible, actions, allowed, observe):
    """Return observation->common-action map only when every branch is covered."""
    result = {}
    for label in {observe[world] for world in possible}:
        branch = {world for world in possible if observe[world] == label}
        action = common_safe_action(branch, actions, allowed)
        if action is None:
            return None
        result[label] = action
    return result


class RobustActionSemantics(unittest.TestCase):
    def test_complete_three_world_truth_tables_and_refinement_monotonicity(self):
        worlds, actions = (0, 1, 2), ("a", "b", "c")
        pairs = tuple(product(worlds, actions))
        beliefs = [
            frozenset(comb)
            for size in (1, 2, 3)
            for comb in combinations(worlds, size)
        ]
        for mask in range(1 << len(pairs)):
            allowed = {
                pair for index, pair in enumerate(pairs)
                if mask & (1 << index)
            }
            for belief in beliefs:
                action = common_safe_action(belief, actions, allowed)
                if action is not None:
                    self.assertTrue(
                        all((world, action) in allowed for world in belief)
                    )
                    for refined in beliefs:
                        if refined <= belief:
                            self.assertIsNotNone(
                                common_safe_action(refined, actions, allowed),
                                (mask, belief, refined),
                            )
                else:
                    self.assertFalse(
                        any(all((w, a) in allowed for w in belief) for a in actions)
                    )

    def test_observation_unblocks_disjoint_authorized_actions(self):
        beliefs = {"w0", "w1"}
        allowed = {("w0", "disable-a"), ("w1", "disable-b")}
        actions = ("disable-a", "disable-b")
        self.assertIsNone(common_safe_action(beliefs, actions, allowed))
        mapping = contingent_observation_policy(
            beliefs, actions, allowed, {"w0": "a", "w1": "b"},
        )
        self.assertEqual(mapping, {"a": "disable-a", "b": "disable-b"})

    def test_uninformative_observation_does_not_create_sufficiency(self):
        possible = {"w0", "w1"}
        allowed = {("w0", "a"), ("w1", "b")}
        policy = contingent_observation_policy(
            possible, ("a", "b"), allowed, {"w0": "same", "w1": "same"},
        )
        self.assertIsNone(policy)

    def test_authority_and_safety_both_required(self):
        possible = {"w0", "w1"}
        safe = {(w, "delete") for w in possible}
        authorized = {("w0", "delete")}
        allowed = safe & authorized
        self.assertIsNone(common_safe_action(possible, ("delete",), allowed))

    def test_missing_actual_world_breaks_real_world_claim(self):
        # Holding uniformly over an incomplete belief is *not* a guarantee
        # of the actual world when reality was omitted from the model.
        allowed = {("modeled", "act")}
        self.assertEqual(
            common_safe_action({"modeled"}, ("act",), allowed), "act",
        )
        self.assertNotIn(("unmodeled", "act"), allowed)


if __name__ == "__main__":
    unittest.main()
