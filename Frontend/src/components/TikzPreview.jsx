const TikzPreview = ({ tikzCode }) => {
  return (
    <div>
      <h3>Generated TikZ Code:</h3>
      <pre>{tikzCode}</pre>
    </div>
  );
};

export default TikzPreview;
