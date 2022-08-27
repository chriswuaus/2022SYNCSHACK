import styles from "../styles/Butt.module.css";
import House from "../public/house-solid.svg";
import { ButtProps } from "./components.types";
const Plus = (props: ButtProps) => {
  let stylesFR = styles.button;
  if (props.highlighted) stylesFR += " " + styles["button-highlighted"];
  return (
    <button className={stylesFR}>
      <House />
    </button>
  );
};
export default Plus;
