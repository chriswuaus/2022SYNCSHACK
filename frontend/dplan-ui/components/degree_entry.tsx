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
import { DegreeEntryProps } from "./components.types";

const DegreeEntry = ({ onAdd }: DegreeEntryProps) => {
  const [degree, setDegree] = useState<string>();
  const [major, setMajor] = useState<string>();
  const [year, setYear] = useState<string>();
  const [semester, setSemester] = useState<number>();
  return (
    <div className={styles.container}>
      <h2>Add a degree</h2>
      <FormControl sx={{ m: 1, width: 320 }}>
        <InputLabel id="degree-label">Degree</InputLabel>
        <Select
          id="degree"
          value={degree}
          onChange={(ev) => {
            setDegree(ev.target.value);
          }}
          className={styles.padded}
        >
          <MenuItem value="badvcmp">Bachelor of Advanced Computing</MenuItem>
          <MenuItem value="bsci">Bachelor of Science</MenuItem>
        </Select>
      </FormControl>
      <FormControl sx={{ m: 1, maxWidth: 320 }}>
        <InputLabel id="major-label">Major</InputLabel>
        <Select
          id="major"
          value={major}
          onChange={(ev) => {
            setMajor(ev.target.value);
          }}
          className={styles.padded}
        >
          <MenuItem value="compsci">Computer Science</MenuItem>
          <MenuItem value="datasci">Data Science</MenuItem>
        </Select>
      </FormControl>
      <TextField
        sx={{ m: 1, maxWidth: 320 }}
        type="number"
        value={year}
        label="Start Year"
        className={styles.padded}
        onChange={(ev) => {
          setYear(ev.target.value);
        }}
      />
      <FormControl sx={{ m: 1, maxWidth: 320 }}>
        <InputLabel id="semester-label">Semester</InputLabel>
        <Select
          id="Semester"
          value={semester}
          onChange={(ev) => {
            setSemester(ev.target.value);
          }}
          className={styles.padded}
        >
          <MenuItem value={1}>Sem 1</MenuItem>
          <MenuItem value={2}>Sem 2</MenuItem>
        </Select>
      </FormControl>
      <center>
        <Button
          sx={{ m: 1, maxWidth: 100, background: "#86bd33" }}
          variant="contained"
          onClick={() =>
            onAdd({
              degreeName: degree!,
              major: major!,
              degreeYear: year!,
              semester: semester!,
              link: `/degrees/{degree+year+major}`,
            })
          }
          disabled={
            !(
              degree != undefined &&
              major != undefined &&
              year != undefined &&
              semester != undefined
            )
          }
        >
          Add
        </Button>
      </center>
    </div>
  );
};

export default DegreeEntry;
