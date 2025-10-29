from flask import Flask, jsonify, request
app = Flask(__name__)

playlist = [
    {"id": 1, "titulo": "Sei lá", "artista": "Sei lá", "duracao": 666, "url": "teste.com"},
    {"id": 2, "titulo": "Sei lá2", "artista": "Sei lá2", "duracao": 666, "url": "teste.com"}
]

@app.route('/tracks', methods=['GET'])
def get_musicas():
    return jsonify({"playlist":playlist, "total":len(playlist)})

@app.route('/tracks', methods=['POST'])
def add_musica():
    nova_musica = request.json
    nova_musica["id"] = len(playlist) + 1
    playlist.append(nova_musica)
    return jsonify({"mensagem": "Música adicionada!", "musica": nova_musica}), 201

@app.route("/tracks/<int:id>", methods=['GET'])
def get_musica(id):
    for musica in playlist:
        if musica["id"] == id:
            return jsonify({"mensagem": "A música foi encontrada!", "musica": musica})
    return jsonify({"Mensagem": "Música não encontrada"})

@app.route("/tracks/<int:id>", methods=['PUT'])
def update_musica(id):
    dados = request.json
    print("O id informado:", id)
    repetidor = 0
    print(playlist)
    while repetidor < len(playlist):
        print(playlist[repetidor]["id"])
        if playlist[repetidor]["id"] == id:
            playlist[repetidor].update(dados)
            return jsonify({"mensagem": "Música atualizada", "musica": playlist[repetidor]})
        repetidor += 1

    return jsonify({"erro": "Música não encontrada!"}), 404

@app.route("/tracks/<int:id>", methods=['DELETE'])
def delete_musica(id):
    repetidor = 0
    while repetidor < len(playlist):
        print(id)
        if playlist[repetidor]["id"] == id:
            print(playlist[repetidor])
            del playlist[repetidor]
            return jsonify({"mensagem": "Música deletada"})
        repetidor += 1    
    return jsonify({"erro": "Música não encontrada!"}), 404

if __name__ == "__main__":
    app.run(debug=True)