import { FormControl, TextField, Button } from "@mui/material";
import { useState } from "react";
import { usePostItemMutation } from "../app/services/api";
export const FormKeyValue = () => {
  const [postItemMutation] = usePostItemMutation();
  // Component state
  const [key, setKey] = useState("");
  const [value, setValue] = useState("");

  const [keyErrorIndicator, setKeyErrorIndicator] = useState(false);
  const [valueErrorIndicator, setValueErrorIndicator] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    setKeyErrorIndicator(false);
    setValueErrorIndicator(false);

    if (!key) setKeyErrorIndicator(true);
    if (!value) setValueErrorIndicator(true);

    if (key && value) postItemMutation({ key, value });
  };
  return (
    <form autoComplete="off" onSubmit={handleSubmit}>
      <FormControl>
        <TextField
          label="Key"
          onChange={(e) => setKey(e.target.value)}
          value={key}
          error={keyErrorIndicator}
        ></TextField>
        <TextField
          label="Value"
          color="secondary"
          onChange={(e) => setValue(e.target.value)}
          value={value}
          error={valueErrorIndicator}
        ></TextField>
        <Button type="submit">Submit</Button>
      </FormControl>
    </form>
  );
};
