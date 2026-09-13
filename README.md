# 🛍️ Sistema de PDV e Descontos - Lojas Phenix

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)
![GitHub](https://img.shields.io/badge/GitHub-Repo-181717?style=for-the-badge&logo=github&logoColor=white)

---

## 📌 Sobre o Projeto
O **Sistema de PDV (Ponto de Venda) - Lojas Phenix** é um programa desenvolvido em Python para automatizar o cálculo de descontos progressivos em compras de acordo com o valor total final.

---

## 🎯 Objetivos
* Solicitar ao usuário o valor total das compras.
* Identificar e aplicar automaticamente a faixa de desconto correspondente.
* Exibir a porcentagem de desconto, o valor em reais descontado e o preço final.
* Apresentar mensagens formatadas no terminal com destaque visual.

---

## 🛠️ Linguagem Utilizada
* **Python 3** — Linguagem principal de desenvolvimento.

---

## 🧮 Regras de Desconto e Fórmula Utilizada

### Tabela de Descontos Progressivos
* **Compras abaixo de R$ 200,00:** 5% de desconto (`0.05`)
* **Compras de R$ 200,00 até R$ 299,99:** 10% de desconto (`0.10`)
* **Compras de R$ 300,00 ou mais:** 15% de desconto (`0.15`)

### Fórmula do Cálculo
$$\text{Valor Final} = \text{Preço} \times (1 - \text{Taxa de Desconto})$$

$$\text{Valor do Desconto} = \text{Preço} \times \text{Taxa de Desconto}$$

---

## 🚀 Como Executar o Programa

1. Certifique-se de ter o **Python 3** instalado em seu computador.
2. Faça o download do arquivo `pdv_1.0.py`.
3. Abra o terminal na pasta onde o arquivo foi salvo.
4. Execute o comando:

```bash
python Rafael_Ag6_DS_I.py