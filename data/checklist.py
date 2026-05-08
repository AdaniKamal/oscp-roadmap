READINESS = {
    "🐧 Linux Skills": [
        "Navigate filesystem, manage permissions, find files confidently without googling",
        "Read and write bash scripts with loops, conditionals, and argument parsing",
        "Understand processes, cron jobs, SUID/SGID binaries and their security implications",
        "Transfer files to/from a target using at least 5 different methods",
        "Spawn a stable interactive shell from a limited reverse shell",
        "Run linpeas and manually verify every finding it reports",
        "Escalate privileges via at least 4 different PrivEsc vectors without hints",
    ],
    "🪟 Windows Skills": [
        "Navigate and enumerate Windows from CMD and PowerShell without GUI",
        "Understand Windows services, registry, scheduled tasks, and their attack surface",
        "Run winpeas and manually verify its findings",
        "Exploit SeImpersonatePrivilege (at least one Potato exploit)",
        "Escalate via unquoted service paths, weak service permissions, AlwaysInstallElevated",
        "Dump credentials from memory using mimikatz or pypykatz",
        "Transfer files to Windows using certutil, PowerShell, SMB, and BITS",
    ],
    "🌐 Active Directory": [
        "Build and explain the structure of a domain — DC, GPO, OU, trusts",
        "Enumerate AD with BloodHound and identify attack paths to Domain Admin",
        "Perform Kerberoasting and crack the resulting hash offline",
        "Perform AS-REP Roasting against accounts without pre-auth",
        "Execute Pass-the-Hash and Pass-the-Ticket attacks",
        "Perform DCSync to dump all domain hashes",
        "Abuse at least 2 ACL misconfigurations (WriteDACL, GenericAll, etc.)",
        "Own a full AD lab from initial user to Domain Admin unassisted",
        "Use CrackMapExec/NetExec for SMB enumeration, spraying, and execution",
        "Use impacket suite fluently (psexec, wmiexec, secretsdump, GetUserSPNs)",
    ],
    "🌍 Web Application": [
        "Manually exploit SQL injection — UNION-based and Blind — without sqlmap",
        "Identify and exploit Local File Inclusion (LFI) including log poisoning",
        "Exploit file upload vulnerabilities including extension bypass techniques",
        "Test for and exploit SSRF, XXE, and SSTI",
        "Use Burp Suite to intercept, modify, and replay requests fluently",
        "Find hidden directories and files with gobuster/ffuf using appropriate wordlists",
        "Enumerate and attack APIs and understand REST vs SOAP security issues",
    ],
    "🔌 Pivoting & Tunneling": [
        "Set up a SOCKS5 proxy through a compromised machine using Ligolo-ng",
        "Route traffic through a pivot host using proxychains",
        "Use Chisel for HTTP tunneling in both server and client mode",
        "Perform a double-pivot (attacker → host1 → host2 → host3)",
        "Transfer tools into an isolated internal network segment",
        "Enumerate internal network hosts from behind a pivot",
    ],
    "💣 Exploitation": [
        "Find, read, and modify public exploits from Exploit-DB/searchsploit",
        "Write a working x86 stack buffer overflow exploit from scratch in Python",
        "Generate and encode payloads with msfvenom for multiple platforms",
        "Use Metasploit efficiently AND replicate the same attack manually",
        "Create reverse shells in bash, Python, PHP, and PowerShell from memory",
        "Identify the correct exploit for a given CVE and service version",
    ],
    "🔑 Password Attacks": [
        "Use hashcat with correct hash modes and rule-based attacks",
        "Use hydra for brute forcing multiple protocols (SSH, FTP, HTTP, SMB)",
        "Generate targeted wordlists with cewl and cupp",
        "Identify hash types without a tool",
        "Perform credential stuffing and password spray across services",
    ],
    "📝 Reporting & Documentation": [
        "Write a professional pentest report with executive summary and technical findings",
        "Capture screenshots of every exploitation step with IP and hostname visible",
        "Document your attack chain clearly enough that someone else could replicate it",
        "Write a report for an AD compromise showing the full attack path",
        "Use a consistent note-taking system throughout an engagement",
    ],
    "⏱️ Exam Readiness": [
        "Root an easy HTB/PG machine in under 90 minutes",
        "Root a medium HTB/PG machine in under 3 hours",
        "Complete a full mock exam session (4+ machines) within 24 hours",
        "Write a full exam-quality report after a mock exam within 8 hours",
        "Comfortable working for 8+ hours with only short breaks",
        "Have a documented personal methodology checklist for every service",
    ],
}

