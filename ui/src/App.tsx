import React from 'react';
import SearchBar from './components/SearchBar';
import AddCompany from './components/AddCompany';

const App: React.FC = () => {
  return (
    <div className="App">
      <h1>Company Rankings</h1>
      <SearchBar />
      <AddCompany />
    </div>
  );
};

export default App;
