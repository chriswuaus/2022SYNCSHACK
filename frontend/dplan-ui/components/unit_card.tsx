import { UnitCardProps } from "./components.types";
import styles from "../styles/UnitCard.module.css";

const UnitCard = (props: UnitCardProps) => {
  return (
    <div className={styles.container}>
      <div className={styles.code}>{props.unitCode}</div>
      <div className={styles.name}>{props.unitName}</div>
      <div>
        <img src="/star-solid.svg" width={50} alt="deez"></img>
        <img src="/star-solid.svg" width={50} alt="deez"></img>
        <img src="/star-solid.svg" width={50} alt="deez"></img>
        <img src="/star-solid.svg" width={50} alt="deez"></img>
        <img src="/star-solid.svg" width={50} alt="deez"></img>
      </div>
    </div>
  );
};
export default UnitCard;
