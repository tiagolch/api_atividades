from flask import Flask, request
from flask_restful import Resource, Api
from models import *
app = Flask(__name__)
api  = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            response = {
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "id": pessoa.id
            }
        except AttributeError:
            response = {
                "Status": "Error!",
                "mensagem": "Pessoa nao encontrada."
            }
        return response


    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }
        return response


    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        mensagem = {"Status": "Sucesso",
                    "Mensagem":"{} excluido".format( pessoa.nome )}
        pessoa.delete()
        return mensagem


class ListaPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id":i.id,"nome":i.nome, "idade":i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response



class Atividade(Resource):
    def get(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        try:
            response = {
                "id": atividade.id,
                "nome": atividade.nome,
                "pessoa":atividade.pessoa.name
            }
        except AttributeError:
            response = {
                "Status": "Error!",
                "Mensagem": "Registro nao encontrado"
            }
        return response

    def put(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        dados = request.json
        if 'nome' in dados:
            atividade.nome = dados["nome"]
        if 'pessoa' in dados:
            atividade.pessoa.name = dados['pessoa']
        atividade.save()
        response = {
            "id": atividade.id,
            "nome": atividade.nome,
            "pessoa": atividade.pessoa.name
        }
        return response

    def delete(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        mensagem = "Registro '{}' excluido com sucesso".format(atividade.nome)
        atividade.delete()
        response = {
            "Status":"Concluido",
            "Mensagem": mensagem
        }
        return response



class ListaAtividades(Resource):
    def get(self):
        atividades = Atividades.query.all()
        try:
            response = [{'id':i.id, 'nome':i.nome} for i in atividades]
        except AttributeError:
            response = {
                "Status": "Error!",
                "Mensagem": "Registros nao encontrado."
            }
        return response


    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados["pessoa"]).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }
        return response

api.add_resource(Pessoa, "/pessoa/<string:nome>/")
api.add_resource(ListaPessoas, '/pessoas/')
api.add_resource(ListaAtividades, '/atividades/')
api.add_resource(Atividade, '/atividade/<int:id>/')


if __name__ == '__main__':
    app.run(debug=True)