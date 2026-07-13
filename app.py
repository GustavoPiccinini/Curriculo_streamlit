import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title=" Gustavo Piccinini | Engenheiro de Dados",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── FOTO (base64, com fallback para avatar de iniciais) ─────────────────────
ASSETS_DIR = Path(__file__).parent / "assets"
PHOTO_PATH = ASSETS_DIR / "foto.jpg"
RESUME_PDF_PATH = ASSETS_DIR / "Gustavo_Piccinini_Curriculo.pdf"


# ── PROJETOS ──────────────────────────────────────────────────────────────
# Para adicionar um projeto novo: copie um dicionário abaixo, ajuste os campos
# e cole no final da lista. "link" é opcional — se o repositório for privado
# ou não existir, é só remover a chave (ou deixar None) que o botão some sozinho.
PROJECTS = [
    {
        "title": "Data Lake PoD Cartões",
        "period": "2026",
        "context": "Projeto PoD Academy",
        "description": (
            "Data Lake completo na AWS (Raw, Trusted, Refined). Processamento com PySpark, "
            "Parquet particionado no S3 e Book de Variáveis (U1M/U3M/U6M/U12M) "
            "de inadimplência. Dashboard em Streamlit com DuckDB como engine de consulta."
        ),
        "stack": [("b-violet", "PySpark"), ("b-green", "AWS S3"), ("b-sky", "DuckDB"), ("b-amber", "Streamlit")],
        "link": "https://github.com/GustavoPiccinini/Data_Lake_PoD_Cartoes",
    },
    {
        "title": "Data Lake E-commerce",
        "period": "2026",
        "context": "Projeto PoD Academy",
        "description": (
            "Data Lake na AWS para usuários/produtos/vendas com arquitetura em medalhão "
            "(ingestion, raw, curated, controle). Ingestão Postgres → S3, processamento "
            "em PySpark orquestrado por Airflow/EMR e Book de Variáveis "
            "agregadas por usuário nas janelas U1M/U3M/U6M."
        ),
        "stack": [("b-violet", "PySpark"), ("b-green", "Airflow"), ("b-sky", "AWS EMR"), ("b-amber", "S3")],
        "link": None,  "https://github.com/GustavoPiccinini/Data_Lake-E_Comerce"
    },
    {
        "title": "Pivotando o Desktop 4C Digital",
        "period": "2026",
        "context": "Fintech de cobrança digital",
        "description": (
            "Orquestração através de Airflow de uma solução do hackathon Pivotando o Desktop,"
            " substituindo processo manual em Excel/VBA."
        ),
        "stack": [("b-violet", "PySpark"), ("b-green", "Airflow"), ("b-sky", "Spark SQL"), ("b-pink", "Arquitetura Medalhão")],
        "link": None,
    },
    {
        "title": "Dashboard de Atendimentos — Assistência Social",
        "period": "2026 – Atual",
        "context": "Prefeitura de Jacarezinho · uso interno",
        "description": (
            "Dashboard em Streamlit integrando dados do CadÚnico e Bolsa Família a partir de "
            "exportações de dados do Governo Federal. Monitoria, integridade e linhagem dos dados."
        ),
        "stack": [("b-sky", "DuckDB"), ("b-violet", "Pandas"), ("b-amber", "Streamlit"), ("b-pink", "Dados Públicos")],
        "link": None,
    },
]


def render_project_card(p: dict) -> str:
    badges = "".join(f'<span class="badge {cls}">{label}</span>' for cls, label in p["stack"])
    link_html = ""
    if p.get("link"):
        link_html = f'<a class="tl-link" href="{p["link"]}" target="_blank">⌥ {p["link"].replace("https://", "")} ↗</a>'

    return f"""
    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">{p['title']}</div>
        <div class="tl-period">{p['period']}</div>
      </div>
      <div class="tl-company">{p['context']}</div>
      <div class="tl-desc">{p['description']}</div>
      <div class="badge-row">{badges}</div>
      {link_html}
    </div>
    """


