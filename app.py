import streamlit as st

st.set_page_config(
    page_title="Gustavo | Full Stack Data & Analytics",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="collapsed",
)

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
    padding: 2.8rem 0 2rem 0;
    border-bottom: 1px solid #1e2130;
    margin-bottom: 2.5rem;
  }
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
    font-size: 3rem;
    font-weight: 600;
    color: #f0f2f8;
    line-height: 1.1;
    margin: 0 0 0.4rem 0;
  }
  .hero-name span {
    color: #6c74e8;
  }
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
st.markdown("""
<div class="hero">
  <div class="hero-eyebrow">◈ Full Stack Data & Analytics</div>
  <div class="hero-name">Gustavo <span>[Sobrenome]</span></div>
  <div class="hero-role">Data Engineering · Analytics · AI Solutions · São Paulo, BR</div>
  <div class="hero-links">
    <a class="hero-link" href="mailto:seuemail@email.com">✉ seuemail@email.com</a>
    <a class="hero-link" href="https://linkedin.com/in/seu-perfil" target="_blank">↗ linkedin.com/in/seu-perfil</a>
    <a class="hero-link" href="https://github.com/seu-usuario" target="_blank">⌥ github.com/seu-usuario</a>
  </div>
</div>
""", unsafe_allow_html=True)


# ── KPI CARDS ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="kpi-row">
  <div class="kpi-card">
    <div class="kpi-value">X+</div>
    <div class="kpi-label">Anos de experiência</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-value">60M+</div>
    <div class="kpi-label">Registros em produção</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-value">N</div>
    <div class="kpi-label">Pipelines entregues</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-value">3</div>
    <div class="kpi-label">Domínios: eng · analytics · AI</div>
  </div>
