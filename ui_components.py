"""
Research Scope AI - UI Components & Custom Styling
Defines glassmorphism CSS, card renderers, and HTML templates for Gradio.
Clean, modern enterprise styling with zero emojis.
"""
from typing import Dict, Any, List
from academic_retrieval import Paper
from llm_engine import IdeaStructure

CUSTOM_CSS = """
/* Import Modern Typography */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg-primary: #050308;
    --bg-secondary: #100719;
    --bg-card: rgba(18, 8, 32, 0.82);
    --border-color: rgba(192, 132, 252, 0.16);
    --border-highlight: rgba(168, 85, 247, 0.52);
    --accent-indigo: #8B5CF6;
    --accent-cyan: #C084FC;
    --accent-emerald: #D946EF;
    --accent-purple: #A855F7;
    --accent-rose: #F0ABFC;
    --text-main: #F8FAFC;
    --text-secondary: #C4B5FD;
    --text-muted: #8B7AA8;
}

body, .gradio-container {
    background:
        radial-gradient(circle at 50% -20%, rgba(126, 34, 206, 0.18), transparent 38%),
        #050308 !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    color: var(--text-main) !important;
    width: 100% !important;
    max-width: none !important;
    margin: 0 !important;
    padding: 10px 18px !important;
    box-sizing: border-box !important;
}

.gradio-container > .main,
.gradio-container .main,
.gradio-container .contain,
.gradio-container .contain > .block {
    width: 100% !important;
    max-width: none !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
}

.gradio-container .main {
    padding: 0 !important;
}

footer {
    display: none !important;
}

/* Semantic decomposition and knowledge graph tab */
.graph-tab-hero {
    position: relative;
    overflow: hidden;
    margin: 4px 0 16px;
    padding: 22px 26px;
    border: 1px solid rgba(165, 180, 252, 0.28);
    border-radius: 16px;
    background:
        radial-gradient(circle at 88% 20%, rgba(192, 132, 252, 0.2), transparent 28%),
        radial-gradient(circle at 12% 110%, rgba(34, 211, 238, 0.15), transparent 34%),
        linear-gradient(110deg, rgba(11, 8, 25, 0.99), rgba(28, 15, 49, 0.96));
    box-shadow:
        0 14px 34px rgba(2, 6, 23, 0.28),
        0 0 30px rgba(168, 85, 247, 0.08),
        inset 0 1px rgba(255, 255, 255, 0.08);
}

.graph-tab-hero::before {
    content: "";
    position: absolute;
    left: 26px;
    right: 26px;
    bottom: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #22D3EE 20%, #A855F7 80%, transparent);
    opacity: 0.75;
}

.back-to-input-btn {
    width: auto !important;
    min-width: 190px !important;
    margin: 4px 0 0 auto !important;
    border: 1px solid rgba(148, 163, 184, 0.24) !important;
    background: rgba(18, 8, 32, 0.82) !important;
    color: #CBD5E1 !important;
}

.back-to-input-btn:hover {
    border-color: rgba(165, 180, 252, 0.65) !important;
    color: #F8FAFC !important;
}

.graph-tab-hero::after {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    right: 7%;
    top: -108px;
    border: 1px solid rgba(192, 132, 252, 0.2);
    border-radius: 50%;
    box-shadow: 0 0 0 22px rgba(168, 85, 247, 0.045), 0 0 0 44px rgba(34, 211, 238, 0.03);
}

.graph-tab-kicker {
    position: relative;
    z-index: 1;
    color: #C4B5FD;
    font: 700 10px/1.2 'JetBrains Mono', monospace;
    letter-spacing: 1.6px;
}

.graph-tab-kicker span {
    display: inline-block;
    width: 5px;
    height: 5px;
    margin: 0 8px 2px;
    border-radius: 50%;
    background: #D946EF;
    box-shadow: 0 0 10px #D946EF;
}

.graph-tab-title {
    position: relative;
    z-index: 1;
    margin-top: 9px;
    color: #F8FAFC;
    font: 800 25px/1.15 'Outfit', sans-serif;
    letter-spacing: -0.5px;
}

.graph-tab-title em {
    background: linear-gradient(100deg, #67E8F9 0%, #A78BFA 52%, #E879F9 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    font-style: normal;
}

.graph-tab-subtitle {
    position: relative;
    z-index: 1;
    max-width: 650px;
    margin-top: 8px;
    color: #C4B5FD;
    font-size: 12.5px;
    line-height: 1.55;
}

.graph-tab-grid {
    gap: 16px !important;
}

.graph-tab-panel {
    min-width: 0;
    padding: 0 !important;
}

.graph-tab-panel > .block {
    height: 100%;
}

.graph-visual-panel {
    overflow: hidden;
    border: 1px solid rgba(168, 85, 247, 0.2);
    border-radius: 14px;
    background: linear-gradient(145deg, rgba(18, 8, 32, 0.96), rgba(8, 3, 18, 0.99));
    box-shadow: 0 14px 30px rgba(2, 6, 23, 0.22), 0 0 24px rgba(168, 85, 247, 0.07);
}

.knowledge-graph-plot {
    padding: 6px !important;
}

.knowledge-graph-plot .wrap {
    border-radius: 10px;
}

/* Direction deep-dive tab */
.deep-dive-hero {
    position: relative;
    overflow: hidden;
    margin: 4px 0 16px;
    padding: 22px 26px;
    border: 1px solid rgba(168, 85, 247, 0.24);
    border-radius: 16px;
    background:
        radial-gradient(circle at 90% 0%, rgba(217, 70, 239, 0.16), transparent 28%),
        radial-gradient(circle at 8% 100%, rgba(34, 211, 238, 0.12), transparent 32%),
        linear-gradient(110deg, rgba(18, 8, 32, 0.98), rgba(12, 19, 42, 0.96));
    box-shadow: 0 14px 34px rgba(2, 6, 23, 0.24), inset 0 1px rgba(255, 255, 255, 0.06);
}

.deep-dive-kicker {
    color: #C4B5FD;
    font: 700 10px/1.2 'JetBrains Mono', monospace;
    letter-spacing: 1.6px;
}

.deep-dive-kicker span {
    display: inline-block;
    width: 5px;
    height: 5px;
    margin: 0 8px 2px;
    border-radius: 50%;
    background: #A78BFA;
    box-shadow: 0 0 10px #A78BFA;
}

.deep-dive-title {
    margin-top: 9px;
    color: #F8FAFC;
    font: 800 25px/1.15 'Outfit', sans-serif;
    letter-spacing: -0.5px;
}

.deep-dive-title em {
    color: #E879F9;
    font-style: normal;
}

.deep-dive-subtitle {
    max-width: 700px;
    margin-top: 8px;
    color: #C4B5FD;
    font-size: 12.5px;
    line-height: 1.55;
}

.deep-dive-layout {
    gap: 16px !important;
}

.deep-dive-controls {
    align-self: flex-start;
    padding: 18px !important;
    border: 1px solid rgba(148, 163, 184, 0.14);
    border-radius: 14px;
    background: linear-gradient(160deg, rgba(18, 8, 32, 0.96), rgba(8, 3, 18, 0.99));
    box-shadow: 0 14px 30px rgba(2, 6, 23, 0.22);
}

.deep-dive-control-heading {
    display: flex;
    gap: 11px;
    align-items: center;
    margin-bottom: 15px;
}

.deep-dive-step {
    display: grid;
    width: 30px;
    height: 30px;
    place-items: center;
    border: 1px solid rgba(103, 232, 249, 0.35);
    border-radius: 9px;
    background: rgba(34, 211, 238, 0.12);
    color: #67E8F9;
    font: 700 11px 'JetBrains Mono', monospace;
}

.deep-dive-control-title {
    color: #F8FAFC;
    font: 700 14px 'Outfit', sans-serif;
}

.deep-dive-control-copy {
    margin-top: 3px;
    color: #64748B;
    font-size: 11px;
}

.deep-dive-action-btn {
    margin-top: 12px !important;
    width: 100% !important;
}

.evidence-legend {
    margin-top: 18px;
    padding: 14px;
    border: 1px solid rgba(192, 132, 252, 0.12);
    border-radius: 11px;
    background: rgba(2, 6, 23, 0.32);
}

.evidence-legend-title {
    margin-bottom: 11px;
    color: #CBD5E1;
    font: 700 10px 'JetBrains Mono', monospace;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.evidence-legend-item {
    display: flex;
    gap: 9px;
    align-items: flex-start;
    margin-top: 10px;
    color: #CBD5E1;
    font-size: 11px;
    line-height: 1.35;
}

.evidence-legend-item small {
    color: #64748B;
    font-size: 10px;
}

.evidence-dot {
    width: 8px;
    height: 8px;
    flex: 0 0 auto;
    margin-top: 3px;
    border-radius: 50%;
}

.evidence-dot-paper {
    background: #D946EF;
    box-shadow: 0 0 9px rgba(217, 70, 239, 0.7);
}

.evidence-dot-inferred {
    background: #C084FC;
    box-shadow: 0 0 9px rgba(192, 132, 252, 0.7);
}

/* Saturation matrix and activity timeline tab */
.saturation-hero {
    position: relative;
    overflow: hidden;
    margin: 4px 0 14px;
    padding: 22px 26px;
    border: 1px solid rgba(232, 121, 249, 0.24);
    border-radius: 16px;
    background:
        radial-gradient(circle at 88% 0%, rgba(232, 121, 249, 0.16), transparent 27%),
        radial-gradient(circle at 7% 100%, rgba(34, 211, 238, 0.13), transparent 34%),
        linear-gradient(110deg, rgba(18, 8, 32, 0.98), rgba(27, 13, 45, 0.95));
    box-shadow: 0 14px 34px rgba(2, 6, 23, 0.24), inset 0 1px rgba(255, 255, 255, 0.06);
}

.saturation-kicker {
    color: #E879F9;
    font: 700 10px/1.2 'JetBrains Mono', monospace;
    letter-spacing: 1.6px;
}

.saturation-kicker span {
    display: inline-block;
    width: 5px;
    height: 5px;
    margin: 0 8px 2px;
    border-radius: 50%;
    background: #22D3EE;
    box-shadow: 0 0 10px #22D3EE;
}

.saturation-title {
    margin-top: 9px;
    color: #F8FAFC;
    font: 800 25px/1.15 'Outfit', sans-serif;
    letter-spacing: -0.5px;
}

.saturation-title em {
    color: #C4B5FD;
    font-style: normal;
}

.saturation-subtitle {
    max-width: 720px;
    margin-top: 8px;
    color: #C4B5FD;
    font-size: 12.5px;
    line-height: 1.55;
}

.saturation-guide {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-bottom: 16px;
}

.saturation-guide-item {
    display: flex;
    gap: 10px;
    align-items: flex-start;
    padding: 11px 13px;
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    background: rgba(18, 8, 32, 0.68);
}

.saturation-guide-item b {
    display: block;
    color: #E2E8F0;
    font-size: 11px;
}

.saturation-guide-item small {
    display: block;
    margin-top: 3px;
    color: #64748B;
    font-size: 10px;
}

.signal-dot {
    width: 8px;
    height: 8px;
    flex: 0 0 auto;
    margin-top: 3px;
    border-radius: 50%;
}

.signal-dot-opportunity {
    background: #E879F9;
    box-shadow: 0 0 10px rgba(232, 121, 249, 0.8);
}

.signal-dot-active {
    background: #22D3EE;
    box-shadow: 0 0 10px rgba(34, 211, 238, 0.8);
}

.signal-dot-maturity {
    background: #A78BFA;
    box-shadow: 0 0 10px rgba(167, 139, 250, 0.8);
}

.saturation-chart-grid {
    gap: 16px !important;
}

.saturation-chart-card {
    min-width: 0;
    padding: 17px 17px 8px !important;
    border: 1px solid rgba(148, 163, 184, 0.14);
    border-radius: 14px;
    background: linear-gradient(160deg, rgba(18, 8, 32, 0.96), rgba(8, 3, 18, 0.99));
    box-shadow: 0 14px 30px rgba(2, 6, 23, 0.22);
}

.saturation-matrix-card {
    border-color: rgba(232, 121, 249, 0.18);
}

.saturation-timeline-card {
    border-color: rgba(34, 211, 238, 0.18);
}

.saturation-card-kicker {
    color: #64748B;
    font: 700 10px 'JetBrains Mono', monospace;
    letter-spacing: 1.1px;
}

.saturation-card-kicker span {
    float: right;
    color: #475569;
}

.saturation-card-title {
    margin-top: 6px;
    color: #F8FAFC;
    font: 700 16px 'Outfit', sans-serif;
}

.saturation-card-copy {
    margin-top: 3px;
    color: #64748B;
    font-size: 11px;
}

.saturation-plot {
    margin-top: 8px;
}

@media (max-width: 900px) {
    .saturation-title {
        font-size: 21px;
    }

    .saturation-guide {
        grid-template-columns: 1fr;
    }
}

.deep-dive-results {
    min-width: 0;
}

.deep-dive-output {
    display: block;
}

.deep-dive-gap-card {
    margin-bottom: 9px;
    padding: 12px 14px;
    border: 1px solid rgba(255, 255, 255, 0.07);
    border-left: 3px solid;
    border-radius: 9px;
    background: rgba(18, 8, 32, 0.7);
}

.deep-dive-connection-card {
    margin-bottom: 16px;
    padding: 15px;
    border: 1px solid rgba(168, 85, 247, 0.3);
    border-radius: 11px;
    background: linear-gradient(135deg, rgba(168, 85, 247, 0.14), rgba(34, 211, 238, 0.06));
}

.deep-dive-summary-card {
    padding: 18px !important;
}

.deep-dive-paper-card {
    padding: 17px 18px;
    border-color: rgba(217, 70, 239, 0.16);
}

.deep-dive-section-label {
    display: flex;
    align-items: center;
    gap: 9px;
    margin: 18px 0 10px;
    color: #F8FAFC;
    font: 700 13.5px 'Outfit', sans-serif;
    letter-spacing: 0.4px;
    text-transform: uppercase;
}

.deep-dive-section-label span {
    color: #E879F9;
    font: 700 10px 'JetBrains Mono', monospace;
}

.deep-dive-section-label small {
    margin-left: auto;
    color: #64748B;
    font: 500 10px 'JetBrains Mono', monospace;
    letter-spacing: 0;
    text-transform: none;
}

@media (max-width: 900px) {
    .deep-dive-title {
        font-size: 21px;
    }
}

@media (max-width: 900px) {
    .graph-tab-title {
        font-size: 21px;
    }
}

/* Glassmorphism Containers */
.glass-panel {
    background: var(--bg-card) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 12px !important;
    padding: 20px !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35) !important;
    transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.glass-panel:hover {
    border-color: rgba(255, 255, 255, 0.14) !important;
}

.hero-header {
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(circle at 92% 15%, rgba(217, 70, 239, 0.2), transparent 25%),
        radial-gradient(circle at 12% 115%, rgba(34, 211, 238, 0.16), transparent 34%),
        linear-gradient(135deg, rgba(27, 13, 50, 0.98), rgba(9, 8, 28, 0.98));
    border: 1px solid rgba(192, 132, 252, 0.28);
    border-radius: 20px;
    padding: 30px 34px;
    margin-bottom: 18px;
    box-shadow: 0 18px 48px rgba(2, 6, 23, 0.38), inset 0 1px rgba(255, 255, 255, 0.08);
}

.hero-header::before {
    content: "";
    position: absolute;
    inset: 0;
    opacity: 0.22;
    background-image: linear-gradient(rgba(148, 163, 184, 0.13) 1px, transparent 1px), linear-gradient(90deg, rgba(148, 163, 184, 0.13) 1px, transparent 1px);
    background-size: 34px 34px;
    mask-image: linear-gradient(90deg, black, transparent 76%);
    pointer-events: none;
}

.hero-header::after {
    content: "";
    position: absolute;
    width: 240px;
    height: 240px;
    right: 7%;
    top: -170px;
    border: 1px solid rgba(165, 180, 252, 0.22);
    border-radius: 50%;
    box-shadow: 0 0 0 28px rgba(165, 180, 252, 0.04), 0 0 0 56px rgba(165, 180, 252, 0.025);
    pointer-events: none;
}

.hero-title {
    position: relative;
    z-index: 1;
    font-family: 'Outfit', sans-serif;
    font-size: clamp(30px, 4vw, 44px);
    font-weight: 800;
    background: linear-gradient(90deg, #FFFFFF 0%, #C4B5FD 42%, #E879F9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    letter-spacing: -1.2px;
    display: flex;
    align-items: center;
    gap: 12px;
}

.hero-subtitle {
    position: relative;
    z-index: 1;
    color: #94A3B8;
    max-width: 650px;
    font-size: 14px;
    margin-top: 9px;
    font-weight: 400;
    line-height: 1.55;
    letter-spacing: 0.1px;
}

.hero-header .status-pill {
    position: relative;
    z-index: 1;
    backdrop-filter: blur(10px);
}

.input-screen {
    width: min(100%, 1080px) !important;
    margin: 0 auto !important;
    padding: 0 !important;
    gap: 0 !important;
    background: transparent !important;
    border: 0 !important;
    box-shadow: none !important;
}

.input-screen > .block {
    background: transparent !important;
}

.dashboard-shell {
    width: 100% !important;
    max-width: none !important;
    margin: 0 auto !important;
    padding: 0 12px 32px !important;
}

.dashboard-shell > .block,
.dashboard-shell .tabs,
.dashboard-shell .tabitem,
.dashboard-shell .tabitem > .block {
    width: 100% !important;
    max-width: none !important;
}

.dashboard-shell .tab-nav {
    width: 100% !important;
}

.dashboard-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    margin: 5px 0 18px;
    padding: 11px 15px;
    border: 1px solid rgba(192, 132, 252, 0.18);
    border-radius: 12px;
    background: linear-gradient(90deg, rgba(18, 8, 32, 0.9), rgba(29, 12, 52, 0.72));
    box-shadow: inset 0 1px rgba(255, 255, 255, 0.05), 0 8px 20px rgba(2, 0, 8, 0.22);
}

.dashboard-identity {
    display: flex;
    align-items: center;
    gap: 10px;
}

.dashboard-orb {
    width: 9px;
    height: 9px;
    border: 2px solid #E879F9;
    border-radius: 50%;
    box-shadow: 0 0 12px rgba(232, 121, 249, 0.9);
}

.dashboard-identity b {
    display: block;
    color: #F3E8FF;
    font: 700 11px 'JetBrains Mono', monospace;
    letter-spacing: 1px;
}

.dashboard-identity small {
    display: block;
    margin-top: 3px;
    color: #8B7AA8;
    font-size: 10px;
}

.dashboard-status {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    color: #D8B4FE;
    font: 700 9px 'JetBrains Mono', monospace;
    letter-spacing: 0.8px;
}

.dashboard-status span {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #D946EF;
    box-shadow: 0 0 9px #D946EF;
}

.dashboard-shell .graph-tab-hero,
.dashboard-shell .deep-dive-hero,
.dashboard-shell .saturation-hero {
    width: 100%;
}

.input-studio-heading {
    position: relative;
    overflow: hidden;
    margin: 0 0 14px;
    padding: 24px 28px 21px;
    border: 1px solid rgba(129, 140, 248, 0.22);
    border-radius: 16px;
    background:
        radial-gradient(circle at 100% 0%, rgba(217, 70, 239, 0.14), transparent 29%),
        linear-gradient(135deg, rgba(20, 28, 59, 0.92), rgba(11, 19, 37, 0.96));
    box-shadow: 0 12px 30px rgba(2, 6, 23, 0.22), inset 0 1px rgba(255, 255, 255, 0.05);
}

.input-studio-heading::after {
    content: "";
    position: absolute;
    right: 7%;
    top: -85px;
    width: 150px;
    height: 150px;
    border: 1px solid rgba(165, 180, 252, 0.14);
    border-radius: 50%;
    box-shadow: 0 0 0 18px rgba(165, 180, 252, 0.03), 0 0 0 36px rgba(165, 180, 252, 0.02);
    pointer-events: none;
}

.input-command-studio {
    position: relative;
    overflow: hidden;
    margin: 0 auto 24px;
    padding: 28px 30px 24px !important;
    border: 1px solid rgba(168, 85, 247, 0.24) !important;
    border-radius: 18px !important;
    background:
        radial-gradient(circle at 100% 0%, rgba(217, 70, 239, 0.14), transparent 26%),
        linear-gradient(150deg, rgba(18, 8, 32, 0.96), rgba(9, 5, 22, 0.98)) !important;
    box-shadow: 0 18px 42px rgba(2, 6, 23, 0.3), inset 0 1px rgba(255, 255, 255, 0.05);
}

.input-studio-heading {
    position: relative;
    z-index: 1;
    margin-bottom: 20px;
}

.input-studio-eyebrow {
    color: #C4B5FD;
    font: 700 10px/1.2 'JetBrains Mono', monospace;
    letter-spacing: 1.6px;
}

.input-studio-eyebrow span {
    display: inline-block;
    width: 5px;
    height: 5px;
    margin: 0 8px 2px;
    border-radius: 50%;
    background: #A78BFA;
    box-shadow: 0 0 10px #A78BFA;
}

.input-studio-title {
    margin-top: 10px;
    color: #F8FAFC;
    font: 800 clamp(22px, 3vw, 31px)/1.12 'Outfit', sans-serif;
    letter-spacing: -0.7px;
}

.input-studio-title em {
    color: #E879F9;
    font-style: normal;
}

.input-studio-copy {
    max-width: 690px;
    margin-top: 8px;
    color: #C4B5FD;
    font-size: 12.5px;
    line-height: 1.55;
}

.research-input-shell {
    position: relative;
    overflow: hidden;
    padding: 0 !important;
    border: 1px solid rgba(168, 85, 247, 0.34) !important;
    border-radius: 15px !important;
    background:
        radial-gradient(circle at 12% 20%, rgba(168, 85, 247, 0.2), transparent 30%),
        radial-gradient(circle at 88% 80%, rgba(34, 211, 238, 0.13), transparent 34%),
        linear-gradient(135deg, rgba(27, 13, 50, 0.98), rgba(9, 8, 28, 0.99)) !important;
    box-shadow:
        0 12px 28px rgba(2, 6, 23, 0.28),
        inset 0 1px rgba(255, 255, 255, 0.07),
        0 0 0 1px rgba(168, 85, 247, 0.06);
    transition: border-color 0.25s ease, box-shadow 0.25s ease, transform 0.25s ease;
}

.research-input-shell:hover {
    border-color: rgba(232, 121, 249, 0.58) !important;
    box-shadow: 0 16px 34px rgba(2, 6, 23, 0.34), 0 0 26px rgba(168, 85, 247, 0.12);
    transform: translateY(-1px);
}

.research-input-topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    padding: 12px 16px;
    border-bottom: 1px solid rgba(148, 163, 184, 0.12);
    background: linear-gradient(90deg, rgba(168, 85, 247, 0.12), rgba(34, 211, 238, 0.05));
}

.research-input-label {
    color: #C7D2FE;
    font: 700 10px 'JetBrains Mono', monospace;
    letter-spacing: 1.15px;
}

.input-signal-dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    margin: 0 5px 1px 0;
    border-radius: 50%;
    background: #E879F9;
    box-shadow: 0 0 9px rgba(232, 121, 249, 0.9);
}

.input-label-muted {
    color: #475569;
    font-weight: 500;
}

.research-input-status {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: #67E8F9;
    font: 700 9px 'JetBrains Mono', monospace;
    letter-spacing: 0.8px;
}

.research-input-status span {
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #22D3EE;
    box-shadow: 0 0 8px #22D3EE;
}

.research-idea-input {
    position: relative;
    z-index: 1;
}

.research-idea-input textarea {
    min-height: 174px !important;
    padding: 21px 20px !important;
    border: 0 !important;
    border-radius: 0 !important;
    background:
        linear-gradient(135deg, rgba(38, 16, 72, 0.62), rgba(10, 23, 48, 0.7)) !important;
    color: #F8FAFC !important;
    font-size: 14.5px !important;
    line-height: 1.7 !important;
    resize: vertical !important;
    caret-color: #67E8F9 !important;
    transition: background 0.25s ease, box-shadow 0.25s ease !important;
}

.research-idea-input textarea::placeholder {
    color: #94A3B8 !important;
    opacity: 0.9 !important;
}

.research-idea-input textarea:hover {
    background:
        linear-gradient(135deg, rgba(57, 21, 99, 0.7), rgba(12, 36, 69, 0.76)) !important;
}

.research-idea-input textarea:focus {
    background:
        linear-gradient(135deg, rgba(70, 24, 118, 0.76), rgba(13, 43, 80, 0.82)) !important;
    box-shadow:
        inset 0 0 0 1px rgba(232, 121, 249, 0.42),
        inset 0 0 34px rgba(168, 85, 247, 0.14),
        0 0 22px rgba(34, 211, 238, 0.09) !important;
}

.research-idea-input textarea::selection {
    color: #FFFFFF !important;
    background: rgba(168, 85, 247, 0.72) !important;
}

.research-input-footer {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    padding: 10px 16px 12px;
    border-top: 1px solid rgba(148, 163, 184, 0.1);
    color: #8B7AA8;
    font-size: 10px;
    line-height: 1.4;
}

.research-input-footer b {
    color: #A5B4FC;
    font: 700 9px 'JetBrains Mono', monospace;
    letter-spacing: 0.8px;
}

.research-input-shortcut {
    color: #8B7AA8;
    font: 9px 'JetBrains Mono', monospace;
    text-align: right;
}

.input-studio-hint {
    margin: 10px 2px 14px;
    color: #8B7AA8;
    font-size: 11px;
}

.input-studio-hint span {
    margin-right: 6px;
    color: #C084FC;
    font-size: 16px;
}

/* System Status Indicator Dots */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 5px 12px;
    border-radius: 9999px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.4px;
    text-transform: uppercase;
    font-family: 'JetBrains Mono', monospace;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    display: inline-block;
}

.status-active {
    background: rgba(217, 70, 239, 0.12);
    color: #E879F9;
    border: 1px solid rgba(217, 70, 239, 0.3);
}

.status-active .status-dot {
    background: #D946EF;
    box-shadow: 0 0 8px #D946EF;
}

.status-llm {
    background: rgba(34, 211, 238, 0.12);
    color: #67E8F9;
    border: 1px solid rgba(34, 211, 238, 0.3);
}

.status-llm .status-dot {
    background: #22D3EE;
    box-shadow: 0 0 8px #22D3EE;
}

/* Badges */
.badge-tag {
    display: inline-flex;
    align-items: center;
    padding: 4px 10px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
    margin: 2px 4px 2px 0;
    letter-spacing: 0.3px;
    font-family: 'Inter', sans-serif;
}

.badge-paper {
    background: rgba(217, 70, 239, 0.15);
    color: #F0ABFC;
    border: 1px solid rgba(217, 70, 239, 0.35);
}

.badge-inferred {
    background: rgba(139, 92, 246, 0.15);
    color: #C084FC;
    border: 1px solid rgba(139, 92, 246, 0.35);
}

.badge-domain {
    background: rgba(168, 85, 247, 0.15);
    color: #C4B5FD;
    border: 1px solid rgba(168, 85, 247, 0.35);
}

.badge-neutral {
    background: rgba(148, 163, 184, 0.12);
    color: #CBD5E1;
    border: 1px solid rgba(148, 163, 184, 0.25);
}

/* Card Styling */
.research-card {
    background: rgba(18, 8, 32, 0.86);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 10px;
    padding: 16px 18px;
    margin-bottom: 12px;
    transition: all 0.2s ease-in-out;
}

.research-card:hover {
    border-color: rgba(232, 121, 249, 0.42);
    box-shadow: 0 6px 18px rgba(0, 0, 0, 0.35);
    transform: translateY(-1px);
}

.card-title {
    font-family: 'Outfit', sans-serif;
    font-size: 15.5px;
    font-weight: 700;
    color: #F8FAFC;
    margin-bottom: 6px;
    line-height: 1.4;
}

.meta-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px;
    color: #94A3B8;
    font-size: 12px;
    margin-bottom: 8px;
}

.paper-abstract {
    color: #CBD5E1;
    font-size: 12.5px;
    line-height: 1.6;
    margin-top: 6px;
}

.btn-doi {
    display: inline-flex;
    align-items: center;
    background: linear-gradient(135deg, #7C3AED 0%, #D946EF 100%);
    color: #FFFFFF !important;
    padding: 5px 12px;
    border-radius: 6px;
    font-size: 11.5px;
    font-weight: 600;
    text-decoration: none;
    margin-top: 8px;
    letter-spacing: 0.2px;
    transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.btn-doi:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(217, 70, 239, 0.35);
}

/* Refined Form Controls */
textarea, input[type="text"] {
    background: rgba(18, 8, 32, 0.86) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 8px !important;
    color: #F8FAFC !important;
    font-family: 'Inter', sans-serif !important;
}

textarea:focus, input[type="text"]:focus {
    border-color: #D946EF !important;
    box-shadow: 0 0 0 2px rgba(217, 70, 239, 0.25) !important;
}

.primary-btn {
    background: linear-gradient(135deg, #6D28D9 0%, #A855F7 48%, #E879F9 100%) !important;
    color: #FFFFFF !important;
    font-weight: 700 !important;
    letter-spacing: 0.3px !important;
    border: none !important;
    border-radius: 8px !important;
    box-shadow: 0 4px 18px rgba(168, 85, 247, 0.42) !important;
    transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}

.explore-command-btn {
    position: relative;
    overflow: hidden;
    min-height: 52px !important;
    font-size: 13px !important;
    letter-spacing: 0.7px !important;
}

.explore-command-btn::after {
    content: "";
    position: absolute;
    top: 0;
    left: -80%;
    width: 45%;
    height: 100%;
    transform: skewX(-20deg);
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
    transition: left 0.6s ease;
}

.explore-command-btn:hover::after {
    left: 135%;
}

.primary-btn:hover {
    transform: translateY(-2px) scale(1.005) !important;
    box-shadow: 0 10px 30px rgba(168, 85, 247, 0.58), 0 0 26px rgba(232, 121, 249, 0.2) !important;
}

.primary-btn:active {
    transform: translateY(0) scale(0.995) !important;
}

/* Modern Tabs */
.tab-nav {
    display: flex !important;
    align-items: stretch !important;
    background: rgba(10, 4, 18, 0.92) !important;
    border: 1px solid rgba(168, 85, 247, 0.28) !important;
    border-radius: 13px !important;
    padding: 5px !important;
    gap: 5px !important;
    margin-bottom: 18px !important;
    box-shadow: 0 10px 24px rgba(2, 0, 8, 0.24), inset 0 1px rgba(255, 255, 255, 0.04) !important;
}

.tab-nav button {
    flex: 1 1 0 !important;
    min-width: 0 !important;
    border-radius: 8px !important;
    font-weight: 650 !important;
    font-size: 11px !important;
    color: #8B7AA8 !important;
    padding: 11px 12px !important;
    border: 1px solid transparent !important;
    transition: all 0.2s ease !important;
    font-family: 'Inter', sans-serif !important;
    white-space: nowrap !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
}

.tab-nav button:hover {
    color: #F8FAFC !important;
    background: rgba(168, 85, 247, 0.12) !important;
}

.tab-nav button.selected {
    background: linear-gradient(135deg, rgba(126, 34, 206, 0.32), rgba(217, 70, 239, 0.18)) !important;
    color: #FFFFFF !important;
    border: 1px solid rgba(192, 132, 252, 0.48) !important;
    box-shadow: 0 4px 16px rgba(168, 85, 247, 0.28) !important;
}

@media (max-width: 900px) {
    .dashboard-topbar {
        align-items: flex-start;
        flex-direction: column;
    }

    .tab-nav button {
        font-size: 10px !important;
        padding: 10px 7px !important;
    }
}

/* Accordion Styling */
.gr-accordion {
    border: 1px solid rgba(192, 132, 252, 0.18) !important;
    border-radius: 8px !important;
    background: rgba(18, 8, 32, 0.52) !important;
}

/* Semantic decomposition content */
.concept-panel {
    padding: 18px !important;
}

.concept-pipeline {
    display: flex;
    align-items: center;
    gap: 7px;
    flex-wrap: wrap;
    padding: 12px;
    border: 1px solid rgba(168, 85, 247, 0.25);
    border-radius: 11px;
    background: linear-gradient(135deg, rgba(126, 34, 206, 0.16), rgba(18, 8, 32, 0.68));
}

.concept-pipeline-label,
.concept-section-label {
    color: #C4B5FD;
    font: 700 10px 'JetBrains Mono', monospace;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.concept-pipeline-step {
    padding: 6px 9px;
    border: 1px solid rgba(192, 132, 252, 0.28);
    border-radius: 7px;
    background: rgba(168, 85, 247, 0.13);
    color: #E9D5FF;
    font: 700 10px 'JetBrains Mono', monospace;
    letter-spacing: 0.2px;
}

.concept-pipeline-arrow {
    color: #A855F7;
    font-size: 14px;
}

.concept-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
    margin: 18px 0 13px;
    padding-bottom: 11px;
    border-bottom: 1px solid rgba(192, 132, 252, 0.14);
}

.concept-title {
    color: #F8FAFC;
    font: 800 17px 'Outfit', sans-serif;
    letter-spacing: 0.2px;
    text-transform: uppercase;
}

.concept-specificity {
    margin: 0 !important;
    white-space: nowrap;
}

.concept-fact-grid {
    display: grid;
    grid-template-columns: minmax(150px, 0.8fr) minmax(0, 1.8fr);
    gap: 10px;
    margin-bottom: 17px;
}

.concept-fact-card {
    min-height: 68px;
    padding: 12px 14px;
    border: 1px solid rgba(192, 132, 252, 0.13);
    border-radius: 10px;
    background: rgba(18, 8, 32, 0.66);
}

.concept-fact-label {
    color: #8B7AA8;
    font: 700 9px 'JetBrains Mono', monospace;
    letter-spacing: 0.8px;
    text-transform: uppercase;
}

.concept-fact-value {
    margin-top: 6px;
    color: #F3E8FF;
    font-size: 13px;
    font-weight: 650;
    line-height: 1.4;
}

.concept-section {
    margin-top: 15px;
}

.concept-section-label {
    margin-bottom: 8px;
    color: #A78BFA;
}

.concept-chip-row {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
}

.concept-chip {
    display: inline-flex;
    align-items: center;
    padding: 6px 10px;
    border: 1px solid rgba(192, 132, 252, 0.25);
    border-radius: 7px;
    background: rgba(168, 85, 247, 0.12);
    color: #E9D5FF;
    font-size: 11px;
    font-weight: 600;
}

.concept-chip-technique {
    border-color: rgba(232, 121, 249, 0.24);
    background: rgba(217, 70, 239, 0.1);
    color: #F5D0FE;
}

.concept-queries {
    margin-top: 17px;
    padding: 14px;
    border: 1px solid rgba(192, 132, 252, 0.16);
    border-radius: 11px;
    background: rgba(10, 4, 18, 0.48);
}

.concept-query-list {
    display: grid;
    gap: 7px;
    margin: 10px 0 0;
    padding: 0;
    list-style: none;
}

.concept-query-item {
    display: flex;
    gap: 9px;
    align-items: flex-start;
    padding: 9px 10px;
    border: 1px solid rgba(192, 132, 252, 0.1);
    border-radius: 7px;
    background: rgba(18, 8, 32, 0.7);
    color: #DDD6FE;
    font: 11px/1.45 'JetBrains Mono', monospace;
}

.concept-query-item::before {
    content: "↗";
    flex: 0 0 auto;
    color: #E879F9;
    font-size: 13px;
}

/* Direction review content */
.direction-review {
    display: grid;
    gap: 14px;
}

.direction-summary-card,
.direction-papers-card {
    padding: 18px !important;
}

.direction-title-row {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 14px;
    padding-bottom: 14px;
    border-bottom: 1px solid rgba(192, 132, 252, 0.14);
}

.direction-title {
    margin: 0;
    color: #F8FAFC;
    font: 800 20px/1.2 'Outfit', sans-serif;
    letter-spacing: -0.2px;
}

.direction-title-label {
    display: block;
    margin-bottom: 6px;
    color: #A78BFA;
    font: 700 9px 'JetBrains Mono', monospace;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.direction-paper-count {
    flex: 0 0 auto;
    margin: 0 !important;
}

.direction-section-heading {
    display: flex;
    align-items: center;
    gap: 9px;
    margin-bottom: 10px;
    color: #F3E8FF;
    font: 700 13px 'Outfit', sans-serif;
    letter-spacing: 0.4px;
    text-transform: uppercase;
}

.direction-section-number {
    color: #E879F9;
    font: 700 10px 'JetBrains Mono', monospace;
}

.direction-connection-card {
    margin-top: 16px;
    padding: 15px;
    border: 1px solid rgba(168, 85, 247, 0.3);
    border-radius: 11px;
    background: linear-gradient(135deg, rgba(126, 34, 206, 0.16), rgba(18, 8, 32, 0.68));
}

.direction-connection-summary {
    margin: 0 0 14px;
    color: #E9D5FF;
    font-size: 12.5px;
    line-height: 1.6;
}

.direction-fact-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 8px;
}

.direction-fact {
    padding: 10px 11px;
    border: 1px solid rgba(192, 132, 252, 0.14);
    border-radius: 8px;
    background: rgba(10, 4, 18, 0.42);
    color: #C4B5FD;
    font-size: 11px;
    line-height: 1.45;
}

.direction-fact b {
    display: block;
    margin-bottom: 4px;
    color: #8B7AA8;
    font: 700 9px 'JetBrains Mono', monospace;
    letter-spacing: 0.7px;
    text-transform: uppercase;
}

.direction-fact-differentiator {
    grid-column: 1 / -1;
    border-color: rgba(232, 121, 249, 0.2);
    color: #F5D0FE;
}

.direction-gaps {
    margin-top: 18px;
}

.direction-gap-list {
    display: grid;
    gap: 8px;
}

.direction-papers-heading {
    display: flex;
    align-items: baseline;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 11px;
}

.direction-papers-heading small {
    color: #8B7AA8;
    font: 500 10px 'JetBrains Mono', monospace;
}

@media (max-width: 700px) {
    .direction-title-row,
    .direction-papers-heading {
        align-items: flex-start;
        flex-direction: column;
    }

    .direction-fact-grid {
        grid-template-columns: 1fr;
    }

    .direction-fact-differentiator {
        grid-column: auto;
    }
}

@media (max-width: 700px) {
    .concept-fact-grid {
        grid-template-columns: 1fr;
    }

    .concept-header {
        align-items: flex-start;
        flex-direction: column;
    }
}
"""

