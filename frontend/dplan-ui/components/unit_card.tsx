import { UnitCardProps } from "./components.types";
import styles from "../styles/UnitCard.module.css";

import Star from "../public/star-solid.svg";

const UnitCard = (props: UnitCardProps) => {
  return (
    <div className={styles.container}>
      <div className={styles.code}>{props.unitCode}</div>
      <div className={styles.name}>{props.unitName}</div>
      <div className={styles.cont}>
        {Array.from(Array(props.unitRating).keys()).map((_) => (
          <Star />
        ))}
        <div className={styles.number}>(3)</div>
      </div>
    </div>
  );
};
export default UnitCard;
