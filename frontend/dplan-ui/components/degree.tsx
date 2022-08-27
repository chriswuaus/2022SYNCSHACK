import { DegreeProps } from "./components.types";
import styles from "../styles/Degree.module.css";

const Degree = (props: DegreeProps) => {
  return (
    <div className={styles.container}>
      <div className={styles.name}>
        {props.degreeName} {props.degreeYear}
        <div className={styles.major}>Major: {props.major}</div>
      </div>
      <div className={styles.sem}>Starting Semester {props.semester}</div>
    </div>
  );
};
export default Degree;
