# 🚀 GUIA RÁPIDO - Como Rodar o AgroVision AI

## Para o Professor Testar

### ⚡ Forma Mais Rápida (Recomendado)

#### 1️⃣ No Windows (PowerShell ou CMD):
```bash
cd C:\Users\[seu-usuario]\Facul\POC\POC_AgroVision-AI
python -m streamlit run src/app.py
```

#### 2️⃣ No macOS/Linux (Terminal):
```bash
cd ~/Facul/POC/POC_AgroVision-AI
python3 -m streamlit run src/app.py
```

---

### 📋 Passos Detalhados (Se não tiver Python instalado)

#### Windows:

1. **Instalar Python 3.13+**
   - Baixe em: https://www.python.org/downloads/
   - ⚠️ MARQUE: "Add Python to PATH"

2. **Abrir PowerShell/CMD na pasta do projeto**
   ```bash
   cd C:\Users\[seu-usuario]\Facul\POC\POC_AgroVision-AI
   ```

3. **Criar ambiente virtual**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Rodar a aplicação**
   ```bash
   python -m streamlit run src/app.py
   ```

#### macOS/Linux:

1. **Instalar Python (se não tiver)**
   ```bash
   # macOS (usando Homebrew)
   brew install python@3.13
   
   # Ubuntu/Debian
   sudo apt-get install python3.13 python3.13-venv
   ```

2. **Navegar para a pasta**
   ```bash
   cd ~/Facul/POC/POC_AgroVision-AI
   ```

3. **Criar ambiente virtual**
   ```bash
   python3.13 -m venv venv
   source venv/bin/activate
   ```

4. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Rodar**
   ```bash
   python3 -m streamlit run src/app.py
   ```

---

## 🌐 Acessar a Aplicação

Após rodar um dos comandos acima, você verá no terminal:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.x:8501
```

A aplicação abrirá automaticamente! Se não, abra no navegador:
👉 http://localhost:8501

---

## 🧪 Testando a Aplicação

1. **Clique em "Selecione uma imagem"**
2. **Escolha uma foto de planta** (JPG ou PNG)
3. **Clique em "🚀 ANALISAR PLANTA"**
4. **Veja o diagnóstico instantâneo!**

---

## ✅ Checklist antes de Entregar

- [ ] Python 3.8+ instalado
- [ ] Pasta `POC_AgroVision-AI` clonada ou baixada
- [ ] Dependências instaladas (`requirements.txt`)
- [ ] Streamlit rodando sem erros
- [ ] Interface carrega em http://localhost:8501
- [ ] Upload de imagem funciona
- [ ] Análise retorna resultado correto

---

## 🆘 Problema? Tente Isso:

### "Module 'streamlit' not found"
```bash
pip install streamlit
```

### "Porta 8501 já está em uso"
```bash
streamlit run src/app.py --server.port 8502
```

### "Python não é reconhecido"
- Windows: Desinstale e reinstale Python com "Add to PATH" ✓
- macOS/Linux: Use `python3` em vez de `python`

### "Arquivo app.py não encontrado"
- Verifique se está na pasta correta: `POC_AgroVision-AI/`
- O arquivo deve estar em: `POC_AgroVision-AI/src/app.py`

---

## 📞 Suporte

Se precisar de ajuda, verifique:
1. README.md (documentação completa)
2. Terminal output (mensagens de erro)
3. Certifique-se que todas as dependências foram instaladas

---

**Pronto para testar! 🌿**
