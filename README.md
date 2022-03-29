# Manual Gerador de Carteirinhas v2

## Intro 

· O Natan fez um gerador magnífico, até com GUI, que estou com preguiça de sair modificando. E também a preguiça de ficar corrigindo os erros de engines faltando.

## Lista de alunos

· O template se encontra na mesma pasta ou no github (https://github.com/swy-326/gerador-carteirinha-2022/blob/main/alunos.xlsx) <br>

· Deve ser um arquivo .xlsx <br>

· Obrigatoriamente deve ter: nome completo do aluno; id cpe; e turno (vespertino ou noturno) <br>

· Link para foto é opcional, uma vez que podemos colar as fotos que os alunos trazem na hora da matrícula.

## Customizando

· Imagem base: as cores de ```base2.png``` está diferente de ```base.png``` pq caguei com color replace do photoshop. Mas o psd tá aí para modificar.

· Vc pode abrir em notepad, um editor de texto ou Google Colab (detalhes na seção Rodando) <br>

· Imagem base: troque o arquivo base.png para outra que vc quer. Caso mude de nome, modifique também na linha 64 do código <br>

· Tome cuidado para as dimensões da imagem, pois precisará modificar as posições x, y dos textos. (É a preguiça,  devia ter deixado relativo) <br>

· def add_text() é uma função que adiciona textos à imagem, como nome, id, turno e validade. <br>

· Para modificar fontes, é este trecho de código ```textFont = ImageFont.truetype('NotoSans-Regular.ttf', 40)```. textFont é referente às informações pessoais e validFont à validade. Foi utilizada notosans regular e de tamanho 40 e 25, respectivamente. Caso queiram mudar ou adicionar, é só colocar o nome do arquivo ttf e o novo tamanho. <br>

· Quando o nome é muito comprido (mais que 25 caracteres incluindo espaço branco), é quebrado em duas linhas. <br>

· Para mudar as posições do texto, modifique as coordenadas desta parte do código ```new_img.text((540, 443)```, onde o primeiro é coordenada x e segunda, y. <br>

· Para mudar a fonte, ```font=textFont``` troque esta parte para fonte desejada. Para isso já deve ter sido declarado nova fonte e tamanho anteriormente, como em ```textFont = ImageFont.truetype('NotoSans-Regular.ttf', 40)```. <br>

· Para mudar a cor do texto, modifique esta parte ```fill=(255,255,255)```, onde cada número representa RGB. 



## Rodando

### Direto no PC

· Precisa ter instalado python e bibliotecas utilizadas <br>

· Se não souber, faça no Colab mesmo ou me perguntem (@judyyoon) <br>

· Na linha de comando, digite <br>
```python gerador.py listaDeAlunos.xlsx``` <br>
onde ```listaDeAlunos.xlsx``` pode variar de acordo com o nome do arquivo xlsx que contém a lista de alunos

### No Google Drive

· Baixe todos os arquivos do drive ou do repositório e coloque numa pasta do GD <br>

· Em colab.research.google.com, abra o menu e procure por Arquivo -> Google Drive e selecione o arquivo ```cpe-gerador-carteirinha-2022.ipynb```<br>

· Na última linha do primeiro bloco, modifique por pasta onde se encontram todos os recursos necessários. As carteirinhas serão geradas nessa mesma pasta<br>
```os.chdir('/content/gdrive/My Drive/**MODIFIQUEAQUI**/'```

· Aperte play ▶️ no canto superior esquerdo de cada bloquinho na ordem que se encontram.<br>

· O primeiro bloco exige que vc autorize o Colab a acessar seu drive. Isso é necessário para ler os recursos e escrever as carteirinhas
