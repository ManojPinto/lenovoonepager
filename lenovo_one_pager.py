"""
Lenovo Knowledge Vault - IT Helpdesk Home
==========================================
Streamlit app — single file, zero extra dependencies beyond streamlit.

Usage:
    streamlit run lenovo_one_pager.py
"""

import streamlit as st
import streamlit.components.v1 as components

# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                         EMBEDDED HTML PAGE                              ║
# ╚══════════════════════════════════════════════════════════════════════════╝
HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Lenovo One Pager - IT Helpdesk Home</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    html, body {
      height: 100%;
      font-family: 'Segoe UI', Arial, sans-serif;
      background: #e5e5e5;
      color: #000000;
    }

    body {
      display: flex;
      flex-direction: column;
      height: 100vh;
      overflow: hidden;
    }

    /* PAGE HEADING */
    .page-heading {
      background: linear-gradient(135deg, #0a0a23 0%, #1a1a4e 50%, #2d0036 100%);
      padding: 22px 36px;
      flex-shrink: 0;
      border-bottom: 3px solid #e50000;
    }
    .page-heading h1 {
      font-size: 1.7rem;
      font-weight: 900;
      letter-spacing: 3px;
      text-transform: uppercase;
      color: #fff;
      text-shadow: 0 2px 16px rgba(229,0,0,0.4);
    }
    .page-heading p {
      margin-top: 4px;
      font-size: 0.82rem;
      color: #999;
    }

    /* MAIN WRAPPER */
    .main-wrapper {
      display: flex;
      flex: 1;
      overflow: hidden;
    }

    /* SIDEBAR */
    .sidebar {
      width: 230px;
      min-width: 230px;
      background: #0e0e1c;
      border-right: 1px solid rgba(255,255,255,0.07);
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      flex-shrink: 0;
    }
    .sidebar-label {
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      color: #555;
      padding: 18px 20px 8px;
    }
    .nav-item {
      display: flex;
      align-items: center;
      gap: 11px;
      padding: 13px 20px;
      cursor: pointer;
      color: #aaa;
      font-size: 0.88rem;
      font-weight: 500;
      border-left: 3px solid transparent;
      transition: background 0.15s, color 0.15s, border-color 0.15s;
      user-select: none;
    }
    .nav-item:hover { background: rgba(255,255,255,0.05); color: #fff; }
    .nav-item.active {
      background: rgba(229,0,0,0.12);
      color: #fff;
      border-left-color: #e50000;
    }
    .nav-item .nav-icon { font-size: 1rem; flex-shrink: 0; width: 20px; text-align: center; }

    /* CONTENT PANEL */
    .content-panel {
      flex: 1;
      overflow-y: auto;
      background: #13131f;
      position: relative;
    }

    .panel {
      display: none;
      padding: 32px 40px;
      animation: fadeIn 0.2s ease;
    }
    .panel.active { display: block; }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateX(8px); }
      to   { opacity: 1; transform: translateX(0); }
    }

    .panel-title {
      font-size: 1.3rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 22px;
      padding-bottom: 12px;
      border-bottom: 2px solid #e50000;
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* FILE VIEWER */
    #file-viewer {
      display: none;
      flex-direction: column;
      height: 100%;
      padding: 20px 32px;
      animation: fadeIn 0.2s ease;
    }
    #file-viewer.active { display: flex; }

    .viewer-topbar {
      display: flex;
      align-items: center;
      gap: 14px;
      margin-bottom: 16px;
      flex-shrink: 0;
    }
    .btn-back {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 16px;
      background: rgba(255,255,255,0.08);
      border: 1px solid rgba(255,255,255,0.15);
      border-radius: 7px;
      color: #ccc;
      font-size: 0.85rem;
      font-weight: 600;
      cursor: pointer;
      transition: background 0.2s, color 0.2s;
    }
    .btn-back:hover { background: rgba(255,255,255,0.15); color: #fff; }

    .viewer-filename {
      font-size: 0.95rem;
      font-weight: 600;
      color: #fff;
      flex: 1;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .btn-newtab {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 8px 14px;
      background: #e50000;
      border: none;
      border-radius: 7px;
      color: #fff;
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      transition: background 0.2s;
      white-space: nowrap;
    }
    .btn-newtab:hover { background: #b30000; }

    .file-type-badge {
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      flex-shrink: 0;
    }
    .badge-excel { background: #1d6f42; color: #fff; }
    .badge-word  { background: #2b579a; color: #fff; }
    .badge-pdf   { background: #c0392b; color: #fff; }
    .badge-text  { background: #555;    color: #fff; }

    #viewer-frame {
      flex: 1;
      width: 100%;
      border: none;
      border-radius: 10px;
      background: #fff;
      min-height: 0;
    }

    /* LINK GRID */
    .link-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(190px, 1fr));
      gap: 12px;
    }
    .link-card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.09);
      border-radius: 10px;
      padding: 13px 14px;
      text-decoration: none;
      color: #ccc;
      font-size: 0.85rem;
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 10px;
      cursor: pointer;
      transition: background 0.2s, border-color 0.2s, transform 0.15s, color 0.15s;
    }
    .link-card:hover {
      background: rgba(229,0,0,0.18);
      border-color: #e50000;
      color: #fff;
      transform: translateY(-2px);
    }
    .dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      background: #e50000;
      flex-shrink: 0;
    }

    /* INFO CARDS */
    .card-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 18px;
    }
    .info-card {
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.1);
      border-radius: 12px;
      padding: 22px;
      display: flex;
      flex-direction: column;
    }
    .info-card h3 { font-size: 1.05rem; font-weight: 700; color: #fff; margin-bottom: 4px; }
    .info-card .domain { font-size: 0.73rem; color: #666; margin-bottom: 10px; }
    .info-card p { font-size: 0.82rem; color: #aaa; line-height: 1.6; flex: 1; margin-bottom: 16px; }
    .info-card a.btn {
      display: inline-block;
      padding: 8px 18px;
      background: #e50000;
      color: #fff;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.82rem;
      font-weight: 600;
      align-self: flex-start;
      transition: background 0.2s;
    }
    .info-card a.btn:hover { background: #b30000; }

    /* DOC PILLS */
    .doc-grid { display: flex; flex-wrap: wrap; gap: 10px; }
    .doc-pill {
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 9px 14px;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 22px;
      text-decoration: none;
      color: #ccc;
      font-size: 0.84rem;
      font-weight: 500;
      cursor: pointer;
      transition: background 0.2s, color 0.2s, border-color 0.2s;
    }
    .doc-pill:hover { background: #e50000; color: #fff; border-color: #e50000; }
    .pill-icon { font-size: 0.82rem; }

    /* PHONE TABLE */
    .phone-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 32px; }
    .phone-block h3 {
      font-size: 0.9rem; font-weight: 700; color: #e50000;
      margin-bottom: 14px; text-transform: uppercase;
      letter-spacing: 1px; text-decoration: underline;
    }
    .phone-block ul { list-style: none; }
    .phone-block ul li {
      padding: 7px 0;
      border-bottom: 1px solid rgba(255,255,255,0.05);
      font-size: 0.86rem; color: #bbb;
      display: flex; justify-content: space-between; flex-wrap: wrap; gap: 4px;
    }
    .phone-block ul li strong { color: #fff; min-width: 160px; }

    /* SOCIAL */
    .social-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 12px; }
    .social-card {
      display: flex; align-items: center; gap: 12px;
      padding: 14px 16px;
      background: rgba(255,255,255,0.05);
      border: 1px solid rgba(255,255,255,0.09);
      border-radius: 10px;
      text-decoration: none; color: #bbb;
      font-size: 0.86rem; font-weight: 500;
      transition: background 0.2s, transform 0.15s, color 0.15s;
    }
    .social-card:hover { background: rgba(229,0,0,0.15); border-color: #e50000; color: #fff; transform: translateY(-2px); }
    .social-icon {
      width: 34px; height: 34px; border-radius: 8px;
      display: flex; align-items: center; justify-content: center;
      font-size: 1rem; font-weight: 700; flex-shrink: 0; color: #fff;
    }
    .fb { background: #1877f2; }
    .ig { background: linear-gradient(45deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888); }
    .yt { background: #ff0000; }
    .tw { background: #111; }
    .li { background: #0a66c2; }

    /* FEEDBACK */
    .feedback-box {
      background: linear-gradient(135deg, #1a1a2e, #2d0036);
      border: 1px solid rgba(229,0,0,0.3);
      border-radius: 16px;
      padding: 34px 38px;
      display: flex; align-items: center;
      justify-content: space-between; gap: 24px; flex-wrap: wrap;
    }
    .feedback-box h2 { font-size: 1.4rem; font-weight: 700; margin-bottom: 8px; }
    .feedback-box p  { color: #aaa; font-size: 0.9rem; max-width: 460px; }
    .feedback-box a {
      display: inline-block; padding: 13px 28px;
      background: #fff; color: #e50000;
      font-weight: 700; font-size: 0.92rem;
      border-radius: 8px; text-decoration: none;
      white-space: nowrap; transition: background 0.2s, color 0.2s;
    }
    .feedback-box a:hover { background: #e50000; color: #fff; }

    /* FOOTER */
    footer {
      background: #09090f;
      text-align: center;
      padding: 11px;
      color: #444;
      font-size: 0.73rem;
      border-top: 1px solid rgba(255,255,255,0.06);
      flex-shrink: 0;
    }
  </style>
</head>
<body>

<!-- PAGE HEADING -->
<div class="page-heading">
  <h1>Lenovo One Pager</h1>
  <p>Introduced by the IN CEC Training Team</p>
</div>

<!-- MAIN: SIDEBAR + CONTENT -->
<div class="main-wrapper">

  <!-- SIDEBAR -->
  <nav class="sidebar">
    <div class="sidebar-label">Sections</div>
    <div class="nav-item active" data-target="lenovo-urls">
      <span class="nav-icon">&#128279;</span> Lenovo URLs
    </div>
    <div class="nav-item" data-target="learning">
      <span class="nav-icon">&#127891;</span> Learning &amp; Development
    </div>
    <div class="nav-item" data-target="process-docs">
      <span class="nav-icon">&#128193;</span> Process Documents
    </div>
    <div class="nav-item" data-target="contact">
      <span class="nav-icon">&#128222;</span> Contact Numbers
    </div>
    <div class="nav-item" data-target="j2w">
      <span class="nav-icon">&#9889;</span> J2W URLs
    </div>
    <div class="nav-item" data-target="community">
      <span class="nav-icon">&#127760;</span> Our Community
    </div>
    <div class="nav-item" data-target="feedback">
      <span class="nav-icon">&#128172;</span> Help Us Improve
    </div>
  </nav>

  <!-- CONTENT PANEL -->
  <div class="content-panel">

    <!-- FILE VIEWER -->
    <div id="file-viewer">
      <div class="viewer-topbar">
        <button class="btn-back" onclick="closeFileViewer()">&#8592; Back</button>
        <span class="file-type-badge" id="viewer-badge"></span>
        <span class="viewer-filename" id="viewer-title"></span>
        <a class="btn-newtab" id="viewer-newtab" href="#" target="_blank">Open in new tab &#8599;</a>
      </div>
      <iframe id="viewer-frame" src="" title="File Viewer"></iframe>
    </div>

    <!-- LENOVO URLs -->
    <div class="panel active" id="lenovo-urls">
      <div class="panel-title">&#128279; Lenovo URLs</div>
      <div class="link-grid">
        <a class="link-card" href="https://buyalenovo.com/" target="_blank"><span class="dot"></span>Carry-In Locator</a>
        <a class="link-card" href="https://analytics.bsharpcorp.com/open-view/104207000008114715" target="_blank"><span class="dot"></span>PUDO Status Check</a>
        <a class="link-card" href="https://todo.bsharpcorp.com/kpi/kpi_dashboard" target="_blank"><span class="dot"></span>Check Your KPI</a>
        <a class="link-card" href="https://support.lenovo.com/in/en/parts-lookup?linktrack=footer:support_parts%20lookup" target="_blank"><span class="dot"></span>Parts Look-up</a>
        <a class="link-card" href="https://pcsupport.lenovo.com/in/en/iwslookup#" target="_blank"><span class="dot"></span>IWS Warranty Check</a>
        <a class="link-card" href="https://secure.logmeinrescue.com/" target="_blank"><span class="dot"></span>LogMeIn Rescue - Web</a>
        <a class="link-card" href="https://outlook.office.com/" target="_blank"><span class="dot"></span>Outlook Web</a>
        <a class="link-card" href="https://support.lenovo.com/" target="_blank"><span class="dot"></span>Support Site</a>
        <a class="link-card" href="https://psref.lenovo.com/" target="_blank"><span class="dot"></span>PSREF</a>
        <a class="link-card" href="https://forms.office.com/pages/responsepage.aspx?id=KAt9XPi9DEGqk03zcrFiAx8XhD7PAPpHqdVcJ7FDVOdURFJXTzZHNUdWRThVSkcwNUhJODBHMTA5Ri4u&origin=lprLink&route=shorturl" target="_blank"><span class="dot"></span>Raise Lead &#8211; Laptop &amp; Accessory</a>
        <a class="link-card" href="http://103.30.234.106:8080/ui/ad/v1/index.html" target="_blank"><span class="dot"></span>Workspace Link 1 (103)</a>
        <a class="link-card" href="https://10.128.245.138:8443/ui/ad/v1/index.html" target="_blank"><span class="dot"></span>Workspace Link 2 (10)</a>
        <a class="link-card" href="https://helpdesk.aforeserve.co.in/" target="_blank"><span class="dot"></span>Monitor Ticket Logging</a>
        <a class="link-card" href="https://forms.office.com/pages/responsepage.aspx?id=KAt9XPi9DEGqk03zcrFiA4fdXVSLOTFDhvE87_lA3nBUMjBXVFlKS1VXVFlQMlc5SDg1N1JLQ1VYNi4u&route=shorturl" target="_blank"><span class="dot"></span>Resolve &#8211; Billable Lead</a>
        <a class="link-card" href="https://lenovo-plrs-uat.crm5.dynamics.com/" target="_blank"><span class="dot"></span>MSD UAT</a>
        <a class="link-card" href="https://lenovo-plrs-prod.crm5.dynamics.com/" target="_blank"><span class="dot"></span>MSD PROD</a>
        <a class="link-card" href="https://download.lenovo.com/bsco/index.html" target="_blank"><span class="dot"></span>BIOS Simulator Center</a>
        <a class="link-card" href="http://csp.lenovo.com/ibinapp/il/Login.jsp" target="_blank"><span class="dot"></span>CSP</a>
      </div>
    </div>

    <!-- LEARNING & DEVELOPMENT -->
    <div class="panel" id="learning">
      <div class="panel-title">&#127891; Learning and Development</div>
      <div class="card-row">
        <div class="info-card">
          <h3>LEAP</h3>
          <div class="domain">apps.bsharpcorp.com</div>
          <p>Click Here to access LEAP, where you will find all learning modules related to products, diagnostics, and other essential topics.</p>
          <a class="btn" href="https://apps.bsharpcorp.com/" target="_blank">Open LEAP &#8599;</a>
        </div>
        <div class="info-card">
          <h3>UKM</h3>
          <div class="domain">ukm.lenovo.com</div>
          <p>Click here to access UKM, which provides all known tips, the Problem Determination Guide, and various additional resources.</p>
          <a class="btn" href="https://ukm.lenovo.com/" target="_blank">Open UKM &#8599;</a>
        </div>
        <div class="info-card">
          <h3>Communicare</h3>
          <div class="domain">lenovoind-my.sharepoint.com</div>
          <p>Access Call Script, Call Disclaimers and Phonetics documents. Please let us know if anything is required to be included.</p>
          <a class="btn" href="https://lenovoind-my.sharepoint.com/:f:/r/personal/mpintoo_lenovo_com/Documents/One%20Pager/Communicare?csf=1&web=1&e=s5LdaE" target="_blank">Open Communicare &#8599;</a>
        </div>
      </div>
    </div>

    <!-- PROCESS DOCUMENTS -->
    <div class="panel" id="process-docs">
      <div class="panel-title">&#128193; Process Documents</div>
      <div class="doc-grid">
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:t:/g/personal/mpintoo_lenovo_com/IQB_yvlRXUWDSI6_9Ugrwd7qAbVIkFNE9jSQ6bYxopHLKGw?e=b7VEpb" data-type="word" data-name="Case Template">
          <span class="pill-icon">&#128221;</span>Case Template
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:b:/g/personal/mpintoo_lenovo_com/IQAalfwa-QbxTo6BTUw-GlwZAfutGFAdPRazc34PFKbI3yA?e=4d9mQB" data-type="pdf" data-name="CEC Call Logging Process">
          <span class="pill-icon">&#128196;</span>CEC Call Logging Process
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQAWtzQPy-V9T4sHaR0tpv-mAbF7jQcoq9TYk6PcKuV8IXs?e=IQJegN" data-type="excel" data-name="Remote &amp; Rescue Guide">
          <span class="pill-icon">&#128202;</span>Remote &amp; Rescue Guide
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:t:/g/personal/mpintoo_lenovo_com/IQD2ujAlc69HTbc-c_GfVbSfAa1a0V8HBDNi_w44fPGyqPQ?e=yGQPGK" data-type="word" data-name="Service Delivery Instruction">
          <span class="pill-icon">&#128221;</span>Service Delivery Instruction
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQCQKdSxst1RQpI12zczcoSTAaAScDRX7OZl8Pi-44DFHN0?e=fNyvCv" data-type="excel" data-name="RRR Selection Guide in WO">
          <span class="pill-icon">&#128202;</span>RRR Selection Guide in WO
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQDXlepyUdUnQ44nI2Ae4mX8AXVRNA6jSjxU2lBLOAGEMq4?e=9IqHR9" data-type="excel" data-name="Windows Reset &amp; OSRI Guide">
          <span class="pill-icon">&#128202;</span>Windows Reset &amp; OSRI Guide
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:t:/g/personal/mpintoo_lenovo_com/IQDhJdns8NWLRpHNASUyb-TrAZp-S6o2BiWJkAvespudg-g?e=db5mDu" data-type="word" data-name="Shipping Instructions">
          <span class="pill-icon">&#128221;</span>Shipping Instructions
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQCT406A9M6zRo-rvQfUfCd0AY4wnYYaxrS0IshO2rGPdp4?e=xO0oyt" data-type="excel" data-name="HCS Code">
          <span class="pill-icon">&#128202;</span>HCS Code
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:f:/g/personal/mpintoo_lenovo_com/IgBYdvNPCnMNQ5001O6T1AyLAbgJOU9KpMaEYKlzAIsqPjY?e=LdnUL2" data-type="link" data-name="Consumer Accessory Details">
          <span class="pill-icon">&#128193;</span>Consumer Accessory Details
        </span>
        <span class="doc-pill" data-href="https://lenovoind-my.sharepoint.com/:x:/g/personal/mpintoo_lenovo_com/IQCbBdj6ADpoSJdbJzYzw102AcJJmV5WPDwH825TGA3ioHk?e=4qOToW" data-type="excel" data-name="LFR &amp; LES Partner List">
          <span class="pill-icon">&#128202;</span>LFR &amp; LES Partner List
        </span>
        <span class="doc-pill" data-href="https://support.lenovo.com/in/en/solutions/ht035306-lcd-display-pixel-policy-idealenovo-laptops-and-tablets" data-type="link" data-name="Dead Pixel Policy">
          <span class="pill-icon">&#128279;</span>Dead Pixel Policy
        </span>
        <span class="doc-pill" data-href="https://download.lenovo.com/lenovo/lsw/adp_sa_en_in_think.pdf" data-type="pdf" data-name="ADP Terms (Commercial)">
          <span class="pill-icon">&#128196;</span>ADP Terms (Commercial)
        </span>
        <span class="doc-pill" data-href="https://download.lenovo.com/lenovo/lsw/adp_sa_en_in_idea.pdf" data-type="pdf" data-name="ADP Terms (Consumer)">
          <span class="pill-icon">&#128196;</span>ADP Terms (Consumer)
        </span>
        <span class="doc-pill" data-href="https://download.lenovo.com/pccbbs/thinkcentre_pdf/l505-0010-03_en_update.pdf" data-type="pdf" data-name="Lenovo Limited Warranty Terms">
          <span class="pill-icon">&#128196;</span>Lenovo Limited Warranty Terms
        </span>
        <span class="doc-pill" data-href="https://support.lenovo.com/kn/en/solutions/ht505335" data-type="link" data-name="IWS Terms">
          <span class="pill-icon">&#128279;</span>IWS Terms
        </span>
      </div>
    </div>

    <!-- CONTACT NUMBERS -->
    <div class="panel" id="contact">
      <div class="panel-title">&#128222; Contact Numbers</div>
      <div class="phone-grid">
        <div class="phone-block">
          <h3>Toll Free Number</h3>
          <ul>
            <li><strong>Commercial</strong><span>1800-419-4666 / 1800-121-8465</span></li>
            <li><strong>Consumer</strong><span>1800-419-7555 / 1800-121-5366</span></li>
            <li><strong>Premium Care</strong><span>1800-121-9339</span></li>
            <li><strong>Premier Support</strong><span>1800-419-9339</span></li>
            <li><strong>MBG (Smartphone)</strong><span>1800-419-6686</span></li>
            <li><strong>Tablet</strong><span>1800-208-7555</span></li>
            <li><strong>Workstation</strong><span>1800-121-7225</span></li>
            <li><strong>Post Sales</strong><span>1800-572-6465</span></li>
            <li><strong>Sales</strong><span>1800-4199-733</span></li>
            <li><strong>Moto book</strong><span>18004196686</span></li>
            <li><strong>Fujitsu</strong><span>1800-891-2273</span></li>
            <li><strong>Server</strong><span>+91 80 6884 6800</span></li>
          </ul>
        </div>
        <div class="phone-block">
          <h3>Direct Transfer Number</h3>
          <ul>
            <li><strong>Commercial</strong><span>12409</span></li>
            <li><strong>Consumer</strong><span>12428</span></li>
            <li><strong>Premium Care</strong><span>12421</span></li>
            <li><strong>Premier Support</strong><span>12419</span></li>
            <li><strong>MBG (Smartphone)</strong><span>13440</span></li>
            <li><strong>Tablet</strong><span>12429</span></li>
            <li><strong>Workstation</strong><span>12415</span></li>
          </ul>
        </div>
      </div>
    </div>

    <!-- J2W URLs -->
    <div class="panel" id="j2w">
      <div class="panel-title">&#9889; J2W URLs <small style="font-size:0.78rem;font-weight:400;color:#666;margin-left:8px;">Joules to Watts &#8212; Time Matters</small></div>
      <div class="link-grid" style="max-width:480px;">
        <a class="link-card" href="https://apiv2.trackervigil.com/Account/Login?ReturnUrl=/connect/authorize/callback?client_id%3Detms-web.app%26redirect_uri%3Dhttps%253A%252F%252Fj2w.trackervigil.com%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520offline_access%26state%3D85c2bad31f3a41ac8f91ddb73a7953c1%26code_challenge%3Dx5ovYtpxb0b4YTOj9d-EBABAYbIx7XS4XwXVp-yHYds%26code_challenge_method%3DS256%26acr_values%3Dtenant%253Aj2w%26response_mode%3Dquery%26host%3Dhttps%253A%252F%252Fj2w" target="_blank"><span class="dot"></span>Transport &#8211; Trackervigil</a>
        <a class="link-card" href="https://j2wlenovo.greythr.com/v3/portal/ess/home" target="_blank"><span class="dot"></span>Attendance Marking</a>
      </div>
    </div>

    <!-- OUR COMMUNITY -->
    <div class="panel" id="community">
      <div class="panel-title">&#127760; Our Community</div>
      <div class="social-grid">
        <a class="social-card" href="https://www.facebook.com/LenovoIndia/" target="_blank">
          <div class="social-icon fb">f</div><span>Lenovo India &#8211; Facebook</span>
        </a>
        <a class="social-card" href="https://www.instagram.com/lenovo_india/" target="_blank">
          <div class="social-icon ig">&#128248;</div><span>@lenovo_india &#8211; Instagram</span>
        </a>
        <a class="social-card" href="https://www.youtube.com/user/lenovoindia" target="_blank">
          <div class="social-icon yt">&#9654;</div><span>Lenovo India &#8211; YouTube</span>
        </a>
        <a class="social-card" href="https://x.com/Lenovo_in" target="_blank">
          <div class="social-icon tw">&#120143;</div><span>@Lenovo_in &#8211; X (Twitter)</span>
        </a>
        <a class="social-card" href="https://in.linkedin.com/company/lenovoin" target="_blank">
          <div class="social-icon li">in</div><span>Lenovo India &#8211; LinkedIn</span>
        </a>
      </div>
    </div>

    <!-- FEEDBACK -->
    <div class="panel" id="feedback">
      <div class="panel-title">&#128172; Help Us Improve Together</div>
      <div class="feedback-box">
        <div>
          <h2>Help Us Improve Together</h2>
          <p>Your insights help us build a better workplace &#8212; share your thoughts with us.</p>
        </div>
        <a href="https://forms.office.com/r/iMgYfdaFmh" target="_blank">Submit Your Feedback</a>
      </div>
    </div>

  </div><!-- /content-panel -->
</div><!-- /main-wrapper -->

<footer>
  IT Helpdesk Home &bull; IN CEC Training Team &bull; Published 5/5/2026
</footer>

<script>
  let currentPanelId = 'lenovo-urls';

  document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
      const target = item.dataset.target;
      currentPanelId = target;
      document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
      item.classList.add('active');
      closeFileViewer(false);
      document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
      document.getElementById(target).classList.add('active');
    });
  });

  function getFileType(href, explicitType) {
    if (explicitType && explicitType !== 'link') return explicitType;
    if (href.includes('/:x:/')) return 'excel';
    if (href.includes('/:t:/')) return 'word';
    if (href.includes('/:b:/')) return 'pdf';
    const path = href.split('?')[0].toLowerCase();
    if (path.endsWith('.xlsx') || path.endsWith('.xls') || path.endsWith('.csv')) return 'excel';
    if (path.endsWith('.docx') || path.endsWith('.doc')) return 'word';
    if (path.endsWith('.pdf')) return 'pdf';
    if (path.endsWith('.txt')) return 'text';
    return 'link';
  }

  const badgeConfig = {
    excel: { label: 'Excel', cls: 'badge-excel' },
    word:  { label: 'Word',  cls: 'badge-word'  },
    pdf:   { label: 'PDF',   cls: 'badge-pdf'   },
    text:  { label: 'Text',  cls: 'badge-text'  },
  };

  function buildEmbedUrl(href, type) {
    // Only called for non-SharePoint embeddable files (public PDFs, etc.)
    return href;
  }

  function openFileViewer(href, name, type) {
    const cfg = badgeConfig[type] || { label: type.toUpperCase(), cls: 'badge-text' };
    document.getElementById('viewer-badge').textContent = cfg.label;
    document.getElementById('viewer-badge').className   = 'file-type-badge ' + cfg.cls;
    document.getElementById('viewer-title').textContent = name;
    document.getElementById('viewer-newtab').href       = href;
    document.getElementById('viewer-frame').src         = buildEmbedUrl(href, type);
    document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
    document.getElementById('file-viewer').classList.add('active');
  }

  function closeFileViewer(restorePanel = true) {
    document.getElementById('file-viewer').classList.remove('active');
    document.getElementById('viewer-frame').src = '';
    if (restorePanel) document.getElementById(currentPanelId).classList.add('active');
  }

  document.querySelectorAll('.doc-pill[data-href]').forEach(pill => {
    pill.addEventListener('click', () => {
      const href = pill.dataset.href;
      const name = pill.dataset.name;
      const type = getFileType(href, pill.dataset.type);

      // SharePoint / OneDrive enforce X-Frame-Options: SAMEORIGIN —
      // they refuse to load inside any iframe.  Open in a new tab instead
      // (the browser already has the user's auth session there).
      if (href.includes('sharepoint.com') || type === 'link') {
        window.open(href, '_blank');
        return;
      }

      // Public files (e.g. download.lenovo.com PDFs) can be embedded inline.
      openFileViewer(href, name, type);
    });
  });
</script>

</body>
</html>"""


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║                         STREAMLIT APP                                   ║
# ╚══════════════════════════════════════════════════════════════════════════╝

st.set_page_config(
    page_title            = "Lenovo One Pager",
    page_icon             = "🔴",
    layout                = "wide",
    initial_sidebar_state = "collapsed",
)

# ── Global CSS: hide Streamlit chrome on every page ─────────────────────────
st.markdown("""
<style>
    #MainMenu, header, footer               { visibility: hidden; height: 0; }
    .stApp                                  { margin: 0 !important; padding: 0 !important; background: #13131f; }
    .block-container                        { padding: 0 !important; margin: 0 !important; max-width: 100% !important; }
    [data-testid="stToolbar"]               { display: none !important; }
    [data-testid="stDecoration"]            { display: none !important; }
    [data-testid="stStatusWidget"]          { display: none !important; }
    [data-testid="stSidebar"]               { display: none !important; }
    iframe                                  { border: none !important; display: block; }

    /* Login page styles */
    .login-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        background: linear-gradient(135deg, #0a0a23 0%, #1a1a4e 50%, #2d0036 100%);
        padding: 40px 20px;
    }
    .login-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 16px;
        padding: 48px 44px;
        width: 100%;
        max-width: 420px;
        text-align: center;
    }
    .login-box h1 {
        font-size: 1.6rem;
        font-weight: 900;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: #fff;
        margin-bottom: 6px;
    }
    .login-box p  { color: #999; font-size: 0.88rem; margin-bottom: 28px; }
    .login-badge  {
        display: inline-block;
        background: #e50000;
        color: #fff;
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        padding: 4px 12px;
        border-radius: 20px;
        margin-bottom: 20px;
    }

    /* Override Streamlit input/button styles for login */
    div[data-testid="stTextInput"] input {
        background: #ffffff !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 8px !important;
        color: #111111 !important;
        font-size: 0.9rem !important;
        padding: 12px 14px !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #e50000 !important;
        box-shadow: 0 0 0 2px rgba(229,0,0,0.25) !important;
    }
    div[data-testid="stTextInput"] label { color: #aaa !important; font-size: 0.82rem !important; }
    div[data-testid="stForm"] { border: none !important; padding: 0 !important; }

    button[kind="primaryFormSubmit"],
    button[kind="primary"] {
        background: #e50000 !important;
        border: none !important;
        border-radius: 8px !important;
        font-size: 0.9rem !important;
        font-weight: 700 !important;
        padding: 12px !important;
        width: 100% !important;
        margin-top: 8px !important;
    }
    button[kind="primaryFormSubmit"]:hover,
    button[kind="primary"]:hover {
        background: #b30000 !important;
    }
</style>
""", unsafe_allow_html=True)


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  LOGIN GATE — require Lenovo ID before showing the dashboard            ║
# ╚══════════════════════════════════════════════════════════════════════════╝

if "lenovo_id" not in st.session_state or not st.session_state["lenovo_id"]:

    # Centre the form on the page
    _, mid, _ = st.columns([1, 1.6, 1])

    with mid:
        st.markdown("""
        <div style="height:60px"></div>
        <div style="text-align:center;">
            <div style="display:inline-block;background:#e50000;color:#fff;
                        font-size:0.7rem;font-weight:700;letter-spacing:1.5px;
                        text-transform:uppercase;padding:4px 14px;
                        border-radius:20px;margin-bottom:18px;">
                IT Helpdesk Portal
            </div>
            <h1 style="font-size:1.7rem;font-weight:900;letter-spacing:3px;
                       text-transform:uppercase;color:#fff;
                       text-shadow:0 2px 16px rgba(229,0,0,0.4);margin-bottom:6px;">
                Lenovo One Pager
            </h1>
            <p style="color:#888;font-size:0.85rem;margin-bottom:30px;">
                Sign in with your Lenovo ID to continue
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
            lenovo_id = st.text_input(
                "Lenovo ID",
                placeholder="e.g. jsmith@lenovo.com",
                help="Enter your official Lenovo email address"
            )
            submitted = st.form_submit_button("Continue →", use_container_width=True, type="primary")

        if submitted:
            val = lenovo_id.strip().lower()
            if not val:
                st.error("Please enter your Lenovo ID to continue.")
            elif not val.endswith("@lenovo.com"):
                st.error("Access restricted — only @lenovo.com email addresses are allowed.")
            else:
                st.session_state["lenovo_id"] = lenovo_id.strip()
                st.rerun()

        st.markdown("""
        <p style="text-align:center;color:#444;font-size:0.75rem;margin-top:24px;">
            IN CEC Training Team &bull; IT Helpdesk Home &bull; 2026
        </p>
        """, unsafe_allow_html=True)

    st.stop()   # ← don't render dashboard until logged in


# ╔══════════════════════════════════════════════════════════════════════════╗
# ║  DASHBOARD — shown after successful Lenovo ID entry                     ║
# ╚══════════════════════════════════════════════════════════════════════════╝

# Thin top strip showing who is logged in + logout button
top_left, top_right = st.columns([8, 1])
with top_left:
    st.markdown(
        f"<p style='color:#666;font-size:0.75rem;padding:4px 8px;margin:0;'>"
        f"&#128100; Logged in as <b style='color:#ccc'>{st.session_state['lenovo_id']}</b></p>",
        unsafe_allow_html=True
    )
with top_right:
    if st.button("Logout", use_container_width=True):
        del st.session_state["lenovo_id"]
        st.rerun()

# ── Render the full HTML dashboard ──────────────────────────────────────────
# height uses JS to detect viewport; fallback is 900px
components.html(
    HTML_CONTENT + """
    <script>
      // Tell Streamlit iframe to resize to full window height
      function setHeight() {
        const h = window.innerHeight || document.documentElement.clientHeight || 850;
        window.frameElement && (window.frameElement.style.height = h + 'px');
      }
      setHeight();
      window.addEventListener('resize', setHeight);
    </script>
    """,
    height=870,
    scrolling=False,
)
