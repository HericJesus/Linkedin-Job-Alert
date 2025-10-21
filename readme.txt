# 🚀 LinkedIn Job Alert

Automação em Python para buscar vagas no **LinkedIn**, filtrá-las por critérios personalizados e armazenar as informações localmente.  
O projeto utiliza **Selenium** para a automação do navegador e **Tkinter** para a interface gráfica de login.

---

## 🧠 Funcionalidades

- 🔐 Janela de login com Tkinter (entrada de e-mail e senha do LinkedIn, Cargo, Localização)
- 🌐 Acesso automático ao LinkedIn com Selenium
- 🔎 Busca de vagas conforme filtros definidos (cargo, localização, tipo de vaga, etc.)
- 💾 Armazenamento dos resultados em planilha Excel (`.xlsx`)
- ⚙️ Estrutura modular e fácil de expandir (cada parte em um arquivo: `credentials.py`, `login.py`, `pesquisa.py`, etc.)
- 🧩 Código pronto para empacotamento em `.exe` via **PyInstaller**

---

## 🧰 Tecnologias utilizadas

| Ferramenta | Descrição |
|-------------|------------|
| 🐍 Python 3.x | Linguagem principal |
| 🧠 Tkinter | Interface gráfica para login |
| 🌍 Selenium | Automação do navegador |
| 📊 Pandas / OpenPyXL | Manipulação e exportação de dados |
| 🧱 PyInstaller | Geração de executável standalone |
| 💻 ChromeDriver | Driver utilizado pelo Selenium |

---

## 📂 Estrutura do projeto

Linkedin Job Alert/
│
├── main.py # Arquivo principal - executa o fluxo completo
├── credentials.py # Interface Tkinter para login e senha
├── login.py # Realiza o login no LinkedIn via Selenium
├── pesquisa.py # Pesquisa e coleta das vagas
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── venv/ # Ambiente virtual (não subir para o GitHub)

⚠️ Observações importantes

O uso de automação no LinkedIn deve respeitar os Termos de Uso da plataforma.

É recomendado limitar a frequência de buscas e logins automáticos para evitar bloqueios.

Configure corretamente o ChromeDriver compatível com a sua versão do Chrome.

As credenciais não devem ser armazenadas em texto plano — o projeto pode ser estendido para usar criptografia.

📈 Próximos passos

 Implementar filtro por data da vaga e nível de experiência

 Adicionar logs e tratamento de erros

 Salvar histórico de vagas aplicadas

 Integração com e-mail para alertas automáticos

👨‍💻 Autor

Heric Gonçalves de Jesus
📍 São José dos Pinhais – PR
📧 heric.sjp@hotmail.com
🔗 https://www.linkedin.com/in/heric-goncalves-de-jesus/