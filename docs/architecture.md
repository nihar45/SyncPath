# Architecture

```text
Scenario JSON -> validated Scenario -> event queue -> Network / Server
                                              |          |
                                              +-- attempts + side effects
                                                       |
                                                  Metrics / reports

Question -> passage retrieval -> cited answer
```

The simulator is an in-process discrete-event model. It has no production API, no mobile-device transport, and no user-authentication service. All application data used in the examples is non-sensitive demonstration data.
