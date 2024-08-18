import React, { useState } from 'react';
import { gql, useMutation } from '@apollo/client';

const ADD_COMPANY = gql`
  mutation AddCompany($name: String!, $description: String!) {
    createCompany(name: $name, description: $description) {
      company {
        name
        description
      }
    }
  }
`;

const AddCompany: React.FC = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [addCompany, { loading, error }] = useMutation(ADD_COMPANY);
  const [message, setMessage] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const response = await addCompany({ variables: { name, description } });
      if (response.data && response.data.createCompany) {
        setMessage(`Company added: ${response.data.createCompany.company.name}`);
        // Clear the message after 3 seconds
        setTimeout(() => setMessage(null), 3000);
      }
    } catch (err) {
      console.error('Error adding company:', err);
    }
    setName('');
    setDescription('');
  };

  return (
    <div>
      <h3>Add Company</h3>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Company Name"
          required
        />
        <textarea
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          placeholder="Company Description"
          required
        />
        <button type="submit" disabled={loading}>
          {loading ? 'Adding...' : 'Add Company'}
        </button>
      </form>
      {message && <p>{message}</p>}
      {error && <p style={{ color: 'red' }}>Error: {error.message}</p>}
    </div>
  );
};

export default AddCompany;
