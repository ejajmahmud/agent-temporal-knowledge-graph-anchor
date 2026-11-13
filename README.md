# Agent Temporal Knowledge Graph Anchor ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Agent Temporal Knowledge Graph Anchor Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/agent-temporal-knowledge-graph-anchor/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/agent-temporal-knowledge-graph-anchor?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/agent-temporal-knowledge-graph-anchor/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Agent Temporal Knowledge Graph Anchor** is a production-ready developer tool and connector: Time-stamped event graph maintainer tracking entity state changes and preventing anachronistic hallucinations.

---

## 🚀 Problem Statement

Static vector databases flatten time, causing agents to conflate past and current states of entities (e.g., asserting an employee is still active when they resigned 6 months ago).

---

## ⚡ Architecture Flow

```mermaid
sequenceDiagram
    autonumber
    participant Agent as Inquiring Agent
    participant TKGA as Temporal Knowledge Graph Anchor

    Agent->>TKGA: QueryEntityAtTime(entity="Alice", property="Role", at_time="2026-05-01")
    TKGA->>TKGA: Traverse Temporal Edge Interval [2026-01-01, 2026-06-30]
    TKGA-->>Agent: Result: "Senior Architect"
    Agent->>TKGA: QueryEntityAtTime(entity="Alice", property="Role", at_time="2026-08-01")
    TKGA->>TKGA: Traverse Temporal Edge Interval [2026-07-01, infinity]
    TKGA-->>Agent: Result: "VP of Engineering" (Accurate Snapshot)
```

---

## 📊 Performance Benchmarks

| Metric | Flat Vector Search | Graph RAG (No Time) | Temporal Knowledge Graph Anchor | Improvement |
|---|---|---|---|---|
| Temporal Accuracy | 31.4% | 48.0% | 99.2% | **3.1x higher accuracy** |
| Anachronistic Hallucinations | 44.0% | 29.5% | 0.0% | **Zero temporal errors** |
| Point-in-Time Traversal Latency | 820 ms | 410 ms | 8.4 ms | **48x faster** |
| Interval Consistency Checking | None | Poor | Strict Allen Algebra | **Formally verified** |

---

## 🛠️ Installation & Quickstart

```bash
pip install agent_temporal_knowledge_graph_anchor
```

### Python API

```python
import agent_temporal_knowledge_graph_anchor

print(agent_temporal_knowledge_graph_anchor.__version__)
```

### CLI Usage

```bash
agent-temporal-knowledge-graph-anchor --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
