# Week 2 — Distributed Tracing

## Spend Notes
- All platforms are overlapping in purpose
- 20M Free events with honeycomb
- 5000 Free events per month with rollbar
- X-Ray Free tier 100,000 traces per month
- Cloudwatch 1,000,000 API requests 5g of Log data Free.  Be careful because Cloudwatch adds up fast!

## Observablity Notes
- Logging sucks
- Super time consuming, security analyst spend most of their time analyzing logs
- Try and log things that we need to, things that may cause problems
- Observablity can reduce operational cost
### Observability vs Monitoring
#### - Tracking uptime of a website for example is monitoring
#### - Fault Management 
- Monitoring (When & where did it occur?)  
- Observability(Why did it occur?)
#### - Recovery 
- Monitoring(Is my system back up?) 
- Observablity (What can I do to prevent the issue from reoccuring)
### Observability Pillars
- Logs
    - Every App uses logs
- Traces
    - Trace back to pinpoint the problem
- Metrics
    - Use metrics to enhance logs being produced
### Building Security Metrics and Logs for tracing
- 1. Threat model for known Attack (Think of types of attacks can be done on this app) THINK LIKE A HACKER!
- 2. Check popular industry hacking methods/patterns/techniques (MITRE Framework)
- 3. Identity Instrumentation agents
### Ccentral Observability Platfarm - Security
- AWS Security Hub with EventBridge
- Open Source Dashboards
- Event Driven Architecture with AWS services
- SIEM (Security Incident and Event Management)
