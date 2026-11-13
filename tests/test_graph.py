"""Unit tests for agent-temporal-knowledge-graph-anchor."""
import unittest
from agent_temporal_knowledge_graph_anchor.graph import TemporalKnowledgeGraph

class TestTemporalKnowledgeGraph(unittest.TestCase):
    def setUp(self):
        self.tkg = TemporalKnowledgeGraph()

    def test_point_in_time_query(self):
        self.tkg.assert_fact("ProjectX", "Status", "Planning", valid_from=10.0, valid_to=50.0)
        self.tkg.assert_fact("ProjectX", "Status", "Active", valid_from=50.0, valid_to=100.0)
        self.assertEqual(self.tkg.query("ProjectX", "Status", 30.0), "Planning")
        self.assertEqual(self.tkg.query("ProjectX", "Status", 75.0), "Active")
        self.assertIsNone(self.tkg.query("ProjectX", "Status", 5.0))

    def test_auto_cap_previous_fact(self):
        self.tkg.assert_fact("Server1", "Leader", "NodeA", valid_from=1.0)
        self.tkg.assert_fact("Server1", "Leader", "NodeB", valid_from=10.0)
        self.assertEqual(self.tkg.query("Server1", "Leader", 5.0), "NodeA")
        self.assertEqual(self.tkg.query("Server1", "Leader", 15.0), "NodeB")

if __name__ == "__main__":
    unittest.main()
