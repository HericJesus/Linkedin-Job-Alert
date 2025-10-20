from credentials import LoginWindow
from login import  login_linkedin
from search import abrir_link_vagas


if __name__ == "__main__":


# 1- Solicita email e senha de acesso ao linkedin
    janela = LoginWindow()
    email, password = janela.get_login()  # Espera o usuário digitar e clicar "Ok"

# 2- abrir google chrome
# 3- Logar no Linkedin    
    driver = login_linkedin(email, password)

# 4- Pesquisar por vagas
# 5- Salvar vagas em uma planilha
    driver = abrir_link_vagas(driver)




