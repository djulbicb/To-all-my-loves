# Lifting state
Data should be immutable. Easier to check equality `obj1==obj2`. Reference equality is faster than value equality.
## Copy object
- `Object.assign({}, state, {what:"add this property");` Create new obj, copy state, append property
- Copy via spread. Creates shallow copies
```
const newState = {...state, role: "admin"};
const newUsers = [...state.users]

const user = {
    name: 'Bojan',
    address: { state: 'California' }
}
const userCopy = { ...user };
const userCopy = { ...user, address: {...user.address} }; 
```
When working with states avoid nested objects. Better have user and address as seperate.
Deep cloning is expensive cause change of one property.

For arrays avoid push, pop, reverse. Better do map, filter, reduce, concat, spread.

When defining object you cna shorthand
```
{id, name, sku} == { id: id, name: name, sku: sku}
```

Setting state in react is async. It will batch multiple state changes and then execute them.
Due to batching old state may be outdated so use function to reference existing state
```
const [count, setCount] = useState(0);
// Avoid since unreliable
setCount(count + 1);
// Prefer this - use a function form to reference existing state
setCount((count) => count + 1);
```
#### Detail.js
```
import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import NotFound from "./NotFound";
import Spinner from "./Spinner";
import useFetch from "./useFetch";

export default function Detail() {
    const [sku, setSku] = useState("");

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
            <select
                id="size"
                value={sku}
                onChange={(e) => {
                    setSku(e.target.value);
                }}>   
                <option value="">Which size?</option>        
                {
                    product.skus.map((s)=> 
                        <option key={s.sku} value={s.sku}>{s.size}</option>        
                    )
                }
            </select>
            <button disabled={!sku} className="btn btn-primary" onClick={()=>navigate("/cart")}>
                Go to cart
            </button>
        </p>
        <img src={`/images/${product.image}`} alt={product.category} />
    </div>
    );
}
```

Cart should be placed in the parent App, and then pass it to Detail and Cart.
In big app when lifting state, often state is lifted for 2 parent level.

# Saving cart

#### App.js - Lift state to parent
```
import logo from './logo.svg';
import './App.css';
import Products from './Products';
import Header from './Header';
import {Routes, Route} from 'react-router-dom';
import Detail from './Detail';
import Cart from './Cart';
import { useState } from 'react';

function App(props) {

  const [cart, setCart] = useState([]);

  function updateQuantity(sku, quantity) {
    setCart((items) => {
      if (quantity === 0) {
        return items.filter(i => i.sku !== sku)
      }
      return items.map((i) => (i.sku === sku ? {...i, quantity} : i));
    })
  }

  function addToCart(id, sku) {
    setCart((items) => {
      // Predicate, function that returns true/false
      const itemInCart = items.find(i => i.sku === sku);
      if (itemInCart) {
        // map runs function on each element in array
        // return new array with updated element
        return items.map(i => 
          i.sku === sku ? {...i, quantity: i.quantity + 1} : i 
        );
      } else {
        // object shorthand syntax. Omit left if right matches
        // return [...items, {id:id, sku:sku, quantity: 1}]
        return [...items, {id, sku, quantity: 1}]
      }
    }) 
  }

  return (
    <div>
      <Header></Header>
      <Routes>
        <Route path='/' element={<h1>Welcome to carved Rock</h1>}></Route>
        <Route path='/:category' element={<Products/>}></Route>
        <Route path='/detail/:id' element={<Detail addToCart={addToCart}/>}></Route>
        <Route path='/cart' element={<Cart cart={cart} updateQuantity={updateQuantity}/>}></Route>
      </Routes>
    </div>
  )
}

export default App;
```

#### Cart
```
import React, { useMemo } from "react";
import useFetchAll from "./services/useFetchAll";
import Spinner from "./Spinner";

export default function Cart({ cart, updateQuantity }) {
    const urls = cart.map((i) => `products/${i.id}`);
    const { data: products, loading, error } = useFetchAll(urls);
  
    function renderItem(itemInCart) {
      const { id, sku, quantity } = itemInCart;
      const { price, name, image, skus } = products.find(
        (p) => p.id === parseInt(id)
      );
      const { size } = skus.find((s) => s.sku === sku);
  
      return (
        <li key={sku} className="cart-item">
          <img src={`/images/${image}`} alt={name} />
          <div>
            <h3>{name}</h3>
            <p>${price}</p>
            <p>Size: {size}</p>
            <p>
              <select
                aria-label={`Select quantity for ${name} size ${size}`}
                onChange={(e) => updateQuantity(sku, parseInt(e.target.value))}
                value={quantity}
              >
                <option value="0">Remove</option>
                <option value="1">1</option>
                <option value="2">2</option>
                <option value="3">3</option>
                <option value="4">4</option>
                <option value="5">5</option>
              </select>
            </p>
          </div>
        </li>
      );
    }
  
    if (loading) return <Spinner />;
    if (error) throw error;
  
    // total is previous iteration result. 0 is initial value (Acumulators initial value)
    const numItemsInCart = cart.reduce((total, item) => total + item.quantity, 0);
    // useMemo: must be used before return.
    // So that count isnt calculated each render useMemo. With useMemo its calculated only on dependency change
    // const num = useMemo(
    //     () => cart.reduce((total, item) => total + item.quantity, 0),
    //     [cart]
    // )

    return (
      <section id="cart">
        <h1>
          {numItemsInCart === 0
            ? "Your cart is empty"
            : `${numItemsInCart} Item${numItemsInCart > 1 ? "s" : ""} in My Cart`}
        </h1>
        <ul>{cart.map(renderItem)}</ul>
      </section>
    );
  }
```

