import './App.css';
import 'bootswatch/dist/sandstone/bootstrap.min.css'; 
import { Nav, Navbar } from "react-bootstrap";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import { MainRegistration } from './MainRegistration';
import { Cart } from './Cart';
import { useMemo, useState } from 'react';
import { CartContext } from "./CartContext";

function App() {
  const [classes, setClasses] = useState<number[]>([]);

  const addClass = (classNum: number) => {
    if (!classes.includes(classNum)) {
      setClasses([...classes, classNum]);
    }
  }

  const removeClass = (classNum: number) => {
    if (classes.includes(classNum)) {
      setClasses(classes.filter(c => c !== classNum));
    }
  }
  
  const cartContextValue = useMemo(() => ({
    classes,
    addClass,
    removeClass
  }), [classes]);

  return (
    <Router>
      <CartContext.Provider value={cartContextValue}>
        <div>
          <Navbar bg="dark" expand="lg">
            <Navbar.Brand>Vandy CS Registration</Navbar.Brand>
            <Nav>
              <Nav.Link as={Link} to="/">Home</Nav.Link>
              <Nav.Link as={Link} to="/cart">Cart ({classes.length})</Nav.Link>
            </Nav>
          </Navbar>
          <Switch>
            <Route path="/cart">
              <Cart />
            </Route>
            <Route path="/">
              <MainRegistration />
            </Route>
          </Switch>
        </div>
      </CartContext.Provider>
    </Router>
  );
}

export default App;