def render_hero_header() -> str:
    return """
    <div class="hero-header">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:12px;">
            <div>
                <div style="position:relative; z-index:1; color:#67E8F9; font:700 10px/1.2 'JetBrains Mono', monospace; letter-spacing:1.7px; margin-bottom:9px;">RESEARCH INTELLIGENCE PLATFORM <span style="color:#64748B;">/</span> EVIDENCE-FIRST</div>
                <h1 class="hero-title">RESEARCH SCOPE AI</h1>
                <p class="hero-subtitle">Turn an early research idea into a verified landscape, a defensible gap, and a publication-ready direction.</p>
            </div>
            <div style="display:flex; gap:10px; flex-wrap:wrap;">
                <span class="status-pill status-active"><span class="status-dot"></span>Semantic Scholar & OpenAlex Live</span>
                <span class="status-pill status-llm"><span class="status-dot"></span>Groq Neural Synthesizer</span>
            </div>
        </div>
    </div>
    """

def render_concept_breakdown(idea: IdeaStructure) -> str:
    modalities_html = "".join([f'<span class="concept-chip">{m}</span>' for m in idea.input_modalities])
    subfields_html = "".join([f'<span class="concept-chip concept-chip-technique">{s}</span>' for s in idea.ai_subfields])
    queries_html = "".join([f'<li class="concept-query-item">{q}</li>' for q in idea.academic_search_queries])

    return f"""
    <div class="glass-panel concept-panel">
        <div class="concept-pipeline">
            <span class="concept-pipeline-label">Pipeline</span>
            <span class="concept-pipeline-step">01 · DECOMPOSE</span>
            <span class="concept-pipeline-arrow">→</span>
            <span class="concept-pipeline-step">02 · RETRIEVE</span>
            <span class="concept-pipeline-arrow">→</span>
            <span class="concept-pipeline-step">03 · CONNECT</span>
            <span class="concept-pipeline-arrow">→</span>
            <span class="concept-pipeline-step">04 · DISCOVER GAPS</span>
        </div>

        <div class="concept-header">
            <div class="concept-title">AI interpretation layer</div>
            <span class="badge-tag {'badge-paper' if idea.specificity_level=='High' else 'badge-inferred'} concept-specificity">SPECIFICITY · {idea.specificity_level.upper()}</span>
        </div>
        
        <div class="concept-fact-grid">
            <div class="concept-fact-card">
                <div class="concept-fact-label">Primary domain</div>
                <div class="concept-fact-value">{idea.domain}</div>
            </div>
            <div class="concept-fact-card">
                <div class="concept-fact-label">Target problem</div>
                <div class="concept-fact-value">{idea.primary_problem}</div>
            </div>
        </div>

        <div class="concept-section">
            <div class="concept-section-label">Input modalities</div>
            <div class="concept-chip-row">{modalities_html}</div>
        </div>

        <div class="concept-section">
            <div class="concept-section-label">AI subfields & techniques</div>
            <div class="concept-chip-row">{subfields_html}</div>
        </div>

        <div class="concept-queries">
            <div class="concept-section-label">Automated academic queries <span style="color:#8B7AA8; font-weight:500;">/ Semantic Scholar + OpenAlex</span></div>
            <ul class="concept-query-list">
                {queries_html}
            </ul>
        </div>
    </div>
    """

