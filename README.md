# 🛡️ Autonomous Red vs Blue AI Defense System

An autonomous cybersecurity platform where AI agents continuously attack and defend enterprise infrastructure.

## Architecture
- 🔴 Red Team Agent: Nmap, SQLMap, Hydra via LangChain + groqapi
- 🔵 Blue Team Agent: block_ports,restart_services
- 🧠 Orchestrator: FastAPI + Celery + Redis
- 🗄️ Database: PostgreSQL
  

## Status
- [x] Phase 1: Infrastructure Setup
- [x] Phase 2: Backend (FastAPI + PostgreSQL)
- [x] Phase 3: Red Agent
- [x] Phase 4: Blue Agent
- [x] Phase 5: Orchestration Engine
- [x] Phase 6: Dashboard
- [ ] Phase 7: Integrate dashboard and backend
