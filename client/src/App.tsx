import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
import Home from "./Pages/Home";
import "./App.css";

const App = () => {
  // const { t } = useTranslation();
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        <Route path="/home" index element={<Home />} />
      </>
    )
  );

  return (
    <div className="App">
      <RouterProvider router={router}></RouterProvider>
    </div>
  );
};
export default App;
