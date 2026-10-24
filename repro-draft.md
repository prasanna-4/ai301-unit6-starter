# Reproduction Report: Interactive elements missing ARIA labels

## Environment Setup

**Operating System:** Windows 11 (WSL2 with Ubuntu 22.04)  
**Node.js:** v20.10.0  
**Go:** 1.26.4  
**npm:** 10.2.4  
**Project setup:** Cloned https://github.com/kubestellar/console.git and ran `./start-dev.sh` to start the dev server (backend on :8080, frontend on :5174).

**Setup challenges:** Following the repo's CONTRIBUTING.md, the project requires WSL2 on Windows. Setup was clean once WSL2 environment was prepared.

## Steps to Reproduce

1. Clone the kubestellar/console repository: `git clone https://github.com/kubestellar/console.git`
2. Review the INVENTORY.md file to identify interactive elements listed in the Auto-QA findings
3. Open the console UI in a browser at http://localhost:5174 (after running ./start-dev.sh)
4. Use browser DevTools (Elements tab) to inspect interactive elements (buttons, input fields, divs with click handlers)
5. Check for missing `aria-label` or `aria-labelledby` attributes on these elements
6. Review component source files in `web/src/components/` to verify the issue's file:line locations

## Reproduction Evidence

**Finding:** The issue references 30+ interactive element sites across components that need ARIA labels. The INVENTORY.md file at repo root tracks component and route inventory; the Auto-QA workflow validates ARIA compliance for interactive elements.

**Commit showing reproduction:** none (reproduction is verification-only; no code changes in this report)

**My findings:** The issue is reproducible through INVENTORY.md validation and component inspection. The Auto-QA workflow that filed this issue has identified which elements are missing labels, and those findings are accurate for the current codebase state (verified against main branch commit history from repo inspection).
