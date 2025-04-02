# 🔹 CI (Continuous Integration) no GitHub Actions para Machine Learning

Este repositório utiliza **GitHub Actions** para automatizar o processo de **CI (Continuous Integration)**, garantindo qualidade e confiabilidade no desenvolvimento do projeto de **Machine Learning**.

## 📌 O que é CI (Continuous Integration)?
O CI garante que o código está sempre funcionando corretamente ao rodar testes automaticamente a cada mudança no repositório.

No **GitHub Actions**, um workflow de CI normalmente faz:
✅ **Checkout do código** (pegar a versão mais recente do repositório).  
✅ **Rodar linter e formatador** (garante que o código segue um padrão, ex: `black`, `flake8`).  
✅ **Executar testes automatizados** (testa se tudo está funcionando, ex: `pytest`).  
✅ **Verificar dependências** (instala pacotes e verifica se tudo roda certo).  
✅ **Construir a aplicação** (garante que o código pode ser empacotado, por exemplo, em um container Docker).  

## 🛠 **Como isso se aplica ao projeto de ML?**
No projeto de **Machine Learning**, o CI pode ser usado para:
- Testar os modelos antes de subi-los para produção.
- Garantir que o código da **API FastAPI** e os scripts do **MLflow** estão funcionando corretamente.
- Rodar testes automatizados em funções de pré-processamento, modelos e APIs de inferência.

📌 **Na prática**, o workflow de CI (`.github/workflows/ci.yaml`) roda sempre que há um `push` ou `pull request`, verificando a qualidade do código e rodando os testes antes de permitir mudanças no repositório principal.

## 🚀 Benefícios do CI
✅ **Automação** → Menos erros manuais e mais velocidade no desenvolvimento.  
✅ **Confiabilidade** → O código sempre passa por testes antes de ser integrado.  
✅ **Menos tempo corrigindo bugs** → Testes automatizados evitam problemas em produção.  

Com esse setup, sempre que o código for ajustado, ele será testado automaticamente, garantindo que tudo funcione corretamente antes de ser integrado ao projeto. 🔥

---

### 📜 Exemplo de Workflow:
- **CI:** `.github/workflows/ci.yaml`
