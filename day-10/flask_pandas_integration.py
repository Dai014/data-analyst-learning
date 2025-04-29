from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({"error": "Filename is required"}), 400
    
    try:
        data = pd.read_csv(filename)
        return jsonify(data.to_dict(orient='records'))
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)