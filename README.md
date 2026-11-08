# incident-rca-agent

An agent that triages incidents on a Kubernetes cluster. When something breaks, it pulls logs from Loki, metrics from Prometheus, and pod events from the Kubernetes API, looks up related runbooks and past post-mortems, and writes up a likely root cause with a confidence score.

## Stack

- Python, LangGraph / LangChain
- Loki, Prometheus, OpenTelemetry
- Kubernetes (Kind), Helm, Docker
- ChromaDB for runbook and post-mortem search

## Getting started

```bash
git clone https://github.com/Shihasz/incident-rca-agent.git
cd incident-rca-agent
python3 -m venv .venv
source .venv/bin/activate
```

Requires Python 3.11 or newer. Developed on Ubuntu under WSL2.

## Status

Early setup. More documentation will be added as the pieces land.
