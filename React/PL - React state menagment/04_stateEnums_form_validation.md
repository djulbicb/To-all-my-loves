# State machine
We can use multiple useState for each field, but with forms its recommended to use single useState if the data is related.
Tradeoff is setting state is more complex.

For working with fiels we use js computed property syntaxt `[e.target.id]`.
Since field has id same as field name. e.persist() isnt required in React 17 cause it pools events.
```
  function handleChange(e) {
    e.persiste(); // react will ignore e in arror function by default
    setAddress((currentAddress) => {
        return {
            ...currentAddress,
            [e.target.id]: e.target.value
        }
    })
  }
```

### Validation Decisions
1. Where to display errors: by field, at top
2. When display errors: onSubmit, onBlur, onChange
3. When disable submit: While submitting
4. When revalidate: onSubmit, onChange, onBlur

### What state we need
#### touched
1. touched - what field is touched
#### status
2. submitted - is form submitted
3. isSubmitting - is form submission in progress
#### derived
4. isValid - is the form currently valid
5. errors - What error for each field
6. dirty - Is form changed

### Tip: Enums
Better to pick enum instead of multiple states. If form state is discrete.
```
  const [submitting, setSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);
  const [completed, setCompleted] = useState(false);

  const STATUS = {
      IDLE: "IDLE",
      SUBMITTING: "SUBMITTING",
      SUBMITTED: "SUBMITTED",
      COMPLETED: "COMPLETED"
  }
  const [status, setStatus] = useState(STATUS.IDLE)
```

#### shippingService.js
```
const baseUrl = process.env.REACT_APP_API_BASE_URL;

export async function getShippingAddress(userId) {
  return fetch(baseUrl + "shippingAddress/" + userId).then((response) => {
    if (response.ok) return response.json();
    throw response;
  });
}

export async function saveShippingAddress(address) {
  return fetch(baseUrl + "shippingAddress", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(address),
  });
}
```

#### Checkout.js
```
import React, { useState } from "react";
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

export default function Checkout({ cart, emptyCart }) {
  const [status, setStatus] = useState(STATUS.IDLE)
  const [address, setAddress] = useState(emptyAddress);
  const [saveError, setSaveError] = useState(null);

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

  function handleBlur(event) {
    // TODO
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setStatus(STATUS.SUBMITTING);
    try {
        await saveShippingAddress(address);
        emptyCart()
        setStatus(STATUS.COMPLETED);
    } catch (e) {
        setSaveError(e);
    }
  }
  if (saveError) throw saveError;
  if (status === STATUS.COMPLETED) {
      return (<h1>Thanks for shopping</h1>)
  }
  return (
    <>
      <h1>Shipping Info</h1>
      {JSON.stringify(address)}
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
        </div>

        <div>
          <input
            type="submit"
            className="btn btn-primary"
            value="Save Shipping Info"
            disabled={status === STATUS.SUBMITTING}
          />
        </div>
      </form>
    </>
  );
}
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
import Checkout from './Checkout';

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

  function emptyCart() {
    setCart([]);
  }

  return (
    <div>
      <Header></Header>
      <Routes>
        <Route path='/' element={<h1>Welcome to carved Rock</h1>}></Route>
        <Route path='/:category' element={<Products/>}></Route>
        <Route path='/detail/:id' element={<Detail addToCart={addToCart}/>}></Route>
        <Route path='/cart' element={<Cart cart={cart} updateQuantity={updateQuantity}/>}></Route>
        <Route path='/checkout' element={<Checkout cart={cart} emptyCart={emptyCart}/>}></Route>
      </Routes>
    </div>
  )
}

export default App;
```

# Finite machine
We use state enums where logic has discreet states. For complex example we use finite state machine (only one state can be active and state goes from one to another). Example of frameworks are `XState`.

# Form validation
Library for form validation are `Formik, React Hook Form`.
#### Checkout.js
```
import React, { useState } from "react";
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

export default function Checkout({ cart, emptyCart }) {
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
            emptyCart()
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
      </form>
    </>
  );
}
```