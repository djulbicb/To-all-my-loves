# State - NOT FINISHED
In class components you cant use useState. Things have to declared as single object in constructor or as a field
#### as function
```
export default function Checkout({ cart, dispatch }) {
  const [status, setStatus] = useState(STATUS.IDLE)
  const [address, setAddress] = useState(emptyAddress);
  const [saveError, setSaveError] = useState(null);
  const [touched, setTouched] = useState({});

  const errors = getErrors(address);
  const isValid = Object.keys(errors).length === 0;
```
#### as constructor
```
export default class Checkout extends React.Component{
  constructor (props) {
    super(props)
    this.state = {
      address: emptyAddress,
      status: STATUS.IDLE,
      saveError:null,
      touched: {}
    }
  }
```
#### as field
```
export default class Checkout extends React.Component{
    state = {
      address: emptyAddress,
      status: STATUS.IDLE,
      saveError:null,
      touched: {}
    }

  constructor (props) {
    super(props)
  }
```

- cant write function
- setState is added by default. Receives old state as param
- during state merge react does shallow merge. Only set state is changed, rest stays the same
```
        return {
        address: {
          ...state.address,
          [e.target.id]: e.target.value,
        },
      };
  ```
- 
#### Checkout.js
```
import React from "react";
import { saveShippingAddress } from "./services/shippingService";

const STATUS = {
  IDLE: "IDLE",
  SUBMITTED: "SUBMITTED",
  SUBMITTING: "SUBMITTING",
  COMPLETED: "COMPLETED",
};

// Declaring outside component to avoid recreation on each render
const emptyAddress = {
  city: "",
  country: "",
};

export default class Checkout extends React.Component {
  state = {
    address: emptyAddress,
    status: STATUS.IDLE,
    saveError: null,
    touched: {},
  };

  isValid() {
    const errors = this.getErrors(this.state.address);
    return Object.keys(errors).length === 0;
  }

  handleChange = (e) => {
    e.persist(); // persist the event
    this.setState((state) => {
      return {
        address: {
          ...state.address,
          [e.target.id]: e.target.value,
        },
      };
    });
  };

  handleBlur = (event) => {
    event.persist();
    this.setState((state) => {
      return { touched: { ...state.touched, [event.target.id]: true } };
    });
  };

  handleSubmit = async (event) => {
    event.preventDefault();
    this.setState({ status: STATUS.SUBMITTING });
    if (this.isValid()) {
      try {
        await saveShippingAddress(this.state.address);
        this.props.dispatch({ type: "empty" });
        this.setState({ status: STATUS.COMPLETED });
      } catch (e) {
        this.setState({ saveError: e });
      }
    } else {
      this.setState({ status: STATUS.SUBMITTED });
    }
  };

  getErrors(address) {
    const result = {};
    if (!address.city) result.city = "City is required";
    if (!address.country) result.country = "Country is required";
    return result;
  }

  render() {
    const { status, saveError, touched, address } = this.state;

    //Derived state
    const errors = this.getErrors(this.state.address);

    if (saveError) throw saveError;
    if (status === STATUS.COMPLETED) {
      return <h1>Thanks for shopping!</h1>;
    }

    return (
      <>
        <h1>Shipping Info</h1>
        {!this.isValid() && status === STATUS.SUBMITTED && (
          <div role="alert">
            <p>Please fix the following errors:</p>
            <ul>
              {Object.keys(errors).map((key) => {
                return <li key={key}>{errors[key]}</li>;
              })}
            </ul>
          </div>
        )}
        <form onSubmit={this.handleSubmit}>
          <div>
            <label htmlFor="city">City</label>
            <br />
            <input
              id="city"
              type="text"
              value={address.city}
              onBlur={this.handleBlur}
              onChange={this.handleChange}
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
              onBlur={this.handleBlur}
              onChange={this.handleChange}
            >
              <option value="">Select Country</option>
              <option value="China">China</option>
              <option value="India">India</option>
              <option value="United Kingdom">United Kingdom</option>
              <option value="USA">USA</option>
            </select>

            <p role="alert">
              {(touched.country || status === STATUS.SUBMITTED) &&
                errors.country}
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
}
```

#### this for methods
```
# use arrow functions
  handleBlur = (event) => {
    event.persist();
    this.setState((state) => {
      return { touched: { ...state.touched, [event.target.id]: true } };
    });
  };
  
   handleSubmit = async (event) => {
    event.preventDefault();
    this.setState({ status: STATUS.SUBMITTING });
    if (this.isValid()) {
      try {
        await saveShippingAddress(this.state.address);
        this.props.dispatch({ type: "empty" });
        this.setState({ status: STATUS.COMPLETED });
      } catch (e) {
        this.setState({ saveError: e });
      }
    } else {
      this.setState({ status: STATUS.SUBMITTED });
    }
  };
  
# or not recommended in constructor
class Foo extends React.Component{
  constructor( props ){
    super( props );
    this.handleClick = this.handleClick.bind(this);
  }
  
  handleClick(event){
    // your event handling logic
  }
  
  render(){
    return (
      <button type="button" 
      onClick={this.handleClick}>
      Click Me
      </button>
    );
  }
}

ReactDOM.render(
  <Foo />,
  document.getElementById("app")
);  
```

# Detail.class.js
```
import React from "react";
import { useParams, useNavigate } from "react-router-dom";
import { Fetch } from "./services/useFetch";
import Spinner from "./Spinner";
import PageNotFound from "./PageNotFound";
import { CartContext } from "./cartContext";

export default function DetailWrapper() {
  const { id } = useParams();
  return <Detail id={id} navigate={useNavigate()} />;
}

class Detail extends React.Component {
  state = {
    sku: "",
  };

  render() {
    const { id, navigate } = this.props;
    const { sku } = this.state;

    return (
      <CartContext.Consumer>
        {({ dispatch }) => {
          return (
            <Fetch url={`products/${id}`}>
              {(product, loading, error) => {
                if (loading) return <Spinner />;
                if (!product) return <PageNotFound />;
                if (error) throw error;

                return (
                  <div id="detail">
                    <h1>{product.name}</h1>
                    <p>{product.description}</p>
                    <p id="price">${product.price}</p>

                    <select
                      id="size"
                      value={sku}
                      onChange={(e) => this.setState({ sku: e.target.value })}
                    >
                      <option value="">What size?</option>
                      {product.skus.map((s) => (
                        <option key={s.sku} value={s.sku}>
                          {s.size}
                        </option>
                      ))}
                    </select>

                    <p>
                      <button
                        disabled={!sku}
                        className="btn btn-primary"
                        onClick={() => {
                          this.context.dispatch({ type: "add", id, sku });
                          navigate("/cart");
                        }}
                      >
                        Add to cart
                      </button>
                    </p>
                    <img
                      src={`/images/${product.image}`}
                      alt={product.category}
                    />
                  </div>
                );
              }}
            </Fetch>
          );
        }}
      </CartContext.Consumer>
    );
  }
}
`