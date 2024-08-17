from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from ranking.ranker import Ranker, calculate_similarity

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
ranker = Ranker()


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Company {self.name}>"


@app.route('/add_company', methods=['POST'])
def add_company():
    data = request.json
    new_company = Company(name=data['name'], description=data['description'])
    db.session.add(new_company)
    db.session.commit()
    return jsonify({'message': 'Company added successfully!'}), 201


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q', '')
    if query:
        query_embedding = ranker.encode_text(query)
        companies = Company.query.all()
        company_data = [{'name': company.name, 'description': company.description} for company in companies]

        scores = []
        for company in company_data:
            description_embedding = ranker.encode_text(company['description'])
            similarity_score = calculate_similarity(query_embedding, description_embedding)
            scores.append((company, similarity_score))

        # Sort companies by similarity score in descending order
        ranked_companies = sorted(scores, key=lambda x: x[1], reverse=True)
        ranked_results = [{'name': company['name'], 'description': company['description']} for company, _ in
                          ranked_companies]

        return jsonify(ranked_results), 200
    else:
        return jsonify({'message': 'No search term provided'}), 400


if __name__ == '__main__':
    app.run(debug=True)
