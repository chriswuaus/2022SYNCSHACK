import {
  Button,
  FormControl,
  InputLabel,
  MenuItem,
  Select,
  TextField,
} from "@mui/material";
import { useReducer, useState } from "react";
import styles from "../styles/DegreeEntry.module.css";
import { UnitEntryProps } from "./components.types";

const UnitEntry = (props: UnitEntryProps) => {
  const [subject, setSubject] = useState<string>();
  //   props.subjects.map();
  return (
    <div className={styles.container}>
      <h2>Add a unit</h2>
      <FormControl sx={{ m: 1, maxWidth: 320 }}>
        <InputLabel id="degree-label">unit</InputLabel>
        <Select
          id="unit"
          value={subject}
          onChange={(ev) => {
            setSubject(ev.target.value);
          }}
          className={styles.padded}
        >
          <MenuItem value="badvcmp">Bachelor of Advanced Computing</MenuItem>
          <MenuItem value="bsci">Bachelor of Science</MenuItem>
        </Select>
      </FormControl>

      <Button
        sx={{ m: 1, maxWidth: 100, background: "#86bd33" }}
        variant="contained"
      >
        Add
      </Button>
    </div>
  );
};

export default UnitEntry;
