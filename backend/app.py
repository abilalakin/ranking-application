from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_graphql import GraphQLView
import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
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


# GraphQL Types
class CompanyType(SQLAlchemyObjectType):
    class Meta:
        model = Company


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    search_companies = graphene.List(
        CompanyType,
        query=graphene.String(required=True)
    )

    def resolve_search_companies(self, info, query):
        query_embedding = ranker.encode_text(query)
        companies = Company.query.all()
        company_data = [{'name': company.name, 'description': company.description} for company in companies]

        scores = []
        for company in company_data:
            description_embedding = ranker.encode_text(company['description'])
            similarity_score = calculate_similarity(query_embedding, description_embedding)
            scores.append((company, similarity_score))

        ranked_companies = sorted(scores, key=lambda x: x[1], reverse=True)
        ranked_results = [Company(name=company['name'], description=company['description']) for company, _ in
                          ranked_companies]

        return ranked_results


class CreateCompany(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String(required=True)

    company = graphene.Field(lambda: CompanyType)

    def mutate(self, info, name, description):
        new_company = Company(name=name, description=description)
        db.session.add(new_company)
        db.session.commit()
        return CreateCompany(company=new_company)


class Mutation(graphene.ObjectType):
    create_company = CreateCompany.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

# GraphQL route
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == '__main__':
    app.run(debug=True)
