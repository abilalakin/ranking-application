import ReactDOM from 'react-dom/client';
import { ApolloProvider, InMemoryCache, ApolloClient } from '@apollo/client';
import App from './App';
import './styles.css';


const client = new ApolloClient({
  uri: 'http://127.0.0.1:5000/graphql',
  cache: new InMemoryCache(),
});

const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>
);
