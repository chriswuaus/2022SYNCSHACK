import { DegreeProps } from "./components.types";
import styles from "../styles/Degree.module.css";
import Link from "next/link";

const Degree = (props: DegreeProps) => {
  return (
    <Link href="/degree_plan">
    <div className={styles.container}>
      <div className={styles.name}>
        {props.degreeName} {props.degreeYear}
        <div className={styles.major}>Major: {props.major}</div>
      </div>
      <div className={styles.sem}>Starting Semester {props.semester}</div>
    </div></Link>
  );
};
export default Degree;
