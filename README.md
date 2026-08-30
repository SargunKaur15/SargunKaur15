# Hi, I'm Sargun Kaur 👋

## Cybersecurity | Blue Team | SOC Analyst (Student)

Cybersecurity student focused on Blue Team and SOC operations. I build
defensive security tooling around threat detection, alert triage,
investigation, MITRE ATT&CK mapping, and applied machine learning for
security — most recently as SOCGenie, a full SOC platform prototype.

## 🛡️ What I Build

Defensive security projects that follow a real analyst workflow, end to end:

```
Detection → Triage → Investigation → Risk → MITRE ATT&CK → Response
```

Not dashboards for their own sake — systems where each stage genuinely feeds
the next, and where a claim in the UI ("model trained," "X techniques
mapped") is backed by real code, not a placeholder.

## 🚀 Featured Projects

### [SOCGenie](https://github.com/SargunKaur15/SOCGenie)
**Intelligent Security Operations Platform**

A SOC platform prototype covering the full analyst workflow: a Command
Center, alert monitoring and triage, a rule-based log detection engine
(7 deterministic rules), an investigation workspace with attack-path
visualization, a seven-factor risk-scoring engine, and a MITRE ATT&CK
technique map (14 techniques across 10 tactics) tied to real alert
evidence. Alongside the SOC console, a Random Forest + Isolation Forest
model was trained and evaluated offline on CSE-CIC-IDS2018, with real,
disclosed metrics (99.97% accuracy, 0.961 macro-F1 on the held-out test
set) — offline evaluation results, not a production benchmark.

`React` `TypeScript` `Three.js` `Python` `FastAPI` `scikit-learn`

### [AI-CyberSentinel-SOC-Dashboard](https://github.com/SargunKaur15/AI-CyberSentinel-SOC-Dashboard)
**AI-assisted Level-1 alert triage**

A SOC dashboard that extracts indicators of compromise (IPs, URLs, file
hashes) from pasted SIEM alerts or raw logs, produces a structured triage
summary with a severity rating, and generates a downloadable incident
report. Runs fully offline with deterministic rule-based triage when no
API key is configured.

`Python` `Streamlit`

## 🔐 Security Focus

**Strong evidence:** Security Detection · MITRE ATT&CK · Security
Investigation · Rule-Based Detection · Applied ML for Security

**Some evidence:** Log Analysis · Threat Intelligence · Incident Response ·
Security Automation · Networking

## ⚙️ Tech Stack

**Languages:** Python · TypeScript · JavaScript

**Security:** MITRE ATT&CK mapping · detection engineering · log parsing

**ML:** scikit-learn · pandas · numpy

**Frontend:** React · Vite · Tailwind CSS

**Visualization:** Three.js (`@react-three/fiber`, `@react-three/drei`)

**Backend:** Node.js/TypeScript · Python/FastAPI

## 🎯 Currently Focused On

- SOC operations and detection engineering
- Incident investigation workflows
- MITRE ATT&CK-driven analysis
- Applied machine learning for security use cases

## 📫 Contact

Open to connecting — reach out here on GitHub.
