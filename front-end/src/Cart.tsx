import { useContext, useEffect, useMemo } from "react"
import { Button, Container } from "react-bootstrap"
import { CartContext } from "./CartContext";
import useAxios from "axios-hooks";
import classData from "./classes.json";

const classObj = Object.fromEntries(
  classData.map(c => [c.catalogNum, c])
);


const CartItem: React.FC<{ classNum: number }> = ({ classNum }) => {
  const { removeClass } = useContext(CartContext);

  const itemClass = classObj[classNum];

  return (
    <div className="p-3 w-100 border d-flex justify-content-between">
      {itemClass.title}
      <Button onClick={() => removeClass(classNum)}>Remove Class</Button>
    </div>
  )
}

const RecommendedItem: React.FC<{ classNum: number }> = ({ classNum }) => {
  const { addClass } = useContext(CartContext);
  const itemClass = classObj[classNum];

  return (
    <div className="p-3 w-100 border d-flex justify-content-between">
      {itemClass.title}
      <Button onClick={() => addClass(classNum)}>Add Class</Button>
    </div>
  )
}

export const Cart: React.FC = () => {
  const { classes } = useContext(CartContext);

  const [{ loading, data = [] }, refetch] = useAxios({
    url: process.env.REACT_APP_RECOMMENDATION_URL,
    method: "POST",
    headers: {
      'Content-Type': 'application/json'
    },
    data: { in_cart: classes }
  });

  // eslint-disable-next-line react-hooks/exhaustive-deps
  useEffect(() => {refetch()}, [classes]);

  return (
    <Container>
      <h2>Cart</h2>
      <div>
        {classes.map(c => <CartItem key={c} classNum={c} />)}
      </div>
      <h2>Recommended Courses</h2>
      <div>
        {loading && "Loading..."}
        {data.map((c: number) => <RecommendedItem key={c} classNum={c} />)}
      </div>
    </Container>
  )
}