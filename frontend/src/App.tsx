import "./App.css";
import { useGetCountsQuery } from "./app/services/api";
function App() {
  const { data, isSuccess, isFetching } = useGetCountsQuery();

  return (
    <div className="App">
      {!isFetching && isSuccess ? data.result || "" : ""}
    </div>
  );
}

export default App;
