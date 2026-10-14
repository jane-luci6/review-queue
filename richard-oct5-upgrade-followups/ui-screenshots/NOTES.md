# Jane UI screenshots — Oct 5 2026 (batch 1 of 2+)

Context for Upgrade Guide / Richard follow-ups. Not for external use.

## Files
1. `01-systems-hcap-procentric.png` — Systems / HCAP Application Manager. Catalog gaps (55UL3J-B / Bar TV / Sportsbook TV). Deploy reminder: Service XML pending, panel does not auto-deploy. XAIT/HCAP/WebSocket chain green. ~10 Connected HCAP devices.
2. `02-system-logs-device-incidents.png` — Device Incidents (21). Active: Test LG offline since Sep 30 (~1445 failures, ping_failure). Header: Establishing connection.
3. `03-analytics-reliability.png` — Reliability 7d: 1 open Offline incident (Test LG). Header: Establishing connection. Sidebar shows Video Wall Config.
4. `04-analytics-automation.png` — Automation 7d: Entryway Afternoon Default 7/7 (100%). Header: Establishing connection.
5. `05-analytics-commands.png` — Commands 7d: mostly green; recent failure spike ~10–11am; Lg Display avg latency 108.5s vs Enseo 11ms. Header: Establishing connection.
6. `06-analytics-overview.png` — Overview 7d: 206 cmds 96.1%; 1 open incident; header **Realtime degraded**.
7. `07-dashboard-overview.png` — Dashboard: Degraded; 26 total / 23 online / 3 offline; Video Wall **0/2**; Test LG offline 5d; TV 19 volume cmds ~112–121s latency.
8. `08-dashboard-corex-health.png` — CoreX Health: heartbeat healthy; Realtime degraded; health events cycling realtime via ui_realtime failed/connecting; Test LG 1444 failures.

## Ties to elevated undecided
- U-01–03 bugs: realtime degraded / establishing connection; Test LG noise; LG/TV latency.
- U-04 video wall: dashboard Video Wall 0/2; sidebar Video Wall Config.
- U-05 demo deploy: Systems deploy-from-Service-XML banner + catalog gaps.
