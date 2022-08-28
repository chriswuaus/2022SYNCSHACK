import { UnitCardProps } from "./components.types";
import styles from "../styles/UnitCard.module.css";

import Star from "../public/star-solid.svg";

const UnitCard = (props: UnitCardProps) => {
  return (
    <div className={styles.container}>
      <div className={styles.code}>{props.unitCode}</div>
      <div className={styles.name}>{props.unitName}</div>
      <div>
        <Star />
        <Star />
        <Star />
        <Star />
        <Star />
      </div>
    </div>
  );
};
export default UnitCard;
