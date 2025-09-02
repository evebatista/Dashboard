# 📊 Dashboard de Análise de Dados

Este projeto é um **Dashboard interativo** desenvolvido em **Python + Streamlit**, que permite visualizar e explorar dados de forma simples e intuitiva.  

---

## 🚀 Tecnologias Utilizadas
- Python 3.8+
- [Streamlit](https://streamlit.io/)
- Pandas
- Matplotlib / Plotly (para gráficos)

---

## 📂 Estrutura do Projeto
dashboard/
│-- app.py # Código principal do dashboard
│-- dados.csv # Base de dados usada no projeto
│-- requirements.txt # Dependências do projeto

---

## ⚙️ Como Rodar o Projeto

### 1️⃣ Clone o repositório
```bash
git clone https://github.com/seu-usuario/dashboard.git
cd dashboard
2️⃣ Crie um ambiente virtual (opcional, mas recomendado)
bash
Copiar código
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
3️⃣ Instale as dependências
bash
Copiar código
pip install -r requirements.txt
4️⃣ Rode o Streamlit
bash
Copiar código
streamlit run app.py
Se o comando acima não funcionar, rode:

bash
Copiar código
python -m streamlit run app.py

📊 Exemplo de Funcionalidades

Visualização de dados em tabelas.

Gráficos interativos (barras, pizza, dispersão).

Filtros dinâmicos para explorar os dados.

Relatórios estatísticos básicos.

