# AgentForge RL

Reinforcement learning framework for training autonomous AI agents to master MCP tool ecosystems through multi-step reasoning, intelligent tool chaining, and reward-driven optimization using GRPO and RULER.

---

# Overview

AgentForge RL is an advanced AI research and engineering project focused on training autonomous LLM agents to become expert tool users inside MCP (Model Context Protocol) environments.

Instead of relying only on prompt engineering, the framework uses reinforcement learning to teach agents how to:

* explore environments
* reason across multiple steps
* chain tools effectively
* recover from failures
* optimize decision-making strategies

The project demonstrates how small language models can learn sophisticated behaviors through iterative interaction with MCP servers.

---

# Key Features

* MCP-based tool ecosystem
* Reinforcement learning with GRPO
* Automatic reward scoring using RULER
* Multi-step reasoning workflows
* Autonomous tool chaining
* SQL reasoning and JOIN generation
* Schema exploration
* Self-correcting agent behavior
* Rollout-based optimization
* Secure read-only query execution

---

# Tech Stack

## AI & Reinforcement Learning

* OpenPipe ART
* GRPO
* RULER
* Qwen 2.5 3B Instruct

## MCP Infrastructure

* FastMCP
* SQLite

## Backend

* Python
* AsyncIO

## Training & Evaluation

* Reinforcement Learning
* Rollout Sampling
* LLM-as-a-Judge Evaluation

---

# MCP Server

The framework includes a custom MCP server exposing tools for interacting with a relational database environment.

## Available Tools

| Tool                         | Description                      |
| ---------------------------- | -------------------------------- |
| `list_tables()`              | Discover available tables        |
| `describe_table(table_name)` | Inspect schemas and columns      |
| `run_query(sql)`             | Execute secure read-only queries |

The environment contains interconnected company data involving:

* employees
* departments
* projects

This setup forces agents to learn:

* schema discovery
* relational reasoning
* JOIN construction
* query planning
* error recovery

---

# How It Works

1. The MCP server runs locally with a structured SQLite database
2. ART generates diverse training scenarios
3. The agent attempts each scenario through multiple rollouts
4. MCP tools are dynamically invoked during reasoning
5. RULER evaluates trajectory quality automatically
6. GRPO reinforces successful behaviors
7. The agent progressively improves tool mastery

Over time, the model learns behaviors not present in the base model:

* strategic tool usage
* intelligent query planning
* multi-step reasoning
* autonomous correction

---

# Project Goals

The primary goal of AgentForge RL is to explore the future of:

* agentic AI systems
* autonomous reasoning
* reinforcement-trained LLM agents
* tool-native intelligence
* self-improving AI workflows

The project aims to move beyond static prompting toward adaptive autonomous AI systems capable of learning how to interact with real environments.

---

# Future Roadmap

Planned upgrades include:

* multi-agent collaboration
* memory-enhanced agents
* curriculum learning
* observability dashboard
* trajectory visualization
* reward analytics
* autonomous debugging agents
* distributed training
* self-improving workflows

---

# Repository Structure

```bash
agentforge-rl/
│
├── agents/
├── training/
├── evaluation/
├── mcp_server/
├── memory/
├── tools/
├── configs/
├── notebooks/
├── datasets/
├── observability/
├── docs/
└── README.md
```

---

# Why This Project Matters

Most AI systems today:

* rely heavily on static prompts
* use hardcoded workflows
* struggle with reliable tool usage

AgentForge RL explores a different direction:

> training autonomous AI agents to master tool ecosystems through reinforcement learning.

This project represents:

* AI infrastructure engineering
* autonomous reasoning systems
* adaptive agent behavior
* next-generation agentic AI architectures

---

# Contribution

Contributions are welcome.

Potential contribution areas:

* new MCP environments
* reward function improvements
* multi-agent systems
* observability tooling
* benchmarking pipelines
* evaluation frameworks

Fork the repository and submit a pull request with your improvements.

---

# Vision

AgentForge RL aims to explore the next generation of autonomous AI systems where agents do not simply call tools —
they learn how to master them.
