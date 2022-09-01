import { createSlice } from "@reduxjs/toolkit";
import { getBrowsingData } from "../api/browsingApi";
import getDenimimg from "../api/clothesdenimapi/denim";
import getRealmeimg from "../api/realmeapi/realme";

const cardslice = createSlice({
  name: "cards",
  initialState: {
    search: "",
    sizeOfCart: 0,
    listOfAllObject: getBrowsingData(),
    listOfRealmeObject: getRealmeimg(),
    listOfClothesObject: getDenimimg(),
    listOfCartOjbect: [],
  },
  reducers: {
    onSearchChanging(state, action) {
      state.search = action.payload;
    },
    incrementCart(state, action) {
      state.sizeOfCart += 1;
    },
    decrementCart(state, action) {
      state.sizeOfCart -= 1;
    },
    handleincrese1(state, action) {
      const productexit = state.listOfAllObject.find(
        (item) => item.id === action.payload
      );

      state.listOfAllObject = state.listOfAllObject.map((item) =>
        item.id === action.payload
          ? { ...productexit, quantity: productexit.quantity + 1 }
          : item
      );
    },
    handledecrese1(state, action) {
      const productexit = state.listOfAllObject.find(
        (item) => item.id === action.payload
      );

      state.listOfAllObject = state.listOfAllObject.map((item) =>
        item.id === action.payload
          ? {
              ...productexit,
              quantity:
                productexit.quantity === 0
                  ? productexit.quantity
                  : productexit.quantity - 1,
            }
          : item
      );
    },

    handleproduct2(state, action) {
      const productexit = state.listOfCartOjbect.find(
        (item) => item.id === action.payload.id
      );
      if (productexit) {
        state.listOfCartOjbect = state.listOfCartOjbect.map((item) =>
          item.id === action.payload.id ? { ...productexit } : item
        );
      } else {
        state.listOfCartOjbect = [
          ...state.listOfCartOjbect,
          { ...action.payload },
        ];
      }
    },

    handleremove2(state, action) {
      const productexit = state.listOfAllObject.find(
        (item) => item.id === action.payload.id
      );

      if (productexit.quantity === 0) {
        state.listOfCartOjbect = state.listOfCartOjbect.filter(
          (item) => item.id !== action.payload.id
        );
      } else {
        state.listOfCartOjbect = state.listOfCartOjbect.map((item) =>
          item.id === action.payload.id ? { ...productexit } : item
        );
      }
      console.log(productexit.quantity);
    },
  },
});

export const {
  onSearchChanging,
  incrementCart,
  decrementCart,
  handledecrese1,
  handleincrese1,
  handleproduct2,
  handleremove2,
} = cardslice.actions;
export default cardslice.reducer;
