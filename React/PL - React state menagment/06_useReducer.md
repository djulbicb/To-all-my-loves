# useReducer
We create a function that manages state of component outside of the component

```
const initialState = {count: 0};

function reducer (state, action) {
    switch(action.type) {
        case 'increment':
            return {count: state.count + 1 };
        case 'decrement':
            return {count: state.count - 1 };
        default:
            throw new Error();              
        }
}

function Counter() {
    const [state, dispatch] = useReducer(reducer, initialState);
    return (
        <>
            Count: {state.count}
            <button onClick=={() => dispatch({type: 'decrement'})}>-</button>
        </>
    )
}
```

## Adding useReducer
#### cartReducer.js
```
import { act } from "react-dom/test-utils";

// whatever we return from reducer becomes new state
export default function cartReducer (cart, action) {
    switch (action.type) {
        case 'empty':
            return [];
        case 'add': {
            const {id, sku} = action;
            const itemInCart = cart.find(i => i.sku === sku);
            if (itemInCart) {
                return cart.map(i => 
                i.sku === sku ? {...i, quantity: i.quantity + 1} : i 
                );
            } else {
                return [...cart, {id, sku, quantity: 1}]
            }
        }
        case 'updateQuantity': {
            const {quantity, sku} = action;
            if (quantity === 0) {
                return cart.filter(i => i.sku !== sku)
            }
            return cart.map((i) => (i.sku === sku ? {...i, quantity} : i));
        }
        default:
            throw new Error("Unhandled action " + action.type)
    }
}
```
#### App.js
```
import React, { useReducer, useEffect } from "react";
import "./App.css";
import Header from "./Header";
import Products from "./Products";
import { Routes, Route } from "react-router-dom";
import Detail from "./Detail";
import Cart from "./Cart";
import Checkout from "./Checkout";
import cartReducer from "./services/cartReducer";

let initialCart;
try {
  initialCart = JSON.parse(localStorage.getItem("cart")) ?? [];
  console.log(initialCart);
} catch {
  console.error("The cart could not be parsed into JSON.");
  initialCart = [];
}

export default function App() {
  const [cart, dispatch] = useReducer(cartReducer, initialCart);

  useEffect(() => localStorage.setItem("cart", JSON.stringify(cart)), [cart]);

  return (
    <>
      <div className="content">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<h1>Welcome to Carved Rock Fitness</h1>} />
            <Route path="/:category" element={<Products />} />
            <Route
              path="/:category/:id"
              element={<Detail dispatch={dispatch} />}
            />
            <Route
              path="/cart"
              element={<Cart cart={cart} dispatch={dispatch} />}
            />
            <Route
              path="/checkout"
              element={<Checkout cart={cart} dispatch={dispatch} />}
            />
          </Routes>
        </main>
      </div>
    </>
  );
}
```

#### cart.js
```
import React, { useMemo } from "react";
import { useNavigate } from "react-router-dom";
import useFetchAll from "./services/useFetchAll";
import Spinner from "./Spinner";

export default function Cart({ cart, dispatch }) {
  const navigate = useNavigate();
  const urls = cart.map((i) => `products/${i.id}`);
  const { data: products, loading, error } = useFetchAll(urls);
  console.log(error, products);

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
              onChange={(e) =>
                dispatch({
                  type: "updateQuantity",
                  sku,
                  quantity: parseInt(e.target.value),
                })
              }
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

  const numItemsInCart = cart.reduce((total, item) => total + item.quantity, 0);

  return (
    <section id="cart">
      <h1>
        {numItemsInCart === 0
          ? "Your cart is empty"
          : `${numItemsInCart} Item${numItemsInCart > 1 ? "s" : ""} in My Cart`}
      </h1>
      <ul>{cart.map(renderItem)}</ul>
      {cart.length > 0 && (
        <button
          className="btn btn-primary"
          onClick={() => navigate("/checkout")}
        >
          Checkout
        </button>
      )}
    </section>
  );
}
```

#### checkout.js
```
import React, { useState } from "react";
import RefExample from "./RefExample";
import { saveShippingAddress } from "./services/shippingService";

// Declaring outside component to avoid recreation on each render
const emptyAddress = {
  city: "",
  country: "",
};

const STATUS = {
    IDLE: "IDLE",
    SUBMITTING: "SUBMITTING",
    SUBMITTED: "SUBMITTED",
    COMPLETED: "COMPLETED"
}

export default function Checkout({ cart, dispatch }) {
  const [status, setStatus] = useState(STATUS.IDLE)
  const [address, setAddress] = useState(emptyAddress);
  const [saveError, setSaveError] = useState(null);
  const [touched, setTouched] = useState({});

  const errors = getErrors(address);
  const isValid = Object.keys(errors).length === 0;

  // each field has id same as field name
  // js computed property syntaxt [e.target.id]
  function handleChange(e) {
    e.persist();
    setAddress((currentAddress) => {
        return {
            ...currentAddress,
            [e.target.id]: e.target.value
        }
    })
  }

  function handleBlur(e) {
    setTouched((current) => {
        return {...current, [e.target.id]: true}
    });
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setStatus(STATUS.SUBMITTING);
    if (isValid) {
        try {
            await saveShippingAddress(address);
            dispatch({type: 'empty'})
            setStatus(STATUS.COMPLETED);
        } catch (e) {
            setSaveError(e);
        }
    } else {
        setStatus(STATUS.SUBMITTED)
    }
  }

  function getErrors(address) {
      const result = {};
      if (!address.city) result.city = "City is required";
      if (!address.country) result.country = "Country is required"
      return result;
  }

  if (saveError) throw saveError;
  if (status === STATUS.COMPLETED) {
      return (<h1>Thanks for shopping</h1>)
  }
  return (
    <>
      <h1>Shipping Info</h1>
      {
          !isValid && (status === STATUS.SUBMITTED) && (
              <div role="alert">
                <p>Please fix errors</p>
                <ul>
                    {
                        Object.keys(errors).map(key => {
                            return <li key={key}>{errors[key]}</li>
                        })
                    }
                </ul>
              </div>
          )
      }
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="city">City</label>
          <br />
          <input
            id="city"
            type="text"
            value={address.city}
            onBlur={handleBlur}
            onChange={handleChange}
          />
          <p role="alert">
              {(touched.city || status === STATUS.SUBMITTED) && errors.city}
          </p>
        </div>

        <div>
          <label htmlFor="country">Country</label>
          <br />
          <select
            id="country"
            value={address.country}
            onBlur={handleBlur}
            onChange={handleChange}
          >
            <option value="">Select Country</option>
            <option value="China">China</option>
            <option value="India">India</option>
            <option value="United Kingdom">United Kingdom</option>
            <option value="USA">USA</option>
          </select>
          <p role="alert">
              {(touched.country || status === STATUS.SUBMITTED) && errors.country}
          </p>
        </div>

        <div>
          <input
            type="submit"
            className="btn btn-primary"
            value="Save Shipping Info"
            disabled={status === STATUS.SUBMITTING}
          />
        </div>
        <RefExample></RefExample>
      </form>
    </>
  );
}
```

#### detail.js
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
                props.dispatch({type: 'add', id, sku});
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