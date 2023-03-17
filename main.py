from cpf_cnpj import Documento, DocCpf, DocCnpj

documento_digitado = input("Digite o CPF ou CNPJ para validação: ")
documento = Documento.cria_documento(documento_digitado)

print(f'o Documento {documento} é valido')