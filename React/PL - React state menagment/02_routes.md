```
# install
npm i json-server
npm i npm-run-all
npm i cross-env
npm i react-router-dom
```
#### package.json
```
  "dependencies": {
    "@testing-library/jest-dom": "^5.16.4",
    "@testing-library/react": "^13.2.0",
    "@testing-library/user-event": "^13.5.0",
    "cross-env": "^7.0.3",
    "json-server": "^0.17.0",
    "npm-run-all": "^4.1.5",
    "react": "^18.1.0",
    "react-dom": "^18.1.0",
    "react-router-dom": "^6.3.0",
    "react-scripts": "5.0.1",
    "web-vitals": "^2.1.4"
  },
  "scripts": {
    "start": "run-p start-app start-api",
    "start-app": "cross-env REACT_APP_API_BASE_URL=http://localhost:3002/ react-scripts start",
    "start-api": "json-server --port 3002 --watch db.json --delay 0",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
```

#### App.js
```
import logo from './logo.svg';
import './App.css';
import Products from './Products';
import Header from './Header';
import {Routes, Route} from 'react-router-dom';
import Detail from './Detail';
import Cart from './Cart';

function App(props) {

  return (
    <div>
      <Header></Header>
      <Routes>
        <Route path='/' element={<h1>Welcome to carved Rock</h1>}></Route>
        <Route path='/:category' element={<Products/>}></Route>
        <Route path='/detail/:id' element={<Detail/>}></Route>
        <Route path='/cart' element={<Cart/>}></Route>
      </Routes>
    </div>
  )
}

export default App;
```
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

img {
  max-height: 100px;
}
```
#### Products.js
```
import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { getProducts } from './productService';
import Spinner from './Spinner';
import useFetch from './useFetch';
import { Link, useParams } from 'react-router-dom';
import NotFound from './NotFound';

function Products(props) {
  const [size, setSize] = useState("");
  // for url params. Has property for each variable
  const {category} = useParams();

  const { data: products, loading, error } = useFetch(
    "products?category=" + category
  );

  const filteredProducts = size
    ? products.filter((p) => p.skus.find((s) => s.size === parseInt(size)))
    : products;

  const renderProduct = (product) => {
    return (
      <div key={product.id} className="product">
        <Link to={`/detail/${product.id}`}>
          <img src={`/images/${product.image}`} alt={product.name}></img>
          <h3>{product.name}</h3>
          <h3>{product.price}</h3>
        </Link>
      </div>
    )
  }

  if (error) throw error;
  if (loading) return <Spinner></Spinner>
  if (products.length === 0) return <NotFound></NotFound>
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

export default Products;
```

#### Header.js
```
import React from "react";
import {Link, NavLink} from "react-router-dom";

// Navlink has applied css style whenever active
const activeStyle = {
    color: "red"
}
export default function Header() {
  return (
    <header>
      <nav>
        <Link to="/">Header</Link>
        <NavLink activestyle={activeStyle} to="/shoes">Shoes</NavLink>
        <NavLink activestyle={activeStyle} to="/cart">Cart</NavLink>
        <hr></hr>
      </nav>
    </header>
  );
}
```

#### Cart.js
```
import React from "react";

export default function Cart() {
  return <h1>Cart</h1>;

  // TODO: Display these products details
  // return (
  //   <div id="detail">
  //     <h1>{product.name}</h1>
  //     <p>{product.description}</p>
  //     <p id="price">${product.price}</p>
  //     <img src={`/images/${product.image}`} alt={product.category} />
  //   </div>
  // );
}
```

#### Detail.js
```
import React from "react";
import { useNavigate, useParams } from "react-router-dom";
import NotFound from "./NotFound";
import Spinner from "./Spinner";
import useFetch from "./useFetch";

export default function Detail() {
    const {id} = useParams();
    const {data:product, loading, error} = useFetch(`products/${id}`)

    const navigate = useNavigate();

    if (loading) return <Spinner></Spinner>
    if (!product) return <NotFound></NotFound>
    if (error) throw error;

    return (
        <div id="detail">
        <h1>{product.name}</h1>
        <p>{product.description}</p>
        <p id="price">${product.price}</p>
        <p>
            <button className="btn btn-primary" onClick={()=>navigate("/cart")}>
                Go to cart
            </button>
        </p>
        <img src={`/images/${product.image}`} alt={product.category} />
        </div>
    );
}
```

#### NotFound
```
import React from "react";

export default function NotFound() {
  return (
    <div>
        Page Not Found
    </div>
  );
}
```

#### ErrorBoundary
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
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import ErrorBoundary from './ErrorBoundary'
import {BrowserRouter} from 'react-router-dom';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <ErrorBoundary>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </ErrorBoundary>
  </React.StrictMode>
);

reportWebVitals();
```

#### ProductService.js
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