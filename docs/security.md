# Security model

This application does not authenticate end users and should not be exposed as a public web service. The simulator and local lexical assistant require no secrets.

Do not commit `.env` or API keys. The `.gitignore` excludes `.env` by default. If integrating an external language-model provider, inject credentials through environment variables, use HTTPS, enforce a timeout, and avoid sending personal or sensitive payloads. External LLM integration is not enabled by default.

Operation identifiers in the demonstration are not credentials and are used solely to demonstrate idempotency.
