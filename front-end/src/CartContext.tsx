import React from "react";

interface CartContextType {
  classes: number[];
  addClass: (classNum: number) => void;
  removeClass: (classNum: number) => void;
} 
export const CartContext = React.createContext<CartContextType>({classes: [], addClass: () => {}, removeClass: () => {}});