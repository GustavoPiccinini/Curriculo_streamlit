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
    color: #6c74e8;
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
    color: #8a91a8;
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
      <a class="hero-link" href="https://www.linkedin.com/in/gustavoapiccinini" target="_blank">↗ linkedin.com/in/gustavoapiccinini</a>
      <a class="hero-link" href="https://github.com/GustavoPiccinini" target="_blank">⌥ github.com/GustavoPiccinini</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── KPI CARDS ───────────────────────────────────────────────────────────────
st.markdown("""
  <div class="kpi-card">
    <div class="kpi-value">4</div>
    <div class="kpi-label">Projetos</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-value">3</div>
    <div class="kpi-label">Domínios: Engenharia de Dados · AWS · OCI · GCP · Spark · PySpark·</div>
  </div>
</div>
""", unsafe_allow_html=True)


# ── LAYOUT PRINCIPAL ─────────────────────────────────────────────────────────
col_main, col_side = st.columns([3, 2], gap="large")

with col_main:

    # ABOUT
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">about</span>
      <div class="sec-line"></div>
    </div>
    <div class="about-box">
      Profissional de dados em formação Full Stack em Dados e Analytics, com atuação prática em Engenharia,
      de Dados. Tenho vivência com arquitetura medalhão (Bronze, Silver, Gold) em PySpark e Airflow,Data Lakes na AWS, GCP e OCI, e SQL avançado.
      Atualmente desenvolvo e mantenho um dashboard de gestão no setor assistência social (CadÚnico/Bolsa Família) usando DuckDB, Pandas e Streamlit.
      Atuando na área financeira, possuo uma visão de negócio aplicada à resolução de problemas como inadimplência e risco de crédito.
    </div>
    """, unsafe_allow_html=True)

    # PROJETOS
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">projects</span>
      <div class="sec-line"></div>
    </div>

    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">Data Lake PoD Cartões</div>
        <div class="tl-period">2026</div>
      </div>
      <div class="tl-company">github.com/GustavoPiccinini/Data_Lake_PoD_Cartoes</div>
      <div class="tl-desc">
        Data Lake completo na AWS (Raw, Trusted, Refined). Processamento com PySpark, Parquet particionado no S3 e Book de
        Variáveis (U1M/U3M/U6M/U12M) para análise de inadimplência. Dashboard em Streamlit
        com DuckDB como engine de consulta.
      </div>
      <div class="badge-row">
        <span class="badge b-violet">PySpark</span>
        <span class="badge b-green">AWS S3</span>
        <span class="badge b-sky">DuckDB</span>
        <span class="badge b-amber">Streamlit</span>
      </div>
    </div>
    
    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">Pivotando o Desktop 4C Digital</div>
        <div class="tl-period">2026</div>
      </div>
      <div class="tl-company">Fintech de cobrança digital</div>
      <div class="tl-desc">
        Pipeline de dados de um DataLake com arquitetura medalhão (Bronze/Silver/Gold) em PySpark e
        Airflow, substituindo processo manual em Excel/VBA.
      </div>
      <div class="badge-row">
        <span class="badge b-violet">PySpark</span>
        <span class="badge b-green">Airflow</span>
        <span class="badge b-sky">Spark SQL</span>
        <span class="badge b-pink">Arquitetura Medalhão</span>
      </div>
    </div>            

    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">Dashboard de Atendimentos — Assistência Social</div>
        <div class="tl-period">2026 – Atual</div>
      </div>
      <div class="tl-company">Prefeitura de Jacarezinho · uso interno</div>
      <div class="tl-desc">
        Dashboard em Streamlit integrando dados do CadÚnico e Bolsa Família a partir de
        exportações de dados do Governo Federal. Monitoria, integridade e linhagem, dos dados.
      </div>
      <div class="badge-row">
        <span class="badge b-sky">DuckDB</span>
        <span class="badge b-violet">Pandas</span>
        <span class="badge b-amber">Streamlit</span>
        <span class="badge b-pink">Dados Públicos</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_side:

    # STACK
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">tech stack</span>
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
      <div class="tl-company">Empresa de Cobrança Digital</div>
      <div class="tl-desc">
        Pipeline com arquitetura medalhão (Bronze/Silver/Gold) usando PySpark e Airflow,
        substituindo processo manual em Excel/VBA. Orquestração de DAGs de ponta a ponta.
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
      <span class="sec-mono">education</span>
      <div class="sec-line"></div>
    </div>

    <div class="mini-card">
      <div class="mini-title">Full Stack em Dados e Analytics</div>
      <div class="mini-sub">PoD Academy · 2026</div>
      <div class="mini-desc">Formação completa cobrindo engenharia de dados, analytics e IA.</div>
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
    """, unsafe_allow_html=True)

    # IDIOMAS
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">languages</span>
      <div class="sec-line"></div>
    </div>
    <div class="mini-card">
      <div class="badge-row">
        <span class="badge b-green">🇧🇷 Português — Nativo</span>
        <span class="badge b-sky">🇺🇸 Inglês — Fluente</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
