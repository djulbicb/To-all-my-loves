# Start up
**db.json**
```
{
  "products": [
    {
      "id": 1,
      "category": "shoes",
      "image": "shoe1.jpg",
      "name": "Hiker",
      "price": 94.95,
      "skus": [
        { "sku": "17", "size": 7 },
        { "sku": "18", "size": 8 }
      ],
      "description": "This rugged boot will get you up the mountain safely."
    },
    {
      "id": 2,
      "category": "shoes",
      "image": "shoe2.jpg",
      "name": "Climber",
      "price": 78.99,
      "skus": [
        { "sku": "28", "size": 8 },
        { "sku": "29", "size": 9 }
      ],
      "description": "Sure-footed traction in slippery conditions."
    },
    {
      "id": 3,
      "category": "shoes",
      "image": "shoe3.jpg",
      "name": "Explorer",
      "price": 145.95,
      "skus": [
        { "sku": "37", "size": 7 },
        { "sku": "38", "size": 8 },
        { "sku": "39", "size": 9 }
      ],
      "description": "Look stylish while stomping in the mud."
    }
  ],
  "shippingAddress": [
    {
      "id": 1,
      "city": "",
      "country": ""
    }
  ]
}
```
```
# install
npm i json-server
npm i npm-run-all
npm i cross-env
npm i react-router-dom

# add scripts
"scripts": {
    "start": "run-p start-app start-api",
    "start-app": "cross-env REACT_APP_API_BASE_URL=http://localhost:3001/ react-scripts start",
    "start-api": "json-server --port 3001 --watch db.json --delay 0",

npm start
```

sku - stock keeping unit. Product with size and color.



## Using debugger
Add `debugger;` and it will trigger breakpoint in browser. Install `React developer tools`.
```
if (condition) {
    debugger;
}
React develop tools - it will show hooks in order
```

## About array deconstructed in state
Hooks can be defined only on root level, so the hooks are executed in order. 
```
  // Array deconstructor
  const [sss, setSss] = useState("");
  const state = useState("test");
  const getter = state[0];
  const setter = state[1];

  // Wrong: Cant wrap in conditionals
  if (props.isAdmin) {
    const [role, setRole] = useState();
  }
  // Wrong: Cant be put in function
  function enableAdming() {
    [on, setOn] = useState(false);
  }
```

# Basic app
**App.js**
```
import logo from './logo.svg';
import './App.css';
import { useState } from 'react';

const products = [
    ...
];

function App(props) {
  const [size, setSize] = useState("");

  const filteredProducts = size ? products.filter(p=> p.skus.find(s=>s.size === parseInt(size)) ) : products;

  const renderProduct = (product) => {
    return (
      <div key={product.id} className="product">
        <a href='/'>
          <img src={`/images/${product.image}`} alt={product.name}></img>
          <h3>{product.name}</h3>
          <h3>{product.price}</h3>
        </a>
      </div>
    )
  }

  return (
    <div className="App">
      /* Controlled component - when react controls value of component */
      <select
        id="size"
        value={size}
        onChange={(e) => {
          setSize(e.target.value);
          // debugger;
        }}
      >
        <option value="">All sizes</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
      </select>

      <div className='products'>
        {/* Point free style of calling method. This or lambda */}
        {filteredProducts.map(renderProduct)}  
      </div>
  
    </div>
  );
}
export default App;
```

# Using api fetch

#### productService.js
```
const BASE_URL = process.env.REACT_APP_API_BASE_URL;

export async function getProducts (category) {
    const response = await fetch(BASE_URL + "products?category=" + category);
    if (response.ok) return response.json();
    throw response;
}

export async function getProduct(id) {
    const response = await fetch (BASE_URL + "products/" + id);
    if (response.ok) return response.json();
    throw response;
}
```

#### App.js
```
import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { getProducts } from './productService';

function App(props) {
  const [size, setSize] = useState("");
  const [products, setProducts] = useState([]);

  useEffect(()=>{
    getProducts("shoes").then(response => {
      setProducts(response);
    })
  }, []);
```

# Error Boundary
Error boundary doesnt catch error if they happen in async code
```
import React from "react";

export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}
```

#### index.js
```
root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);
```

Throw error if not null. Because Error boundary doesnt activate if async code.

#### App.js
```
function App(props) {
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);

  useEffect(()=>{
    getProducts("shoes").then(response => {
      setProducts(response);
    }).catch(e => {
      setError(e);
    })
  }, []);
    
    ...

  if (error) throw error;
  return (
    <div className="App">
      <select
```

# Loading screen
#### Spinner.js
```
import React from 'react';
const Spinner = (props) => {
    return (
        <div>
            Loading...
        </div>
    )
}
export default Spinner;
```
#### App.js
```
function App(props) {
  const [size, setSize] = useState("");
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(()=>{
    getProducts("shoes").then(response => {
      setProducts(response);
    }).catch(e => {
      setError(e);
    }).finally(()=>{setLoading(false)})
  }, []);

  if (error) throw error;
  if (loading) return <Spinner></Spinner>
  return (
    <div className="App">
    </div>
  );
}

export default App;
```

