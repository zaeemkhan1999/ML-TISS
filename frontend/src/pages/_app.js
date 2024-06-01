import "@/styles/globals.css";
import { useState } from "react";
import { MyContext } from "../../context/MyContext";


export default function App({ Component, pageProps }) {
  const [data, setData] = useState(null);


  return (
    <MyContext.Provider value={{ data, setData }}>
        <Component {...pageProps} />
      </MyContext.Provider>
    
  )
}
