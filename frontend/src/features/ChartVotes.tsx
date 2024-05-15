import { useGetCountsQuery, useResetVoteMutation } from "../app/services/api";
import { Pie } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";
import { Button } from "@mui/material";

ChartJS.register(ArcElement, Tooltip, Legend);

export function ChartVotes() {
  const { data, isSuccess, isFetching, refetch } = useGetCountsQuery();
  const [deleteVotes] = useResetVoteMutation();
  if (!isSuccess || isFetching) return <p>Fetching</p>;
  const { countYes, countNo } = data;
  const graph = {
    labels: ["Yes", "No"],
    datasets: [
      {
        label: "# of Votes",
        data: [countYes, countNo],
        backgroundColor: ["rgba(75, 192, 192, 0.2)", "rgba(255, 99, 132, 0.2)"],
      },
    ],
  };
  return (
    <div>
      <div>
        <Button className="mr-100" variant="outlined" onClick={() => refetch()}>
          Get Current votes
        </Button>
      </div>
      <div className="my-2">
        <Button onClick={() => deleteVotes()} variant="outlined">
          Reset votes
        </Button>
      </div>
      <div>
        <Pie data={graph} className="h-96 w-96" />
      </div>
    </div>
  );
}
