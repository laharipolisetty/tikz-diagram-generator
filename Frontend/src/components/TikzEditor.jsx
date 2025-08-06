import React, { useState } from 'react';

const TikzEditor = () => {
  const [description, setDescription] = useState('');
  const [tikzCode, setTikzCode] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!description.trim()) {
      alert("Please enter a diagram description.");
      return;
    }

    setLoading(true);

    try {
      const response = await fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ description })
      });

      if (!response.ok) {
        throw new Error('Failed to fetch TikZ code from backend');
      }

      const data = await response.json();
      setTikzCode(data.tikz_code);
    } catch (error) {
      console.error('Error:', error);
      alert('An error occurred while generating TikZ code.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '800px', margin: 'auto' }}>
      <h2>TikZ Diagram Generator</h2>
      
      <textarea
        rows="4"
        style={{ width: '100%', padding: '10px', fontSize: '16px' }}
        placeholder="Describe your diagram (e.g., A circle with a label inside)"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      ></textarea>

      <button
        style={{
          marginTop: '10px',
          padding: '10px 20px',
          fontSize: '16px',
          cursor: 'pointer'
        }}
        onClick={handleGenerate}
        disabled={loading}
      >
        {loading ? 'Generating...' : 'Generate TikZ Code'}
      </button>

      {tikzCode && (
        <div style={{ marginTop: '20px' }}>
          <h3>Generated TikZ Code:</h3>
          <pre style={{ background: '#f4f4f4', padding: '10px', borderRadius: '5px' }}>
            {tikzCode}
          </pre>
        </div>
      )}
    </div>
  );
};

export default TikzEditor;
