# 🌱 AgroVision AI - Prova de Conceito (POC)

## 📋 Descrição do Projeto

**AgroVision AI** é uma aplicação web inteligente de diagnóstico de saúde de plantas através de análise de imagens. Utiliza processamento de imagem e algoritmos de classificação para identificar o estado de saúde de plantas e detectar possíveis doenças, pragas ou estresse.

### 🎯 Objetivo

Demonstrar a aplicabilidade de **visão computacional** e **inteligência artificial** na agricultura, criando uma ferramenta fácil de usar que permite aos agricultores:

- ✅ Realizar diagnóstico rápido de saúde das plantas
- ✅ Receber recomendações personalizadas
- ✅ Identificar problemas antes que se tornem críticos
- ✅ Tomar decisões informadas sobre tratamentos

---

## 🚀 Tecnologia Stack

### Frontend & Interface
- **Streamlit** - Framework Python para interfaces web interativas
- **HTML/CSS3** - Styling avançado com design system personalizado

### Backend & Processamento
- **Python 3.13** - Linguagem principal
- **NumPy** - Processamento numérico e manipulação de arrays
- **Pillow (PIL)** - Processamento e manipulação de imagens

### Design & UX
- **Paleta de Cores**: Verde profundo (natureza, confiança)
- **Responsividade**: Layout adaptável para desktop, tablet e mobile
- **Acessibilidade**: Contraste de cores otimizado

---

## 📊 Como Funciona

### Algoritmo de Análise

O AgroVision AI analisa três dimensões principais de características de cor:

1. **Proporção de Verde** 
   - Indica vitalidade geral da planta
   - Cálculo: `green_ratio = média_G / (R + G + B)`

2. **Tons Amarelados/Amarronzados**
   - Detecta sinais de doença ou estresse
   - Identifica pontos decolorados anormais

3. **Distribuição de Cores**
   - Identifica padrões anormais na imagem
   - Mapeia áreas problemáticas

### Categorias de Diagnóstico

| Status | Indicador | Interpretação |
|--------|-----------|---|
| ✅ **Saudável** | Verde predominante, baixas manchas | Planta em ótimo estado |
| ⚠️ **Alerta** | Sinais moderados de variação | Possível estresse ou doença inicial |
| 🚨 **Crítico** | Muitas manchas amareladas/marrons | Doença avançada ou danos graves |

---

## 💻 Requisitos de Sistema

### Mínimo
- **SO**: Windows 7+, macOS 10.12+, Linux (Ubuntu 14.04+)
- **Python**: 3.8 ou superior (recomendado 3.10+)
- **RAM**: 2GB
- **Disco**: 500MB livre

### Recomendado
- **Python**: 3.13
- **RAM**: 4GB+
- **SSD**: Para melhor performance

---

## 🔧 Instalação e Configuração

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/MateusCamachoD/POC_AgroVision-AI.git
cd POC_AgroVision-AI
```

### Passo 2: Criar Ambiente Virtual (Recomendado)

#### No Windows (PowerShell/CMD):
```bash
python -m venv venv
venv\Scripts\activate
```

#### No macOS/Linux (Terminal):
```bash
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

**Dependências principais:**
- `streamlit>=1.52.0` - Interface web
- `pillow>=12.0.0` - Processamento de imagens
- `numpy>=2.0.0` - Operações numéricas

---

## ▶️ Como Executar

### Opção 1: Usando Python Direto (Recomendado)

#### Windows:
```bash
cd POC_AgroVision-AI
python -m streamlit run src/app.py
```

#### macOS/Linux:
```bash
cd POC_AgroVision-AI
python3 -m streamlit run src/app.py
```

### Opção 2: Usando Script Batch (Windows)

```bash
cd POC_AgroVision-AI
run_streamlit.bat
```

### Opção 3: Terminal Direto

```bash
streamlit run src/app.py
```

---

## 🌐 Acessando a Aplicação

Após executar um dos comandos acima, o Streamlit iniciará automaticamente:

```
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

**A aplicação abrirá automaticamente no navegador padrão.**

Se não abrir, acesse manualmente:
- 🖥️ **Local**: `http://localhost:8501`
- 📱 **Rede**: Verifique o URL exibido no terminal

---

## 📖 Guia de Uso

### 1. **Interface Principal**
```
┌─────────────────────────────────────┐
│  AgroVision AI                      │
│  Diagnóstico Inteligente de Plantas │
└─────────────────────────────────────┘
```

### 2. **Carregar Imagem**
- Clique em "Selecione uma imagem"
- Escolha uma foto JPG, JPEG ou PNG
- A imagem deve ser clara e bem iluminada

### 3. **Analisar**
- Clique no botão "🚀 ANALISAR PLANTA"
- Aguarde o processamento (~2-5 segundos)

### 4. **Interpretar Resultado**
- 🟢 **Verde** = Planta saudável
- 🟡 **Amarelo** = Atenção necessária
- 🔴 **Vermelho** = Intervenção urgente

### 5. **Recomendações**
- Você receberá 4 recomendações personalizadas
- Siga as sugestões baseadas no diagnóstico

