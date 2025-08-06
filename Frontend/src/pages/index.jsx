import TikzEditor from '../components/TikzEditor';
import TikzPreview from '../components/TikzPreview';
import { useState } from 'react';

const IndexPage = () => {
  const [tikzCode, setTikzCode] = useState('');

  const handleGenerate = async (description) => {
    const response = await fetch('http://127.0.0.1:5000/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ description }),
    });
    const data = await response.json();
    setTikzCode(data.tikz_code);
  };

  return (
    <div>
      <h1>TikZ Diagram Generator</h1>
      <TikzEditor onGenerate={handleGenerate} />
      <TikzPreview tikzCode={tikzCode} />
    </div>
  );
};

export default IndexPage;
