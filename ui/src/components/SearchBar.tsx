import React, { useState } from 'react';
import { gql, useLazyQuery } from '@apollo/client';

const SEARCH_COMPANIES = gql`
  query SearchCompanies($query: String!) {
    searchCompanies(query: $query) {
      description
      name
    }
  }
`;

const SearchBar: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchCompanies, { loading }] = useLazyQuery(SEARCH_COMPANIES);

  const [results, setResults] = useState<any[]>([]);

  const handleSearch = () => {
    if (searchTerm.trim() === '') {
      alert('Please enter a search term.');
      return;
    }
    searchCompanies({ variables: { query: searchTerm } })
      .then((result) => {
        if (result.data) {
          setResults(result.data.searchCompanies);
        }
      })
      .catch((err) => {
        console.error('Search error:', err);
      });
  };

  const handleReset = () => {
    setSearchTerm('');
    setResults([]);
  };


  return (
    <div>
      <input
        type="text"
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search companies"
      />
      <div className='search-buttons'>
        <button onClick={handleSearch}>Search</button>
        <button onClick={handleReset}>Reset</button>
      </div>

      {loading && <p>Loading...</p>}
      {results.length > 0 && (
        <ol>
          {results.map((company, index) => (
            <li key={index}>
              <h3>{company.name}</h3>
              <p>{company.description}</p>
            </li>
          ))}
        </ol>
      )}
    </div>
  );
};

export default SearchBar;