#### Detail
```
import React, { useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import NotFound from "./NotFound";
import Spinner from "./Spinner";
import useFetch from "./services/useFetch";

export default function Detail(props) {
    const [sku, setSku] = useState("");

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
            <select
                id="size"
                value={sku}
                onChange={(e) => {
                    setSku(e.target.value);
                }}>   
                <option value="">Which size?</option>        
                {
                    product.skus.map((s)=> 
                        <option key={s.sku} value={s.sku}>{s.size}</option>        
                    )
                }
            </select>
            <button disabled={!sku} className="btn btn-primary" onClick={()=> {
                props.addToCart(id, sku);
                navigate("/cart")
            }}>
                Go to cart
            </button>
        </p>
        <img src={`/images/${product.image}`} alt={product.category} />
    </div>
    );
}
```

#### useFetchAll.js
```
import { useState, useEffect } from "react";

export default function useFetchAll(urls) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const promises = urls.map((url) =>
      fetch(process.env.REACT_APP_API_BASE_URL + url).then((response) => {
        if (response.ok) return response.json();
        throw response;
      })
    );

    Promise.all(promises)
      .then((json) => setData(json))
      .catch((e) => {
        console.error(e);
        setError(e);
      })
      .finally(() => setLoading(false));
    // eslint-disable-next-line
  }, []);

  return { data, loading, error };
}
```

# LocalStorage
Storing data in browser possible with
- cookie
- localStorage - Local, Simple, Offline, limited storage, security risk, some are synchronys so avoid large data. Single browser
- sessionStorage
- indexedDb
- cacheStorage

```
import { useEffect, useState } from 'react';

function App(props) {

  // this should be default, instead of run on every render
  // const [cart, setCart] = useState(JSON.parse(localStorage.getItem("cart")));
  // functions are lazy evaluated
  const [cart, setCart] = useState(() => {
    try {
      // coalesce - if left null use right
      return JSON.parse(localStorage.getItem("cart")) ?? [];
    } catch {
      console.error("The cart cant be parsed")
      return []
    }
  });

  // anytime cart changes store it
  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart))
  }, [cart])
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
import { useEffect, useState } from 'react';

function App(props) {

  // this should be default, instead of run on every render
  // const [cart, setCart] = useState(JSON.parse(localStorage.getItem("cart")));
  // functions are lazy evaluated
  const [cart, setCart] = useState(() => {
    try {
      // coalesce - if left null use right
      return JSON.parse(localStorage.getItem("cart")) ?? [];
    } catch {
      console.error("The cart cant be parsed")
      return []
    }
  });

  // anytime cart changes store it
  useEffect(() => {
    localStorage.setItem("cart", JSON.stringify(cart))
  }, [cart])

  function updateQuantity(sku, quantity) {
    setCart((items) => {
      if (quantity === 0) {
        return items.filter(i => i.sku !== sku)
      }
      return items.map((i) => (i.sku === sku ? {...i, quantity} : i));
    })
  }

  function addToCart(id, sku) {
    setCart((items) => {
      // Predicate, function that returns true/false
      const itemInCart = items.find(i => i.sku === sku);
      if (itemInCart) {
        // map runs function on each element in array
        // return new array with updated element
        return items.map(i => 
          i.sku === sku ? {...i, quantity: i.quantity + 1} : i 
        );
      } else {
        // object shorthand syntax. Omit left if right matches
        // return [...items, {id:id, sku:sku, quantity: 1}]
        return [...items, {id, sku, quantity: 1}]
      }
    }) 
  }

  return (
    <div>
      <Header></Header>
      <Routes>
        <Route path='/' element={<h1>Welcome to carved Rock</h1>}></Route>
        <Route path='/:category' element={<Products/>}></Route>
        <Route path='/detail/:id' element={<Detail addToCart={addToCart}/>}></Route>
        <Route path='/cart' element={<Cart cart={cart} updateQuantity={updateQuantity}/>}></Route>
      </Routes>
    </div>
  )
}

export default App;
```