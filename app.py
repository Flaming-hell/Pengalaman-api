from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
DATA_FILE = 'experience.json'

def load_data():
	if os.path.exists(DATA_FILE):
		with open(DATA_FILE, 'r') as f:
			return json.load(f)
	return []

def save_data(data):
	with open(DATA_FILE, 'w') as f:
		json.dump(data, f, indent=4)
		
@app.route('/experiences', methods=['GET'])
def get_experiences():
	return jsonify(load_data())
	
@app.route('/experiences', methods=['POST'])
def add_experience():
	data = load_data()
	new_exp = request.json
	new_exp['id'] = data[-1]['id'] + 1 if data else 1
	data.append(new_exp)
	save_data(data)
	return jsonify({"message": "Experience added!"}), 201

@app.route('/experiences/<int:exp_id>', methods=['PUT'])
def update_experience(exp_id):
	data = load_data()
	for exp in data:
		if exp['id'] == exp_id:
			exp.update(request.json)
			save_data(data)
			return jsonify({"message": "Experience Update!"})
	return jsonify({"error": "Experience not found"}), 404

@app.route('/experiences/<int:exp_id>', methods=['DELETE'])
def delete_experience(exp_id):
	data = load_data()
	data = [exp for exp in data if exp['id'] != exp_id]
	save_data(data)
	return jsonify({"message": "Experience delete!"})
	
if __name__ == '__main__':
	app.run(debug=True)
