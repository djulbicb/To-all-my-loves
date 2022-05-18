# Refs are used for:
1. Reference HTML element
2. Store value between renders
3. Can mutate ref value directly
4. Dont cause a rerender when they change.
5. For storing values that arent rendered
6. For instance variables
- Keep data between renders
- Storing previous value
- Track if component is mounted
- Hold HTTP request cancel token
- Reference a 3rd party library instance
- Debounce a call/Declare local cache
- Store flag that something happened
- Store value used in useEffect

# When to use refs
- Reference DOM element
- Manage uncontrolled inputs
- Store state that isnt rendered
- Extreme performance demands
- Instance variables in fuctions like previous values and if component mounted

### Ref common use
```
import React, {useRef} from "react";
export default function RefExample() {
    const inputEl = useRef(null);
    const onClick = () => inputEl.current.focus();
    return (
        <>
            <input ref={inputEl}></input>
            <button onClick={onClick}>Focus</button>
        </>
    )
}
```

### Detail.js as uncontrolled components
Uncontrolled component offers less control cause changes dont rerender. Example: disable of button based on property.

Use uncontrolled when:
- if too many components for better components
- when working non-react libraries.
```
import React, { useRef } from "react";
import { useNavigate, useParams } from "react-router-dom";
import NotFound from "./NotFound";
import Spinner from "./Spinner";
import useFetch from "./services/useFetch";

export default function Detail(props) {
    const {id} = useParams();
    const {data:product, loading, error} = useFetch(`products/${id}`)
    const sizeRef = useRef();

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
                ref={sizeRef}>   
                <option value="">Which size?</option>        
                {
                    product.skus.map((s)=> 
                        <option key={s.sku} value={s.sku}>{s.size}</option>        
                    )
                }
            </select>
            <button className="btn btn-primary" onClick={()=> {
                const sku = sizeRef.current.value;
                if (!sku) {
                    alert("Pick size");
                    return;
                }
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

### Updating state when component is unmounted
When changing fast screen, sometimes async call will trigger a state change after view is changed and it shows error in console

#### package.json
Increase delay of json server
```
"scripts": {
    "start": "run-p start-app start-api",
    "start-app": "cross-env REACT_APP_API_BASE_URL=http://localhost:3002/ react-scripts start",
    "start-api": "json-server --port 3002 --watch db.json --delay 1500",
```

#### useFetch.js
```
import { useState, useEffect, useRef } from "react";

const baseUrl = process.env.REACT_APP_API_BASE_URL;

export default function useFetch(url) {
  const isMounted = useRef(false);

  const [data, setData] = useState(null);
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    isMounted.current = true;
    async function init() {
      try {
        const response = await fetch(baseUrl + url);
        if (response.ok) {
          const json = await response.json();
          if (isMounted.current) {
            setData(json);
          } else {
            console.log("Not mounted anymore");
          }
        } else {
          throw response; // will be caught by catch below
        }
      } catch (e) {
        if (isMounted.current) setError(e);
      } finally {
        if (isMounted.current) setLoading(false);
      }
    }
    init();

    return () => {
      isMounted.current = false;   
    }
  }, [url]);

  return { data, error, loading };
}
```

#### Storing state between renders
useFetchAll koristi urls koji se konstantu definisu sa svakom promenom i na svaki render dobija novu listu

#### useFetchAll.js - current situation
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

#### useFetchAll.js - with useRef
```
import { useState, useEffect, useRef } from "react";

export default function useFetchAll(urls) {
  const prevUrls = useRef([]);

  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (areEqual(prevUrls.current, urls)) {
      setLoading(false);
      return;
    }
    prevUrls.current = urls;
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

function areEqual(array1, array2) {
  return (
    array1.length === array2.length &&
    array1.every((value, index) => value === array2[index])
  )
}
```