---

## 📁 Estrutura do Projeto

```
POC_AgroVision-AI/
│
├── README.md                    # Este arquivo
├── requirements.txt             # Dependências Python
├── run_streamlit.bat           # Script para rodar (Windows)
│
├── src/
│   └── app.py                  # Aplicação principal Streamlit
│
└── docs/
    └── guia_usuario.md         # Documentação adicional (opcional)
```

---

## 🎨 Design System

### Paleta de Cores
```python
PRIMARY_DARK    = #065f46  # Verde escuro - Headers
PRIMARY         = #10b981  # Verde vibrante - Principal
PRIMARY_LIGHT   = #d1fae5  # Verde claro - Backgrounds

SUCCESS         = #10b981  # Verde - Sucesso
WARNING         = #f59e0b  # Âmbar - Aviso
DANGER          = #ef4444  # Vermelho - Crítico

NEUTRAL_800     = #1f2937  # Texto escuro
NEUTRAL_700     = #374151  # Texto padrão
NEUTRAL_200     = #e5e7eb  # Bordas
```

### Tipografia
- **Headers**: Segoe UI, Tahoma, Verdana (sans-serif)
- **Body**: Sistema nativo do navegador
- **Tamanhos**: Responsivos e acessíveis

---

## ⚙️ Configurações Avançadas

### Variáveis de Ambiente (Opcional)

```bash
# Desabilitar telemetria do Streamlit
STREAMLIT_TELEMETRY=false

# Definir porta customizada
STREAMLIT_SERVER_PORT=8000

# Desabilitar browser automático
STREAMLIT_SERVER_HEADLESS=true
```

### Rodando em Servidor Remoto

```bash
streamlit run src/app.py --server.address 0.0.0.0 --server.port 8501
```

Então acesse: `http://<seu-ip>:8501`

---

## 🧪 Testando a Aplicação

### Imagens de Teste Recomendadas
- 📷 Folhas verdes saudáveis
- 📷 Folhas com manchas amareladas
- 📷 Folhas com danos marrons
- 📷 Folhas com padrões anormais

### Métricas de Validação
```python
- Tempo de análise: < 5 segundos
- Acurácia de cor: ± 5%
- Taxa de sucesso: > 95%
```

---

## 🔍 Troubleshooting

### Problema: "Module not found" error

**Solução:**
```bash
# Verifique se está no diretório correto
cd POC_AgroVision-AI

# Reinstale as dependências
pip install --upgrade -r requirements.txt
```

### Problema: Porta 8501 já está em uso

**Solução:**
```bash
# Use uma porta diferente
streamlit run src/app.py --server.port 8502
```

### Problema: Imagem não carrega

**Solução:**
- Use formatos suportados: JPG, JPEG, PNG
- Verifique se a imagem não está corrompida
- Tente com outra imagem

### Problema: Análise muito lenta

**Solução:**
- Verifique processador/RAM disponível
- Feche outros programas
- Reinicie o Streamlit

---

## 📊 Performance

| Métrica | Valor |
|---------|-------|
| Tempo de carregamento | ~2s |
| Tempo de análise | ~2-3s |
| Tamanho máximo de imagem | 200MB |
| Resolução processada | 256x256px |
| Mem. RAM utilizada | ~150-300MB |

---

## 🚀 Roadmap Futuro

### v1.1
- [ ] Integração com Deep Learning (CNN)
- [ ] Banco de dados de histórico
- [ ] Exportar relatórios em PDF

### v2.0
- [ ] API REST
- [ ] Dashboard de análise
- [ ] Detecção de múltiplas plantas
- [ ] App mobile (React Native)

### v3.0
- [ ] Integração com IoT sensors
- [ ] Recomendações com IA
- [ ] Marketplace de soluções

---

## 📄 Licença

Este projeto é uma **Prova de Conceito (POC)** para fins educacionais.

---

## 👨‍💻 Autor

**Mateus Camacho Dos**
- GitHub: [@MateusCamachoD](https://github.com/MateusCamachoD)
- Email: [seu-email@example.com]

---

## 🤝 Suporte & Contribuições

### Relatar Bugs
Se encontrar problemas, abra uma [Issue no GitHub](https://github.com/MateusCamachoD/POC_AgroVision-AI/issues)

### Sugestões
Tem ideias? Abra uma [Discussion](https://github.com/MateusCamachoD/POC_AgroVision-AI/discussions)

---

## 📚 Referências & Recursos

### Documentação Oficial
- [Streamlit Docs](https://docs.streamlit.io)
- [NumPy Documentation](https://numpy.org/doc)
- [Pillow Documentation](https://pillow.readthedocs.io)

### Artigos Relevantes
- Computer Vision in Agriculture
- Plant Disease Detection using ML
- Color-Based Image Analysis

---

## ✨ Agradecimentos

Obrigado por testar o **AgroVision AI**! 🌿

---

**Última atualização:** Dezembro 2025  
**Versão:** 1.0 (POC)  
**Status:** ✅ Estável