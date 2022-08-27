import { Button, FormControl, InputLabel, MenuItem, Select, TextField } from "@mui/material"
import { useReducer, useState } from "react"
import styles from "../styles/DegreeEntry.module.css"


const DegreeEntry = () => {
    const [degree, setDegree] = useState<string>()
    const [major, setMajor] = useState<string>()
    const [year, setYear] = useState<string>()
    return <div className={styles.container}>
        <h2>Add a degree</h2>
        <FormControl sx={{ m: 1, maxWidth: 320 }}>
            <InputLabel id="degree-label">Degree</InputLabel>
            <Select id="degree" value={degree} onChange={ev => { setDegree(ev.target.value)}} className={styles.padded}>
                <MenuItem value="badvcmp">Bachelor of Advanced Computing</MenuItem>
                <MenuItem value="bsci">Bachelor of Science</MenuItem>
            </Select>
        </FormControl>
        <FormControl sx={{ m: 1, maxWidth: 320 }}>
            <InputLabel id="major-label">Major</InputLabel>
            <Select id="major" value={major} onChange={ev => { setMajor(ev.target.value)}} className={styles.padded} >
                <MenuItem value="compsci">Computer Science</MenuItem>
                <MenuItem value="datasci">Data Science</MenuItem>
            </Select>
            <TextField type="number" value={year} label="Start Year" className={styles.padded} onChange={ev => { setYear(ev.target.value)}} />
        </FormControl>
        <Button sx={{ m: 1, maxWidth: 100, background: "#86bd33" }} variant="contained">Add</Button>
        <p>
            {degree} ({major}) - {year}
        </p>
    </div>
}

export default DegreeEntry