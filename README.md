# Local Server Control Panel (v1)

This project is a **local web-based control panel** for managing a Minecraft server on Windows.

The goal is to build a **practical, system-oriented tool** that allows starting, stopping and monitoring a server through a simple web interface.

This project is intentionally built **step by step**, focusing on functionality first and security later.

---

## Why this project exists

I am currently training as an IT Trainee and want to go beyond theoretical knowledge.

Instead of using existing tools, I want to:
- understand how server control works internally
- learn how backend systems interact with the operating system
- build something real, usable and explainable

This project also serves as a **learning and documentation project** for my personal development.

---

## Current scope (v1 – local only)

- Local FastAPI backend
- Start / stop a Minecraft server process
- Check server status
- Read server logs
- No authentication
- Localhost only (no external access)

⚠️ **Security note:**  
This version is intentionally **not secured** because it is designed to run locally only.  
Security, authentication and remote access are planned for later iterations.

---

## Tech stack

- Python
- FastAPI
- Windows
- Java (Minecraft server)
- HTML / minimal JavaScript (later)

---

## Project status

**Status:** Setup phase  
**Next step:** Basic FastAPI setup and health endpoint

---

## Planned future steps

- Authentication (basic login)
- Remote access via port forwarding
- HTTPS
- Improved web interface
- Multi-server support (optional)

---

## Disclaimer

This project is built for **learning and demonstration purposes**.  
It is not intended for production use.
