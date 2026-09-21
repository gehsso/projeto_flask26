from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def lista_aluno():
    DB_PATH = "banco_escola.db" # Caminho do arquivo
    conn = sqlite3.connect(DB_PATH) # Cria/conecta ao BD
    cursor = conn.cursor() # Cursor - "caneta" para escrever SQL
    cursor.execute('select id, nome, idade, cidade from aluno') #Executa consulta SQL
    lista = cursor.fetchall() # Retorna lista de tuplas
    return render_template('aluno/lista.html',lista=lista)


@app.route('/professor')
def lista_professor():
    DB_PATH = "banco_escola.db" # Caminho do arquivo
    conn = sqlite3.connect(DB_PATH) # Cria/conecta ao BD
    cursor = conn.cursor() # Cursor - "caneta" para escrever SQL
    cursor.execute('select id, nome, disciplina from professor') #Executa consulta SQL
    lista = cursor.fetchall() # Retorna lista de tuplas
    return render_template('professor/lista.html',lista=lista)


if __name__ == '__main__':
    app.run(debug=True)









"""



    DB_PATH = "banco_escola.db" # Caminho do arquivo
    conn = sqlite3.connect(DB_PATH) # Cria/conecta ao BD
    cursor = conn.cursor() # Cursor - "caneta" para escrever SQL
    cursor.execute('SELECT id, nome, idade, cidade FROM aluno') #Executa consulta SQL
    lista = cursor.fetchall() # Retorna lista de tuplas


lista = [
        (1, "Ana Beatriz Silva", 20, "Teresina"),
        (2, "Carlos Eduardo Lima", 22, "Parnaíba"),
        (3, "Mariana Souza", 19, "Picos"),
        (4, "Rafael Oliveira", 23, "Floriano"),
        (5, "Juliana Costa", 21, "Campo Maior"),
        (6, "Pedro Henrique", 20, "Oeiras"),
        (7, "Fernanda Gomes", 18, "Piripiri"),
        (8, "Lucas Almeida", 22, "Altos"),
        (9, "Bianca Rocha", 24, "Esperantina"),
        (10, "Matheus Ribeiro", 19, "Barras"),
    ]
    
    
    
    
       <table class="table table-bordered table-striped">
        <thead class="table-dark">
        <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Idade</th>
            <th>Cidade</th>
            <th>Ações</th>
        </tr>
    </thead>
    <tbody>
        {% for item in lista_alunos %}
        <tr>
            <td>{{ item[0] }}</td>
            <td>{{ item[1] }}</td>
            <td>{{ item[2] }}</td>
            <td>{{ item[3] }}</td>
            <td>
              
            </td>
        </tr>
        {% endfor %}
    </tbody>
    </table> 
    
    
context = {'msg': 'Teste', 'lista_alunos': alunos}
return render_template('aluno/lista.html', **context)


lista_alunos = [
    (1, "Ana Beatriz Silva", 20, "Teresina"),
    (2, "Carlos Eduardo Lima", 22, "Parnaíba"),
    (3, "Mariana Souza", 19, "Picos"),
    (4, "Rafael Oliveira", 23, "Floriano"),
    (5, "Juliana Costa", 21, "Campo Maior"),
    (6, "Pedro Henrique", 20, "Oeiras"),
    (7, "Fernanda Gomes", 18, "Piripiri"),
    (8, "Lucas Almeida", 22, "Altos"),
    (9, "Bianca Rocha", 24, "Esperantina"),
    (10, "Matheus Ribeiro", 19, "Barras"),
    (11, "Bruna Martins", 21, "Teresina"),
    (12, "João Vitor Nunes", 20, "Parnaíba"),
    (13, "Larissa Mendes", 22, "Picos"),
    (14, "Felipe Santos", 19, "Floriano"),
    (15, "Gabriela Lima", 23, "Campo Maior"),
    (16, "Thiago Oliveira", 20, "Oeiras"),
    (17, "Carolina Silva", 18, "Piripiri"),
    (18, "Vinícius Costa", 22, "Altos"),
    (19, "Patrícia Alves", 24, "Esperantina"),
    (20, "André Pereira", 19, "Barras"),
    (21, "Amanda Rodrigues", 21, "Teresina"),
    (22, "Bruno Carvalho", 20, "Parnaíba"),
    (23, "Cristina Santos", 22, "Picos"),
    (24, "Diego Souza", 19, "Floriano"),
    (25, "Elaine Ferreira", 23, "Campo Maior"),
    (26, "Fabrício Gomes", 20, "Oeiras"),
    (27, "Gisele Rocha", 18, "Piripiri"),
    (28, "Henrique Lima", 22, "Altos"),
    (29, "Isabela Costa", 24, "Esperantina"),
    (30, "Júlio César", 19, "Barras"),
    (31, "Letícia Martins", 21, "Teresina"),
    (32, "Marcelo Silva", 20, "Parnaíba"),
    (33, "Natália Oliveira", 22, "Picos"),
    (34, "Otávio Nunes", 19, "Floriano"),
    (35, "Priscila Santos", 23, "Campo Maior"),
    (36, "Renato Almeida", 20, "Oeiras"),
    (37, "Sandra Lima", 18, "Piripiri"),
    (38, "Tiago Pereira", 22, "Altos"),
    (39, "Valéria Costa", 24, "Esperantina"),
    (40, "Wagner Souza", 19, "Barras"),
    (41, "Aline Rodrigues", 21, "Teresina"),
    (42, "Bernardo Carvalho", 20, "Parnaíba"),
    (43, "Cássia Santos", 22, "Picos"),
    (44, "Daniel Silva", 19, "Floriano"),
    (45, "Eduarda Ferreira", 23, "Campo Maior"),
    (46, "Fábio Gomes", 20, "Oeiras"),
    (47, "Gabriel Rocha", 18, "Piripiri"),
    (48, "Helena Lima", 22, "Altos"),
    (49, "Igor Costa", 24, "Esperantina"),
    (50, "Jéssica Martins", 19, "Barras"),
    (51, "Leandro Silva", 21, "Teresina"),
    (52, "Márcia Oliveira", 20, "Parnaíba"),
    (53, "Nelson Nunes", 22, "Picos"),
    (54, "Olívia Santos", 19, "Floriano"),
    (55, "Paulo Almeida", 23, "Campo Maior"),
    (56, "Raquel Lima", 20, "Oeiras"),
    (57, "Samuel Pereira", 18, "Piripiri"),
    (58, "Tatiana Costa", 22, "Altos"),
    (59, "Ubirajara Souza", 24, "Esperantina"),
    (60, "Viviane Rodrigues", 19, "Barras"),
    (61, "Alexandre Carvalho", 21, "Teresina"),
    (62, "Bárbara Santos", 20, "Parnaíba"),
    (63, "César Silva", 22, "Picos"),
    (64, "Débora Ferreira", 19, "Floriano"),
    (65, "Eduardo Gomes", 23, "Campo Maior"),
    (66, "Francisca Rocha", 20, "Oeiras"),
    (67, "Guilherme Lima", 18, "Piripiri"),
    (68, "Iara Costa", 22, "Altos"),
    (69, "Joana Martins", 24, "Esperantina"),
    (70, "Kelvin Souza", 19, "Barras"),
    (71, "Lívia Almeida", 21, "Teresina"),
    (72, "Murilo Pereira", 20, "Parnaíba"),
    (73, "Nádia Silva", 22, "Picos"),
    (74, "Oscar Nunes", 19, "Floriano"),
    (75, "Paula Santos", 23, "Campo Maior"),
    (76, "Rogério Lima", 20, "Oeiras"),
    (77, "Sabrina Costa", 18, "Piripiri"),
    (78, "Túlio Rodrigues", 22, "Altos"),
    (79, "Ursula Carvalho", 24, "Esperantina"),
    (80, "Valentina Souza", 19, "Barras"),
    (81, "Wellington Gomes", 21, "Teresina"),
    (82, "Xuxa Silva", 20, "Parnaíba"),
    (83, "Yara Santos", 22, "Picos"),
    (84, "Zaqueu Ferreira", 19, "Floriano"),
    (85, "Amélia Rocha", 23, "Campo Maior"),
    (86, "Benedito Lima", 20, "Oeiras"),
    (87, "Cecília Costa", 18, "Piripiri"),
    (88, "Davi Martins", 22, "Altos"),
    (89, "Emília Souza", 24, "Esperantina"),
    (90, "Fernando Almeida", 19, "Barras"),
    (91, "Gustavo Pereira", 21, "Teresina"),
    (92, "Heloísa Silva", 20, "Parnaíba"),
    (93, "Ítalo Nunes", 22, "Picos"),
    (94, "Janaina Santos", 19, "Floriano"),
    (95, "Karla Lima", 23, "Campo Maior"),
    (96, "Leonardo Costa", 20, "Oeiras"),
    (97, "Michele Rodrigues", 18, "Piripiri"),
    (98, "Nathan Carvalho", 22, "Altos"),
    (99, "Olga Souza", 24, "Esperantina"),
    (100, "Pedro Paulo", 19, "Barras")
]



"""