def get_avatar_html() -> str:
    if PHOTO_PATH.exists():
        ext = PHOTO_PATH.suffix.lstrip(".")
        b64 = base64.b64encode(PHOTO_PATH.read_bytes()).decode()
        return f'<img class="avatar-img" src="data:image/{ext};base64,{b64}" alt="Gustavo Piccinini" />'
    # fallback: avatar com iniciais, caso a foto ainda não tenha sido adicionada
    return '<div class="avatar-fallback">GP</div>'


st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=DM+Sans:wght@300;400;500;600&display=swap');

  html, body, [class*="css"] {
    background-color: #111318;
    color: #dde1ea;
    font-family: 'DM Sans', sans-serif;
  }
  .main { background-color: #111318; }
  .block-container {
    padding: 2.5rem 2.5rem 5rem 2.5rem;
    max-width: 1100px;
    margin: 0 auto;
  }

  /* ── HERO ── */
  .hero {
    display: flex;
    align-items: center;
    gap: 1.8rem;
    padding: 2.8rem 0 2rem 0;
    border-bottom: 1px solid #1e2130;
    margin-bottom: 2.5rem;
  }
  .avatar-img {
    width: 108px;
    height: 108px;
    border-radius: 50%;
    object-fit: cover;
    border: 2px solid #6c74e8;
    flex-shrink: 0;
  }
  .avatar-fallback {
    width: 108px;
    height: 108px;
    border-radius: 50%;
    border: 2px solid #6c74e8;
    background: #16191f;
    color: #6c74e8;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'DM Mono', monospace;
    font-size: 2rem;
    font-weight: 500;
    flex-shrink: 0;
  }
  .hero-text { flex: 1; }
  .hero-eyebrow {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #8a91a8;
    margin-bottom: 0.6rem;
  }
  .hero-name {
    font-family: 'DM Sans', sans-serif;
    font-size: 2.7rem;
    font-weight: 600;
    color: #6c74e8;
    line-height: 1.1;
    margin: 0 0 0.4rem 0;
  }
  .hero-name span { color: #6c74e8; }
  .hero-role {
    font-family: 'DM Sans', sans-serif;
    font-size: 1.05rem;
    font-weight: 300;
    color: #6c74e8;
    margin-bottom: 1.4rem;
  }
  .hero-links {
    display: flex;
    flex-wrap: wrap;
    gap: 1.2rem;
  }
  .hero-link {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #8a91a8;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 0.35rem;
    transition: color 0.2s;
  }
  .hero-link:hover { color: #6c74e8; }

  /* ── KPI CARDS ── */
  .kpi-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin-bottom: 2.5rem;
  }
  .kpi-card {
    background: #16191f;
    border: 1px solid #1e2130;
    border-radius: 10px;
    padding: 1.2rem 1.4rem;
    position: relative;
    overflow: hidden;
  }
  .kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #6c74e8, #4ade80);
    opacity: 0.6;
  }
  .kpi-value {
    font-family: 'DM Mono', monospace;
    font-size: 1.9rem;
    font-weight: 500;
    color: #f0f2f8;
    line-height: 1;
  }
  .kpi-label {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.75rem;
    color: #555e78;
    margin-top: 0.35rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
  }

  /* ── SECTION HEADER ── */
  .sec-header {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin-bottom: 1rem;
    margin-top: 2.2rem;
  }
  .sec-mono {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    color: #6c74e8;
    text-transform: uppercase;
    letter-spacing: 0.15em;
  }
  .sec-line {
    flex: 1;
    height: 1px;
    background: #1e2130;
  }

  /* ── TIMELINE CARDS ── */
  .tl-card {
    background: #16191f;
    border: 1px solid #1e2130;
    border-radius: 10px;
    padding: 1.3rem 1.6rem;
    margin-bottom: 0.85rem;
    transition: border-color 0.2s, background 0.2s;
  }
  .tl-card:hover {
    border-color: #6c74e8;
    background: #191c26;
  }
  .tl-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    flex-wrap: wrap;
    gap: 0.3rem;
    margin-bottom: 0.2rem;
  }
  .tl-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.97rem;
    font-weight: 600;
    color: #e8eaf2;
  }
  .tl-period {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #555e78;
    white-space: nowrap;
  }
  .tl-company {
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #4ade80;
    margin-bottom: 0.6rem;
  }
  .tl-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.86rem;
    color: #8a91a8;
    line-height: 1.65;
    margin-bottom: 0.7rem;
  }

  /* ── BADGES ── */
  .badge-row { display: flex; flex-wrap: wrap; gap: 5px; }
  .badge {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    padding: 3px 10px;
    border-radius: 4px;
    border: 1px solid;
  }
  .b-violet { color: #a5aaff; border-color: #2a2d55; background: #13152e; }
  .b-green  { color: #4ade80; border-color: #1a3a28; background: #0d1f17; }
  .b-amber  { color: #fbbf24; border-color: #3a2e10; background: #1e1900; }
  .b-pink   { color: #f472b6; border-color: #3a1a2e; background: #1f0d1a; }
  .b-sky    { color: #38bdf8; border-color: #1a2e3a; background: #0d1820; }

  /* ── SKILL GRID ── */
  .skill-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.85rem;
  }
  .skill-card {
    background: #16191f;
    border: 1px solid #1e2130;
    border-radius: 10px;
    padding: 1rem 1.2rem;
  }
  .skill-cat {
    font-family: 'DM Mono', monospace;
    font-size: 0.65rem;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #555e78;
    margin-bottom: 0.55rem;
  }

  /* ── ABOUT ── */
  .about-box {
    background: #16191f;
    border: 1px solid #1e2130;
    border-left: 3px solid #6c74e8;
    border-radius: 10px;
    padding: 1.3rem 1.6rem;
    font-family: 'DM Sans', sans-serif;
    font-size: 0.9rem;
    color: #8a91a8;
    line-height: 1.75;
  }

  /* ── EDUCATION & LANG ── */
  .mini-card {
    background: #16191f;
    border: 1px solid #1e2130;
    border-radius: 10px;
    padding: 1rem 1.3rem;
    margin-bottom: 0.75rem;
  }
  .mini-title {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.92rem;
    font-weight: 600;
    color: #e8eaf2;
  }
  .mini-sub {
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    color: #4ade80;
    margin: 0.15rem 0 0.4rem;
  }
  .mini-desc {
    font-family: 'DM Sans', sans-serif;
    font-size: 0.82rem;
    color: #8a91a8;
  }

  /* ── DOWNLOAD CV BUTTON ── */
  div[data-testid="stDownloadButton"] {
    margin: 0.4rem 0 0.4rem 0;
  }
  div[data-testid="stDownloadButton"] button {
    font-family: 'DM Mono', monospace !important;
    font-size: 0.8rem !important;
    color: #f0f2f8 !important;
    background: linear-gradient(90deg, #6c74e8, #4ade80) !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.55rem 1.3rem !important;
    font-weight: 500 !important;
    transition: opacity 0.2s !important;
  }
  div[data-testid="stDownloadButton"] button:hover {
    opacity: 0.85;
    color: #f0f2f8 !important;
  }

  /* ── PROJECT REPO LINK ── */
  .tl-link {
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    color: #6c74e8;
    text-decoration: none;
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    margin-top: 0.65rem;
    padding-top: 0.65rem;
    border-top: 1px solid #1e2130;
    width: 100%;
    transition: color 0.2s;
  }
  .tl-link:hover { color: #4ade80; }

  /* hide streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  .stDeployButton { display: none; }
</style>
""", unsafe_allow_html=True)


# ── HERO ────────────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  {get_avatar_html()}
  <div class="hero-text">
    <div class="hero-eyebrow">◈ Engenharia de Dados</div>
    <div class="hero-name">Gustavo <span>Piccinini</span></div>
    <div class="hero-role">Engenheiro de Dados · Full Stack Data & Analytics PoD Academy · Ourinhos, SP</div>
    <div class="hero-links">
      <a class="hero-link" href="mailto:gusaugusto@outlook.com">✉ gusaugusto@outlook.com</a>
      <a class="hero-link" href="tel:+5514998207736">☎ (14) 99820-7736</a>
      <a class="hero-link" href="https://www.linkedin.com/in/gustavoapiccinini" target="_blank">
        <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667h-3.554v-11.452h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zm-15.117-13.019c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019h-3.564v-11.452h3.564v11.452zm16.545-20.452h-20.454c-.979 0-1.771.774-1.771 1.729v20.542c0 .956.792 1.729 1.771 1.729h20.451c.978 0 1.778-.773 1.778-1.729v-20.542c0-.955-.8-1.729-1.778-1.729z"/></svg>
        LinkedIn
      </a>
      <a class="hero-link" href="https://github.com/GustavoPiccinini" target="_blank">
        <svg viewBox="0 0 24 24" fill="currentColor" xmlns="http://www.w3.org/2000/svg"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.605-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
        GitHub
      </a>
      <a class="hero-link" href="https://github.com/GustavoPiccinini/oracle-certificados" target="_blank">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>
        Certificados
      </a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

if RESUME_PDF_PATH.exists():
    with open(RESUME_PDF_PATH, "rb") as f:
        st.download_button(
            label="⬇  Baixar currículo em PDF",
            data=f,
            file_name="Gustavo_Piccinini_Curriculo.pdf",
            mime="application/pdf",
        )

# ── LAYOUT PRINCIPAL ─────────────────────────────────────────────────────────
col_main, col_side = st.columns([3, 2], gap="large")

with col_main:

    # ABOUT
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">Sobre</span>
      <div class="sec-line"></div>
    </div>
    <div class="about-box">
      Profissional de dados em formação Full Stack em Dados e Analytics na PoD Academy, com atuação prática em Engenharia,
      de Dados. Tenho vivência com arquitetura medalhão (Bronze, Silver, Gold) em PySpark e Airflow,Data Lakes na AWS, GCP e OCI, e SQL.
      Atualmente desenvolvo e mantenho um dashboard de gestão no setor assistência social (CadÚnico/Bolsa Família) usando DuckDB, Pandas e Streamlit.
      Atuação na área financeira, permitiu uma visão de negócio aplicada à resolução de problemas como inadimplência e risco de crédito.
    </div>
    """, unsafe_allow_html=True)

    # PROJETOS
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">Projetos</span>
      <div class="sec-line"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("".join(render_project_card(p) for p in PROJECTS), unsafe_allow_html=True)

with col_side:

    # STACK
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">Linguagens e Habilidades</span>
      <div class="sec-line"></div>
    </div>
    <div class="skill-grid">
      <div class="skill-card">
        <div class="skill-cat">Engineering</div>
        <div class="badge-row">
          <span class="badge b-violet">PySpark</span>
          <span class="badge b-violet">Airflow</span>
          <span class="badge b-violet">ETL/ELT</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Cloud & Infra</div>
        <div class="badge-row">
          <span class="badge b-green">AWS</span>
          <span class="badge b-green">GCP</span>
          <span class="badge b-green">OCI</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Data & Analytics</div>
        <div class="badge-row">
          <span class="badge b-sky">SQL</span>
          <span class="badge b-sky">DuckDB</span>
          <span class="badge b-sky">Streamlit</span>
          <span class="badge b-sky">Plotly</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Languages</div>
        <div class="badge-row">
          <span class="badge b-amber">Python</span>
          <span class="badge b-amber">SQL</span>
          <span class="badge b-amber">Rust (em estudo)</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Dev Tools</div>
        <div class="badge-row">
          <span class="badge b-pink">VS Code</span>
          <span class="badge b-pink">uv</span>
          <span class="badge b-pink">Git / GitHub</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Practices</div>
        <div class="badge-row">
          <span class="badge b-sky">LGPD</span>
          <span class="badge b-sky">Data Lake</span>
          <span class="badge b-sky">Modelagem Dimensional</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # EXPERIÊNCIAS
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">Experiências</span>
      <div class="sec-line"></div>
    </div>
    
    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">Hackathon PoD Academy - Claro</div>
        <div class="tl-period">2026</div>
      </div>
      <div class="tl-company">Lider da equipe de Engenharia de Dados</div>
      <div class="tl-desc">
        Liderança da equipe de engenharia de dados responsavel pela criação do Data Lake,Pipelines e ETL com PySpark para 
        processando milhões de linhas em OCI (~1h30 de execução, custo de ~R$ 100/mês).
      </div>
      <div class="badge-row">
        <span class="badge b-violet">PySpark</span>
        <span class="badge b-green">OCI</span>
      </div>
    </div>

     <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">Engenheiro de Dados — Hackathon 4C Digital</div>
        <div class="tl-period">2026</div>
      </div>
      <div class="tl-company">Fintech de Cobrança Digital</div>
      <div class="tl-desc">
        Pipeline com arquitetura medalhão (Bronze/Silver/Gold) usando PySpark e Airflow,
        substituindo processo defasado e manual.Orquestração de DAGs de ponta a ponta.
      </div>
      <div class="badge-row">
        <span class="badge b-violet">PySpark</span>
        <span class="badge b-amber">Airflow</span>
      </div>
    </div>                       
                
    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">Engenheiro de Dados</div>
        <div class="tl-period">2026 – Atual</div>
      </div>
      <div class="tl-company">Prefeitura de Jacarezinho — Assistência Social</div>
      <div class="tl-desc">
        Desenvolvimento e manutenção de dashboard para gestão de atendimentos,
        integrando CadÚnico e Bolsa Família(dados do Governo Federal). Pipeline com DuckDB e Pandas, focando na monitoria, integridade e linhagem dos dados.
        Visualizações interativas com Plotly.
      </div>
      <div class="badge-row">
        <span class="badge b-violet">Python</span>
        <span class="badge b-sky">DuckDB</span>
        <span class="badge b-green">Streamlit</span>
      </div>
    </div>

    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">Administrador e Gestor Financeiro</div>
        <div class="tl-period">2015 – Atual</div>
      </div>
      <div class="tl-company">Piccinini Saúde Ocupacional</div>
      <div class="tl-desc">
        Gestão financeira e desenvolvimento de dashboards e automações para controle
        de custos e relatórios gerenciais.
      </div>
      <div class="badge-row">
        <span class="badge b-sky">Excel</span>
        <span class="badge b-amber">Gestão</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # EDUCAÇÃO
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">Formações</span>
      <div class="sec-line"></div>
    </div>

    <div class="mini-card">
      <div class="mini-title">Full Stack em Dados e Analytics</div>
      <div class="mini-sub">PoD Academy · 2026</div>
      <div class="mini-desc">Formação completa cobrindo Engenharia de dados, Análise, Ciência de Dados e IA.</div>
    </div>

    <div class="mini-card">
      <div class="mini-title">Ciência de Dados</div>
      <div class="mini-sub">FATEC Ourinhos · em andamento, previsão julho/2027</div>
      <div class="mini-desc"></div>
    </div>

    <div class="mini-card">
      <div class="mini-title">Administração</div>
      <div class="mini-sub">UNICENTRO · 2006</div>
      <div class="mini-desc"></div>
    </div>

    <div class="mini-card">
      <div class="mini-title">Técnico em Edificações</div>
      <div class="mini-sub">ETEC Ourinhos · 2020</div>
      <div class="mini-desc"></div>
    </div>

    <div class="mini-card">
      <div class="mini-title">Engenharia Civil</div>
      <div class="mini-sub">Estácio de Sá Ourinhos · 2018</div>
      <div class="mini-desc"></div>
    </div>
    """, unsafe_allow_html=True)

    # IDIOMAS
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">Idiomas</span>
      <div class="sec-line"></div>
    </div>
    <div class="mini-card">
      <div class="badge-row">
        <span class="badge b-green">🇧🇷 Português — Nativo</span>
        <span class="badge b-sky">🇺🇸 Inglês — Fluente</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
