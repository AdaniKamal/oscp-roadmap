import streamlit as st

st.set_page_config(
    page_title="Road to OSCP",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── THEME ─────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;600;700;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}
.stApp { background: #0a0d12; color: #e6edf3; }
section[data-testid="stSidebar"] { background: #0d1117 !important; border-right: 1px solid #21262d; }
section[data-testid="stSidebar"] * { color: #e6edf3 !important; }

h1,h2,h3,h4 { font-family: 'Inter', sans-serif; }

.hero-title {
    font-size: 3rem; font-weight: 900; letter-spacing: -2px;
    background: linear-gradient(135deg, #00ff9d, #00ccff);
    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    margin-bottom: 0;
}
.hero-sub { color: #888; font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; letter-spacing: 3px; }

.phase-card {
    background: #0d1117; border: 1px solid #21262d;
    border-left: 4px solid; border-radius: 10px;
    padding: 1.4rem; margin-bottom: 1rem;
}
.phase-card h3 { margin-top: 0; font-size: 1.1rem; }
.phase-card p, .phase-card li { color: #c9d1d9; font-size: 0.9rem; line-height: 1.7; }

.cert-card {
    background: #161b22; border: 1px solid #30363d; border-radius: 10px;
    padding: 1.2rem; height: 100%;
}
.cert-card h4 { margin-top: 0; font-size: 1rem; }
.cert-card p { color: #8b949e; font-size: 0.85rem; }

.badge {
    display: inline-block; padding: 2px 10px; border-radius: 20px;
    font-size: 0.75rem; font-weight: 700; font-family: 'JetBrains Mono', monospace;
    margin: 2px;
}
.badge-green  { background: rgba(0,255,157,0.15); color: #00ff9d; border: 1px solid rgba(0,255,157,0.3); }
.badge-blue   { background: rgba(0,204,255,0.15); color: #00ccff; border: 1px solid rgba(0,204,255,0.3); }
.badge-orange { background: rgba(255,107,53,0.15); color: #ff6b35; border: 1px solid rgba(255,107,53,0.3); }
.badge-red    { background: rgba(255,79,79,0.15);  color: #ff4f4f; border: 1px solid rgba(255,79,79,0.3); }
.badge-yellow { background: rgba(212,160,23,0.15); color: #d4a017; border: 1px solid rgba(212,160,23,0.3); }
.badge-purple { background: rgba(188,100,255,0.15);color: #bc64ff; border: 1px solid rgba(188,100,255,0.3); }

.tool-chip {
    display: inline-block; background: #161b22; border: 1px solid #30363d;
    color: #00ff9d; font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem; padding: 3px 10px; border-radius: 5px; margin: 3px;
}
.warn-box {
    background: rgba(255,79,79,0.08); border: 1px solid rgba(255,79,79,0.3);
    border-left: 4px solid #ff4f4f; border-radius: 8px; padding: 1rem; margin: 0.5rem 0;
}
.info-box {
    background: rgba(0,255,157,0.05); border: 1px solid rgba(0,255,157,0.2);
    border-left: 4px solid #00ff9d; border-radius: 8px; padding: 1rem; margin: 0.5rem 0;
}
.tip-box {
    background: rgba(0,204,255,0.05); border: 1px solid rgba(0,204,255,0.2);
    border-left: 4px solid #00ccff; border-radius: 8px; padding: 1rem; margin: 0.5rem 0;
}
.timeline-row {
    background: #0d1117; border: 1px solid #21262d; border-radius: 8px;
    padding: 1rem 1.2rem; margin-bottom: 0.6rem;
    display: flex; align-items: flex-start; gap: 1rem;
}
.checklist-item { padding: 6px 0; border-bottom: 1px solid #21262d; font-size: 0.9rem; }
.section-label {
    font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;
    color: #00ff9d; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 0.3rem;
}
.stTabs [data-baseweb="tab"] { background: #0d1117; color: #888; border-radius: 6px 6px 0 0; }
.stTabs [aria-selected="true"] { background: #161b22 !important; color: #00ff9d !important; border-bottom: 2px solid #00ff9d; }
.stExpander { background: #0d1117 !important; border: 1px solid #21262d !important; border-radius: 8px !important; }

/* table */
table { width: 100%; border-collapse: collapse; font-size: 0.85rem; }
th { background: #161b22; color: #00ff9d; font-family: 'JetBrains Mono', monospace;
     padding: 10px 14px; text-align: left; border: 1px solid #30363d; font-size: 0.8rem; letter-spacing: 1px; }
td { padding: 9px 14px; border: 1px solid #21262d; color: #c9d1d9; vertical-align: top; }
tr:hover td { background: #161b22; }
</style>
""", unsafe_allow_html=True)

# ── DATA ──────────────────────────────────────────────────────
from data.phases       import PHASES
from data.certs        import CERTS
from data.timeline     import TIMELINE, WEEKLY_SCHEDULE, DAILY_ROUTINE
from data.tools        import TOOLS_BY_PHASE
from data.resources    import RESOURCES
from data.checklist    import READINESS, MISTAKES, FAIL_REASONS
from data.mastertable  import MASTER_TABLE
from data.topics       import TOPICS

# ── SIDEBAR ───────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="section-label">// Navigation</div>', unsafe_allow_html=True)
    st.markdown("## 🎯 Road to OSCP")
    st.markdown('<span class="badge badge-green">Target: Aug 2027</span>', unsafe_allow_html=True)
    st.divider()
    page = st.radio("Go to", [
        "🏠 Overview",
        "🗺️ Phase Roadmap",
        "📜 Certifications",
        "📅 Timeline",
        "🛠️ Tools & Topics",
        "🔬 Labs & Resources",
        "✅ Am I Ready?",
        "📋 Master Table",
    ])
    st.divider()
    st.markdown('<div class="section-label">// Quick Stats</div>', unsafe_allow_html=True)
    st.metric("Months to OSCP", "~26", "Aug 2027")
    st.metric("Phases", "7", "Foundation → Exam")
    st.metric("Certs Before OSCP", "2–3", "eJPT → PNPT/CPTS")

# ── PAGES ─────────────────────────────────────────────────────

# ─ OVERVIEW ──────────────────────────────────────────────────
if page == "🏠 Overview":
    st.markdown('<div class="hero-title">Road to OSCP</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-sub">// OFFENSIVE SECURITY MENTORSHIP ROADMAP · TARGET: AUG 2027</div>', unsafe_allow_html=True)
    st.markdown("")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="phase-card" style="border-left-color:#00ff9d"><h3>🎯 Goal</h3><p>OSCP certified by August 2027 with real-world pentesting skills — not just exam passing.</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="phase-card" style="border-left-color:#00ccff"><h3>📍 Starting Point</h3><p>VA/Cloud analyst. Nessus, Burp, OpenVAS experience. Needs offensive depth.</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="phase-card" style="border-left-color:#d4a017"><h3>⏱️ Time</h3><p>~26 months. Full-time job. 2–3 hrs weekdays, 5–6 hrs weekends. Structured phases.</p></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="phase-card" style="border-left-color:#ff6b35"><h3>🔥 Focus</h3><p>Manual exploitation. Active Directory. PrivEsc. Pivoting. Methodology over memorisation.</p></div>', unsafe_allow_html=True)

    st.divider()
    st.markdown("### Your Honest Skill Gap Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
<div class="info-box">
<strong style="color:#00ff9d">✅ What you already have</strong><br><br>
• Vulnerability scanning mindset (Nessus, OpenVAS)<br>
• Burp Suite familiarity — big advantage for web<br>
• Cloud security thinking (helps with modern AD labs)<br>
• Report writing exposure from VA work<br>
• Understanding of CVEs and vulnerability lifecycle<br>
• Professional security environment context
</div>
""", unsafe_allow_html=True)
    with col2:
        st.markdown("""
<div class="warn-box">
<strong style="color:#ff4f4f">⚠️ What you need to build</strong><br><br>
• Manual exploitation (not scanner-dependent)<br>
• Linux & Windows privilege escalation — deeply<br>
• Active Directory attacks (OSCP is now 40%+ AD)<br>
• Pivoting & tunneling (Ligolo-ng, Chisel, SOCKS)<br>
• Buffer overflow / basic exploit dev (legacy OSCP)<br>
• Offensive scripting (Python, Bash, PowerShell)<br>
• Exam-pace thinking: enumerate → exploit → pivot fast
</div>
""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### The 7-Phase Journey")
    phases_overview = [
        ("1", "Foundation", "Linux, networking, scripting, basic recon", "#4a5568", "Months 1–2"),
        ("2", "Beginner Offensive", "eJPT, TryHackMe, first real exploits", "#00ff9d", "Months 3–5"),
        ("3", "Intermediate Pentesting", "PNPT/CPTS, HackTheBox, web attacks", "#00ccff", "Months 6–10"),
        ("4", "Active Directory", "BloodHound, Kerberoast, CrackMapExec, CRTO", "#bc64ff", "Months 11–15"),
        ("5", "Buffer Overflow", "BOF, basic exploit dev, shellcode", "#d4a017", "Months 16–17"),
        ("6", "OSCP Prep", "PEN-200, PWK labs, full methodology", "#ff6b35", "Months 18–23"),
        ("7", "Exam Simulation", "Mock exams, time management, reporting", "#ff4f4f", "Months 24–26"),
    ]
    for num, name, desc, color, timing in phases_overview:
        st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-left:4px solid {color};
border-radius:8px;padding:0.9rem 1.2rem;margin-bottom:0.5rem;display:flex;gap:1rem;align-items:center">
<span style="font-size:1.5rem;font-weight:900;color:{color};font-family:'JetBrains Mono',monospace;min-width:30px">{num}</span>
<div>
<strong style="color:#e6edf3">{name}</strong>
<span style="color:#555;margin:0 8px">·</span>
<span style="color:#8b949e;font-size:0.85rem">{desc}</span>
<span class="badge badge-yellow" style="margin-left:10px">{timing}</span>
</div>
</div>
""", unsafe_allow_html=True)

# ─ PHASE ROADMAP ──────────────────────────────────────────────
elif page == "🗺️ Phase Roadmap":
    st.markdown("# 🗺️ Phase Roadmap")
    st.markdown('<div class="section-label">// 7 Phases · Foundation to Exam Ready</div>', unsafe_allow_html=True)
    st.markdown("")

    for phase in PHASES:
        color = phase["color"]
        with st.expander(f"{'⬛'*0} Phase {phase['num']}: {phase['name']}  —  {phase['timing']}", expanded=phase['num']=="1"):
            col1, col2 = st.columns([2,1])
            with col1:
                st.markdown(f'<div class="section-label">// Objective</div>', unsafe_allow_html=True)
                st.markdown(f"**{phase['objective']}**")
                st.markdown(f'<div class="section-label" style="margin-top:1rem">// Why This Phase Matters</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="tip-box">{phase["why"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="section-label" style="margin-top:1rem">// Key Topics</div>', unsafe_allow_html=True)
                for topic in phase["topics"]:
                    st.markdown(f"- {topic}")
            with col2:
                st.markdown(f'<div class="section-label">// Tools This Phase</div>', unsafe_allow_html=True)
                for tool in phase["tools"]:
                    st.markdown(f'<span class="tool-chip">{tool}</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="section-label" style="margin-top:1rem">// Labs</div>', unsafe_allow_html=True)
                for lab in phase["labs"]:
                    st.markdown(f"- {lab}")
                st.markdown(f'<div class="section-label" style="margin-top:1rem">// Milestone</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="info-box" style="font-size:0.85rem">{phase["milestone"]}</div>', unsafe_allow_html=True)

# ─ CERTIFICATIONS ─────────────────────────────────────────────
elif page == "📜 Certifications":
    st.markdown("# 📜 Certification Comparison")
    st.markdown('<div class="section-label">// Pre-OSCP Cert Stack — Ordered by Difficulty</div>', unsafe_allow_html=True)
    st.markdown("")

    st.markdown("""
<div class="info-box">
<strong style="color:#00ff9d">Recommended Stack for Your Background:</strong>
eJPT (Month 3–4) → PNPT (Month 8–10) → CPTS (Month 12–15, optional) → CRTO (Month 13–15, AD focus) → OSCP (Aug 2027)
</div>
""", unsafe_allow_html=True)

    for cert in CERTS:
        color = cert["color"]
        st.markdown(f"""
<div class="phase-card" style="border-left-color:{color}">
<div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem">
<div>
<h3 style="color:{color};margin-bottom:4px">{cert['name']}</h3>
<span class="badge badge-yellow">{cert['provider']}</span>
<span class="badge badge-blue">{cert['difficulty']}</span>
<span class="badge badge-green">{cert['cost']}</span>
<span class="badge badge-orange">{cert['exam_format']}</span>
</div>
<div style="text-align:right">
<span style="color:#888;font-size:0.8rem;font-family:JetBrains Mono,monospace">{cert['timing']}</span>
</div>
</div>
<div style="margin-top:1rem;display:grid;grid-template-columns:1fr 1fr;gap:1rem">
<div>
<div class="section-label">// What it covers</div>
<p style="color:#c9d1d9;font-size:0.875rem">{cert['covers']}</p>
</div>
<div>
<div class="section-label">// Honest Assessment</div>
<p style="color:#c9d1d9;font-size:0.875rem">{cert['honest']}</p>
</div>
</div>
</div>
""", unsafe_allow_html=True)

    st.divider()
    st.markdown("### Quick Comparison Matrix")
    st.markdown("""
<table>
<tr>
  <th>Cert</th><th>Closest to OSCP?</th><th>AD Coverage</th><th>Reporting</th><th>Practical Skill</th><th>Harder than OSCP?</th>
</tr>
<tr>
  <td><strong style="color:#00ff9d">eJPT</strong></td>
  <td>❌ Much easier</td><td>⭐ Minimal</td><td>⭐ Basic</td><td>⭐⭐ Good starter</td><td>❌ Much easier</td>
</tr>
<tr>
  <td><strong style="color:#00ccff">PNPT</strong></td>
  <td>✅ Very similar feel</td><td>⭐⭐⭐ Good</td><td>⭐⭐⭐⭐ Best in class</td><td>⭐⭐⭐⭐ Excellent</td><td>❌ Slightly easier</td>
</tr>
<tr>
  <td><strong style="color:#bc64ff">CPTS</strong></td>
  <td>✅✅ Closest to OSCP</td><td>⭐⭐⭐⭐ Deep</td><td>⭐⭐⭐ Good</td><td>⭐⭐⭐⭐⭐ Best overall</td><td>✅ Arguably harder</td>
</tr>
<tr>
  <td><strong style="color:#d4a017">CRTO</strong></td>
  <td>🟡 Different focus</td><td>⭐⭐⭐⭐⭐ Best</td><td>⭐⭐ Minimal</td><td>⭐⭐⭐⭐ AD-specific</td><td>🟡 Different scope</td>
</tr>
<tr>
  <td><strong style="color:#ff6b35">OSCP</strong></td>
  <td>— This IS the target —</td><td>⭐⭐⭐⭐ Heavy now</td><td>⭐⭐⭐ Required</td><td>⭐⭐⭐⭐⭐ Industry gold</td><td>— Baseline —</td>
</tr>
</table>
""", unsafe_allow_html=True)

# ─ TIMELINE ───────────────────────────────────────────────────
elif page == "📅 Timeline":
    st.markdown("# 📅 Timeline")
    st.markdown('<div class="section-label">// Month-by-Month · May 2025 → August 2027</div>', unsafe_allow_html=True)
    st.markdown("")

    tab1, tab2, tab3 = st.tabs(["📆 Month-by-Month", "📅 Weekly Schedule", "🌅 Daily Routine"])

    with tab1:
        for entry in TIMELINE:
            color = entry.get("color", "#555")
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-left:4px solid {color};
border-radius:8px;padding:1rem 1.2rem;margin-bottom:0.6rem">
<div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.5rem">
<strong style="color:{color}">{entry['period']}</strong>
<span class="badge badge-yellow">{entry['phase']}</span>
</div>
<div style="color:#e6edf3;font-size:0.9rem;font-weight:600;margin-bottom:0.3rem">{entry['focus']}</div>
<div style="color:#8b949e;font-size:0.85rem">{entry['details']}</div>
<div style="margin-top:0.5rem"><span class="badge badge-green">✓ {entry['milestone']}</span></div>
</div>
""", unsafe_allow_html=True)

    with tab2:
        st.markdown("### Weekly Study Schedule (Full-Time Worker)")
        st.markdown('<div class="info-box">Target: ~17–20 hrs/week. Consistency beats intensity. Never skip weekends.</div>', unsafe_allow_html=True)
        st.markdown("")
        for day in WEEKLY_SCHEDULE:
            col1, col2, col3 = st.columns([1, 2, 3])
            with col1:
                st.markdown(f"**{day['day']}**")
            with col2:
                st.markdown(f'<span class="badge badge-blue">{day["hours"]}</span>', unsafe_allow_html=True)
            with col3:
                st.markdown(f"<span style='color:#c9d1d9;font-size:0.875rem'>{day['focus']}</span>", unsafe_allow_html=True)
            st.divider()

    with tab3:
        st.markdown("### Daily Routine Example (Weekday)")
        st.markdown("")
        for block in DAILY_ROUTINE:
            col1, col2, col3 = st.columns([1, 1, 4])
            with col1:
                st.markdown(f'<span style="color:#00ff9d;font-family:JetBrains Mono,monospace;font-size:0.85rem">{block["time"]}</span>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<span class="badge badge-purple">{block["duration"]}</span>', unsafe_allow_html=True)
            with col3:
                st.markdown(f"<span style='color:#c9d1d9;font-size:0.875rem'>{block['activity']}</span>", unsafe_allow_html=True)
            st.divider()

# ─ TOOLS & TOPICS ─────────────────────────────────────────────
elif page == "🛠️ Tools & Topics":
    st.markdown("# 🛠️ Tools & Deep Topics")
    st.markdown('<div class="section-label">// Every tool and topic you must master</div>', unsafe_allow_html=True)
    st.markdown("")

    tab1, tab2 = st.tabs(["🔧 Tools by Phase", "📚 Deep Topic Breakdowns"])

    with tab1:
        for phase_name, tools in TOOLS_BY_PHASE.items():
            st.markdown(f"#### {phase_name}")
            cols = st.columns(5)
            for i, tool in enumerate(tools):
                with cols[i % 5]:
                    st.markdown(f'<span class="tool-chip">{tool}</span>', unsafe_allow_html=True)
            st.markdown("")

    with tab2:
        for topic in TOPICS:
            with st.expander(f"{topic['icon']} {topic['name']}"):
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown(f'<div class="section-label">// Why It Matters</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="tip-box" style="font-size:0.875rem">{topic["why"]}</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="section-label" style="margin-top:1rem">// Key Techniques</div>', unsafe_allow_html=True)
                    for t in topic["techniques"]:
                        st.markdown(f"- `{t}`")
                with col2:
                    st.markdown(f'<div class="section-label">// Key Tools</div>', unsafe_allow_html=True)
                    for tool in topic["tools"]:
                        st.markdown(f'<span class="tool-chip">{tool}</span>', unsafe_allow_html=True)
                    st.markdown(f'<div class="section-label" style="margin-top:1rem">// Practice Resources</div>', unsafe_allow_html=True)
                    for r in topic["resources"]:
                        st.markdown(f"- {r}")
                    st.markdown(f'<div class="section-label" style="margin-top:1rem">// OSCP Relevance</div>', unsafe_allow_html=True)
                    st.markdown(f'<div class="warn-box" style="font-size:0.875rem">{topic["oscp_note"]}</div>', unsafe_allow_html=True)

# ─ LABS & RESOURCES ───────────────────────────────────────────
elif page == "🔬 Labs & Resources":
    st.markdown("# 🔬 Labs & Resources")
    st.markdown('<div class="section-label">// Platforms · Books · YouTube · Communities · GitHub</div>', unsafe_allow_html=True)
    st.markdown("")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["🧪 Lab Progression", "📚 Books", "▶️ YouTube", "🌐 Communities", "⚙️ Setup"])

    with tab1:
        st.markdown("### TryHackMe Path")
        st.markdown('<div class="info-box">Start here. Lower barrier. Great for building fundamentals before HTB.</div>', unsafe_allow_html=True)
        for item in RESOURCES["thm"]:
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:0.7rem 1rem;margin-bottom:0.4rem">
<span class="badge badge-green">{item['level']}</span>
<strong style="color:#e6edf3;margin-left:8px">{item['room']}</strong>
<span style="color:#8b949e;font-size:0.8rem;margin-left:8px">— {item['why']}</span>
</div>
""", unsafe_allow_html=True)

        st.markdown("### HackTheBox Path")
        st.markdown('<div class="info-box">Closer to real OSCP feel. Do after 2–3 months of THM.</div>', unsafe_allow_html=True)
        for item in RESOURCES["htb"]:
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:0.7rem 1rem;margin-bottom:0.4rem">
<span class="badge badge-orange">{item['level']}</span>
<strong style="color:#e6edf3;margin-left:8px">{item['name']}</strong>
<span style="color:#8b949e;font-size:0.8rem;margin-left:8px">— {item['why']}</span>
</div>
""", unsafe_allow_html=True)

        st.markdown("### Build Your Own AD Lab at Home")
        st.markdown("""
<div class="tip-box">
<strong style="color:#00ccff">Minimum Setup:</strong><br>
• 1x Windows Server 2019/2022 (Domain Controller) — free evaluation ISO<br>
• 2x Windows 10/11 Pro machines (domain joined)<br>
• 1x Kali Linux attacker machine<br>
• VMware Workstation Pro (free now) or VirtualBox<br>
• RAM: 16GB minimum, 32GB recommended<br><br>
<strong>Resources:</strong> GOAD (Game of Active Directory) by Orange Cyberdefense — automated Vagrant lab<br>
<code>github.com/Orange-Cyberdefense/GOAD</code>
</div>
""", unsafe_allow_html=True)

        st.markdown("### Pivoting Practice at Home")
        st.markdown("""
<div class="tip-box">
<strong style="color:#00ccff">Setup:</strong> 3 VMs on isolated VMware/VirtualBox network segments<br>
• Kali (attacker) → Target 1 (pivot host) → Target 2 (internal only)<br>
• Tools to practice: Ligolo-ng, Chisel, SSHuttle, SOCKS5 with proxychains<br>
• Concept: compromise T1, set up tunnel, pivot through to T2 which Kali can't reach directly<br><br>
<strong>Lab idea:</strong> Ubuntu server (T1, dual-homed) + Windows (T2, internal only) — practice full pivot chain
</div>
""", unsafe_allow_html=True)

    with tab2:
        st.markdown("### Essential Books")
        for book in RESOURCES["books"]:
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:0.8rem 1rem;margin-bottom:0.5rem">
<strong style="color:#e6edf3">{book['title']}</strong>
<span class="badge badge-purple" style="margin-left:8px">{book['priority']}</span><br>
<span style="color:#8b949e;font-size:0.85rem">{book['note']}</span>
</div>
""", unsafe_allow_html=True)

    with tab3:
        st.markdown("### YouTube Channels")
        for ch in RESOURCES["youtube"]:
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:0.8rem 1rem;margin-bottom:0.5rem">
<strong style="color:#ff4f4f">{ch['channel']}</strong>
<span class="badge badge-orange" style="margin-left:8px">{ch['focus']}</span><br>
<span style="color:#8b949e;font-size:0.85rem">{ch['note']}</span>
</div>
""", unsafe_allow_html=True)

    with tab4:
        st.markdown("### Communities & Discord")
        for comm in RESOURCES["communities"]:
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:0.8rem 1rem;margin-bottom:0.5rem">
<strong style="color:#00ccff">{comm['name']}</strong>
<span class="badge badge-blue" style="margin-left:8px">{comm['type']}</span><br>
<span style="color:#8b949e;font-size:0.85rem">{comm['note']}</span>
</div>
""", unsafe_allow_html=True)
        st.markdown("### GitHub Repos to Star")
        for repo in RESOURCES["github"]:
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-radius:6px;padding:0.7rem 1rem;margin-bottom:0.4rem">
<code style="color:#00ff9d">{repo['repo']}</code>
<span style="color:#8b949e;font-size:0.8rem;margin-left:10px">— {repo['note']}</span>
</div>
""", unsafe_allow_html=True)

    with tab5:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### Kali Linux Setup")
            st.markdown("""
<div class="tip-box" style="font-size:0.875rem">
<strong>Base Setup:</strong><br>
• Kali Linux (latest) — bare metal or VM<br>
• 50GB+ disk space for tools + loot<br>
• tmux + custom config (split panes for recon)<br>
• Neovim or VSCode for note-taking/scripting<br><br>
<strong>Essential installs beyond default:</strong><br>
<code>ligolo-ng, evil-winrm, bloodhound (Python),
kerbrute, chisel, pwncat-cs, pypykatz,
crackmapexec/netexec, impacket (full suite),
feroxbuster, ffuf, seclists (full)</code><br><br>
<strong>Folder structure:</strong><br>
<code>~/oscp/{machine_name}/{nmap,web,smb,loot,exploit,notes}/</code>
</div>
""", unsafe_allow_html=True)

            st.markdown("### Note-Taking System")
            st.markdown("""
<div class="tip-box" style="font-size:0.875rem">
<strong>Recommended: Obsidian</strong> (offline, markdown, graph view)<br>
• One vault per engagement/machine<br>
• Template: Target Info → Recon → Services → Exploits → PrivEsc → Flags → Lessons<br><br>
<strong>Alternative: CherryTree</strong> — popular with OSCP students, hierarchical notes<br><br>
<strong>Key habit:</strong> Screenshot EVERYTHING. Every command, every output.
For exam: you need proof screenshots with IP + flag visible.
</div>
""", unsafe_allow_html=True)

        with col2:
            st.markdown("### Hardware Recommendation")
            st.markdown("""
<div class="tip-box" style="font-size:0.875rem">
<strong>Minimum:</strong><br>
• CPU: Intel i7 / Ryzen 7 (8 cores+)<br>
• RAM: 32GB (for running 3–4 VMs simultaneously)<br>
• SSD: 1TB NVMe<br>
• Monitor: Dual monitor recommended (Kali + notes)<br><br>
<strong>Ideal:</strong><br>
• CPU: Ryzen 9 / Intel i9<br>
• RAM: 64GB<br>
• SSD: 2TB<br>
• GPU: Not critical for pentesting<br><br>
<strong>Budget Option:</strong> Cloud-based Kali (DigitalOcean $24/mo) + local VMs for AD lab
</div>
""", unsafe_allow_html=True)

            st.markdown("### Budget Estimation")
            st.markdown("""
<table style="font-size:0.82rem">
<tr><th>Item</th><th>Cost (USD)</th></tr>
<tr><td>eJPT</td><td>~$200</td></tr>
<tr><td>PNPT</td><td>~$400</td></tr>
<tr><td>CPTS (HTB Annual)</td><td>~$168/yr</td></tr>
<tr><td>CRTO</td><td>~$400</td></tr>
<tr><td>OSCP (PEN-200)</td><td>~$1,499</td></tr>
<tr><td>TryHackMe Premium</td><td>~$168/yr</td></tr>
<tr><td>VMware / VirtualBox</td><td>Free</td></tr>
<tr><td>Books (select)</td><td>~$150</td></tr>
<tr><td><strong>Total Estimate</strong></td><td><strong>~$3,000–$3,500</strong></td></tr>
</table>
<br><span style="color:#8b949e;font-size:0.8rem">Spread over 26 months = ~$115–135/month</span>
""", unsafe_allow_html=True)

            st.markdown("### Report Template Structure")
            st.markdown("""
<div class="tip-box" style="font-size:0.875rem">
<strong>OSCP Exam Report Must Have:</strong><br>
1. Cover Page (name, date, exam ID)<br>
2. Executive Summary<br>
3. Methodology overview<br>
4. Each machine section:<br>
&nbsp;&nbsp;• Service enumeration findings<br>
&nbsp;&nbsp;• Vulnerability discovered<br>
&nbsp;&nbsp;• Exploitation steps (screenshots)<br>
&nbsp;&nbsp;• PrivEsc path (screenshots)<br>
&nbsp;&nbsp;• Proof.txt / local.txt (screenshot with IP visible)<br>
5. AD set section: full attack chain<br>
6. Appendix: full command list<br><br>
<strong>Template:</strong> Use whoisflynn or noraj OSCP report templates on GitHub
</div>
""", unsafe_allow_html=True)

# ─ AM I READY ─────────────────────────────────────────────────
elif page == "✅ Am I Ready?":
    st.markdown("# ✅ Am I Ready for OSCP?")
    st.markdown('<div class="section-label">// Readiness Checklist · Common Mistakes · Failure Analysis</div>', unsafe_allow_html=True)
    st.markdown("")

    tab1, tab2, tab3, tab4 = st.tabs(["✅ Readiness Checklist", "❌ Common Mistakes", "💀 Why People Fail", "🧠 Mindset & Exam Strategy"])

    with tab1:
        st.markdown('<div class="info-box">Check every box honestly. If you cannot do it without looking it up, it\'s not ticked.</div>', unsafe_allow_html=True)
        st.markdown("")
        for category, items in READINESS.items():
            st.markdown(f"#### {category}")
            for item in items:
                st.checkbox(item, key=f"check_{item[:30]}")
            st.markdown("")

    with tab2:
        st.markdown("### Common Mistakes OSCP Students Make")
        for i, mistake in enumerate(MISTAKES, 1):
            st.markdown(f"""
<div class="warn-box" style="margin-bottom:0.5rem">
<strong style="color:#ff4f4f">#{i} {mistake['title']}</strong><br>
<span style="color:#c9d1d9;font-size:0.875rem">{mistake['detail']}</span>
</div>
""", unsafe_allow_html=True)

    with tab3:
        st.markdown("### Why People Fail OSCP")
        for reason in FAIL_REASONS:
            st.markdown(f"""
<div style="background:#0d1117;border:1px solid #21262d;border-left:3px solid #ff4f4f;
border-radius:6px;padding:0.8rem 1rem;margin-bottom:0.5rem">
<strong style="color:#ff4f4f">{reason['reason']}</strong>
<span style="color:#d4a017;margin-left:8px;font-size:0.8rem">{reason['frequency']}</span><br>
<span style="color:#8b949e;font-size:0.85rem">{reason['detail']}</span><br>
<span style="color:#00ff9d;font-size:0.85rem">Fix: {reason['fix']}</span>
</div>
""", unsafe_allow_html=True)

    with tab4:
        st.markdown("### Exam Strategy & Mindset")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
<div class="tip-box">
<strong style="color:#00ccff">Exam Time Management (48 hrs)</strong><br><br>
• First 15 min: Read all targets, plan order<br>
• Start with standalone machines (easier points)<br>
• AD set: attempt after getting some standalones<br>
• Take notes WHILE exploiting — not after<br>
• Screenshot EVERYTHING in real time<br>
• If stuck 45–60 min: move on. Come back fresh.<br>
• Sleep. Seriously. 4–6 hrs during exam night.<br>
• Report writing: start during exam, not after<br>
• Always verify flags: local.txt + proof.txt<br><br>
<strong>Points breakdown (current):</strong><br>
• 3x standalone machines: up to 60 pts<br>
• 1x AD set (3 machines): up to 40 pts<br>
• Pass: 70 pts + valid report
</div>
""", unsafe_allow_html=True)

        with col2:
            st.markdown("""
<div class="tip-box">
<strong style="color:#00ccff">What Separates Good Pentesters from Script Kiddies</strong><br><br>
✅ They understand <em>why</em> an exploit works<br>
✅ They can enumerate manually without scanners<br>
✅ They adapt when tools fail<br>
✅ They document as they go<br>
✅ They know when to move on vs. dig deeper<br>
✅ They can write exploits, not just run them<br>
✅ They understand the underlying protocol<br>
✅ They have a consistent methodology<br><br>
<strong style="color:#00ccff">Most Important Real-World Skills:</strong><br>
• Clear written reports clients can act on<br>
• Network understanding (not just tool output)<br>
• AD attacks (every corporate target has AD)<br>
• Web app testing (OWASP Top 10 minimum)<br>
• Python scripting for custom tools/exploits
</div>
""", unsafe_allow_html=True)

        st.markdown("""
<div class="warn-box" style="margin-top:1rem">
<strong style="color:#ff4f4f">Metasploit Limitation in OSCP:</strong><br>
You may use Metasploit's auxiliary, exploit, and post modules on ONLY ONE machine during the exam.
Use it wisely (save it for a hard target). Practice manual exploitation for everything else.
Know how to replicate Metasploit exploits manually using searchsploit + Python/C.
</div>
""", unsafe_allow_html=True)

# ─ MASTER TABLE ───────────────────────────────────────────────
elif page == "📋 Master Table":
    st.markdown("# 📋 Master Roadmap Table")
    st.markdown('<div class="section-label">// Complete Timeline · All Phases · All Milestones</div>', unsafe_allow_html=True)
    st.markdown("")

    st.markdown("""
<table>
<tr>
  <th>Timeline</th>
  <th>Phase</th>
  <th>Key Skills</th>
  <th>Labs / Certs</th>
  <th>Expected Outcome</th>
  <th>Difficulty</th>
  <th>Milestone</th>
</tr>
""" + "\n".join([f"""
<tr>
  <td style="color:#00ff9d;font-family:JetBrains Mono,monospace;white-space:nowrap">{r['timeline']}</td>
  <td><strong>{r['phase']}</strong></td>
  <td style="font-size:0.82rem">{r['skills']}</td>
  <td style="font-size:0.82rem">{r['labs']}</td>
  <td style="font-size:0.82rem">{r['outcome']}</td>
  <td><span class="badge badge-{r['diff_color']}">{r['difficulty']}</span></td>
  <td style="font-size:0.82rem;color:#00ff9d">✓ {r['milestone']}</td>
</tr>
""" for r in MASTER_TABLE]) + "</table>", unsafe_allow_html=True)

    st.markdown("")
    st.markdown("""
<div class="info-box" style="margin-top:1.5rem">
<strong style="color:#00ff9d">Final Note from Your Mentor:</strong><br><br>
OSCP is not about being the smartest person in the room. It's about being the most <em>methodical</em>.
The exam rewards people who enumerate thoroughly, stay calm, move on when stuck, and document everything.
You have 26 months. That is more than enough time if you put in consistent daily effort.
Your VA background is an advantage — you understand systems, CVEs, and report writing.
Now you just need to go offensive. Build the habit. Hack daily. Document everything. Stay curious.<br><br>
<strong>Try Harder</strong> — but more importantly, <strong>Try Smarter.</strong>
</div>
""", unsafe_allow_html=True)
