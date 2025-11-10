# E.ON Mail Copilot - Local LLM assistant for analyzing and drafting customer emails.**

This repository implements a initial proof-of-concept for semi-automated email handling at **E.ON**.  
The goal is to support Customer Agents (CAs) by analyzing incoming messages, generating draft replies, and providing stylistic variations — while the CA remains in control of the final answer.

---

## 🚀 Local setup

We use [Ollama](https://ollama.com) with **Llama 3.2 3B Instruct**, which runs efficiently on laptops and requires no external API tokens.

```bash
# 1. Install Ollama (https://ollama.com/download)
# 2. Pull the model via terminal (e.g. Powershell if on Windows)
ollama pull llama3.2
# 3. Test the model
ollama run llama3.2
