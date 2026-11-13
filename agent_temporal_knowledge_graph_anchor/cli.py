"""CLI for agent-temporal-knowledge-graph-anchor."""
import sys
import argparse
from .graph import TemporalKnowledgeGraph

def main():
    parser = argparse.ArgumentParser(description="Agent Temporal Knowledge Graph Anchor CLI")
    parser.add_argument("--demo", action="store_true", help="Run temporal knowledge graph query demo")
    args = parser.parse_args()

    if args.demo:
        tkg = TemporalKnowledgeGraph()
        tkg.assert_fact("Bob", "Title", "Junior Engineer", valid_from=100.0, valid_to=200.0)
        tkg.assert_fact("Bob", "Title", "Staff Engineer", valid_from=200.0, valid_to=None)
        print(f"[+] Bob Title at t=150: {tkg.query('Bob', 'Title', 150.0)}")
        print(f"[+] Bob Title at t=250: {tkg.query('Bob', 'Title', 250.0)}")
        print(f"[+] Full history: {tkg.history('Bob', 'Title')}")
    else:
        parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