MISTAKES = [
    {
        "title": "Over-relying on automated scanners",
        "detail": "Running autorecon and waiting for it to find everything. OSCP tests manual enumeration. If a scanner misses something, you miss the box. Learn to enumerate manually first, then use scanners to verify.",
    },
    {
        "title": "Skipping the fundamentals phase",
        "detail": "Jumping straight to HTB hard machines without solid Linux/networking/scripting foundations. You'll hit a wall on every box and not know why. Phase 1 is boring but critical.",
    },
    {
        "title": "Not taking notes during practice",
        "detail": "Rooting machines without documenting the process. During the exam you MUST document everything in real time. Build this habit in every practice session from Day 1.",
    },
    {
        "title": "Watching walkthroughs instead of struggling",
        "detail": "When stuck, immediately watching IppSec. You need 1–2 hours of genuine struggle before looking for hints. The struggling is where learning happens. Watching is passive. Hacking is active.",
    },
    {
        "title": "Underestimating Active Directory",
        "detail": "Treating AD as one topic among many. The current OSCP is 40 points of AD. If you can't own a full AD chain, you cannot pass. AD needs months of dedicated practice, not weeks.",
    },
    {
        "title": "Not practising under time pressure",
        "detail": "Always having unlimited time in practice. OSCP is 47h45m. If you've never tried to root a machine in under 2 hours, the exam pressure will destroy your performance. Time-box your practice sessions.",
    },
    {
        "title": "Metasploit dependency",
        "detail": "Using Metasploit for everything in practice. You get ONE Metasploit use in the exam. If you've never exploited manually, you'll use your Metasploit card on the wrong machine. Practice manual exploitation from Phase 2.",
    },
    {
        "title": "Neglecting report writing until exam day",
        "detail": "Never writing full reports during practice. The exam report is as important as the hacking. A missing screenshot or unclear chain can cost you the passing score. Write reports for every lab machine.",
    },
    {
        "title": "Not sleeping during the exam",
        "detail": "Trying to hack for 48 hours straight. Your brain stops working after 20+ hours without sleep. Schedule 4–6 hours of sleep. You will find solutions faster after rest than you will grinding through exhaustion.",
    },
    {
        "title": "Giving up enumeration too early",
        "detail": "Scanning only common ports or only TCP. UDP has SNMP, NFS, TFTP. High ports have services. All ports with nmap (-p-) is mandatory. 'I couldn't find anything' usually means 'I didn't enumerate enough.'",
    },
]

FAIL_REASONS = [
    {
        "reason": "Insufficient Active Directory knowledge",
        "frequency": "Most common post-2022",
        "detail": "The AD set is worth 40 points. Most people who fail score 0 on AD because they don't know the attack chain. You cannot wing AD — it requires months of deliberate practice.",
        "fix": "Build local GOAD lab. Own Forest, Active, Sauna, Cascade on HTB. Do CRTO. Practice full DA chains unassisted.",
    },
    {
        "reason": "Poor time management during exam",
        "frequency": "Very common",
        "detail": "Spending 6+ hours on one machine that they can't crack. Meanwhile easier machines sit untouched. OSCP rewards breadth — you need to score enough points from multiple machines.",
        "fix": "Time-box practice. Never spend more than 90 minutes stuck. Move on, come back. Practice this discipline daily.",
    },
    {
        "reason": "Incomplete or missing report",
        "frequency": "Surprisingly common",
        "detail": "People who technically compromised enough machines but submitted poor reports — missing screenshots, unclear steps, or late submission. The report is 50% of the assessment.",
        "fix": "Write full reports in practice. Use the official OffSec template. Screenshot every command output and every flag with IP visible.",
    },
    {
        "reason": "Enumerate too shallow",
        "frequency": "Common",
        "detail": "Missing services on high ports, UDP services (SNMP = 161, NFS = 2049), or virtual hosts. One missed service = one missed attack vector = one missed box.",
        "fix": "Always run full port scan (-p-). Always run UDP top 1000. Always check for vhosts on web services. Build a checklist and follow it every time.",
    },
    {
        "reason": "Exam anxiety and panic",
        "frequency": "Common",
        "detail": "First few hours of exam with no progress leads to panic spiral. Starts doubting skills. Brain stops working effectively. Downward performance cycle.",
        "fix": "Do full 48-hour mock exams before attempting. Know what a slow start feels like. Have a mental reset protocol. Trust your methodology.",
    },
    {
        "reason": "Not enough lab practice hours",
        "frequency": "Common",
        "detail": "Buying PEN-200 and rushing the exam after 30 days. Skill in pentesting is built through hundreds of hours of hands-on practice, not course reading.",
        "fix": "Minimum 300–400 hours of hands-on lab time before attempting. Quality over quantity — every machine should have a written report.",
    },
]
