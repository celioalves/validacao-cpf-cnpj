# validacao-cpf-cnpj

---

### Como funciona?
---

##### Basta fazer o download do projeto, e executar (run) o arquivo main.py. </br>
##### No input, ele pedirá para que você digite um documento, podendo ser um CPF ou CNPJ, após, fará a validação do mesmo.

</br></br></br></br>
Por debaixo dos panos: </br>
No arquivo cpf_cnpj fora feita a utilização da biblioteca validate_docbr. </br>
À partir do momento que é digitado um documento, ele fara a distinção. Se o documento tiver 11 dígitos, entenderá como sendo um CPF. Já, se possuir 14 dígitos, entenderá como sendo um CNPJ.</br>
Se o documento digitado não possuir uma dessas quantidades, levantará um erro "documento(cpf ou cnpj) inválido.</br>
</br> Assim, ele começa a validação usando a biblioteca citada.</br>
</br> Se positiva, a validação, devolverá o documento formatado pelo uso de uma máscara.
</br> No caso do CPF: xxx.xxx.xxx-xx
</br> No caso do CNPJ xx.xxx.xxx/xxxx-xx

