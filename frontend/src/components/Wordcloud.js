import React from "react";
import ReactDOM from "react-dom";
import ReactWordcloud from "react-wordcloud";
import { Resizable } from "re-resizable";

import "tippy.js/dist/tippy.css";
import "tippy.js/animations/scale.css";

import words from "./words";

const resizeStyle = {
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
  border: "solid 1px #ddd",
  background: "#f0f0f0"
};

function App() {
  return (
    <div>
      <p>Resize the container!</p>
      <Resizable
        defaultSize={{
          width: 600,
          height: 300
        }}
        style={resizeStyle}
      >
        <div style={{ width: "100%", height: "100%" }}>
          <ReactWordcloud words={words} />
        </div>
      </Resizable>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