# Refactor into async/await
#### App.js
```
function App(props) {
  const [size, setSize] = useState("");
  const [products, setProducts] = useState([]);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(()=>{
    async function init() {
      try {
        const response = await getProducts("shoes");
        setProducts(response);
      } catch (e) {
        setError(e)
      } finally {
        setLoading(false)
      }
    } 
    init();
  }, []);
```

# Custom hook for fetch
Create file `useFetch.js`. React scans for files with prefix `use...` and considers it hooks.

#### useFetch.js
```
import { useState, useEffect } from "react";

const baseUrl = process.env.REACT_APP_API_BASE_URL;

export default function useFetch(url) {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function init() {
      try {
        const response = await fetch(baseUrl + url);
        if (response.ok) {
          const json = await response.json();
          setData(json);
        } else {
          throw response; // will be caught by catch below
        }
      } catch (e) {
        setError(e);
      } finally {
        setLoading(false);
      }
    }
    init();
  }, [url]);

  return { data, error, loading };
}
```

#### App.js
```
import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { getProducts } from './productService';
import Spinner from './Spinner';
import useFetch from './useFetch';

function App(props) {
  const [size, setSize] = useState("");

  const { data: products, loading, error } = useFetch(
    "products?category=shoes"
  );

  const filteredProducts = size
    ? products.filter((p) => p.skus.find((s) => s.size === parseInt(size)))
    : products;

  const renderProduct = (product) => {
    return (
      <div key={product.id} className="product">
      </div>
    )
  }

  return (
      <div className='products'>
        {filteredProducts.map(renderProduct)}  
      </div>
    </div>
  );
}

export default App;
```

# Final
#### App.css
```
.App {
  margin: auto;
  max-width: 80%;
}

.products {
  display: flex;
}
.product {
  text-align: center;
  border: 1px solid black;
  margin-right: 1em;
}
.product:hover {
  background-color: #ccc;
}

.product img {
  max-height: 100px;
}
```
#### App.js
```
import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { getProducts } from './productService';
import Spinner from './Spinner';
import useFetch from './useFetch';

function App(props) {
  const [size, setSize] = useState("");

  const { data: products, loading, error } = useFetch(
    "products?category=shoes"
  );

  const filteredProducts = size
    ? products.filter((p) => p.skus.find((s) => s.size === parseInt(size)))
    : products;

  const renderProduct = (product) => {
    return (
      <div key={product.id} className="product">
        <a href='/'>
          <img src={`/images/${product.image}`} alt={product.name}></img>
          <h3>{product.name}</h3>
          <h3>{product.price}</h3>
        </a>
      </div>
    )
  }

  if (error) throw error;
  if (loading) return <Spinner></Spinner>
  return (
    <div className="App">
      <select
        id="size"
        value={size}
        onChange={(e) => {
          setSize(e.target.value);
          // debugger;
        }}
      >
        <option value="">All sizes</option>
        <option value="7">7</option>
        <option value="8">8</option>
        <option value="9">9</option>
      </select>

      <div className='products'>
        {/* Point free style of calling method. This or lambda */}
        {filteredProducts.map(renderProduct)}  
      </div>
  
    </div>
  );
}

export default App;
```

#### ErrorBoundary.js
```
import React from "react";

export default class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    // Update state so the next render will show the fallback UI.
    return { hasError: true };
  }

  render() {
    if (this.state.hasError) {
      // You can render any custom fallback UI
      return <h1>Something went wrong.</h1>;
    }

    return this.props.children;
  }
}
```

#### index.js
```
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <App />
    </ErrorBoundary>
  </React.StrictMode>
);
reportWebVitals();
```

#### Spinner.js
```
import React from 'react';
const Spinner = (props) => {
    return (
        <div>
            Loading...
        </div>
    )
}
export default Spinner;
```

#### productService.js
```
const BASE_URL = process.env.REACT_APP_API_BASE_URL;

export async function getProducts (category) {
    const response = await fetch(BASE_URL + "products?category=" + category);
    if (response.ok) return response.json();
    throw response;
}

export async function getProduct(id) {
    const response = await fetch (BASE_URL + "products/" + id);
    if (response.ok) return response.json();
    throw response;
}
```
#### db.json
Pored package.json fajl
```
{
    "products": [
      {
        "id": 1,
        "category": "shoes",
        "image": "shoe1.jpg",
        "name": "Hiker",
        "price": 94.95,
        "skus": [
          { "sku": "17", "size": 7 },
          { "sku": "18", "size": 8 }
        ],
        "description": "This rugged boot will get you up the mountain safely."
      },
      {
        "id": 2,
        "category": "shoes",
        "image": "shoe2.jpg",
        "name": "Climber",
        "price": 78.99,
        "skus": [
          { "sku": "28", "size": 8 },
          { "sku": "29", "size": 9 }
        ],
        "description": "Sure-footed traction in slippery conditions."
      },
      {
        "id": 3,
        "category": "shoes",
        "image": "shoe3.jpg",
        "name": "Explorer",
        "price": 145.95,
        "skus": [
          { "sku": "37", "size": 7 },
          { "sku": "38", "size": 8 },
          { "sku": "39", "size": 9 }
        ],
        "description": "Look stylish while stomping in the mud."
      }
    ],
    "shippingAddress": [
      {
        "id": 1,
        "city": "",
        "country": ""
      }
    ]
  }
```