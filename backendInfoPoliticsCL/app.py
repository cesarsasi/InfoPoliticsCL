from flask import Flask, jsonify, request

app = Flask(__name__)

from documents import documents

# Testing Route
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'response': 'pong!'})

# Get Data Routes
@app.route('/documents')
def getDocuments():
    # return jsonify(documents)
    return jsonify({'documents': documents})


@app.route('/documents/<string:document_name>')
def getDocument(document_name):
    documentFound = [
        document for document in documents if document['nombre'] == document_name.lower()]
    if (len(documentFound) > 0):
        return jsonify({'document': documentFound[0]})
    return jsonify({'message': 'Document Not found'})

# Create Data Routes
@app.route('/documents', methods=['POST'])
def addDocument():
    new_document = {
        'nombre': request.json['nombre'],
        'nivel_estudios': request.json['nivel_estudios'],
        'carreras': request.json['carreras'],
        'partido': request.json['partido'],
        'comuna': request.json['comuna'],
        'region': request.json['region'],
        'cargo_actual': request.json['cargo_actual'],
        'cargos_anteriores': request.json['cargos_anteriores']
    }
    documents.append(new_document)
    return jsonify({'documents': documents})

# Update Data Route
@app.route('/documents/<string:document_name>', methods=['PUT'])
def editDocument(document_name):
    documentFound = [document for document in documents if document['nombre'] == document_name]
    if (len(documentFound) > 0):
        documentFound[0]['nombre']: request.json['nombre']
        documentFound[0]['nivel_estudios']: request.json['nivel_estudios']
        documentFound[0]['carreras']: request.json['carreras']
        documentFound[0]['partido']: request.json['partido']
        documentFound[0]['comuna']: request.json['comuna']
        documentFound[0]['region']: request.json['region']
        documentFound[0]['cargo_actual']: request.json['cargo_actual']
        documentFound[0]['cargos_anteriores']: request.json['cargos_anteriores']
        return jsonify({
            'message': 'Document Updated',
            'document': documentFound[0]
        })
    return jsonify({'message': 'Document Not found'})

# DELETE Data Route
@app.route('/documents/<string:document_name>', methods=['DELETE'])
def deleteDocument(document_name):
    documentsFound = [document for document in documents if document['name'] == document_name]
    if len(documentsFound) > 0:
        documents.remove(documentsFound[0])
        return jsonify({
            'message': 'Document Deleted',
            'documents': documents
        })

if __name__ == '__main__':
    app.run(debug=True, port=4000)
