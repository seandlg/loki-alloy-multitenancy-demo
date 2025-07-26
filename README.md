# Grafana Alloy and Loki: Dynamic Tenant Routing for Logs

This repository shows how to process logs with Grafana Alloy, s.t. they are dynamically routed to different tenants in Loki.

## Getting started

Install [just](https://just.systems/man/en/) and [docker](https://docs.docker.com/engine/install/). Run `just` to see available commands. In order to spin up the stack, run:

```bash
just dev
```

Browse to [http://localhost:12000](http://localhost:12000) to see the Grafana UI and view logs.

## Loki tenants

Alloy is configured to set the loki tenant dynamically based on the content of the log message. This demo uses the tenants `app` (all logs), `tenant1`, and `tenant2`.
