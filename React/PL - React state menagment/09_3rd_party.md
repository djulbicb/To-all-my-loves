# Local state - manage components state
#### Build in react
- useState
- Class state
- useReducer
- refs
- Derived state in render

#### Also:
- XState - enforce state transitions. Easy to test in isolation

#### Global state
#### Builtin
- lift state
- Context
#### Also
- Redux - if app complex, want to cache, handle cross cutting concerns. Redux is scalable
- MobX - A lot of derived state, Optimized for that. useMemo can handle most of stuff.
- Recoil

## Server state
Good data fetching library handle most common issue. Relay and Apollo are good for graphQL endpoint.
#### build in 
- none
#### also
- fetch
- axios
- react-query
- swr
- relay
- apollo

#### Products.react-query.js
It will show cached results before sending request
```
import React, { useState } from "react";
import Spinner from "./Spinner";
import { useParams } from "react-router-dom";
import PageNotFound from "./PageNotFound";
import { Link } from "react-router-dom";
import { useQuery } from "react-query";

// Copied from productService.js.
// Added key arg since react-query passes the query key as the first argument.
export async function getProducts(key, category) {
  const response = await fetch(
    process.env.REACT_APP_API_BASE_URL + "products?category=" + category
  );
  if (response.ok) return response.json();
  throw response;
}

export default function Products() {
  const { category } = useParams();
  const [size, setSize] = useState("");
  const { data: products, isLoading, error } = useQuery(
    ["products", category],
    getProducts
  );

  function renderProduct(p) {
    return (
      <div key={p.id} className="product">
        <Link to={`/${category}/${p.id}`}>
          <img src={`/images/${p.image}`} alt={p.name} />
          <h3>{p.name}</h3>
          <p>${p.price}</p>
        </Link>
      </div>
    );
  }

  const filteredProducts = size
    ? products.filter((p) => p.skus.find((s) => s.size === parseInt(size)))
    : products;

  if (isLoading) return <Spinner />;
  if (error) throw error;
  if (products.length === 0) return <PageNotFound />;

  return (
    <>
      <section id="filters">
        <label htmlFor="size">Filter by Size:</label>{" "}
        <select
          id="size"
          value={size}
          onChange={(e) => setSize(e.target.value)}
        >
          <option value="">All sizes</option>
          <option value="7">7</option>
          <option value="8">8</option>
          <option value="9">9</option>
        </select>
        {size && <h2>Found {filteredProducts.length} items</h2>}
      </section>

      <section id="products">{filteredProducts.map(renderProduct)}</section>
    </>
  );
}
```

## Immutable state
#### builtin
- none
#### also
- Immer - write mutative code
#### cart.immer.js
```
/* This file uses Immer to handle state updates
   Note the it mutates the draft state instead of the state passed in.
   Immer returns a copy of the updated state, using the draft,
   so even though the code below mutates the draft, the state is 
   handled in an immutable friendly way. 👍
*/
import { produce } from "immer";

export default function cartReducer(cart, action) {
  switch (action.type) {
    case "add":
      const { id, sku } = action;
      const itemInCart = cart.find((i) => i.sku === sku);
      return produce(cart, (draft) => {
        if (itemInCart) {
          const itemIndex = draft.findIndex((i) => i.sku === sku);
          draft[itemIndex].quantity++;
        } else {
          draft.push({ id, sku, quantity: 1 });
        }
      });

    case "updateQuantity": {
      const { quantity, sku } = action;

      return produce(cart, (draft) => {
        const index = cart.findIndex((i) => i.sku === sku);
        if (quantity === 0) {
          delete draft[index];
        } else {
          draft[index].quantity = quantity;
        }
      });
    }

    case "empty":
      return [];

    default:
      throw new Error("Unhandled action" + action.type);
  }
}
```

## Form
- Formik
- React Hook Form
#### formik
```
import React, { useState } from "react";
import { saveShippingAddress } from "./services/shippingService";
import { useCart } from "./cartContext";
import { Formik, Field, ErrorMessage, Form } from "formik";
import * as Yup from "yup";

// Declaring outside component to avoid recreation on each render
const emptyAddress = {
  city: "",
  country: "",
};

const STATUS = {
  IDLE: "IDLE",
  SUBMITTED: "SUBMITTED",
  SUBMITTING: "SUBMITTING",
  COMPLETED: "COMPLETED",
};

const checkoutSchema = Yup.object().shape({
  city: Yup.string().required("City is required."),
  country: Yup.string().required("Country is required"),
});

export default function Checkout() {
  const { dispatch } = useCart();
  const [saveError, setSaveError] = useState(null);

  function getErrors(address) {
    const result = {};
    if (!address.city) result.city = "City is required.";
    if (!address.country) result.country = "Country is required.";
    return result;
  }

  async function handleSubmit(address, formikProps) {
    const { setStatus, setSubmitting } = formikProps;
    try {
      await saveShippingAddress(address);
      dispatch({ type: "empty" });
      setSubmitting(false);
      setStatus(STATUS.COMPLETED);
    } catch (err) {
      setSaveError(err);
    }
  }

  return (
    <Formik
      initialValues={emptyAddress}
      // validate={getErrors}           // Uncomment this to use our existing validation logic instead
      validationSchema={checkoutSchema} // Using YUP for validation
      onSubmit={handleSubmit}
    >
      {({
        errors,
        isValid,
        status = STATUS.IDLE,
        /* and other goodies */
      }) => {
        if (saveError) throw saveError;
        if (status === STATUS.COMPLETED) return <h1>Thanks for shopping!</h1>;

        return (
          <Form>
            <h1>Shipping Info</h1>
            {!isValid && status === STATUS.SUBMITTED && (
              <div role="alert">
                <p>Please fix the following errors:</p>
                <ul>
                  {Object.keys(errors).map((key) => {
                    return <li key={key}>{errors[key]}</li>;
                  })}
                </ul>
              </div>
            )}

            <div>
              <label htmlFor="city">City</label>
              <br />
              <Field type="text" name="city" />
              <ErrorMessage role="alert" name="city" component="p" />
            </div>

            <div>
              <label htmlFor="country">Country</label>
              <br />
              <Field as="select" name="country">
                <option value="">Select Country</option>
                <option value="China">China</option>
                <option value="India">India</option>
                <option value="United Kingodom">United Kingdom</option>
                <option value="USA">USA</option>
              </Field>
              <ErrorMessage role="alert" name="country" component="p" />
            </div>

            <div>
              <input
                type="submit"
                className="btn btn-primary"
                value="Save Shipping Info"
                disabled={status === STATUS.SUBMITTING}
              />
            </div>
          </Form>
        );
      }}
    </Formik>
  );
}
```