def render_node_deep_dive(cluster_name: str, connection_info: Dict[str, Any], gaps: List[Dict[str, str]], papers: List[Paper]) -> str:
    gaps_html = ""
    for g in gaps:
        badge_cls = "badge-paper" if g["type"] == "From Paper" else "badge-inferred"
        gaps_html += f"""
        <div class="deep-dive-gap-card" style="border-left-color:{'#D946EF' if g['type']=='From Paper' else '#A855F7'};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
                <span class="badge-tag {badge_cls}">[{'PUBLISHED LITERATURE' if g['type']=='From Paper' else 'AI-SYNTHESIZED'}]</span>
                <span style="font-size:11px; color:#94A3B8;">Anchor: {g.get('source', 'Literature')}</span>
            </div>
            <div style="font-size:12.5px; color:#E2E8F0; line-height:1.5;">{g['text']}</div>
        </div>
        """

    papers_html = ""
    for p in papers:
        papers_html += f"""
        <div class="research-card deep-dive-paper-card">
            <div class="card-title">{p.title}</div>
            <div class="meta-row">
                <span>Author: {p.authors_display}</span>
                <span>Year: {p.year or 'Recent'}</span>
                <span>Citations: {p.citation_count}</span>
                <span class="badge-tag badge-paper">{p.source_api}</span>
            </div>
            <div class="paper-abstract">{p.abstract}</div>
            <a href="{p.clean_url}" target="_blank" class="btn-doi">View Verified Source / DOI &rarr;</a>
        </div>
        """

    return f"""
    <div class="direction-review">
        <div class="glass-panel direction-summary-card">
            <div class="direction-title-row">
                <div>
                    <span class="direction-title-label">Selected research direction</span>
                    <h2 class="direction-title">{cluster_name}</h2>
                </div>
                <span class="badge-tag badge-domain direction-paper-count">{len(papers)} ANCHOR PAPERS</span>
            </div>
            
            <div class="direction-connection-card">
                <div class="direction-section-heading"><span class="direction-section-number">01</span> Connection to your proposed research</div>
                <p class="direction-connection-summary">{connection_info.get('connection_summary', '')}</p>
                <div class="direction-fact-grid">
                    <div class="direction-fact"><b>Shared problem</b>{connection_info.get('shared_problem', '')}</div>
                    <div class="direction-fact"><b>Shared technique</b>{connection_info.get('shared_technique', '')}</div>
                    <div class="direction-fact direction-fact-differentiator"><b>Key differentiator</b>{connection_info.get('key_difference', '')}</div>
                </div>
            </div>

            <div class="direction-gaps">
                <div class="direction-section-heading"><span class="direction-section-number">02</span> Identified literature gaps & limitations</div>
                <div class="direction-gap-list">{gaps_html}</div>
            </div>
        </div>

        <div class="glass-panel direction-papers-card">
            <div class="direction-papers-heading">
                <h3 class="deep-dive-section-label"><span>03</span> Peer-reviewed papers</h3>
                <small>{len(papers)} verified literature anchors</small>
            </div>
            {papers_html}
        </div>
    </div>
    """
