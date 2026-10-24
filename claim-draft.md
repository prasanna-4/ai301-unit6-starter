I'd like to take this issue. The problem is clear: interactive elements in the Kubernetes console UI (buttons, inputs, links, divs) are missing ARIA labels for screen reader users, affecting accessibility compliance.

My first step will be to trace through the INVENTORY.md file and the component files listed in the issue to verify which interactive elements need labels, then add `aria-label` attributes where they're missing. I'll run the existing accessibility tests to ensure my changes don't break anything.

I'll post what I find either way by October 27, 2026.
