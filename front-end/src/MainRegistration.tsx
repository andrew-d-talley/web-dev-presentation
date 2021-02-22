import React, { useContext } from "react";
import { Button, Container } from "react-bootstrap";
import classes from "./classes.json";
import styled from "styled-components";
import { CartContext } from "./CartContext";

const ClassGrid = styled.div`
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-column-gap: 20px;
  grid-row-gap: 20px;
`;

interface ClassTileProps {
  title: string;
  catalogNum: number;
  description: string;
}
const ClassTile: React.FC<ClassTileProps> = ({ title, catalogNum, description }) => { 
  const { classes, addClass, removeClass } = useContext(CartContext);

  const inCart = classes.includes(catalogNum);

  return (
    <div className="border p-2">
      <h2>{title}</h2>
      <h4>CS {catalogNum}</h4>
      <p>{description}</p>
      {inCart ? <Button onClick={() => removeClass(catalogNum)}>Remove From Cart</Button> : <Button onClick={() => addClass(catalogNum)}>Add to Cart</Button>}
    </div>
  );
}


export const MainRegistration: React.FC = () => (
  <Container>
    <h1>Registration</h1>
    <ClassGrid>
      {classes.map((classInfo) => (<ClassTile {...classInfo} />))}
    </ClassGrid>
  </Container>
)