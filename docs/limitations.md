# Model limitations

- The simulation is event-driven and does not use actual sockets or mobile radios.
- Lost acknowledgment is modeled through latency exceeding the client timeout; the server may still apply the write.
- Offline queues have no durable disk persistence in this version.
- Seeds support repeatability, not a guarantee of equal random draws across strategies.
- The retrieval assistant uses a fixed documentation corpus and does not browse external documentation.
- The local simulator requires no credentials or authentication.
- A single run does not establish general reliability, availability, or performance in production.