</div>
""", unsafe_allow_html=True)



    # ── LAYOUT PRINCIPAL ────────────────────────────────────────────────────────
col_main, col_side = st.columns([3, 2], gap="large")

with col_main:

    # ABOUT
    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">about</span>
      <div class="sec-line"></div>
    </div>

    <div class="about-box">
      Estudante de Ciência de Dados e Engenharia de Dados, graduado em Administração.
      Desenvolvo projetos completos envolvendo Engenharia de Dados, utilizando Python,
      SQL, PySpark, Apache Airflow, PostgreSQL, Docker e Streamlit. Possuo experiência prática com arquiteturas
      Data Lake (Bronze, Silver e Gold), Data Warehouse, processamento distribuído e soluções em AWS, Google Cloud
      Platform (GCP) e Oracle Cloud Infrastructure (OCI).
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
        <div class="tl-title">Rust + PySpark LGPD Anonymizer</div>
        <div class="tl-period">Open Source</div>
      </div>
      <div class="tl-company">github.com/seu-usuario/lgpd-anonymizer</div>
      <div class="tl-desc">
        Binário Rust integrado a pipeline PySpark/Airflow para anonimização de dados sensíveis
        conforme LGPD — hashing de CPF e mascaramento de nomes com performance nativa.
        MVP completo empacotado para deploy no GCP.
      </div>
      <div class="badge-row">
        <span class="badge b-amber">Rust</span>
        <span class="badge b-violet">PySpark</span>
        <span class="badge b-green">LGPD</span>
        <span class="badge b-pink">Privacy Engineering</span>
      </div>
    </div>

    <div class="tl-card">
      <div class="tl-top">
        <div class="tl-title">AI Credit & Collections Platform</div>
        <div class="tl-period">Hackathon</div>
      </div>
      <div class="tl-company">Setor de crédito e cobrança digital · 60M+ registros</div>
      <div class="tl-desc">
        Arquitetura de solução de IA end-to-end: credit scoring, agente LLM para
        negociação inteligente de dívidas e detecção de fraude. Pipeline de dados
        modernizado para suportar serviços de IA em produção.
      </div>
      <div class="badge-row">
        <span class="badge b-pink">LLM</span>
        <span class="badge b-violet">ML</span>
        <span class="badge b-green">Fraud Detection</span>
        <span class="badge b-sky">Credit Scoring</span>
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
          <span class="badge b-violet">dbt</span>
          <span class="badge b-violet">Kafka</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Cloud & Infra</div>
        <div class="badge-row">
          <span class="badge b-green">GCP</span>
          <span class="badge b-green">BigQuery</span>
          <span class="badge b-green">Docker</span>
          <span class="badge b-green">Terraform</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Analytics</div>
        <div class="badge-row">
          <span class="badge b-sky">SQL</span>
          <span class="badge b-sky">Power BI</span>
          <span class="badge b-sky">Looker</span>
          <span class="badge b-sky">Streamlit</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">AI & ML</div>
        <div class="badge-row">
          <span class="badge b-pink">LLM</span>
          <span class="badge b-pink">MLflow</span>
          <span class="badge b-pink">Scikit-learn</span>
          <span class="badge b-pink">LangChain</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Languages</div>
        <div class="badge-row">
          <span class="badge b-amber">Python</span>
          <span class="badge b-amber">SQL</span>
          <span class="badge b-amber">Rust</span>
          <span class="badge b-amber">Bash</span>
        </div>
      </div>
      <div class="skill-card">
        <div class="skill-cat">Practices</div>
        <div class="badge-row">
          <span class="badge b-sky">CI/CD</span>
          <span class="badge b-sky">DataOps</span>
          <span class="badge b-sky">LGPD</span>
          <span class="badge b-sky">Agile</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # EXPERIÊNCIA

    st.markdown("""
    <div class="sec-header">
      <span class="sec-mono">experience</span>
      <div class="sec-line"></div>
    </div>

    <div class="tl-card">

      <div class="tl-top">
        <div class="tl-title">
            Engenheiro de Dados (Projeto Acadêmico)
        </div>

        <div class="tl-period">
            2025 – Atual
        </div>

      </div>

      <div class="tl-company">
          PoD Academy
      </div>

      <div class="tl-desc">

        Participação no Hackathon Oracle promovido pela PoD Academy, com foco no desenvolvimento de soluções de Engenharia de Dados para análise de crédito. 
        Desenvolvimento de pipelines ETL utilizando Python e PySpark para processamento distribuído de grandes volumes de dados, aplicando arquitetura Data Lake (Bronze, Silver e Gold), modelagem analítica e construção de Book de Variáveis para identificação de clientes adimplentes e inadimplentes. 
        Experiência prática com Oracle Cloud Infrastructure (OCI), utilizando Data Flow, Object Storage e integração entre serviços para processamento e armazenamento de dados em ambiente de nuvem.


      </div>

      <div class="badge-row">

        <span class="badge b-violet">Python</span>
        <span class="badge b-violet">PySpark</span>
        <span class="badge b-sky">SQL</span>
        <span class="badge b-green">OCI</span>
        <span class="badge b-amber">Airflow</span>
        <span class="badge b-sky">Docker</span>

      </div>

    </div>


    <div class="tl-card">

      <div class="tl-top">

        <div class="tl-title">
            Participante – Hackathon Engenharia de Dados
        </div>

        <div class="tl-period">
            2026
        </div>

      </div>

      <div class="tl-company">
          4C Soluções Inteligentes
      </div>

      <div class="tl-desc">

        Desenvolvimento colaborativo de soluções de Engenharia de Dados para automação de processos,
        arquitetura de dados e integração de informações utilizando metodologia Scrum,
        com foco em escalabilidade e boas práticas de desenvolvimento.

      </div>

      <div class="badge-row">

        <span class="badge b-violet">Python</span>
        <span class="badge b-green">Data Lake</span>
        <span class="badge b-amber">Scrum</span>
        <span class="badge b-sky">ETL</span>
        <span class="badge b-violet">Arquitetura de Dados</span>

      </div>

    </div>



    <div class="tl-card">

      <div class="tl-top">

        <div class="tl-title">
            Administrador
        </div>

        <div class="tl-period">
            2010 – 2025
        </div>

      </div>

      <div class="tl-company">
          Empresa Familiar
      </div>

      <div class="tl-desc">

       Responsável pela gestão administrativa e financeira da empresa, acompanhando indicadores de desempenho e apoiando a tomada de decisão baseada em dados. 
       Desenvolvimento de automações para otimização de processos utilizando Excel, VBA e Power BI, reduzindo atividades manuais
       padronizando controles e aumentando a eficiência operacional por meio da análise e visualização de dados.

      </div>

      <div class="badge-row">

        <span class="badge b-violet">Excel</span>
        <span class="badge b-sky">VBA</span>
        <span class="badge b-green">Power BI</span>
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
      <div class="mini-title">Full Stack em Data & Analytics</div>
      <div class="mini-sub">Pod Academy · Em andamento</div>
      <div class="mini-desc">Formação completa cobrindo engenharia de dados, analytics e IA.</div>
    </div>

    <div class="mini-card">
      <div class="mini-title">Ciência de Dados</div>
      <div class="mini-sub">Fatec · 2027</div>
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
        <span class="badge b-sky">🇺🇸 Inglês — [Nível]</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
