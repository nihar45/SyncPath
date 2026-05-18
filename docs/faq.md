# Frequently asked questions

**Why can an operation affect the server but not count as completed?** The response may arrive after the client timeout, even if the write was accepted.

**Does retrying guarantee exactly-once delivery?** No. Server-side idempotency limits duplicate business effects, but acknowledgments can still be lost.

**Does the RAG assistant call an LLM?** No, the default assistant provides lexical retrieval and source-cited excerpts. An LLM is intentionally optional and not bundled.

**Are the sample percentages measured from production mobile devices?** No. They are simulated results under the configured scenarios.
