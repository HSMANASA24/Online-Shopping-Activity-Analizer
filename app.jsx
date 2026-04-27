import { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = () => {
      fetch("http://127.0.0.1:5000/stats")
        .then((res) => res.json())
        .then((data) => setData(data))
        .catch((err) => console.log(err));
    };

    fetchData();
    const interval = setInterval(fetchData, 2000);

    return () => clearInterval(interval);
  }, []);

  const topProduct = Object.entries(data).sort(
    (a, b) => b[1].purchase - a[1].purchase
  )[0];

  return (
    <div
      style={{
        minHeight: "100vh",
        background: "linear-gradient(135deg, #1e3c72, #2a5298)",
        fontFamily: "Arial",
        color: "white",
      }}

      
    >
      
      {/* 🧭 Navbar */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          padding: "15px 30px",
          background: "rgba(0,0,0,0.3)",
        }}
      >
        <h2>🛒 Analyzer</h2>
        <div>
          <span style={{ marginRight: "15px", cursor: "pointer" }}>
            Home
          </span>
          <span style={{ cursor: "pointer" }}>Dashboard</span>
        </div>
      </div>

      {/* 🔥 Top Product */}
      {topProduct && (
        <div
          style={{
            margin: "20px",
            padding: "20px",
            borderRadius: "12px",
            textAlign: "center",
            backdropFilter: "blur(10px)",
            background: "rgba(255,255,255,0.2)",
          }}
        >
          <h2>🔥 Top Product</h2>
          <h3>{topProduct[0]}</h3>
          <p>{topProduct[1].purchase} purchases</p>
        </div>
      )}

      {/* 📦 Product Cards */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
          gap: "20px",
          padding: "20px",
        }}
      >
        {Object.keys(data).length === 0 ? (
          <p style={{ textAlign: "center" }}>Loading data...</p>
        ) : (
          Object.entries(data).map(([product, stats]) => (
            <div
              key={product}
              style={{
                backdropFilter: "blur(10px)",
                background: "rgba(255,255,255,0.1)",
                padding: "20px",
                borderRadius: "12px",
                boxShadow: "0 8px 20px rgba(0,0,0,0.3)",
                transition: "0.3s",
              }}
              onMouseEnter={(e) =>
                (e.currentTarget.style.transform = "scale(1.05)")
              }
              onMouseLeave={(e) =>
                (e.currentTarget.style.transform = "scale(1)")
              }
            >
              <h2 style={{ textAlign: "center" }}>{product}</h2>

              <p>👀 Views: {stats.view}</p>
              <p>🛒 Cart: {stats.add_to_cart}</p>
              <p>💳 Purchases: {stats.purchase}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;