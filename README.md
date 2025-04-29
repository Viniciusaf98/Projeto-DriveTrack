
# 📊 Controle Financeiro para Motoristas de Aplicativo

## 📌 Objetivo

Este é um sistema completo de controle financeiro desenvolvido em **Python** para motoristas de aplicativo. Seu objetivo é registrar, calcular e exibir métricas financeiras diárias com base nos dados de trabalho do motorista. Ele foi criado para ser uma alternativa personalizada e funcional ao uso de planilhas ou aplicativos genéricos, oferecendo praticidade, clareza e flexibilidade nas análises.

---

## 🧠 Sobre o Projeto

Sempre utilizei planilhas ou aplicativos para acompanhar meus ganhos como motorista de aplicativo, mas nenhum deles atendia completamente às minhas necessidades. Por isso, resolvi desenvolver minha própria solução — e hoje posso dizer que ela está exatamente como eu queria.

Este projeto foi criado para uso pessoal, mas estou compartilhando aqui no GitHub por dois motivos:

1. Para demonstrar alguns dos conhecimentos que possuo em Python;
2. Caso outro motorista ou desenvolvedor deseje utilizar ou adaptar o programa para suas próprias metas.

---

![ChatGPT Image 29 de abr  de 2025, 02_45_45](https://github.com/user-attachments/assets/67998386-6cde-4323-b61d-a1e0db862822)

## 🏗️ Arquitetura do Projeto

O projeto possui duas funcionalidades principais:

### 1. Registro de Dados Diários
- Coleta informações do dia como:
  - Faturamento
  - Gastos (combustível)
  - Horas trabalhadas
  - Corridas realizadas
  - Quilometragem rodada
- Calcula automaticamente:
  - Lucro do dia
  - Ticket médio bruto (faturamento / corridas)
  - Ticket médio de lucro (lucro / corridas)
- Salva os dados em um arquivo `.json`, nomeado com a data, dentro de uma pasta criada automaticamente no diretório do usuário.

### 2. Consulta de Dados
Permite consultar os dados registrados de forma detalhada:
- **Por Dia**: Faturamento, lucro, corridas, KM, tickets médios e feedback (com base em metas pessoais).
- **Por Semana/Mês/Ano**:
  - Exibe os dados diários coletados
  - Exibe totais de: faturamento, lucro, corridas e KM
  - Exibe médias por dia de faturamento e lucro
  - Exibe ticket médio bruto e de lucro

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**

---

## 📦 Bibliotecas Utilizadas

- `os` – Manipulação de diretórios
- `json` – Leitura e gravação de arquivos de dados
- `datetime` – Manipulação de datas
- `calendar` – Cálculo de semanas e meses

---

## 📋 Protocolo de Comandos

### Menu Principal:
```
1 - Registrar novo dia
2 - Consultar dados (dia, semana, mês ou ano)
0 - Sair
```

### Consulta de dados:
```
1 - Por dia
2 - Por semana
3 - Por mês
4 - Por ano
```

---

## ▶️ Uso e Execução

1. Clone o repositório:
```bash
git clone https://github.com/Viniciusaf98/Projeto-DriveTrack.git
```

2. Execute o script Python:
```bash
python controle_financeiro.py
```

3. Siga as instruções no terminal para registrar dados ou realizar consultas.

---

