from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Vanessa', idade=34)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoa = Pessoas.query.all()
    #pessoa = Pessoas.query.filter_by(nome='Tiago Chaves').first()
    #print(pessoa.idade)
    #print(pessoa.nome)
    print(pessoa)


def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Tiago Chaves').first()
    #pessoa.nome = 'Tiago Chaves'
    pessoa.idade = 22
    pessoa.save()


def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Tiago').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()

