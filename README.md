# Currículo Interativo — Gustavo Piccinini

App Streamlit para demonstrar meu perfil de Engenharia de Dados.

## Rodando localmente com `uv` (VS Code)

```bash
# 1. Criar o ambiente virtual
uv venv

# 2. Ativar (Windows)
.venv\Scripts\activate
# Ativar (Mac/Linux)
source .venv/bin/activate

# 3. Instalar dependências
uv pip install -r requirements.txt

# 4. Rodar o app
uv run streamlit run app.py
```

No VS Code: abra a pasta, selecione o interpretador do `.venv` (Ctrl+Shift+P → "Python: Select Interpreter"), e rode `uv run streamlit run app.py` no terminal integrado.

## Adicionando sua foto

Coloque um arquivo `foto.jpg` (ou `.png`) dentro da pasta `assets/`. O app detecta automaticamente e exibe em formato circular. Sem foto, ele mostra um avatar com as iniciais "GP".

## Publicando (Streamlit Community Cloud — grátis)

1. Suba esta pasta para um repositório no GitHub (ex.: `curriculo-streamlit`).
2. Acesse [share.streamlit.io](https://share.streamlit.io), conecte sua conta GitHub.
3. Selecione o repositório, branch `main` e o arquivo `app.py`.
4. Deploy. Você recebe uma URL pública, algo como:
   `https://gustavopiccinini-curriculo.streamlit.app`

## Usando para demonstrar o currículo

- **LinkedIn:** adicione o link na seção "Destaques" (Featured) do seu perfil, ou na descrição "Sobre". Também pode colocar como o link do seu site pessoal nas configurações do perfil.
- **Candidaturas:** envie o link direto no e-mail ou mensagem para o recrutador junto com o PDF tradicional — o app funciona como complemento visual, não substituto do PDF (alguns ATS só aceitam PDF/DOCX).
- **Assinatura de e-mail / cartão de visita digital:** inclua a URL curta.
- Gere um QR code da URL (ex. no site qr-code-generator.com) para colocar no currículo em PDF, permitindo que o recrutador escaneie e veja a versão interativa.
